# ONOS test environment: Vagrant, LXC and cell

Consider using onos.py

A possibly simpler alternative to this approach can be found in [Mininet and onos.py workflow](../guides/developer-guide/development-environment-setup/development-workflow-options/mininet-and-onos.py-workflow.md) - you can pick whichever option seems best for your purposes.

Running multiple VMs that each run an ONOS instance is one way of running a multi-instance ONOS deployment. It is however not practical to do on my resource-constrained laptop. Using Linux Containers is a great alternative that achieves the same thing but uses way less CPU and memory. I also didn't care much for Docker's approach: Docker is very convenient to distribute ONOS as a self-contained application, but I had trouble integrating it into my development cycle which requires fast code/deploy/test cycles.

# Getting Started

I'm using VirtualBox as virtualization environment, but I see no reason why this shouldn't work on VMWare or other hypervisors.

The first step is to complete the first three steps of the [ONOS from Scratch](onos-from-scratch.md) tutorial. So only do the VM preparation, install required software, and setup the build environment. Don't bother creating a cell definition, nor packaging and deploying ONOS. This document has new instructions for those steps.

This VM will eventually host the ONOS instance containers. In the following, we'll first create a single container that is fully configured, and then clone the original as many times as needed.

# Using Vagrant boxes to prepare your development environment

This section replaces the remainder of this document and is an alternative to bootstrapping your environment. Using vagrant we provision two VMs:

1. onosdev - Running three lxc containers preinstalled with Java 8.
2. mn - A vm preinstalled with mininet.

To make use of this you simply need to do the following, assuming you have vagrant and virtualbox installed:

```
$ cd $ONOS_ROOT/tools/dev/vagrant
$ vagrant up
```

At this point you will have to wait for all the ansible scripts to finish before continuing. This may take sometime the first time you run it because it has to download a few ubuntu images.

Once the provisioning is done you should see the following:

```
==> mn: PLAY RECAP *********************************************************************
==> mn: localhost                  : ok=4    changed=3    unreachable=0    failed=0
```

At this point use the vagrant cell to setup your environment:

```
$ cell vagrant
ONOS_CELL=vagrant
OCI=10.100.198.201
OC1=10.100.198.201
OC2=10.100.198.202
OC3=10.100.198.203
OCN=10.100.198.100
ONOS_APPS=drivers,openflow,proxyarp
ONOS_GROUP=ubuntu
ONOS_NIC=10.100.198.*
ONOS_SCENARIOS=$ONOS_ROOT/onos-next/tools/test/scenarios
ONOS_USER=ubuntu
ONOS_WEB_PASS=rocks
ONOS_WEB_USER=onos
```

In older versions the cell name may be lxc instead of *vagrant*.

Finally, just push your ssh keys to the lxc nodes:

```
$ onos-push-keys $OC1
$ onos-push-keys $OC2
$ onos-push-keys $OC3
```

This will prompt you to for a password, which is **ubuntu.**

At this point, you should can use STC to deploy your cluster as shown below.

```
2016-05-27 10:13:17  Check-Apps-2 started -- onos-check-apps 10.100.198.202 drivers,openflow,proxyarp includes
2016-05-27 10:13:17  Check-Logs-2 completed
2016-05-27 10:13:17  Check-Apps-2 completed
2016-05-27 10:13:17  Check-Components-3 completed
2016-05-27 10:13:17  Check-Apps-3 started -- onos-check-apps 10.100.198.203 drivers,openflow,proxyarp includes
2016-05-27 10:13:17  Check-Logs-3 started -- onos-check-logs 10.100.198.203
2016-05-27 10:13:18  Check-Apps-3 completed
2016-05-27 10:13:18  Check-Logs-3 completed
2016-05-27 10:13:18  Setup completed
2:44 Passed! 31 steps succeeded
```

And you can enter your mininet environment with the following command:

```
$ cd $ONOS_ROOT/tools/dev/vagrant
$ vagrant ssh mn
mn$ sudo mn --topo linear,5 --controller remote,ip=10.100.198.201 --controller remote,ip=10.100.198.202 --controller remote,ip=10.100.198.203
```

Enjoy and feel free to report any issues.

# Creating Your First Container

Installing LXC is as simple as running

```
sudo apt-get install lxc
```

You should run `lxc-checkconfig` to determine your system properly supports this technology.

Next we'll create a new container with a clean Ubuntu install. This command will download all kinds of dependencies so it might take a while to complete.

```
sudo lxc-create -n onos1 -t ubuntu
```

You can verify the container is now available on your system. Note the container is currently stopped.

```
sudo lxc-ls --fancy
```

Go ahead and start the container. The -d flag instructs LXC to daemonize the container, so we'll stay in our shell while the container runs in the background.

