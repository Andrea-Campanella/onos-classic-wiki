# Using the CLI

This page explain how to use the SR cli. The example used in the example uses **sr-3node.conf** configuration file, which is explained in the Configuration ONOS section <LINK>

### Show switch information

**show switch** : show the switches connected to the controller (NOTE: any switch not configured in the config file is not shown)

```
onos-vm# sh link 
# Src Switch DPID                     Src Port Dst Switch DPID                     Dst Port Type
-|-----------------------------------|--------|-----------------------------------|--------|------
1 00:00:00:00:00:00:00:01 (Dallas-R1) 7        00:00:00:00:00:00:00:02 (Dallas-R2) 3        packet
2 00:00:00:00:00:00:00:02 (Dallas-R2) 1        00:00:00:00:00:00:00:01 (Dallas-R1) 6        packet
3 00:00:00:00:00:00:00:03 (Dallas-R3) 2        00:00:00:00:00:00:00:02 (Dallas-R2) 2        packet
```

**show switch <switch DPID>** : shows the detail of the switch

```
onos-vm# sh switch 00:00:00:00:00:00:00:01 
# Switch DPID             Alias     Connected Since              Connected At      Type   Controller
-|-----------------------|---------|----------------------------|-----------------|------|----------
1 00:00:00:00:00:00:00:01 Dallas-R1 Wed Dec 03 16:06:40 PST 2014 192.168.0.3:52922 packet onos-vm
```

**show switch <switch DPID> table <acl/ip/mpls>** : shows the specific table  of the switch

```
onos-vm# sh switch 00:00:00:00:00:00:00:01 table acl
# Bytes Packets Dur(s) Cookie Priority In Port Src MAC Dst MAC EthType Src IP Dst IP Protocol Src Port Dst Port Instructions
-|-----|-------|------|------|--------|-------|-------|-------|-------|------|------|--------|--------|--------|------------
1 0     0       525    0      0        *       *       *       *       *      *      *        *        *


onos-vm# sh switch 00:00:00:00:00:00:00:01 table ip
# Bytes Packets Dur(s) Cookie Priority Dst IP         Instructions
-|-----|-------|------|------|--------|--------------|-----------------------------------------------------
1 0     0       423    0      65535    192.168.0.2/32 {goto: {tableid: acl}, write: {dec_nw_ttl, group: 1}}
2 0     0       423    0      65535    192.168.0.3/32 {goto: {tableid: acl}, write: {group: 2}}
3 0     0       423    0      49104    7.7.7.0/24     {goto: {tableid: acl}, write: {group: 2}}
4 0     0       444    0      0        *              {goto: {tableid: acl}, write: {output: controller}}
 
onos-vm# sh switch 00:00:00:00:00:00:00:01 table mpls
# Bytes Packets Dur(s) Priority MPLS Label MPLS BOS MPLS TC Instructions
-|-----|-------|------|--------|----------|--------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------
1 0     0       426    65535    102        false    *       {goto: {tableid: acl}, write: {pop_mpls: 0x8847, copy_ttl_in, group: 1, dec_mpls_ttl}}
2 0     0       426    65535    102        true     *       {goto: {tableid: acl}, write: {pop_mpls: 0x800, dec_nw_ttl, copy_ttl_in, group: 1}}
3 0     0       426    65535    103        true     *       {goto: {tableid: acl}, write: {group: 1, dec_mpls_ttl}}
4 0     0       426    65535    103        false    *       {goto: {tableid: acl}, write: {group: 1, dec_mpls_ttl}}
5 0     0       426    65535    101006     true     *       {goto: {tableid: acl}, write: {pop_mpls: 0x800, dst_mac: 00:00:02:02:02:80, dec_nw_ttl, src_mac: 00:00:01:01:01:80, output: 6, copy_ttl_in}}
6 0     0       426    65535    101006     false    *       {goto: {tableid: acl}, write: {dec_mpls_ttl, pop_mpls: 0x8847, dst_mac: 00:00:02:02:02:80, src_mac: 00:00:01:01:01:80, output: 6, copy_ttl_in}}
7 0     0       426    65535    101007     true     *       {goto: {tableid: acl}, write: {pop_mpls: 0x800, dst_mac: 00:00:02:02:02:80, dec_nw_ttl, src_mac: 00:00:01:01:01:80, output: 7, copy_ttl_in}}
8 0     0       426    65535    101007     false    *       {goto: {tableid: acl}, write: {dec_mpls_ttl, pop_mpls: 0x8847, dst_mac: 00:00:02:02:02:80, src_mac: 00:00:01:01:01:80, output: 7, copy_ttl_in}}
9 0     0       447    0        *          *        *       {goto: {tableid: acl}, write: {output: controller}}
```

