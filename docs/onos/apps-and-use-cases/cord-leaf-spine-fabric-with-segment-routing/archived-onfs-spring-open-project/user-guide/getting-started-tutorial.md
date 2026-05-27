# Getting Started Tutorial

This quick tutorial will walk you through the launch of the controller, cli and mininet, all contained within the pre-built VM. 

1. Download SPRING-OPEN VM here: <http://downloads.onosproject.org/spring-open/SPRING-OPEN.ova>
2. Use VirtualBox to import and run the SPRING-OPEN VM.
3. From a terminal on your host machine, use ssh to login to the VM using the following username (mininet) and password (mininet). Yes, it is a Mininet VM where we have loaded other stuff, which is why the username@host will show up as 'mininet@mininet-vm'. Of course, you have to replace the ip-address shown below '10.1.9.125' with the IP address assigned to the VM during startup.

   ```
   $ ssh -X mininet@10.1.9.125
   mininet@10.1.9.125's password: 
   Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-24-generic x86_64)
    * Documentation:  https://help.ubuntu.com/
   Last login: Mon Dec  1 20:11:46 2014

   mininet@mininet-vm:~$ ls -l
   total 1592
   drwxrwxr-x 13 mininet mininet    4096 Jul 18 05:47 mininet
   drwxrwxr-x 11 mininet mininet    4096 Jan 10  2013 nbeesrc-jan-10-2013
   drwxrwxr-x 16 mininet mininet    4096 Nov 27 15:16 ofsoftswitch13
   -rw-rw-r--  1 mininet mininet 1605450 Nov 25 15:26 openflow.lua
   drwxrwxr-x 16 mininet mininet    4096 Dec  4 15:55 spring-open
   drwxrwxr-x 11 mininet mininet    4096 Dec  4 15:50 spring-open-cli
   drwxr-xr-x 10 mininet mininet    4096 Feb 20  2014 zookeeper-3.4.6
   mininet@mininet-vm:~$
   ```
4. Pull the latest controller code. When pulling code, another screen may pop up declaring a merge operation – just hit Control-X to get rid of it.

   ```
   mininet@mininet-vm:~$ cd spring-open
   mininet@mininet-vm:~/spring-open$ git pull
   ```
5. Make sure that the network-configuration file to be loaded on the controller says 'sr-ecmp10-demo.conf' — see the last line below

   ```
   mininet@mininet-vm:~/spring-open$ cat conf/onos.properties 
   floodlight.modules = net.floodlightcontroller.core.FloodlightProvider,\
   net.floodlightcontroller.threadpool.ThreadPool,\
   net.onrc.onos.core.topology.TopologyPublisher, \
   net.onrc.onos.core.datagrid.HazelcastDatagrid,\
   net.onrc.onos.core.flowprogrammer.FlowProgrammer,\
   net.onrc.onos.core.intent.runtime.PathCalcRuntimeModule,\
   net.onrc.onos.core.intent.runtime.PlanInstallModule,\
   net.onrc.onos.core.registry.ZookeeperRegistry, \
   net.onrc.onos.core.metrics.OnosMetricsModule, \
   net.onrc.onos.apps.websocket.WebSocketModule, \
   net.onrc.onos.core.main.config.DefaultConfiguration, \
   net.onrc.onos.apps.segmentrouting.SegmentRoutingManager
   net.floodlightcontroller.restserver.RestApiServer.port = 8080
   net.floodlightcontroller.core.FloodlightProvider.openflowport = 6633
   net.floodlightcontroller.core.FloodlightProvider.workerthreads = 16
   net.floodlightcontroller.core.FloodlightProvider.cpqdUsePipeline13 = true
   net.floodlightcontroller.forwarding.Forwarding.idletimeout = 5
   net.floodlightcontroller.forwarding.Forwarding.hardtimeout = 0
   net.onrc.onos.apps.websocket.WebSocketModule.port = 8081
   net.floodlightcontroller.core.FloodlightProvider.cpqdUsePipeline13 = true
   # NOTE: Do NOT modify or remove the line below. This value will be overwritten by onos.sh script.
   net.onrc.onos.core.datagrid.HazelcastDatagrid.datagridConfig = 
   # Uncomment and list all the ZooKeeper instances after localhost on multi-instance deployment.
   #net.onrc.onos.core.registry.ZookeeperRegistry.connectionString = localhost:2181,otherhost:2181
   # Specify a network configuration file to be used by the NetworkConfigManager
   net.onrc.onos.core.configmanager.NetworkConfigManager.networkConfigFile = conf/sr-ecmp10-demo.conf
   ```
