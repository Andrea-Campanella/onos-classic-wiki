# Running the published Docker ONOS images in a Cluster (OUTDATED)

This document describes the steps you need to take to build yourself a cluster of ONOS docker images.

[Check this 2 min screencast that goes through this tutorial.](https://www.youtube.com/watch?v=IvfcI3yl78E)

This tutorial assumes that you have docker installed on your system.

You can install it on Ubuntu systems by following the instructions outlined here: <https://docs.docker.com/installation/ubuntulinux/#installation>

## Download the ONOS Docker image

The ONOS docker image is built and published on docker hub (as an automated build). You can simply obtain it by running:

```
docker pull onosproject/onos
```

Please note that this is the latest and greatest ONOS. The build occurs every time code is pushed to GitHub. There are also tagged versions available for previous versions of ONOS.

At this point you should have a copy of the ONOS docker image.

```
$ sudo docker images
REPOSITORY                   TAG                   IMAGE ID            CREATED                  VIRTUAL SIZE
...
onosproject/onos             latest                a427c3589892        Less than a second ago   736.5 MB
...
```

## Run your docker image

Now that the image has been downloaded, let's start a few instances of ONOS.

```
$ sudo docker run  -t -d --name onos1 onosproject/onos 
<cid>
$ sudo docker run  -t -d --name onos2 onosproject/onos 
<cid>
$ sudo docker run  -t -d --name onos3 onosproject/onos 
<cid>
```

Now you have three instance of ONOS running.

## Cluster-ize your instances

Now you have three instances of ONOS. Each of these instances is running independently but we want them to run in a cluster. First we need to download a utility (called onos-form-cluster) that will make it easy for us to form the cluster:

```
$ wget https://raw.githubusercontent.com/opennetworkinglab/onos/master/tools/package/bin/onos-form-cluster
--2015-03-19 19:28:59--  https://raw.githubusercontent.com/opennetworkinglab/onos/master/tools/package/bin/onos-form-cluster
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.27.79.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.27.79.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 717 [text/plain]
Saving to: ‘onos-form-cluster’
100%[=========================================================================================================================]
2015-03-19 19:29:00 (225 MB/s) - ‘onos-form-cluster’ saved [717/717]
```

Then let's make this file an executable:

```
$ chmod u+x onos-form-cluster
```

Next I recommend adding the following to your .bashrc, it will make it easier to get the docker instance IP.

```
docker-ip() {
  sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' "$@"
}
```

Once you have this added do not forget to re-source your .bashrc file:

```
$ . ~/.bashrc
```

Now you are ready to form your cluster by simply running the following:

```
$ ./onos-form-cluster -u karaf -p karaf `docker-ip onos1` `docker-ip onos2` `docker-ip onos3`
```

Notice that the names onos1, onos2, and onos3 are the names you gave your instances when you ran them.

The previous command caused the ONOS instances to restart and come back up as a cluster. We can observe this by ssh'ing into one onos instance:

```
$ ssh -p 8101 karaf@`docker-ip onos1` # password is karaf
Password authentication
Password: 
Welcome to Open Network Operating System (ONOS)!
     ____  _  ______  ____   
    / __ \/ |/ / __ \/ __/    
   / /_/ /    / /_/ /\ \       
   \____/_/|_/\____/___/      
                             

Hit '<tab>' for a list of available commands
and '[cmd] --help' for help on a specific command.
Hit '<ctrl-d>' or type 'system:shutdown' or 'logout' to shutdown ONOS.
onos> nodes
id=172.17.0.73, address=172.17.0.73:9876, state=ACTIVE, updated=39m ago *
id=172.17.0.74, address=172.17.0.74:9876, state=ACTIVE, updated=39m ago 
id=172.17.0.75, address=172.17.0.75:9876, state=ACTIVE, updated=39m ago
```

And now we have a formed ONOS cluster. Pretty easy right?! ![(big grin)](../../assets/biggrin.svg)

## Activate Openflow

Now, the cluster only have essential apps running. To give it a try, activate openflow and the forwarding app:

```
onos> app activate org.onosproject.openflow
onos> app activate org.onosproject.fwd
```

Let's connect mininet to it:

```
sudo mn --topo tree,2 --controller remote,ip=`docker-ip onos1`
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 s2 s3 
*** Adding links:
(s1, s2) (s1, s3) (s2, h1) (s2, h2) (s3, h3) (s3, h4) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 3 switches
s1 s2 s3 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 
h2 -> h1 h3 h4 
h3 -> h1 h2 h4 
h4 -> h1 h2 h3 
*** Results: 0% dropped (12/12 received)
mininet>
```

## Remarks

The ONOS cluster you just created is not running any specific application. To install an application you will need to use the [onos-app](https://github.com/opennetworkinglab/onos/blob/master/tools/dev/bin/onos-app) utility as documented in [Application Subsystem](../guides/architecture-and-internals-guide/application-subsystem.md).

# Building your own ONOS docker image

If you have modified the source code of ONOS, you might want to build your modified ONOS into your own docker image so that you can run it in some environment. The following command will build an ONOS docker image out of an ONOS source tree:

```
$ docker build -t onosproject/onos:test .
```

This builds an image with the tag `onosproject/onos:test`, and of course you are free to tag your image however you'd like.
