# Running ONOS with onos.py

## Starting up ONOS and your data network

After you've completed the prerequisites and built ONOS in the VM, you can use Mininet and `onos.py` to start up a virtual ONOS cluster and data network:

```
cd ~/onos/tools/dev/mininet
sudo mn --custom onos.py --controller onos,1 --topo tree,2,2
```

(In this example, our "cluster" is a single node, but we will change that in a minute!)

You should see a bunch of output showing the startup of the control network and the data network.

### Interacting with Mininet and ONOS (aka one CLI to rule them all)

After ONOS starts up and the switches connect, you should see the customized mininet CLI prompt:

```
mininet-onos>
```

At this point, you can **enter mininet commands** like `pingall` (all-to-all ping test) or `help` (to find out about Mininet CLI commands.)

You can also **enter [ONOS CLI](../../../../administrator-guide/interacting-with-onos/the-onos-cli.md) commands** like `onos:apps` or `onos:balance-masters` and they should be invoked via karaf's `client` command on `onos1`.

You can also **invoke the ONOS client** using the `onos` command - press `control-D` to exit.

You can also connect to the ONOS GUI by following the instructions below.

To exit Mininet, use the `exit` command or press `control-D`.

Once you have verified that a single-node ONOS cluster and simple topology are working correctly, you can try a larger cluster (we recommend 3 nodes if you have configured your VM to use 6-12 GB of RAM) and a larger or more interesting topology (such as a 4x4 torus):

```
sudo mn --custom onos.py --controller onos,3 --topo torus,4,4
```

Pay close attention to error messages - they are there for a reason!

If things don't start up correctly, look carefully at any error messages or exceptions which may have been generated - usually they give you important information which will enable you to figure out what is going wrong and to fix the issue. Also check out the [troubleshooting](troubleshooting-onos.py.md) section.

### Connecting to the [ONOS GUI](#)

One way to connect to the [ONOS GUI](#) is to run a **browser inside the VM**. Install a GUI in your VM if you haven't already (`sudo apt-get install lxde` and reboot), and then run a web browser pointed to the IP address of the ONOS node you want to talk to (for onos1, the default will be `http://192.168.123.1:8181/onos/ui` ). For the GUI to work well, you will want to make sure you've installed the appropriate VM support tools (such as virtualbox tools or VMware tools) for your virtualization platform.

Another (perhaps more enjoyable) way is to run a **browser on your client machine** or server where the VM is running, as long as you have connectivity to the VM (make sure you can ping its IP address and/or connect to it using `ssh`, and make sure that it the ports on your VM aren't being blocked by a firewall.)

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

### Starting ONOS with debug option

You can start ONOS cluster as debug mode with debug option 'debug=True'.

```
sudo mn --custom onos.py --controller onos,3,debug=True --topo torus,4,4
```

For debugging ONOS with intelliJ IDEA, refer to [Debugging ONOS with IntelliJ IDEA.](../../../../../tutorials/screencasts/debugging-onos-with-intellij-idea.md)