6. Run the SPRING-OPEN version of the ONOS controller

   ```
   mininet@mininet-vm:~/spring-open$ ./onos.sh start
   Starting ZooKeeper ... ls: cannot access /home/mininet/spring-open/onos-logs/zk.mininet-vm.log*: No such file or directory
   JMX enabled by default
   Using config: /home/mininet/spring-open/conf/zoo.cfg
   Starting zookeeper ... STARTED
   Starting ONOS controller ...  STARTED
   ```

   You can check if the controller is running correctly as following

   ```
   mininet@mininet-vm:~/spring-open$ ./onos.sh status
   [ZooKeeper]
   JMX enabled by default
   Using config: /home/mininet/spring-open/conf/zoo.cfg
   Mode: standalone
   [RAMCloud coordinator]
   0 RAMCloud coordinator running
   [RAMCloud server]
   0 RAMCloud server running
   [ONOS core]
   1 instance of onos running
   ```
7. You can watch the controller logs if you wish

   ```
   mininet@mininet-vm:~/spring-open$ tail -f onos-logs/onos.mininet-vm.log
   2014-12-04 18:03:48,435 DEBUG [main] n.f.c.i.Controller [Controller.java:832] OFMessageListeners for FLOW_REMOVED: planInstall,
   2014-12-04 18:03:48,436 DEBUG [main] n.f.c.i.Controller [Controller.java:832] OFMessageListeners for BARRIER_REPLY: flowpusher,
   2014-12-04 18:03:48,436 DEBUG [main] n.f.c.i.Controller [Controller.java:832] OFMessageListeners for PACKET_IN: linkdiscovery,hostmanager,packetmodule,
   2014-12-04 18:03:48,438 DEBUG [main] n.f.c.i.Controller [Controller.java:832] OFMessageListeners for PORT_STATUS: linkdiscovery,
   2014-12-04 18:03:48,438 DEBUG [main] n.f.c.i.Controller [Controller.java:840] SwitchUpdate Listeners: FlowProgrammer,linkdiscovery,topologyPublisher,
   2014-12-04 18:03:48,802 INFO [main] n.f.c.i.Controller [Controller.java:1126] Listening for switch connections on 0.0.0.0/0.0.0.0:6633
   ```
8. Open another terminal to run Mininet

   ```
   mininet@mininet-vm:~$ cd mininet/
   mininet@mininet-vm:~/mininet$ cd custom/
   mininet@mininet-vm:~/mininet/custom$ sudo ./testEcmp_10sw.py 
   *** Creating network
   *** Adding controller
   *** Adding hosts:
   h1 h2 h3 h4 
   *** Adding switches:
   s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 
   *** Adding links:
   (h1, s1) (h2, s6) (h3, s7) (h4, s10) (s1, s2) (s1, s3) (s2, s3) (s2, s5) (s2, s8) (s2, s9) (s3, s4) (s4, s5) (s4, s6) (s5, s6) (s5, s8) (s5, s9) (s7, s8) (s7, s9) (s8, s9) (s8, s10) (s9, s10) 
   *** Configuring hosts
   h1 h2 h3 h4 
   *** Starting controller
   *** Starting 10 switches
   s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 
   *** Starting CLI:
   mininet>
   ```
9. On another terminal run the SPRING-OPEN CLI

   ```
   mininet@mininet-vm:~$ cd spring-open-cli/
   mininet@mininet-vm:~/spring-open-cli$ source ./workspace/ve/bin/activate
   (ve)mininet@mininet-vm:~/spring-open-cli$ sudo make start-sdncon
   if ! lsof -iTCP:8000 -sTCP:LISTEN >/dev/null; then \
   	( \
   	  cd /home/mininet/spring-open-cli/sdncon; \
   	  [ -d /home/mininet/spring-open-cli/workspace/ve/cassandra/data/sdncon ] || python manage.py syncdb --noinput; \
   	  /home/mininet/spring-open-cli/build/start-and-wait-for-port.sh -p 8000 -l /home/mininet/spring-open-cli/workspace/ve/log/sdncon.log python manage.py runserver 0.0.0.0:8000; \
   	); \
   	fi
   Creating tables ...
   Installing custom SQL ...
   Installing indexes ...
   No fixtures found.
   Launching python manage.py runserver 0.0.0.0:8000 (log: /home/mininet/spring-open-cli/workspace/ve/log/sdncon.log)
   Waiting for port 8000.... OK
   +++ sdncon running
   (ve)mininet@mininet-vm:~/spring-open-cli$ cd cli/
   (ve)mininet@mininet-vm:~/spring-open-cli/cli$ ./cli.py 
   version200
   default controller: 127.0.0.1:8000, SDN OS 1.0 - custom version
   mininet-vm> enable
   mininet-vm#
   ```