```
sudo lxc-start -n onos1 -d
```

Take a look at the output of `lxc-ls` again: note the container is now started and, if all has gone well, has received an IP address.

# Cell Configuration

Containers are very convenient since we can automatically obtain their IPs. This is what my cell definition looks like; you want to put this in a file in `onos/tools/test/cells/`. You definitely want to verify if the `ONOS_NIC` variable corresponds to your system settings, and also `OCN` which points to the machine where Mininet is running. Feel free to customize the `ONOS_APPS` to your liking. Finally, you have to reload the cell if you create additional containers, so the new IPs get picked up.

```
# LXC-based multi ONOS instance & LINC-OE mininet box
export ONOS_NIC=10.0.3.*
I=1
for CONTAINER in $( sudo lxc-ls ); do
 IP=`sudo lxc-info -n $CONTAINER -iH`
 export OC${I}=${IP}
 let I=I+1
done
export OCI=$OC1
export OCN="192.168.56.9"
export ONOS_APPS="drivers,openflow,proxyarp,optical,bgprouter"
export ONOS_USER=ubuntu
export ONOS_GROUP=ubuntu
```

# Customizing Your Container

You want to do three things: enable paswordless login, enable passwordless sudo, and install Java 8.

First, push your public key to the container (make sure you have reloaded your cell definition):

```
onos-push-keys $OC1
```

Then ssh into the container as user ubuntu:

```
ssh ubuntu@$OC1 
```

Run `sudo visudo` and add the following line to the end of the file:

```
ubuntu ALL=(ALL) NOPASSWD:ALL
```

Installing Java is done as follows:

```
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:webupd8team/java -y
sudo apt-get update
sudo apt-get install oracle-java8-installer oracle-java8-set-default -y
```

Finally, log out of the container by pressing Ctrl-d or typing `exit`.

# Cloning Your Container

We're now ready to make as many clones of the original container as you want ONOS instances. Repeat the following steps as many times as you'd like, giving each new container a unique name.

```
sudo lxc-clone onos1 onos2
sudo lxc-start -n onos2 -d
```

Be sure to reload your cell configuration, which will automatically create and assign new $OCx variables.

# Development Cycle

From now on, it becomes very easy to develop and test code in a multi-instance environment. The process is as follows:

1. Write some code
2. Compile ONOS by running `obs` or `mci`
3. Package ONOS by running `op`
4. Install and run the latest package: `onos-group install -f $OC1 $OC2 $OC3` etc.
5. Go back to step 1 ![(smile)](../../assets/smile.svg)

# Additional Steps

## Linux Bridge Configuration

I ran into the weird problem that the ONOS instances weren't discovering each other. This process is driven by Hazelcast and relies on IP multicast. It turned out that LXC uses Linux bridge for connectivity among the containers, and the bridge by default does not forward multicast traffic! This is easily solved by checking the Linux bridge documentation; here's an excerpt

> IGMP snooping support is not yet included in bridge-utils or iproute2, but it can be easily controlled through sysfs interface. For brN, the settings can be found under /sys/devices/virtual/net/brN/bridge.
>
> `multicast_snooping`
>
> This option allows the user to disable IGMP snooping completely. It also allows the user to reenable snooping when it has been automatically disabled due to hash collisions. If the collisions have not been resolved however the system will refuse to reenable snooping.
>
> `multicast_router`
>
> This allows the user to forcibly enable/disable ports as having multicast routers attached. A port with a multicast router will receive all multicast traffic.
>
> The value 0 disables it completely. The default is 1 which lets the system automatically detect the presence of routers (currently this is limited to picking up queries), and 2 means that the ports will always receive all multicast traffic.
>
> Note: this setting can be enabled/disable on a per-port basis, also through sysfs interface (e.g. if eth0 is some bridge's active port, then you can adjust /sys/...../eth0/brport/multicast\_router)

You may want to add this command to your startup scripts so your don't lose these settings when you reboot.

```
sudo echo 2 > /sys/devices/virtual/net/lxcbr0/bridge/multicast_router
```

## Start Containers on Boot

If you would like your containers to be automatically started on boot, you'll need to add the following line to `/var/lib/lxc/NAME/config`, where NAME is your container's name. By the way, on my system the `/var/lib/lxc` directory is only accessible by root.

```
lxc.start.auto = 1
```

Check using `lxc-ls --fancy` to verify your containers are in fact started on boot.

## Port Forwarding

If you want to access the ONOS GUI from a browser on the host machine, you need to set up port forwarding on the VM. The following command forwards traffic on port 8181 to the first ONOS container (`$OC1`).

```
sudo iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 8181 -j DNAT --to $OC1:8181
```
