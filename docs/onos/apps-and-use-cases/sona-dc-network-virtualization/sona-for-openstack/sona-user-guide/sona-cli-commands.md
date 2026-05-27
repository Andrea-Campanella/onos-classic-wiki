# SONA CLI Commands

# 

# OpenstackNode Commands

### openstack-nodes

Lists up existing openstack nodes.

```
onos> openstack-nodes
Hostname            Type           Integration Bridge      Router Bridge           Management IP       Data IP             VLAN Intf      State
sona-compute-01     COMPUTE        of:00000000000000a1                             10.1.1.162          10.1.1.162                         COMPLETE
sona-compute-02     COMPUTE        of:00000000000000a2                             10.1.1.163          10.1.1.163                         COMPLETE
sona-gateway-02     GATEWAY        of:00000000000000a4     of:00000000000000b4     10.1.1.165          10.1.1.165                         COMPLETE
Total 3 nodes
```

### openstack-node-check [hostname]

Shows detailed states of the given node.

```
onos> openstack-node-check sona-compute-01
[Integration Bridge Status]
OK br-int=of:00000000000000a1 available=true {managementAddress=10.1.1.162, protocol=OF_13, driver=sona, name=of:00000000000000a1, locType=geo, channelId=10.1.1.162:42541}
OK vxlan portNum=1 enabled=true {portName=vxlan, portMac=0a:40:39:40:b5:d6}
```

### openstack-node-init

Initializes the given node.

```
onos> openstack-node-init sona-compute-01
```

# OpenstackNetworking Commands

### openstack-networks

Lists up existing networks. It only shows cached information in the local store, so it may not be synched with Neutron network states. Json results provide more detailed information.

```
onos> openstack-networks
ID                                      Name                VNI                 Subnets
ed537060-75d7-4627-bb1e-f6a070c1a697    net-A               63                  [192.168.0.0/24]
c709de09-84cf-4639-8e70-3d6c4bebe3f0    net-B               38                  [192.168.1.0/24]
b2590504-79b2-49a0-83b3-24458572ff9b    net-public          null                [172.27.0.0/24]
 
onos> openstack-networks -j
[ {
  "network" : {
    "status" : "ACTIVE",
    "subnets" : [ "2790597b-b751-4df4-9ee7-41d65b7f75b9" ],
    "neutronSubnets" : [ {
      "id" : "2790597b-b751-4df4-9ee7-41d65b7f75b9",
      "name" : "",
      "cidr" : "192.168.0.0/24",
      "enable_dhcp" : true,
      "network_id" : "ed537060-75d7-4627-bb1e-f6a070c1a697",
      "tenant_id" : "5c7d0aba63574d009c049622afd66007",
      "dns_nameservers" : [ ],
      "allocation_pools" : [ {
        "start" : "192.168.0.2",
        "end" : "192.168.0.254"
      } ],
      "host_routes" : [ ],
      "ip_version" : 4,
      "gateway_ip" : "192.168.0.1"
    } ],
    "name" : "net-A",
    "id" : "ed537060-75d7-4627-bb1e-f6a070c1a697",
    "shared" : false,
    "admin_state_up" : true,
    "tenant_id" : "5c7d0aba63574d009c049622afd66007",
    "provider:network_type" : "vxlan",
    "router:external" : false,
    "provider:segmentation_id" : "63"
  }
},
```

### openstack-ports

Lists up existing ports. It only shows cached information in the local store, so it may not be synched with Neutron network states. Json results provide more detailed information.

