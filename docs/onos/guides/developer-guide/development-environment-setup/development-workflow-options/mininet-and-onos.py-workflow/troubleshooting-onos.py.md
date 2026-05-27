# Troubleshooting onos.py

## Troubleshooting

#### `onos.py` doesn't work - what should I do?

Here are some things you can try:

* Make sure you've given your VM enough RAM - try using 2-4 GB for each ONOS node (so 6-12 GB for `--controller onos,3`) ; ONOS can be very memory-hungry!
* Make sure you are running the latest version of Mininet (see below)
* Look at the log file(s) and make sure no errors are occurring: `more /tmp/onos1/log; more /tmp/onos1/onos.log`
* Look at the output from running `mn` or `onos.py` and carefully examine and try to understand any error or exception messages - usually they will tell you what is going wrong
* Reset your environment using: `sudo pkill -f  karaf.jar; sudo mn -c`
* Make sure you have built onos: `cd ~/onos; buck build onos`
* Make sure you can run Mininet: `sudo mn --test pingall`
* Invoke Mininet in debug mode by adding the `-v debug` flag to see what is going wrong or hanging:
  + `sudo mn --custom onos.py --controller onos,1 --topo tree,2,2 -v debug`
  + You will want to pay careful attention to each operation as well as any error messages that are being displayed or exceptions that may be occurring.

#### Mininet doesn't work - what should I do?

First, make sure you are running Mininet 2.2.1 or later:

`mn --version`

If you have an older version of Mininet, you can install a newer version from source as described above. Older versions of Mininet may not include `LinuxBridge`, which is required by `onos.py`.

Next, make sure that the following command works:

```
sudo mnexec -n ifconfig -a
```

It should show a single loopback interface and no other interfaces. If this command doesn't work as expected, then Mininet will not work. If you have installed Mininet using `apt-get`, or from source on Ubuntu, Mininet should work correctly. However, you should make sure you don't have multiple or older versions of Mininet installed which might not work correctly with `onos.py`.

Once you've verified that `mnexec` works, you can try a sanity check for `mn`:

```
sudo mn --test pingall
```

This should complete without errors. If it doesn't, try invoking Mininet in debug mode so that you can see what isn't working:

```
sudo mn --test pingall -v debug
```

#### Why can `s1` ping `onos1`, but `onos1` can't ping `s1` (it just pings its own loopback interface?)

Currently, all of the switches are in the root namespace. If you wish to test connectivity from a switch to a controller, try pinging `nat0` instead. In the future we may add support for a more complex control network with separate IP addresses for the switch management interfaces.

#### Why is ONOS startup so slow?

On my laptop, a 3-node ONOS cluster typically takes about a minute to start up, and a single-node ONOS cluster takes up to 20 seconds to start up.

We hope to improve ONOS cluster startup performance in the future.

If your VM or server isn't heavily loaded but startup seems to be frozen for more than a couple of minutes, you can press `control-C` to interrupt `onos.py` startup and then:

```
sudo pkill java  # get rid of stale java processes  
sudo mn -c  # clean up stale Mininet state and interfaces
```

You can also look at `/tmp/onos1/log` to see if exceptions are occurring.

#### Why can't I connect to the GUI that is running somewhere inside my VirtualBox VM?

First, make sure that you've configured your VM appropriately to enable connectivity:

* Usually this means adding a host-only interface (and possibly configuring it with `dhclient`)
* Make sure that you know the correct IP address of the interface you're connecting to
* Make sure you can `ping` that interface from your client machine
* If you're using port forwarding in VirtualBox, double-check to make sure that you've set it up correctly and are connecting to the correct IP address
* Make sure that ONOS is running and that the GUI module is loaded and running
  + You can check this with the `onos:apps --active` CLI command
