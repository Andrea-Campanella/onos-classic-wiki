# ON.LAB demo server setup

The demo server at ON.LAB (IP address 10.254.1.22, login: admin) currently runs XOS, the OpenStack controller services, and a nova-compute node in a VM.  For the demo it is also intended to run two ONOS instances but these have not been configured yet.

Jump to:

* [VM Setup](#ON.LABdemoserversetup-VMSetup)
* [XOS Setup](#ON.LABdemoserversetup-XOSSetup)
* [OpenStack Setup](#ON.LABdemoserversetup-OpenStackSetup)
* [CMI Setup](#ON.LABdemoserversetup-CMI)

# VM Setup

Each service runs in its own KVM virtual machine.  Use **virsh list** to see a list of the running VMs, each named after the service it hosts:

`admin@cordsrv01:~$ virsh list`  
 `Id    Name                    State`  
`----------------------------------------------------`  
 `2     xos                     running`  
 `3     juju                    running`  
 `4     mysql                   running`  
 `5     rabbitmq-server         running`  
 `6     keystone                running`  
 `7     glance                  running`  
 `8     nova-cloud-controller   running`  
 `9     quantum-gateway         running`  
 `10    openstack-dashboard     running`  
 `11    ceilometer              running`  
 `12    nagios                  running  
16    xos                     running`  
 `23    compute-1               running`

All of the VMs are attached to bridge `virbr0` with private addresses on the 192.168.122.0/24 subnet, and so are not reachable externally.  The IP addresses of the VMs are in `/etc/hosts`, or can be obtained using **uvt-kvm ip <VM name>**:

```
admin@cordsrv01:~$ uvt-kvm ip xos  
192.168.122.37
```

## Logging into a VM

Log in to a VM using **ssh ubuntu@<VM name>**.  The default SSH key for the admin user (`/home/admin/.ssh/id_rsa.pub)` has been added for the `ubuntu` user inside all the VMs, so this should just work:

```
admin@cordsrv01:~$ ssh ubuntu@compute-1  
Welcome to Ubuntu 14.04.2 LTS (GNU/Linux 3.13.0-49-generic x86_64)
```

```
...
```

```
ubuntu@compute-1:~$
```

## Creating new VMs

The existing VMs are created using the **uvt-kvm** tool.  To create a new VM (e.g., for ONOS) run **uvt-kvm <VM name> --cpu=<num vCPUs> --memory=<memory MB> --disk=<disk GB>**.  Be aware that this server has a small disk, though plenty of memory and CPU cores.

# XOS Setup

The XOS GUI is at <http://10.254.1.22:8000>.  Contact Scott Baker or Andy Bavier for login credentials.

The changes to support vCPE creation are not yet installed in XOS.  Information on the vCPE service interface will be added soon.

# OpenStack Setup

OpenStack services run in their own VMs.  [Juju](http://www.ubuntu.com/cloud/tools/juju) is used to install the services.  One feature of Juju is that it generates the OpenStack configuration files automatically – this means that all changes to the OpenStack configuration need to be implemented via Juju, or else they will be overwritten.  Contact Andy Bavier to discuss this.

Admin credentials for OpenStack can be found in `/home/admin/admin-openrc.sh` on the server.  The various OpenStack clients are installed and can be run with these credentials.  E.g.:

`admin@cordsrv01:~$ source admin-openrc.sh`  
`admin@cordsrv01:~$ nova service-list`  
`+----------------+-----------------------+----------+---------+-------+----------------------------+-----------------+`  
`| Binary         | Host                  | Zone     | Status  | State | Updated_at                 | Disabled Reason |`  
`+----------------+-----------------------+----------+---------+-------+----------------------------+-----------------+`  
`| nova-scheduler | nova-cloud-controller | internal | enabled | up    | 2015-04-17T19:29:34.000000 | -               |`  
`| nova-cert      | nova-cloud-controller | internal | enabled | up    | 2015-04-17T19:29:36.000000 | -               |`  
`| nova-conductor | nova-cloud-controller | internal | enabled | up    | 2015-04-17T19:29:40.000000 | -               |`  
`| nova-compute   | compute-1             | nova     | enabled | up    | 2015-04-17T19:29:43.000000 | -               |`  
`+----------------+-----------------------+----------+---------+-------+----------------------------+-----------------+`

The installation is automated using [Ansible](http://docs.ansible.com/) so it's easy to tear down and recreate the OpenStack installation if required.  Talk to Andy Bavier about this.

# CMI Setup

The CMI is running in a VM on the demo headnode. The XML defining the VM is at /etc/libvirt/qemu/cmi.xml. The image is in /var/lib/libvirt/images/cmi.qcow.

The CMI makes use of the following port forwarding rules:

iptables -t nat -I PREROUTING -p tcp --dport 8003 -j DNAT --to-destination 192.168.122.217:8003

iptables -t nat -I PREROUTING -p tcp --dport 8004 -j DNAT --to-destination 192.168.122.217:8004

iptables -t nat -I PREROUTING -p tcp --dport 8140 -j DNAT --to-destination 192.168.122.217:8140

iptables -t nat -I PREROUTING -p tcp --dport 1022 -j DNAT --to-destination 192.168.122.217:1022

iptables -I FORWARD -p tcp --dport 8003 -j ACCEPT

iptables -I FORWARD -p tcp --dport 8004 -j ACCEPT

iptables -I FORWARD -p tcp --dport 8140 -j ACCEPT

iptables -I FORWARD -p tcp --dport 1022 -j ACCEPT

The following should be added to the /etc/hosts on each physical machine

10.254.1.22 cordcmi.onlab.org

 The following should be added to the /etc/hosts on the demo headnode:

192.168.122.217 cordcmi

Inside of the CMI, make the following changes from stock configuration:

* Add ports 22 and 1022 to /etc/ssh/sshd\_config
* Open up firewall on port 1022 (iptables -I INPUT -p tcp --dport 1022 -j ACCEPT; service iptables save)
* Modify /etc/config/slices to point to the XOS VM: PS\_HOSTNAME="192.168.122.37"