```
onos> openstack-ports
ID                                      Network             MAC                 Fixed IPs
3b4f8656-bad6-47a8-809f-31efd1fc5ebb    net-public          fa:16:3e:19:fb:88   [172.27.0.12]
651b9bac-ea6d-4f93-a95d-ddd5e04d7f43    net-public          fa:16:3e:c8:5a:5e   [172.27.0.6]
dec5a8c8-5f21-4b6a-b4d9-a075c3bdc52d    net-public          fa:16:3e:2c:1c:40   [172.27.0.2]
8010aab5-1491-4965-960d-38216085ae63    net-B               fa:16:3e:c7:34:4e   [192.168.1.2]
4affa23f-91d9-49c6-a605-2d15d0efad85    net-B               fa:16:3e:16:82:ce   [192.168.1.7]
c73288cd-5fbc-4b92-a3f6-769dcb9afb51    net-B               fa:16:3e:5d:99:1d   [192.168.1.1]
345af6ff-4521-42b6-8a1a-cb2330eec0ee    net-A               fa:16:3e:0c:c0:51   [192.168.0.2]
578fa45e-41a4-46dd-a070-b5ec28c2a98a    net-A               fa:16:3e:2a:85:30   [192.168.0.6]
c80c22dc-03b0-40f5-855c-bbfbce55cbca    net-A               fa:16:3e:64:5e:3a   [192.168.0.5]
d2db27cd-3cbb-4fa0-ba64-bddfb8a76127    net-A               fa:16:3e:7a:0d:aa   [192.168.0.1]
 
onos> openstack-ports -j
[{
  "port" : {
    "id" : "4affa23f-91d9-49c6-a605-2d15d0efad85",
    "name" : "",
    "admin_state_up" : true,
    "device_id" : "7c25e166-c711-4e72-ae22-0505226d8764",
    "device_owner" : "compute:None",
    "fixed_ips" : [ {
      "ip_address" : "192.168.1.7",
      "subnet_id" : "8ced1ce9-d1dd-4a64-91dd-e84fe5867f18"
    } ],
    "allowed_address_pairs" : [ ],
    "mac_address" : "fa:16:3e:16:82:ce",
    "network_id" : "c709de09-84cf-4639-8e70-3d6c4bebe3f0",
    "status" : "ACTIVE",
    "tenant_id" : "5c7d0aba63574d009c049622afd66007",
    "security_groups" : [ "85204220-c22e-4ea0-a1b9-62c149f5ebdd" ],
    "extra_dhcp_opts" : [ ]
  }
},
```

### openstack-routers

Lists up existing ports. It only shows cached information in the local store, so it may not be synched with Neutron network states. Json results provide more detailed information.

```
onos> openstack-routers
ID                                      Name                External            Internal
09561bc4-319f-484d-923a-10f008116ca5    router-01           [172.27.0.6]        [192.168.1.1, 192.168.0.1]
 
onos> openstack-routers -j
[ {
  "router" : {
    "id" : "09561bc4-319f-484d-923a-10f008116ca5",
    "name" : "router-01",
    "status" : "ACTIVE",
    "external_gateway_info" : {
      "network_id" : "b2590504-79b2-49a0-83b3-24458572ff9b",
      "enable_snat" : true
    },
    "admin_state_up" : true,
    "tenant_id" : "5c7d0aba63574d009c049622afd66007",
    "routes" : [ ]
  }
} ]
```

### openstack-floatingips

Lists up existing floating IPs. It only shows cached information in the local store, so it may not be synched with Neutron network states. Json results provide more detailed information.

```
onos> openstack-floatingips
ID                                      Floating IP         Fixed IP
c1eaace2-3381-4c51-80ec-b8ade553937d    172.27.0.12         192.168.0.6
 
onos> openstack-floatingips -j
[ {
  "floatingip" : {
    "id" : "c1eaace2-3381-4c51-80ec-b8ade553937d",
    "router_id" : "09561bc4-319f-484d-923a-10f008116ca5",
    "tenant_id" : "5c7d0aba63574d009c049622afd66007",
    "floating_network_id" : "b2590504-79b2-49a0-83b3-24458572ff9b",
    "floating_ip_address" : "172.27.0.12",
    "fixed_ip_address" : "192.168.0.6",
    "port_id" : "578fa45e-41a4-46dd-a070-b5ec28c2a98a"
  }
} ]
```

### openstack-security-groups

Lists up existing security groups. It only shows cached information in the local store, so it may not be synched with Neutron network states. Json results provide more detailed information including security group rules.