10. Check if all the switches are connected to SPRING-OPEN controller using the controller CLI.

    ```
    mininet-vm# sh switch 
    #  Switch DPID             Alias        Connected Since              Connected At    Type   Controller
    --|-----------------------|------------|----------------------------|---------------|------|----------
    1  00:00:00:00:00:00:00:01 SFO-ER1      Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60315 packet mininet-vm
    2  00:00:00:00:00:00:00:02 SFO-CR2      Thu Dec 04 16:45:03 PST 2014 127.0.0.1:60311 packet mininet-vm
    3  00:00:00:00:00:00:00:03 SFO-CR3      Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60319 packet mininet-vm
    4  00:00:00:00:00:00:00:04 Dallas-CR4   Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60313 packet mininet-vm
    5  00:00:00:00:00:00:00:05 Dallas-CR5   Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60320 packet mininet-vm
    6  00:00:00:00:00:00:00:06 Dallas-ER6   Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60314 packet mininet-vm
    7  00:00:00:00:00:00:00:07 NewYork-ER7  Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60316 packet mininet-vm
    8  00:00:00:00:00:00:00:08 NewYork-CR8  Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60312 packet mininet-vm
    9  00:00:00:00:00:00:00:09 NewYork-CR9  Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60317 packet mininet-vm
    10 00:00:00:00:00:00:00:0a NewYork-ER10 Thu Dec 04 16:45:05 PST 2014 127.0.0.1:60318 packet mininet-vm
    mininet-vm# sh link 
    #  Src Switch DPID                        Src Port Dst Switch DPID                        Dst Port Type
    --|--------------------------------------|--------|--------------------------------------|--------|------
    1  00:00:00:00:00:00:00:01 (SFO-ER1)      3        00:00:00:00:00:00:00:03 (SFO-CR3)      1        packet
    2  00:00:00:00:00:00:00:01 (SFO-ER1)      4        00:00:00:00:00:00:00:03 (SFO-CR3)      4        packet
    3  00:00:00:00:00:00:00:02 (SFO-CR2)      1        00:00:00:00:00:00:00:01 (SFO-ER1)      2        packet
    4  00:00:00:00:00:00:00:02 (SFO-CR2)      3        00:00:00:00:00:00:00:05 (Dallas-CR5)   1        packet
    5  00:00:00:00:00:00:00:02 (SFO-CR2)      4        00:00:00:00:00:00:00:09 (NewYork-CR9)  3        packet
    6  00:00:00:00:00:00:00:02 (SFO-CR2)      5        00:00:00:00:00:00:00:08 (NewYork-CR8)  3        packet
    7  00:00:00:00:00:00:00:02 (SFO-CR2)      6        00:00:00:00:00:00:00:08 (NewYork-CR8)  6        packet
    8  00:00:00:00:00:00:00:03 (SFO-CR3)      2        00:00:00:00:00:00:00:02 (SFO-CR2)      2        packet
    9  00:00:00:00:00:00:00:03 (SFO-CR3)      3        00:00:00:00:00:00:00:04 (Dallas-CR4)   1        packet
    10 00:00:00:00:00:00:00:04 (Dallas-CR4)   2        00:00:00:00:00:00:00:05 (Dallas-CR5)   2        packet
    11 00:00:00:00:00:00:00:05 (Dallas-CR5)   4        00:00:00:00:00:00:00:08 (NewYork-CR8)  4        packet
    12 00:00:00:00:00:00:00:05 (Dallas-CR5)   5        00:00:00:00:00:00:00:09 (NewYork-CR9)  5        packet
    13 00:00:00:00:00:00:00:06 (Dallas-ER6)   2        00:00:00:00:00:00:00:04 (Dallas-CR4)   3        packet
    14 00:00:00:00:00:00:00:06 (Dallas-ER6)   3        00:00:00:00:00:00:00:05 (Dallas-CR5)   3        packet
    15 00:00:00:00:00:00:00:08 (NewYork-CR8)  1        00:00:00:00:00:00:00:07 (NewYork-ER7)  2        packet
    16 00:00:00:00:00:00:00:08 (NewYork-CR8)  2        00:00:00:00:00:00:00:09 (NewYork-CR9)  1        packet
    17 00:00:00:00:00:00:00:08 (NewYork-CR8)  5        00:00:00:00:00:00:00:0a (NewYork-ER10) 3        packet
    18 00:00:00:00:00:00:00:09 (NewYork-CR9)  4        00:00:00:00:00:00:00:07 (NewYork-ER7)  3        packet
    19 00:00:00:00:00:00:00:0a (NewYork-ER10) 2        00:00:00:00:00:00:00:09 (NewYork-CR9)  2        packet
    ```
11. Test connections in mininet

    ```
    mininet> pingall
    *** Ping: testing ping reachability
    h1 -> h2 h3 h4 
    h2 -> h1 h3 h4 
    h3 -> h1 h2 h4 
    h4 -> h1 h2 h3 
    *** Results: 0% dropped (12/12 received)
    ```
12. Done. Here are some things you could do next:

* + See the [prototype videos](../prototype-demo-videos.md) for features you could try.
  + You can replicate the prototype shown in the videos using Software switches in the VM you just used in this Getting Started tutorial. See how in the Configuration section of the User Guide - you would need to configure the [controller](configuring-onos-spring-open.md) AND the [software switches](configuring-cpqd-software-switches.md).
  + You can also try to replicate the prototype (or build your own prototype) with hardware switches. See how in the [Installation Guide](../installation-guide.md).