**show switch <switch DPID> port :** show the port information of the switch

```
 onos-vm# sh switch 00:00:00:00:00:00:00:01 port
# OF Port #     Status Rcv Bytes Rcv Pkts Rcv Errs Rcv Dropped Rcv CRC Rcv Overruns Rcv Frame Errs Xmit Bytes Xmit Pkts Xmit Errs Xmit Dropped Collisions
-|-------------|------|---------|--------|--------|-----------|-------|------------|--------------|----------|---------|---------|------------|----------
1 1 (s1-eth1)   up     480       6        0        0           0       0            0              2948       44        0         0            0
2 2 (s1-eth2)   up     558       7        0        0           0       0            0              2948       44        0         0            0
3 3 (s1-eth3)   up     558       7        0        0           0       0            0              2948       44        0         0            0
4 4 (s1-eth4)   up     558       7        0        0           0       0            0              2948       44        0         0            0
5 5 (s1-eth5)   up     558       7        0        0           0       0            0              2948       44        0         0            0
6 6 (s1-eth6)   up     3015      45       0        0           0       0            0              2948       44        0         0            0
7 7 (s1-eth7)   up     3015      45       0        0           0       0            0              2948       44        0         0            0
8 8 (s1-eth8)   up     3015      45       0        0           0       0            0              2948       44        0         0            0
9 65534 (local) up     0         0        0        0           0       0            0              0          0         0         0            0
```

**show switch <switch DPID> group :**show the group information of the switch

```
onos-vm# sh switch 00:00:00:00:00:00:00:01 group 
# Group Type Group Id Pkts Bytes Bucket Pkts Bucket Bytes Set Src Mac       Set Dst Mac       Push Mpls Set Bos COPY TTL Dec Mpls TTL Outport Group
-|----------|--------|----|-----|-----------|------------|-----------------|-----------------|---------|-------|--------|------------|-------|-----
1 SELECT     1        0    0     0           0            00:00:01:01:01:80 00:00:02:02:02:80                                         6
2 SELECT              0    0     0           0            00:00:01:01:01:80 00:00:02:02:02:80                                         7
3 SELECT     2        0    0     0           0            00:00:01:01:01:80 00:00:02:02:02:80 103       true    True     True         6
4 SELECT              0    0     0           0            00:00:01:01:01:80 00:00:02:02:02:80 103       true    True     True         7
```

**show link**: show the links discovered by the controller (NOTE: any link not configured in the config file is not shown)

```
onos-vm# sh link 
# Src Switch DPID                     Src Port Dst Switch DPID                     Dst Port Type
-|-----------------------------------|--------|-----------------------------------|--------|------
1 00:00:00:00:00:00:00:01 (Dallas-R1) 7        00:00:00:00:00:00:00:02 (Dallas-R2) 3        packet
2 00:00:00:00:00:00:00:02 (Dallas-R2) 1        00:00:00:00:00:00:00:01 (Dallas-R1) 6        packet
3 00:00:00:00:00:00:00:03 (Dallas-R3) 2        00:00:00:00:00:00:00:02 (Dallas-R2) 2        packet
```

**watch** <any command> : repeats the command every two second. It is useful to see any statistics changes

```
onos-vm# watch sh switch 00:00:00:00:00:00:00:01 port 
# OF Port #     Status Rcv Bytes Rcv Pkts Rcv Errs Rcv Dropped Rcv CRC Rcv Overruns Rcv Frame Errs Xmit Bytes Xmit Pkts Xmit Errs Xmit Dropped Collisions
-|-------------|------|---------|--------|--------|-----------|-------|------------|--------------|----------|---------|---------|------------|----------
1 1 (s1-eth1)   up     1880      22       0        0           0       0            0              5651       80        0         0            0
2 2 (s1-eth2)   up     600       8        0        0           0       0            0              4531       68        0         0            0
3 3 (s1-eth3)   up     558       7        0        0           0       0            0              4531       68        0         0            0
4 4 (s1-eth4)   up     558       7        0        0           0       0            0              4489       67        0         0            0
5 5 (s1-eth5)   up     558       7        0        0           0       0            0              4489       67        0         0            0
6 6 (s1-eth6)   up     5144      74       0        0           0       0            0              5101       73        0         0            0
7 7 (s1-eth7)   up     5046      73       0        0           0       0            0              4999       72        0         0            0
8 8 (s1-eth8)   up     4556      68       0        0           0       0            0              4489       67        0         0            0
9 65534 (local) up     0         0        0        0           0       0            0              0          0         0         0            0
Executing sh switch 00:00:00:00:00:00:00:01 port  
# OF Port #     Status Rcv Bytes Rcv Pkts Rcv Errs Rcv Dropped Rcv CRC Rcv Overruns Rcv Frame Errs Xmit Bytes Xmit Pkts Xmit Errs Xmit Dropped Collisions
-|-------------|------|---------|--------|--------|-----------|-------|------------|--------------|----------|---------|---------|------------|----------
1 1 (s1-eth1)   up     2076      24       0        0           0       0            0              5847       82        0         0            0
2 2 (s1-eth2)   up     600       8        0        0           0       0            0              4531       68        0         0            0
3 3 (s1-eth3)   up     558       7        0        0           0       0            0              4531       68        0         0            0
4 4 (s1-eth4)   up     558       7        0        0           0       0            0              4489       67        0         0            0
5 5 (s1-eth5)   up     558       7        0        0           0       0            0              4489       67        0         0            0
6 6 (s1-eth6)   up     5242      75       0        0           0       0            0              5203       74        0         0            0
7 7 (s1-eth7)   up     5144      74       0        0           0       0            0              5101       73        0         0            0
8 8 (s1-eth8)   up     4556      68       0        0           0       0            0              4489       67        0         0            0
9 65534 (local) up     0         0        0        0           0       0            0              0          0         0         0            0
```