```
onos> openstack-security-groups
Hint: use --json option to see security group rules as well
ID                                      Name
fe2f1617-58a8-4c86-b995-68a52439b129    default
fbafa8b4-a822-4ed6-917b-e701e287dce1    default
1004b77f-599a-4eee-bde8-29c0d52a096c    default
ed246013-4914-429c-bfb0-482087cd98fa    default
85204220-c22e-4ea0-a1b9-62c149f5ebdd    default
 
onos> openstack-security-groups -j
[ {
  "security_group" : {
    "id" : "1004b77f-599a-4eee-bde8-29c0d52a096c",
    "tenant_id" : "d5488368f6bc4d7285271bad6edd54cf",
    "description" : "Default security group",
    "name" : "default",
    "security_group_rules" : [ {
      "id" : "058c52f2-2902-4fb2-b66d-7f81b4000f64",
      "tenant_id" : "d5488368f6bc4d7285271bad6edd54cf",
      "security_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c",
      "direction" : "ingress",
      "ethertype" : "IPv4",
      "remote_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c"
    }, {
      "id" : "97047b64-a164-4b35-9316-4603726470f1",
      "tenant_id" : "d5488368f6bc4d7285271bad6edd54cf",
      "security_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c",
      "direction" : "egress",
      "ethertype" : "IPv4"
    }, {
      "id" : "a0de06b4-c380-4692-b5d7-e5437451c9cb",
      "tenant_id" : "d5488368f6bc4d7285271bad6edd54cf",
      "security_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c",
      "direction" : "ingress",
      "ethertype" : "IPv6",
      "remote_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c"
    }, {
      "id" : "e69330ab-0648-433e-950c-e54cf8ec5e16",
      "tenant_id" : "d5488368f6bc4d7285271bad6edd54cf",
      "security_group_id" : "1004b77f-599a-4eee-bde8-29c0d52a096c",
      "direction" : "egress",
      "ethertype" : "IPv6"
    } ]
  }
},
```

### openstack-purge-states

Purges existing network states cached in the local store.

```
onos> openstack-purge-states
```

### openstack-sync-states

Synches network state with Neutron.

```
onos> openstack-sync-states
Synchronizing OpenStack security groups
ID                                      Name
1004b77f-599a-4eee-bde8-29c0d52a096c    default
85204220-c22e-4ea0-a1b9-62c149f5ebdd    default
ed246013-4914-429c-bfb0-482087cd98fa    default
fbafa8b4-a822-4ed6-917b-e701e287dce1    default
fe2f1617-58a8-4c86-b995-68a52439b129    default
Synchronizing OpenStack networks
ID                                      Name                VNI                 Subnets
b2590504-79b2-49a0-83b3-24458572ff9b    net-public          null                [d7e2576e-b7ec-49ac-9fb9-2696ccef4612]
c709de09-84cf-4639-8e70-3d6c4bebe3f0    net-B               38                  [8ced1ce9-d1dd-4a64-91dd-e84fe5867f18]
ed537060-75d7-4627-bb1e-f6a070c1a697    net-A               63                  [2790597b-b751-4df4-9ee7-41d65b7f75b9]
Synchronizing OpenStack subnets
ID                                      Network             CIDR
2790597b-b751-4df4-9ee7-41d65b7f75b9    net-A               192.168.0.0/24
8ced1ce9-d1dd-4a64-91dd-e84fe5867f18    net-B               192.168.1.0/24
d7e2576e-b7ec-49ac-9fb9-2696ccef4612    net-public          172.27.0.0/24
Synchronizing OpenStack ports
ID                                      Network             MAC                 Fixed IPs
345af6ff-4521-42b6-8a1a-cb2330eec0ee    net-A               fa:16:3e:0c:c0:51   [192.168.0.2]
3b4f8656-bad6-47a8-809f-31efd1fc5ebb    net-public          fa:16:3e:19:fb:88   [172.27.0.12]
4affa23f-91d9-49c6-a605-2d15d0efad85    net-B               fa:16:3e:16:82:ce   [192.168.1.7]
578fa45e-41a4-46dd-a070-b5ec28c2a98a    net-A               fa:16:3e:2a:85:30   [192.168.0.6]
651b9bac-ea6d-4f93-a95d-ddd5e04d7f43    net-public          fa:16:3e:c8:5a:5e   [172.27.0.6]
8010aab5-1491-4965-960d-38216085ae63    net-B               fa:16:3e:c7:34:4e   [192.168.1.2]
c73288cd-5fbc-4b92-a3f6-769dcb9afb51    net-B               fa:16:3e:5d:99:1d   [192.168.1.1]
c80c22dc-03b0-40f5-855c-bbfbce55cbca    net-A               fa:16:3e:64:5e:3a   [192.168.0.5]
d2db27cd-3cbb-4fa0-ba64-bddfb8a76127    net-A               fa:16:3e:7a:0d:aa   [192.168.0.1]
dec5a8c8-5f21-4b6a-b4d9-a075c3bdc52d    net-public          fa:16:3e:2c:1c:40   [172.27.0.2]
Synchronizing OpenStack routers
ID                                      Name                External            Internal
09561bc4-319f-484d-923a-10f008116ca5    router-01           [172.27.0.6]        [192.168.1.1, 192.168.0.1]
Synchronizing OpenStack floating IPs
ID                                      Floating IP         Fixed IP
c1eaace2-3381-4c51-80ec-b8ade553937d    192.168.0.6         192.168.0.6
```

