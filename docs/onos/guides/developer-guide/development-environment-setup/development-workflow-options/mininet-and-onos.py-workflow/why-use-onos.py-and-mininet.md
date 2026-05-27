# Why use onos.py and Mininet?

If you are already running Mininet in a VM or on a physical server, it is easy to use `onos.py` to start up a complete emulated **ONOS network in a single VM** - including a ONOS cluster, modeled control network, and data network.

This simplifies development on a laptop, because you can run a **single development VM** (or no VM at all if you are running on a Linux machine!) Moreover, it is **more efficient** than a multi-VM setup because the entire emulated network lives in a single VM and shares a single Linux kernel.

Additionally, `onos.py` models the **control network** as well as the data network; you can easily change the number of nodes in your ONOS cluster, as well as things like the delay or bandwidth between nodes in the control network. It's even possible to change the control network topology as well as the data network topology. (We hope to make this more convenient and powerful in the future.)

`onos.py` provides a single, **unified console** via the `mininet-onos>` prompt, where you can enter both Mininet and ONOS commands - this can be very convenient! (We call this "One Console to Rule Them All.")

`onos.py` also automatically handles **port forwarding**, so you can easily connect to the GUI (or to karaf, or to the controllers' OpenFlow ports) by connecting to ports on the VM.

Chances are you're **already using Mininet**, so it's nice to be able to start an ONOS cluster using Mininet itself without installing or configuring additional software.

`onos.py` **parametrizes** both the control network (ONOS cluster) and the data network; so it's easy to iterate over multiple cluster sizes and network topologies.

We also hope that using `onos.py` will make ONOS development **easier** and more **fun**.
