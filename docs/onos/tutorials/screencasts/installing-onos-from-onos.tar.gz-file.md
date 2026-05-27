# Installing ONOS from onos.tar.gz file

## [YouTube Video](https://www.youtube.com/watch?v=hk1cPmp46n8)

## Overview

Since ONOS is open-source software, anyone is free to checkout the code and build ONOS from scratch. However, ready-to-run ONOS distribution is also available as a compressed *tar.gz* file, which can be downloaded from the the ONOS web-site.

This screencast will demonstrate how to deploy ONOS on multiple machines and it will show how easy it is to form a cluster from the individual ONOS instances using just the *tar.gz* file.

## Context

I will be using iTerm to download, configure and install ONOS on three machines at the same time. The machine’s IP addresses will be the following: 10.128.11.1, 10.128.11.2 and 10.128.11.3.

## Download ONOS tar.gz

First, let’s download the ONOS *tar.gz* distribution file. To do that, we will use wget, but you can use curl or your favourite browser. For our demonstration, we will download the latest daily snapshot of ONOS as follows:

```
$ wget http://downloads.onosproject.org/nightly/onos-1.2.0.latest-NIGHTLY.tar.gz
```

## Untar ONOS tar.gz

Once the download has completed, we will untar the package. I will extract it directly under the home directory, but you can chose an alternate location if you wish.

## Configure ONOS (Deprecated)

Once ONOS download has been extracted, we are ready to configure the environment to run ONOS. To do that we will run the supplied `bin/onos-config` tool and specify the IP prefix for the cluster network as follows:

```
$ bin/onos-config OurCluster 10.128.11.*
```

This will configure ONOS to use the given network for intra-cluster communications.

## Start ONOS

Having configured ONOS, we are now ready to start it. The recommended way to start it is to use some form of a Linux watchdog daemon, such as upstart for example. ONOS comes with `etc/onos.conf` configuration file, which can be used to copy under etc/init folder on Ubuntu to register ONOS as an upstart service.

In our demonstration, we will run ONOS directly, using the supplied `bin/onos-service` script. We will  run it in the server mode and in background as follows:

```
$ bin/onos-service server 1>/tmp/stdout.log 2>/tmp/stderr.log &
```

We can monitor the start-up progress by tailing the log file. Also, we can use the provider bin/onos tool to connect to ONOS command console via `ssh`. Typing the onos:nodes command will reveal that each instance is its own cluster, meaning that these instances are not aware of each other.

## Form ONOS cluster

To form a cluster from these individual instances is quite easy using the supplied `onos-form-cluster` tool.

We simply need to specify the IP addresses of all the cluster nodes and the tool will create a cluster configuration JSON object and upload it to each instance using its REST API.

```
$ bin/onos-form-cluster 10.128.11.1 10.128.11.2 10.128.11.3
```

To complete the operation, each instance will restart automatically and when they all come back up, they will be part of the same ONOS cluster.

We can verify this by connecting to the ONOS command console and typing the `onos:nodes` command again will reveal that each instance knows about the others.

## GUI & Mininet

To prove this further, let’s use the user interface pointed at the first ONOS instance to activate the OpenFlow providers.

Checking via `onos:apps` command, we can see that the providers were activated on all the cluster nodes.

Finally, just for fun, let’s switch the GUI to the topology view and then let’s start a simple mininet topology whose switches are configured with only one of the instances as their controller, say the second one. We can see that the information about the discovered switches was quickly propagated through the cluster as the GUI shows all the switches and the links between them.

## Conclusion

I hope that you find this screencast useful in deploying ONOS on your networks. Have a great day...