### openstack-purge-rules

Purges flow rules installed by openstack networking application.

```
onos> openstack-purge-rules
Successfully purged flow rules installed by OpenStack networking application.
```

### openstack-sync-rules

Installs flow rules based on the existing network states.

```
onos> openstack-sync-rules
Successfully requested re-installing flow rules.
```

# OpenstackTelemetry Commands

### telemetry-configs

Lists up existing telemetry configurations from pre-defined XML.

```
onos> telemetry-configs
Name                          Type           Enabled        Manufacturer                  swVersion
tina-kafka-exporter           KAFKA          PENDING        SK Telecom                    1.0
rest-connector                REST           DISABLED       N/A                           1.0
sona-influxdb-connector-1     INFLUXDB       DISABLED       SK Telecom                    1.0
sona-influxdb-connector-2     INFLUXDB       DISABLED       SK Telecom                    1.0
sona-prometheus-exporter      PROMETHEUS     DISABLED       SK Telecom                    1.0
```

### telemetry-config

Shows the detailed telemetry configuration with the given configuration name.

```
onos> telemetry-config sona-influxdb-connector-1                                         
                  address : 127.0.0.1
                 database : ost
              enableBatch : true
              measurement : sonaflow
                 password : onos
                     port : 8086
                 username : onos
```

### telemetry-enable

Activates a telemetry service with the given telemetry name. Note that, the activation can be failed due to connectivity issue, and the service activation results will be signified using service Status.

```
onos> telemetry-enable tina-kafka-exporter                                               
Successfully enabled telemetry service tina-kafka-exporter!


onos> telemetry-configs
Name                          Type           Enabled        Manufacturer                  swVersion
tina-kafka-exporter           KAFKA          ENABLED        SK Telecom                    1.0
rest-connector                REST           DISABLED       N/A                           1.0
sona-influxdb-connector-1     INFLUXDB       DISABLED       SK Telecom                    1.0
sona-influxdb-connector-2     INFLUXDB       DISABLED       SK Telecom                    1.0
sona-prometheus-exporter      PROMETHEUS     DISABLED       SK Telecom                    1.0
```

### telemetry-disable

Deactivates a telemetry service with the given telemetry name. Note that, the deactivation can be failed, and the service deactivation results will be signified using service Status.

```
onos> telemetry-disable tina-kafka-exporter                                               
Successfully disabled telemetry service tina-kafka-exporter!
```
