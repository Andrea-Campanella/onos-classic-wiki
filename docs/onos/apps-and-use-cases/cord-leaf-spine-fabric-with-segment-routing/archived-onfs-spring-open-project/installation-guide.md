# Installation Guide

UPDATE: SPRING-OPEN has not been supported since 2016. Please refer to docs.trellisfabric.org for a similar offering. Links on this page may no longer work

SPRING-OPEN is not built on the latest version of ONOS (Avocet). It is built on the previous (internal) release of ONOS (Sept 2014). The source code for this project is available from the url below. To try out the prototype, you will need this version of ONOS, and you will also need the CLI that works with this version of the controller. For the switches, you have the choice of using software or hardware segment-routers. The software routers are built from a version of the CPqD OF 1.3 software switch. The hardware routers are built with Dell 4810 switches.

To get started we recommend downloading the pre-built VM from the link below. This VM has the specific version of ONOS (and its dependencies), the specific CLI, and the specific version of the CPqD OF1.3 software switch required for this project. It includes the [Mininet network emulator](http://mininet.org/) required to run the software switches in a network topology of your choice. It also includes the recommended Wireshark dissector for OF1.3.4 protocol messages from the [loxigen project](https://github.com/floodlight/loxigen).

If you do not wish to use this pre-built VM, you can download from source, and follow the installation directions below.

# Pre-built VM

Download the pre-built VM (2.4 GB) from the URL: <http://downloads.onosproject.org/spring-open/SPRING-OPEN.ova>

Get a recent version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to import and run the VM.

You can login to the VM with login:mininet and password:mininet. Then ifconfig to note the IP address assigned to the VM (if you used Bridged-mode and DHCP in the VM's network settings).

You should now be able to ssh into the mininet VM and follow the [Getting Started Tutorial](user-guide/getting-started-tutorial.md)

# ONOS for SPRING-OPEN

If you wish to build from source, download the SPRING-OPEN version of the ONOS controller source code. We are assuming you are running in an Ubuntu linux environment.

```
sudo apt-get install openjdk-7-jdk openjdk-7-doc openjdk-7-jre-lib
git clone https://gerrit.onosproject.org/spring-open
```

You will also need Zookeeper 3.4.6: <http://apache.arvixe.com/zookeeper/stable/>

Download the tar file, and untar it in your home directory.

```
tar xzf zookeeper-3.4.6.tar.gz
```

Run the controller Setup

```
cd ~/spring-open
./onos.sh setup
```

Compile the Controller code.

```
mvn clean
mvn compile
```

To run the controller

```
./onos.sh start
```

To see the controller logs

```
tail -f onos-logs/onos.<host-name>.log
```

Note that ONOS needs to be configured to run a segment routed network. See [Configuring ONOS (spring-open)](user-guide/configuring-onos-spring-open.md) for more details.

To stop the controller

```
./onos.sh stop
```

# CLI for SPRING-OPEN

The CLI used for this project is a modified version of the CLI originally submitted to open-source here: <https://github.com/opendaylight/net-virt-platform/tree/master/cli>

Download a basic functioning build environment plus a few build-time dependencies.

```
sudo apt-get install unzip python-dev python-virtualenv build-essential
```

Download the source code

```
git clone https://gerrit.onosproject.org/spring-open-cli
```

Build the code

```
cd spring-open-cli
./setup.sh
```

To run the CLI, make sure you have the latest code. From the spring-open-cli folder

```
$ git pull
$ source ./workspace/ve/bin/activate
(ve)$ make start-sdncon
(ve)$ cd cli/
(ve)$ ./cli.py
version200
default controller: 127.0.0.1:8000, SDN OS 1.0 - custom version
> enable
#
```

By default the CLI tries to connect to the controller on localhost and expects the controller to be listening on port 8080 (127.0.0.1:8080). To make the CLI connect to a controller on a different host, use

```
./cli.py --controller <ip-addr-of-controller-host>:<port>
```

To see what you can do with the CLI, consider the [Using the CLI section of the User Guide](user-guide/using-the-cli.md). You could also watch the [Prototype demo videos](prototype-demo-videos.md) which make heavy use of the CLI.

# Dell Hardware Switches

For this you will need [Dell 4810 switches](http://www.dell.com/us/business/p/force10-s-series/pd). If you are a network operator and you wish to try out this prototype (for free) in your lab, contact [Saurav Das](mailto:sauravdas@alumni.stanford.edu) or [Jaiwant Virk](mailto:Jaiwant_Virk@dell.com).

Once you have the switches, you will need to load the Force10 OS (FTOS) version the binary for which can be freely downloaded below

Disclaimer

Dell platforms supported by this build are the 4810/4820t.  
This FTOS version is solely for the purpose of features that are part of this project. It is not meant to be used in production and Dell support will not respond to any queries for this version. Dell will not support any bugs solely on the basis of downloading the binary.

Download (~48MB):  <http://downloads.onosproject.org/spring-open/FTOS-SE-1-0-0-3516.bin>

The Dell hardware will be preloaded with a different version of FTOS. Here are few things we need to do before we load the FTOS version for the project. These include configuring the management interface to your management network specifics. Note that the controller needs to be accessible via the management interface for OpenFlow communication between the controllers and switches. We also need to provide ssh access into the switch. Use the console port (and a terminal emulator) for the configuration below.

```
#conf
(conf)# interface managementethernet 0/0
(conf-if-ma-0/0)# ip address <ip-addr-of-mgmt-interface>
(conf-if-ma-0/0)# no shutdown
(conf-if-ma-0/0)# exit
(conf)# management route 0.0.0.0/0 <gateway-ip>
(conf)# username <your-username> password <set-a-pwd> privilege 15
(conf)# ip ssh server enable
(conf)# ip ssh password-authentication enable
(conf)# exit
# sh running config
```

Once the above configuration is complete, the switch should be accessible via ssh. Copy the downloaded FTOS version to the switch using scp from your local machine.

```
$ scp <path/to/>FTOS-SE-1-0-0-3516.bin <username>@<switch-management-IP-addr>:FTOS-SE-1-0-0-3516.bin
```

Now login to the switch using ssh to enter the following commands to load the binary you just copied over. First check that you can see the file in the flash.

```
sr101#dir
Directory of flash:

  1  drwx       4096   Dec 31 1979 16:00:00 -08:00 .  
  2  drwx       3072   Dec 06 2014 03:29:42 -08:00 ..  
  3  drwx       4096   Mar 01 2004 09:35:14 -08:00 TRACE_LOG_DIR  
  4  drwx       4096   Mar 01 2004 09:35:14 -08:00 CORE_DUMP_DIR  
  5  d---       4096   Mar 01 2004 09:35:16 -08:00 ADMIN_DIR  
  6  drwx       4096   Mar 01 2004 09:35:16 -08:00 RUNTIME_PATCH_DIR  
  7  drwx       4096   Nov 28 2014 05:22:32 -08:00 CONFIG_TEMPLATE  
  8  -rwx       6821   Dec 04 2014 07:02:08 -08:00 startup-config  
  9  -rwx   48661501   Nov 28 2014 04:24:34 -08:00 FTOS-SE-1-0-0-3516.bin  
 10  drwx       4096   Aug 24 2013 05:00:16 -08:00 CONFD_LOG_DIR  
 11  -rwx       4094   Nov 04 2014 06:06:10 -08:00 inetd.conf  
 12  -rwx         32   Nov 04 2014 06:06:18 -08:00 ssCronCopy.txt  
 13  -rwx       6278   Nov 01 2014 01:22:30 -08:00 startup-config.bak  
 14  -rwx     230695   Dec 04 2014 07:02:16 -08:00 confd_cdb.tar.gz  
 15  -rwx   39585701   Nov 04 2014 06:10:58 -08:00 BAK-FTOS.bin  

flash: 2056916992 bytes total (1864204288 bytes free)
```

Upgrade the OS. It takes a few minutes.

```
sr101# upgrade system flash://FTOS-SE-1-0-0-3516.bin A:
! .....
 
sr101# reload
```

Once the upgrade is done, reload the box. You will of course lose your ssh session. But once it is back, login again to [configure the OpenFlow instance](user-guide/configuring-dell-hardware-switches.md).

# CPqD Software Switch

**A little history:** The goal of this project was to demonstrate SDN control of segment routing on switching hardware that exists today. We did that with the Dell 4810 switches. However, during controller development we mostly relied on a software switch that could emulate the Hardware Abstraction Layer that the Dell team was building the FTOS to support. In other words, we needed a software switch that we could put in Mininet, and point to the controller to pretend to be a segment routed network. But more importantly the **software switch had to emulate the hardware pipeline**, so that when we actually moved to hardware switches, there would be minimal changes in the controller.

In reality the hardware switching ASIC has tens of tables. The controller does not need to know all the tables, registers etc. Many of the tables can be  abstracted away by creating the right Hardware Abstraction Layer. Think of it as the contract between the controller and the switch – the switch supports the HAL and the controller programs the switch according to the HAL. In OpenFlow terms such a HAL is known as a Typed Table Pipeline (TTP). The [ONF's Forwarding Abstractions WG](https://www.opennetworking.org/technical-communities/areas/specification) is working on this topic. For our project we developed our own TTP known as the [SPRING-OPEN TTP](software-architecture.md).

And so, in our project we needed a switch we could use to support the SPRING-OPEN TTP. At the time we started the project (May 2014) the only software switch that supported OF 1.3 was the [CPqD software switch](https://github.com/CPqD/ofsoftswitch13). Around the August timeframe [OVS released v2.3.0](http://openvswitch.org/download/) which also supported OF1.3. However we chose to continue to use the CPqD switch for the following reasons:

* We needed the software switch to support the TTP - part of the TTP required the use of an OpenFlow feature called 'group-chaining', where one group points to another group which in turn could point to a third group or an outgoing-port. Support for this feature is optional as per the OF 1.3.4 specification. OVS v2.3.0 does not support this optional feature. The CPqD switch does.
* Performance of the software switch dataplane (eg. packets switched per second) was not an issue for us in this project. The job of the software switch was to help in controller development for which switching performance is not critical. OVS is a production quality switch; CPqD is not. But this did not matter as ultimately we work on hardware switches which forwards packets at wire-speed.
* Because of the tight timelines in this project, if we found bugs in the switch, we wanted to quickly fix the bugs ourselves instead of depending on a third party to fix the bugs for us. The CPqD switch is a simpler switch than OVS and so its easier to fix bugs.

Having said that, we do have to jump through some hoops to get the switch to work from source. **Again this is only necessary if you did not download the pre-built VM above** (the VM has the CPqD switch ready to run).

1. Download the source code. If you already have Mininet installed in your system, run the following script - it will download the CPqD software switch and try to install it.

   ```
   mininet/util/install.sh -3f
   ```
2. Or you can download from the CPqD github repo. Check if you can compile it. It may fail ...

   ```
   git clone https://github.com/CPqD/ofsoftswitch13.git
   cd ~/ofsoftswitch13
   ./boot.sh
   ./configure
   make
   sudo make install
   ```
3. If your compile step failed [go to this page fix this issue](installation-guide/cpqd-1.3-switch-on-recent-ubuntu-versions.md). Once you can successfully compile, go to the next step.
4. Once the switch compiles, we are unfortunately not done yet. There are some bugs in the switch, which we have fixed. So we need to patch the code with these fixes. Why patch? Why did we not just submit our fixes upstream so everyone can benefit from our fixes? Well the answer is that while we have made fixes, we have made them in a hacky way - we have taken shortcuts just to make things work and move on because of the tight deadlines in this project. Hopefully these issues will be fixed in a clean way by the switch maintainers. For now, we need to patch the code. To start with we need to go back to the specific checkin on which the patch applies. In the ofsoftswitch13 folder, enter

   ```
   git checkout -b cpqd-spring 36738aeb3501f66fb382e7b59138c88e8843b19c
   ```
5. Now when you do 'git log' you should see this

   ```
   mininet@mininet-vm:~/ofsoftswitch13$ git log

   commit 36738aeb3501f66fb382e7b59138c88e8843b19c
   Author: Jean Tourrilhes <jean.tourrilhes@hp.com>
   Date:   Mon Aug 25 17:00:13 2014 -0700

       Fix a few more warnings.

   commit bd8e7b68951c5ef2293d0a0e45c89b265a2eba17
   Author: Jean Tourrilhes <jean.tourrilhes@hp.com>
   Date:   Mon Aug 25 16:50:09 2014 -0700


       Finish reverting EXT-192/EXT-276 Role Status (1.4 feature).

   ...
   ```
6. Download the following patch: [patchfile-cpqd](../../../../assets/patchfile-cpqd.bin)

   You can apply the patch with the command

   ```
   patch -p0 < patchfile-cpqd
   ```
7. Now if you do 'git status', you should see something like

   ```
   mininet@mininet-vm:~/ofsoftswitch13$ git status
   On branch cpqd-spring
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git checkout -- <file>..." to discard changes in working directory)

   	modified:   oflib/oxm-match.c
   	modified:   secchan/port-watcher.c

   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   	.deps/
   	patchfile
   	utilities/ofp-read
   	utilities/ofp-read.o

   no changes added to commit (use "git add" and/or "git commit -a")
   mininet@mininet-vm:~/ofsoftswitch13$
   ```
8. Finally, compile again

   ```
   mininet@mininet-vm:~/ofsoftswitch13$ make
   mininet@mininet-vm:~/ofsoftswitch13$ sudo make install
   ```

Now you are ready to use the switch in Mininet. See [Configuring CPqD Software Switches](user-guide/configuring-cpqd-software-switches.md).
