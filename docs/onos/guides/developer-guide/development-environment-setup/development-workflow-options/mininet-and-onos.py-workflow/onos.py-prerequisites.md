# onos.py Prerequisites

## Configuring your development VM (or server)

This document assumes that you already have a VM or server  (we recommend Ubuntu 16 LTS, in spite of an annoying kernel bug) where you can compile ONOS.

1. **Configure your VM with enough memory to run ONOS!**
   1. ONOS `java` processes tend to consume a ***huge*** amount of memory. (In the future ONOS may go on a diet, but for now it's pretty heavyweight.)  In order to run an ONOS cluster in a single VM, you should allocate a large amount of RAM to that VM. We recommend 2-4 GB (or more if you have it) for *each* ONOS node that you intend to run. So a 3-node cluster should be usable in a VM with 6-12 GB of RAM. You can see how much memory and CPU ONOS's java processes are using by running `top` - if you start using swap space, the performance of ONOS and Mininet will suffer greatly!
2. **You may find it more convenient to install a GUI in your VM if you haven't already**.
   1. In Ubuntu, you can use the default Ubuntu Unity desktop or the lighter-weight LXDE.
3. **For VirtualBox, you may wish to set up networking so that you can connect from your host machine into your VM**
   1. Usually this means adding a host-only interface to the VM, and making sure it's configured
   2. Make sure that interface has an IP address (you can check with `ifconfig` or `ip addr`)
   3. You may need to run `dhclient` manually

## Getting Mininet (and `bridge-utils)`

In order to use `onos.py`, you need Mininet, which is easy to install in a VM or server running a recent release of Ubuntu.

**Option 1**: If you are running Ubuntu 16.04 or later, you can easily install Mininet 2.2 (and `bridge-utils` for `LinuxBridge`) using `apt-get`:

```
sudo apt-get install mininet bridge-utils
```

**Option 2**: It's also easy to install Mininet from source in an Ubuntu VM or server:

```
git clone http://github.com/mininet/mininet
mininet/util/install.sh -nvfw
```

recommended options: `-n`: install core Mininet dependencies; `-v`: install Open vSwitch; `-f`: install legacy Stanford 1.0 user switch and controller; `-w`: install wireshark and improved OpenFlow wireshark dissector)

**Option 3**: You can also [download](http://mininet.org/download) a pre-built Mininet VM.

Ubuntu 16 Warning!

Unfortunately the Linux 4.4 series kernel shipped in Ubuntu 16.04 (and later, possibly) has a kernel bug/regression which periodically breaks Mininet (and other container systems.) If you see a console (or `dmesg`) message like `unregister_netdevice: waiting for lo to become free. Usage count = 1` you may have to reboot your Mininet VM to return things to normal. With luck this will be fixed in a future Linux kernel.

#### Verifying Your Mininet Installation

Make sure you are running Mininet version 2.2.1 or later:

```
mn --version
```

If not, try installing from the git repository as described above.

And make sure that Mininet works:

```
sudo mn --test pingall
```

If Mininet doesn't work, consult the [troubleshooting](troubleshooting-onos.py.md) page and/or the [Mininet FAQ](http://faq.mininet.org) for troubleshooting hints.

## Building ONOS

In order to run ONOS using onos.py, you will need a correctly built ONOS package in your VM.

We recommend building ONOS *in your Mininet VM or server* using `buck`:

```
cd ~/onos
tools/build/onos-buck build onos
```

Make sure that the build completes without errors - without a correctly built ONOS package, you will not be able to start ONOS.

You can also build elsewhere, copy `onos.tar.gz` into your development VM, and set `ONOS_TAR` to its full path. Since Java is platform independent, you can build on one OS (macOS, Windows) and run on another (Linux.)

It is also possible to share your ONOS source tree between a host system (e.g. Mac, Windows) and a VM (Linux) so that you can run your IDE on the host platform while using `onos.py` to run ONOS within the VM. (Todo: add more detailed instructions on how to do this!)
