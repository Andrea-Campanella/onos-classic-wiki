# SONA Walkthrough

This walkthrough demonstrates most SONA features, as well as its typical usage in concert with OpenStack. The walkthrough assumes that you are familiar with how to use ONOS and OpenStack. If you're not, we recommend you to go through [Tutorials and Walkthroughs](../../../../../tutorials-and-walkthroughs-9832212.md) and [http://docs.openstack.org](http://docs.openstack.org/).

If you are more comfortable with Horizon UI, then please refer to [SONA Walkthrough with Horizon](sona-walkthrough-with-horizon.md).

Tip) The following cloud-init script helps to set password of **"ubuntu"** user to **"ubuntu"** for UEC image, if you pass this script to Nova with **"--user-data"** option when you create a new VM.

```
#cloud-config
password: ubuntu
chpasswd: { expire: False }
ssh_pwauth: True
```

# Switching

Create two tenant networks and virtual machines in OpenStack, and then test tenant network connectivity and isolation.

```
neutron net-create net-A
neutron subnet-create net-A 192.168.0.0/24
neutron net-create net-B
neutron subnet-create net-B 192.168.1.0/24
 
nova boot --flavor 2 --image ubuntu-14.04-server-cloudimg-amd64 --user-data passwd.data --nic net-id=[net-A-UUID] net-A-01
nova boot --flavor 2 --image ubuntu-14.04-server-cloudimg-amd64 --user-data passwd.data --nic net-id=[net-A-UUID] net-A-02
nova boot --flavor 2 --image ubuntu-14.04-server-cloudimg-amd64 --user-data passwd.data --nic net-id=[net-B-UUID] net-B-01
```

* Can ping between net-A-01 and net-A-02
* Can't ping between net-A-01 and net-B-01

# Routing

Create another network for the external access and floating IP with the subnet range specified in the ONOS-vRouter network config(see [SONA Network Configuration Guide](sona-network-configuration-guide.md)).

```
neutron net-create net-public --router:external True --provider:physical_network external --provider:network_type flat
neutron subnet-create net-public 172.27.0.0/24
```

Create a router, and add gateway and interfaces.

```
neutron router-create router-01
neutron router-gateway-set router-01 net-public
neutron router-interface-add rotuer-01 [net-A-subnet UUID]
neutron router-interface-add router-01 [net-B-subnet UUID]
```

Now the network topology should look like the figure below if you check it in Horizon.

![](../../../../../assets/screen-shot-2016-04-05-at-4.19.06-pm.png)

Create a security group to allow external access, and add it to the net-A-01 and net-B-01.

```
neutron security-group-create allow-external
neutron security-group-rule-create --direction ingress --remote-ip-prefix 0.0.0.0/0 allow-external
neutron port-update [net-A-01 port UUID] --security-group [default-security-group UUID] --security-group allow-external
neutron port-update [net-B-01 port UUID] --security-group [default-security-group UUID] --security-group allow-external
```

* Can ping from net-A-01 and net-B-01 to 8.8.8.8
* Can ping between net-A-01 and net-B-01

Currently, SONA security group implementation has a small limitation that it does not allow ingress traffic via a connected session by default. So, you'll need to add allowing rule for ingress direction with remote address "0.0.0.0/0" explicitly for your VM to be able to access the Internet.

Create a floating IP and associate it to net-A-01.

```
neutron floatingip-create net-public
neutron floatingip-associate [floating-ip-id] [net-A-01 port UUID]
```

* Can ping to net-A-01 with the associated floating IP from the external
