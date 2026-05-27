# Running ONOS Under Container Orchestration

Describes the techniques and tools that have been used, to date, to integrate ONOS instantiation under a container orchestration system, specifically Docker Swarm, but should be applicable, with modifications to other systems such as Kubernetes or Mesosphere.

# Caveat

The techniques and tools described on this page were developed based on the current capabilities, as of 1.12, of ONOS. This page is not to imply that there are not other and perhaps better ways to manage ONOS under a container management system; including core changes to ONOS to improve dynamic cluster formation and maintenance.

# Problems

(1) For ONOS to properly form a cluster the IP addresses of the cluster nodes must be known so that proper cluster meta data (configuration) can be available to each ONOS instance. This *a priori* knowledge of node IP addresses run counter to the design principles of container management systems, where instance information is not known until instances are created.

(2) For ONOS to function as part of a solution it often requires a configuration after it is instantiated.

# Solving Problem (1)

To address the problem a new container was introduced as part of the VOLTHA project, [Unum](https://github.com/opencord/voltha/tree/master/unum) (short for E Pluribus Unum\*). The purpose of this container is to monitor the container orchestration system events and when all instances of ONOS have been started and initialized, to generate cluster meta data that is pulled via HTTP by the ONOS instances; at which point the cluster is formed.

## Configuration

The *Unum* container leverages labels against service definitions and replicas to identify ONOS instances that should be included in the cluster formation. As part of the configuration to the *Unum* container the labels for which *Unum* should look can be specified using the environment variables `LABELS` (default: `org.onosproject.cluster:true`) to indicate which service and which ONOS replicas should be considered and `NETWORK` (default `org.onosproject.cluster:true`) to indicate which network the ONOS instance should use as part of the cluster meta data. An example `[docker-compose.yml](https://github.com/opencord/voltha/blob/master/unum/docker-compose.yml)` file that demonstrates starting ONOS is provided as part of the *Unum* container source repository.

## Counting

To determine how many instances of ONOS are expected and how many are operational, the *Unum*, container periodically polls the container orchestration system and locates all the `instances` that contain the specified label and how many *expected* replicas are defined for each instance as well as how many are operational. When the expected count equals the operational count cluster meta data is generated and made available to ONOS instances to pull via HTTP.

## Waiting for the Cluster

While the *Unum* container is waiting for all instances of ONOS to be instantiated and become "ready", the container will return a `204 No Content` response.

# Issues

## Dynamic Changes

The *Unum* container supports dynamic scaling and restart of ONOS instances, such that it will generate cluster meta based on the current operational state of all instances running under the container management system. This means that the cluster meta data will change as instances fail and restart. It has been observed that ONOS does not consistently react "well" to this level of dynamic change in cluster meta data and it is expected that ONOS will become confused in the presence of failed and restarted instances. This is an issue that needs to be addressed in ONOS core regardless if ONOS is run under an orchestration system or directly on a host. This includes scaling up / down the number of instances in the cluster.

## OpenFlow Mastership and Orchestration Load Balancing

When services are instantiated under a container management system that system, typically, creates a virtual IP (VIP) that represents an end point for the service and load balances requests via that end point amongst the instances. Using this pattern, each OpenFlow (OF) switch would be given just the VIP as its controller IP. If would create an OF, TCP, connection through the VIP and be load balanced to one instance of ONOS. In the case of a loss of connection to the controller the ONOS would attempt to reconnect through the single VIP and be load balanced to another instance of ONOS. The container orchestration system controls the load balancing between the OF switch and the controller instances.

This conflicts with the standard OF process where a switch is given the IP of each controller instance, connects to all instances and accepts one as the master. When connectivity is lost to the master one of the other instances is promoted to master and the OF switch then complies with the new masters control. The switch, along with the controllers, controls the load balancing between OF switch and the controller instances.

# Polling v. Events

The current implementation of *Unum* leverages polling of the container orchestration system to retrieve information about ONOS instances. This is an inefficient mechanism to achieve the desired results and instead asynchronous events should be leveraged. When *Unum* was authored the required information was not available via and event stream and thus polling was required. It is unknown if the required information is available via events today. Even with asynchronous event capability Unum will still be required to support synchronous query and processing of the results to retrieve initial information when *Unum* starts as well as to re-sync in the event *Unum* loses connectivity to the event stream.

# Solving Problem (2)

How an initial configuration is supplied to ONOS in a container orchestration system depends on the deployment preferences as well as the static or dynamic nature of the configuration. For example, if the configuration is static that it is a perfectly reasonable choice to create a custom ONOS container image with that static configuration as part of that image. This solution will not work if the configuration is influenced by the state of the deployment when the container is instantiated.

## Custom Container Image

To create a static configuration that is part of a custom container image the integrator would create a `Dockerfile` specification that is `FROM` the required ONOS docker image and `COPY` into that image the static `net-config.json` file. The `Dockerfile` would look similar to the following:

```
FROM onosproject/onos:1.12
COPY network-cfg.json /root/onos/config/network-cfg.json
```

## Volume

The volume approach to initial configuration is similar to the custom container image solution in that it works best when the configuration is static, or at least "known" at the time of ONOS instantiation. In this scenario ONOS is launched with a volume specification to mount the `network-cfg.json` file into the container at the mount point `/root/onos/config/network-cfg.json`. It should be noted that this solution has issues because the container orchestration system may only support directory mounts and not specific file mounts and in the case of ONOS multiple configuration and status files are maintained in /`root/onos/config.`

## HTTP POST

This solution involves generating and pushing the configuration to ONOS via HTTP. Using this mechanism involves a couple of important issues including understanding when the configuration push was successful. Depending on the deployment needs this configuration might be a one time push, or could be a period synchronization.

### One Time Push

Using HTTP POST for a one time push has limited advantage over the other solutions presented as it still works best with a static configuration or a configuration that is "known" at the time ONOS is instanciated. In this scenario a container could be build that continuously attempts to POSt a known configuration to ONOS until it receives a `200 Ok` response from ONOS, at this point the container can exit, never to be restarted.

### Configuration Synchronization

In this scenario the ONOS configuration is periodically queried from ONOS and verified against the known expected configuration. When there is a difference the "expected" configuraiton is POSTed to ONOS. This synchronization can be more or less intelligent based on the needs. For example, a synchronization might only verify portions of the configuration expecting other portions to be dynamic or at least not relevant. In this scenario when a difference in the critical section of the configuration is discovered a configuraiton is generated based on the operational configuation and the required critical sections and POSTed back to ONOS.

## Configuraiton Generation

An ONOS configuraiton can be generated many different ways, and the actual mechanism is left to integrator. However, one such way would be leverage a tool like Consul and its ability to [generate files form templates](https://github.com/hashicorp/consul-template) to generate the expected configuration based on data stored in Consul. Using this mechanism allows the relevant data to be persisted in a key / value store and when it is changed a new configuration file will be generated. A configuration synchronizer can watch for changes in the file and synchronize to ONOS on a change (as well as perhaps to a peridic synchronization).

---

\*E Pluribus Unum is latin "Out of many, one".
