# SONA Testing

This page provides guidelines for testing SONA in an automated way to help developers test their changes do not break anything. As SONA is an implementation of Neutron ML2 mechanism driver, we can make use of general OpenStack testing tools. Particularly, [Tempest](https://docs.openstack.org/developer/tempest/) is OpenStack's official test suit for running a set of functional tests against an OpenStack cluster. Most OpenStack projects employ Tempest as a gate for automated testing of committed change. It is strongly recommended to run Tempest API and scenarios tests described here against your changes to SONA before submitting. Some test cases specific to SONA still need manual testing.

# Setup Test Environment

Some Tempest scenario tests include accessing a VM with floating IP. That means you have to prepare a test machine reachable to the floating range. If you're using all-in-one gateway node, which has Quagga container for external router inside a gateway node, you can run the test at the gateway node. We use Rally for installing and configuring Tempest easily.

1. Install Docker

```
$ wget -qO- https://get.docker.com/ | sudo sh
```

Note that, in CentOS you need to manually start the docker daemon as follows.

```
$ sudo systemctl enable docker
$ sudo systemctl start docker
```

2. Create admin-openrc.sh with access information to target OpenStack deployment.

**admin-openrc.sh**

```
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=nova
export OS_AUTH_URL=http://10.1.1.161:35357/v2.0
export LC_ALL=C
```

3. Create Tempest configuration file for SONA. Note that, we only test the SONA against following API extensions.

1. default-subnetpools: The default subnetpool extension (`default-subnetpools`) allows administrative users to specify default subnetpools (one per IP version). ([link](https://docs.openstack.org/ocata/networking-guide/config-subnet-pools.html))
2. network-ip-availability: The extension `network-ip-availability` allows users to list and show the network IP usage stats of all networks or of a specified network. ([link](https://docs.openstack.org/neutron/pike/contributor/internals/network_ip_availability.html))
3. subnet\_allocation: Subnet allocation extension (`subnet_allocation`) enables allocation of subnets from a subnet pool. ([link](https://docs.openstack.org/neutron/pike/admin/config-mtu.html))
4. external-net: The `external-net` extension adds the `router:external` attribute to networks. This boolean attribute indicates the network has an external routing facility that’s not managed by the networking service. ([link](https://specs.openstack.org/openstack/neutron-specs/specs/api/external_networks__external-net_.html))
5. router: A `router` is a logical entity for forwarding packets across internal subnets and NATting them on external networks through an appropriate external gateway. ([link](https://developer.openstack.org/api-ref/network/v2/index.html#layer-3-networking))
6. security-group: Security group API. ([link](https://docs.openstack.org/neutron/pike/contributor/internals/security_group_api.html))
7. ext-gw-mode: The `ext-gw-mode` extension of the router abstraction for specifying whether SNAT should occur on the external gateway ([link](https://specs.openstack.org/openstack/neutron-specs/specs/api/configurable_external_gateway_modes.html))
8. net-mtu: The `net-mtu` extension allows plug-ins to expose the MTU that is guaranteed to pass through the data path of the segments in the network. This extension introduces a read-only `mtu` attribute. ([link](https://docs.openstack.org/neutron/pike/admin/config-mtu.html))

To test the floating IP features, you need to create an external network named "net-public" with a subnet associated with it in OpenStack. Note that, by far SONA does not support IPv6, so we need to disable the IPv6 related test cases.

**sona-tempest.conf**

```
[network-feature-enabled]
ipv6_subnet_attributes = False
ipv6 = False
api_extensions = default-subnetpools,network-ip-availability,subnet_allocation,external-net,router,security-group,ext-gw-mode,net-mtu,tag,tag-ext,sorting,pagination,project-id,address-scope,standard-attr-description,standard-attr-revisions,standard-attr-timestamp,standard-attr-tag,quotas,flavors,net-mtu-writable,extraroute,quota_details,provider,service-type

[compute-feature-enabled]
metadata_service = False

[compute]
min_compute_nodes = 2

[network]
floating_network_name = net-public
project_networks_reachable = False
```

4. Run rally container through sona-setup. The sona-setup should be executed in SONA gateway node, and the role of sona-setup is to spawn a rally container. Note that, you should be able to connect to OpenStack spawned VM inside rally container by giving VM's floating IP.

```
$ sudo mkdir /var/lib/rally_container
$ sudo chown 65500 /var/lib/rally_container
$ sudo cp ~/admin-openrc.sh /var/lib/rally_container
$ sudo cp ~/sona-tempest.conf /var/lib/rally_container
$ git clone https://github.com/sonaproject/sona-setup.git
$ cd sona-setup && git checkout rally
$ ./createExternalRouter.sh
```

5. Enter rally container and register target OpenStack deployment.

```
$ sudo docker exec -it router bash
###############################################################################
# Welcome to Rally Docker container!                                          #
#                                                                             #
#  WARNING: DO NOT OVERRIDE /home/rally DIRECTORY                             #
#                                                                             #
#  /home/rally/data      - a default place with rally database. Use it for    #
#      mounting own directories and synchronizing rally database.             #
#  /home/rally/source    - a directory with documentation, pre created tasks, #
#      sampes and source code                                                 #
#  /etc/rally/rally.conf - a default configuration file of rally. To override #
#      it, mount custom configuration file to /home/rally/.rally/rally.conf   #
#                                                                             #
#  Rally at readthedocs - http://rally.readthedocs.org                        #
#  How to contribute - http://rally.readthedocs.org/en/latest/contribute.html #
#  If you have any questions, you can reach the Rally team by:                #
#    * e-mail - openstack-dev@lists.openstack.org with tag [Rally] in subject #
#    * gitter - https://gitter.im/xRally/Lobby room                           #
#    * irc - "#openstack-rally" channel at freenode.net                       #
###############################################################################

root@router:/home/rally# rm -rf data && mkdir -p data
root@router:/home/rally# rally db recreate
root@router:/home/rally# source admin-openrc.sh
root@router:/home/rally# rally deployment create --fromenv --name sona-test
```

6. Create Tempest verifier and configure it. It is required to use SONA specific version of Tempest until critical bugs are fixed. Also note that, you need to specify which OpenStack version that you would like to test against. In following example, we test the SONA against OpenStack pike.

```
root@router:/home/rally# rally verify create-verifier --type tempest --name tempest-verifier --source https://github.com/sonaproject/tempest.git --version rocky
root@router:/home/rally# rally verify configure-verifier --extend sona-tempest.conf
```

Run Test

1. Create sona-skip-list.yaml as below to filter out not supported feature tests. Note that, by far SONA is verified against all tempest tests, but if some of the tests fail, you need to add the failed tests into the skip list. The latest version of blacklist of test cases can be found in following link. <https://github.com/sonaproject/tempest-sona-conf/blob/master/sona-skip-list.yaml>

**sona-skip-list.yaml**

```
tempest.scenario.test_snapshot_pattern.TestSnapshotPattern.test_snapshot_pattern[compute,id-608e604b-1d63-4a82-8e3e-91bc665c90b4,image,network,slow]: "not support"
neutron_tempest_plugin.api.test_routers.RoutersTest.test_router_interface_status[id-db3093b1-93b6-4893-be83-c4716c251b3e]: "not support"
```

2. Now, run Tempest network related API and scenario tests.

```
root@router:/home/rally# rally verify start --pattern network --skip-list sona-skip-list.yaml --detail
2017-05-16 06:03:35.215 1109 INFO rally.api [-] Starting verification (UUID=e9fcd543-a438-4845-82a9-62cc2ead2693) for deployment 'sona-test' (UUID=f51f26b4-0603-4f8a-a29a-21d045d898df) by verifier 'tempest-verifier' (UUID=aadced51-ddf6-4cb9-a422-df0d51119679).

======
Totals
======

Ran: 336 tests in 1806.546 sec.
 - Success: 161
 - Skipped: 175
 - Expected failures: 0
 - Unexpected success: 0
 - Failures: 0

Using verification (UUID=42b6f756-7ebf-4d6b-b0f4-dd41c06bd8ae) as the default verification for the future operations.
```

# Verify Against Tempest Plugin

1. If you would like to verify SONA against neutron-tempest-plugin, you need to add the plugin as a tempest extension using following command.

```
root@router:/home/rally# rally verify add-verifier-ext --source https://github.com/openstack/neutron-tempest-plugin.git
```

2. Now, run Tempest network related API and scenario tests.

```
root@router:/home/rally# rally verify start --pattern neutron_tempest_plugin --skip-list sona-skip-list.yaml --detail
2017-05-16 06:03:35.215 1109 INFO rally.api [-] Starting verification (UUID=e9fcd543-a438-4845-82a9-62cc2ead2693) for deployment 'sona-test' (UUID=f51f26b4-0603-4f8a-a29a-21d045d898df) by verifier 'tempest-verifier' (UUID=aadced51-ddf6-4cb9-a422-df0d51119679).
======
Totals
======

Ran: 564 tests in 1052.455 sec.
 - Success: 231
 - Skipped: 333
 - Expected failures: 0
 - Unexpected success: 0
 - Failures: 0

Using verification (UUID=fa929aeb-5d68-464a-9ae2-63a3c689304d) as the default verification for the future operations.
```
