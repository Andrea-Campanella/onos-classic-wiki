# Deployment in elastic environments

# Background

In many use cases the ONOS SDN controller will be deployed as a component in a larger solution. Often the overall solution will have to provide high availability and elasticity to meet the changing demands of a deployment. This means that in some use cases the ONOS controller instances will be deployed and scaled using frameworks like [Google's Kubernetes](http://kubernetes.io/), [Apache Project's Mesos](http://mesos.apache.org/), [Deis](http://deis.io/), or other open source and vendor specific platforms.

# Overview

Leveraging dynamic deployment and scale frameworks present some challenges to the ONOS controller. This is because in an OpenFlow environment the assumption is that the device is configured with the IP address of one or more controller which it will contact to receive control plane instructions, yet in these dynamic deployment environment the IP addresses of the individual components (i.e. ONOS controller instances) are essentially obfuscated and not meant to be exposed or really important as any individual instance should be able to disappear or reappear at will.

# ONOS Clustering

One of the obstacles

* mastership (write authority for device)
* sticky balancing
* if connection from device goes through a load balancer, assumers the bottleneck is not the load balancer
