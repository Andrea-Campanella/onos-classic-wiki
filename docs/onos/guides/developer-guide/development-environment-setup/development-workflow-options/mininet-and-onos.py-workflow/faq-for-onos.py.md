# FAQ for onos.py

#### 

### What do those `mn` command line options do?

`--custom onos.py`: uses `onos.py` to extend Mininet with new controller and switch types as well as a customized CLI

`--controller onos,3`: tells Mininet to start up an ONOS controller cluster with 3 ONOS nodes

`--topo torus,4,4`: tells Mininet to use a 4x4 torus topology for the data network

### What software switch does this use?

By default, it uses [Open vSwitch](http://openvswitch.org). `onos.py` replaces Mininet's `default` switch with a new switch class called `ONOSOVSSwitch` or `--switch onosovs`. This switch class knows how to connect to an ONOS cluster with multiple IP addresses.

### How can I use the user switch (or CPqD switch if I have it installed?)

In order to select the user switch (either Stanford reference switch or CPqD switch, depending on which one you have installed), you can use `--switch onosuser`.

### How can I get more information on Mininet, the `mn` command, writing Mininet scripts, etc.?

There are lots of things you can do with Mininet, including customizing your data network topology, setting link parameters, etc..

For more information on Mininet, please check out <http://docs.mininet.org>

### How can I specify the apps for ONOS to load?

For now, try using `ONOS_APPS` or connecting to the `karaf` console and using ONOS CLI commands.

```
# As root:
ONOS_APPS=drivers,openflow,fwd,proxyarp,mobility mn --custom onos.py --controller onos,3 --topo tree,3,3
# or (using sudo):
sudo env ONOS_APPS=drivers,openflow,fwd,proxyarp,mobility mn --custom onos.py --controller onos,3 --topo tree,3,3
# or
ONOS_APPS=drivers,openflow,fwd,proxyarp,mobility sudo -E mn --custom onos.py --controller onos,3 --topo tree,3,3
```

Note that `sudo` clears environment variables by default, but the `ONOS_APPS` environment variable must be set in order for `mn` to read it.

In the future, there should be an option to `--controller onos` and/or `ONOSCluster()`.

### How is the IP address range/subnet of the ONOS cluster specified?

`--controller onos` and `ONOSCluster()` take an `ipBase` option; the default is `192.168.123.0/24`

You can change it by passing in a new option to `mn` or to `ONOSCluster()`:

```
sudo mn --custom onos.py --controller onos,3,ipBase=172.1.2.0/24 --topo tree,3,3
```

### How can I run ONOS CLI commands from the mininet-onos> prompt?

There are several ways of doing it - you can use the one which works best for you. Here are four equivalent ways of invoking the `onos:apps` command:

```
mininet-onos> onos:apps
mininet-onos> onos :apps
mininet-onos> onos onos:apps
mininet-onos> onos1 client onos:apps
```

The first two methods can be used for executing any commands that begin with "`onos:`".

The last two methods can be used to execute any karaf command.

The final method can be used to run client on a specific ONOS instance (and connect to that instance.)

### How can I connect to the ONOS console from the `mininet-onos>` prompt?

```
mininet-onos> onos
```

press `control-D` to return to the `mininet-onos>` prompt.

### How can I connect to the ONOS console using `ssh`?

From a bash/shell prompt ***inside the Mininet VM***itself:

```
ssh -p 8101 karaf@192.168.123.1  # replace with the IP address of onos1 if it is different
```

In this example, `8101` is the karaf port, and `192.168.123.1` is the IP address of `onos1`.

From ***outside of the Mininet VM (***e.g. from the VM server):

```
ssh -p 8101 karaf@<VM's IP address>  # replace with the IP address of your VM (the one you can ssh into)
```

### How can I connect to the ONOS console using karaf's client?

Warning! Connecting to ONOS using karaf's client is deprecated.

This method is deprecated and may only work with older ONOS versions. For newer ONOS versions, you should connect using **`ssh`**.

Make sure karaf's `bin/` directory is in your path, then:

```
client -h 192.168.123.1   # or the address of the ONOS node you wish to connect to
```

### How can I connect to the ONOS GUI?

Since ONOS is running on Mininet hosts inside the VM, connecting to the GUI is usually done in one of two ways:

One relatively foolproof way is to run a **browser inside the VM**. Install a GUI in your VM if you haven't already (`sudo apt-get install lxde` and reboot), and then run a web browser pointed to the IP address of the ONOS node you want to talk to (for onos1, the default will be `http://192.168.123.1:8181/onos/ui` ). For the GUI to work well, you will want to make sure you've installed the appropriate VM support tools (such as virtualbox tools or VMware tools) for your virtualization platform.

A second (and probably more enjoyable) way is to use a **browser on your client machine** or server where the VM is running, as long as you have connectivity to the VM (make sure you can ping its IP address and/or connect to it using `ssh`, and make sure that it the ports on your VM aren't being blocked by a firewall.)

By default, `onos.py` **automatically forwards** connections to the Mininet VM/server to the appropriate ONOS instance.

| Service | VM port to connect to |
| --- | --- |
| **GUI/REST** | 8181 (`onos1`), 8182 (`onos2`) ... |
| **Karaf via `ssh`** | 8101 (`onos1`), 8102 (`onos2`) ... |
| **OpenFlow** | 6653 (`onos1`), 6654 (`onos2`) ... |

So if you are using a VM whose IP address is `192.168.x.y`, to connect to the GUI on ONOS1, you would use the URL`http://192.168.x.y:8181/onos/ui/`

Use the correct IP address!

You need to use the real, correct IP address for your VM - the address `192.168.x.y` is obviously not a real IP address!

If you are using VirtualBox, you will probably need to add a host-only interface to your VM and you may even need to run `dhclient` to make sure that that interface has an IP address. You can also set up port forwarding on a single interface - in this case you will want to make sure that it is set up for every port you wish to connect to (e.g. `8181` for the GUI on `onos1`.)

### What are the default user name and password for the GUI?

Usually `karaf/karaf` (or sometimes `onos/rocks`)

`onos.py` should also respect the values of `ONOS_WEB_USER` and `ONOS_WEB_PASS`.

### Can I use `onos.py` to control an external hardware (or virtual) network?

Yes you can! Simply use `--topo none` . For example:

```
mn --custom onos.py --controller onos,3 --topo none
```

`onos.py` will forward the ports (e.g. `6653`, `6654`, `6655`) appropriately as described above. Your Mininet VM or server will have to be reachable from the switches' management network, and you will need to configure your switches to connect to you ONOS nodes: the address of each node will be the VM's IP address, and the port will be the appropriate forwarded OpenFlow port.
