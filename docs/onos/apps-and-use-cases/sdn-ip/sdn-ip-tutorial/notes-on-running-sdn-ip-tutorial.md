# Notes on running SDN-IP tutorial

Environment: ONOS tutorial OVA (Ubuntu Xenial ONOS 1.15.0)

The OVA can be downloaded as described here: [https://wiki.onosproject.org/display/ONOS/Basic+ONOS+Tutorial](../../../tutorials/basic-onos-tutorial.md)

1. Checkout SDN-IP tutorial codes under home directory:

`$ svn export https://github.com/opennetworkinglab/onos/trunk/tools/tutorials/sdnip`

2. Install bridge utilities:

`$ sudo apt install bridge-utils`

2. Install Quagga package:

`$ sudo apt-get install quagga`

3. Check the following requirements and adjust as required before running tutorial.py :  
   a. run directory /var/run/quagga exists  
   b. binary of zebra and bgpd installed under /usr/lib/quagga

4. Click desktop icon "Setup ONOS Cluster" and note the IP of onos-1:

`onos> summary`

`node=172.17.0.2, version=1.15.0 clusterId=onos`

`nodes=3, devices=0, links=0, hosts=0, SCC(s)=1, flows=0, intents=0`

5. To peer Mininet host root 10.10.10.2 with docker onos-1, the following network setup could be configured:

`bgp eth1 10.10.10.1        10.10.10.2 eth0 root`

`+------------------------------------------+`

`|`

`sdnip`

`(bridge)`

`|`

`10.10.10.3 eth1 +`

`onos-1`

`------------------+(docker)`

`172.17.0.2 eth0`

onos-1 needs to be assigned another IP say 10.10.10.3 and ~/sdnip/configs/quagga-sdn.conf should be changed accordingly:

`neighbor 10.10.10.3 remote-as 65000`  
 `neighbor 10.10.10.3 port 2000`  
 `neighbor 10.10.10.3 timers connect 5`

6. Create docker bridge:

`$ docker network create --subnet 10.10.10.0/24 --ip-range 10.10.10.0/24 --gateway 10.10.10.2 sdnip`

7. Note name of docker bridge created:

`$ sudo brctl show`  
`bridge name bridge id STP enabled interfaces`  
`br-fb2a5d5b6f8e 8000.02428d00da0a no veth71fb89a`  
`docker0 8000.024231751c7f no veth1289400`  
 `veth46bdbff`  
 `veth8b25d1d`  
 `veth8c5706a`  
 `vethad2fb3e`  
 `vethbb09655`

8. Attach onos-1 to docker bridge:

`$ docker network connect --ip 10.10.10.3 sdnip onos-1`

9. Verify additional network interface is created for onos-1:

`$ docker exec onos-1 ifconfig -a`

10. Run tutorial.py as follows:

`$ sudo mn --custom /home/sdn/sdnip/tutorial.py --topo sdnip --controller remote,172.17.0.2 --nolistenport`

11. Add network interface of Mininet host root to docker bridge:

`$ sudo brctl addif br-fb2a5d5b6f8e root-eth0`

12. Upload network configuration to onos-1:

`$ curl --user onos:rocks -X POST -H "Content-Type: application/json" http://172.17.0.2:8181/onos/v1/network/configuration/ -d @/home/sdn/sdnip/configs/network-cfg.json`

13. Activate ONOS applications required:

`onos> app activate org.onosproject.config`

`onos> app activate org.onosproject.proxyarp`

`onos> app activate org.onosproject.sdnip`

14. Check BGP results:

`onos> bgp-speakers`  
`speaker1: port=of:00000000000000a3/1, vlan=None, peers=[10.0.1.1, 10.0.2.1, 10.0.3.1, 10.0.4.1]`  
`onos> bgp-neighbors`   
`BGP neighbor is 10.10.10.1, remote AS 65000, local AS 65000`  
 `Remote router ID 10.10.10.1, IP /10.10.10.1:47348, BGP version 4, Hold time 9`  
 `Remote AFI/SAFI IPv4 Unicast YES Multicast NO, IPv6 Unicast NO Multicast NO`  
 `Local router ID 10.10.10.3, IP /10.10.10.3:2000, BGP version 4, Hold time 9`  
 `Local AFI/SAFI IPv4 Unicast YES Multicast NO, IPv6 Unicast NO Multicast NO`  
 `4 Octet AS Capability: Advertised Received`  
`onos> bgp-routes`   
 `Network Next Hop Origin LocalPref MED BGP-ID`  
 `192.168.3.0/24 10.0.3.1 IGP 100 0 10.10.10.1` `AsPath 65003`  
 `192.168.2.0/24 10.0.2.1 IGP 100 0 10.10.10.1` `AsPath 65002`  
 `192.168.1.0/24 10.0.1.1 IGP 100 0 10.10.10.1` `AsPath 65001`  
`Total BGP IPv4 routes = 3`

`Network Next Hop Origin LocalPref MED BGP-ID`  
`Total BGP IPv6 routes = 0`

15. Test Mininet topology reachability:

`mininet> pingall`

`*** Ping: testing ping reachability`

`bgp -> X X X X X X X X root`

`h1 -> X h2 h3 X X X X X X`

`h2 -> X h1 h3 X X X X X X`

`h3 -> X h1 h2 X X X X X X`

`h4 -> X X X X X X X X X`

`r1 -> bgp h1 X X X X X X X`

`r2 -> X X h2 X X X X X X`

`r3 -> X X X h3 X X X X X`

`r4 -> X X X X h4 X X X X`

`root -> X X X X X X X X X`

`*** Results: 86% dropped (12/90 received)`