**show policy** : show the policy information created by operators (NOTE: Configuring switches section describe how to create a policy)

```
onos-vm(config)# sh policy 
# Policy Id Policy Type Priority Dst Mac Src Mac Ether Type Dst IP     IP Protocol Src IP      Dst TcpPort Src TcpPort Tunnel Used
-|---------|-----------|--------|-------|-------|----------|----------|-----------|-----------|-----------|-----------|-----------
1 p1        TUNNEL_FLOW 10000    *       *       0x2048     7.7.7.7/32 *           10.0.1.1/32 *           *           t1
```

**show tunnel** : show the tunnel information created by operators (NOTE: Configuring switches section describe how to create a tunnel)

```
onos-vm(config)# sh tunnel 
# Id Policies Tunnel Path [Head-->Tail] Label Stack [Outer-->Inner]
-|--|--------|-------------------------|---------------------------
1 t1          [101, 102, 103]           [[103]]
```

### **Configuring Tunnels and Policies**

**configure**: enter configuration mode

```
mininet-vm> enable
mininet-vm# configure 
mininet-vm(config)#
```

**tunnel <tunnel ID>** : Create a tunnel for a tunnel-flow policy. Specify the node SID of all routers of the tunnel, following **node** keyword.  If you want to suspend creating the tunnel, you can type **end**. It will suspend creating the tunnel and exit the configuration mode.

```
onos-vm(config)# tunnel t1
onos-vm(config-tunnel)# node 101
onos-vm(config-tunnel)# node 102
onos-vm(config-tunnel)# node 103
onos-vm(config-tunnel)# exit
```

**policy <policy ID> policy-type <policy type>:** Create a specific type of policy. Only **tunnel-flow** type is supported now. **flow-entry**, **tunnel**, and **priority** must be specified. IP, TCP, and UDP are supported as the flow-entry type. The first subnet (10.0.1.1/32 in the example) is the source, and the second subnet (7.7.7.7/32 in the example) is the destination.

```
onos-vm(config)# policy p1 policy-type tunnel-flow 
onos-vm(config-policy)# flow-entry ip 10.0.1.1/32 7.7.7.7/32
onos-vm(config-policy)# tunnel t1
onos-vm(config-policy)# priority 10000
onos-vm(config-policy)# exit 
```

**no policy <policy ID>**: remove the policy with the policy ID.

```
onos-vm(config)# sh policy 
# Policy Id Policy Type Priority Dst Mac Src Mac Ether Type Dst IP     IP Protocol Src IP      Dst TcpPort Src TcpPort Tunnel Used
-|---------|-----------|--------|-------|-------|----------|----------|-----------|-----------|-----------|-----------|-----------
1 p1        TUNNEL_FLOW 10000    *       *       0x2048     7.7.7.7/32 *           10.0.1.1/32 *           *           t1
onos-vm(config)# no policy p1
onos-vm(config)# sh policy 
None.
```

**no tunnel <tunnel ID>**: remove the tunnel with the tunnel ID. If the tunnel is being used by any policy, then it is not removed.

```
onos-vm(config)# sh tunnel 
# Id Policies Tunnel Path [Head-->Tail] Label Stack [Outer-->Inner]
-|--|--------|-------------------------|---------------------------
1 t1          [101, 102, 103]           [[103]]
onos-vm(config)# no tunnel t1
onos-vm(config)# sh tunnel 
None.
```
