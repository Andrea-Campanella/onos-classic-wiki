# Appendix A : CLI commands

The following are the list of ONOS CLI commands. As the ONOS CLI builds upon Karaf's CLI, this list is not comprehensive to the full set of commands available in the CLI. Please refer to the [karaf commands documentation](http://karaf.apache.org/manual/latest/commands/commands.html) for further information.

### add-flows

**DESCRIPTION**  
             onos:add-flows  
             Installs a number of test flow rules - for testing only  
     **SYNTAX**  
             onos:add-flows [options] flowPerDevice numOfRuns   
     **ARGUMENTS**  
     **flowPerDevice**  
                     Number of flows to add per device  
     **numOfRuns**  
                     Number of iterations  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### add-host-intent

**DESCRIPTION**  
             onos:add-host-intent  
             Installs host-to-host connectivity intent  
     **SYNTAX**  
             onos:add-host-intent [options] one two   
     **ARGUMENTS**  
     **one**  
                     One host ID  
     **two**  
                     Another host ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### add-mpls-intent

**DESCRIPTION**  
             onos:add-mpls-intent  
             Installs mpls connectivity intent  
     **SYNTAX**  
             onos:add-mpls-intent [options] ingressDevice egressDevice   
     **ARGUMENTS**  
     **ingressDevice**  
                     Ingress Device/Port Description  
     **egressDevice**  
                     Egress Device/Port Description  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ingressLabel**  
                     Ingress Mpls label  
                     (defaults to )  
     **--egressLabel**  
                     Egress Mpls label  
                     (defaults to )  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### add-multi-to-single-intent

**DESCRIPTION**  
             onos:add-multi-to-single-intent  
             Installs point-to-point connectivity intent  
     **SYNTAX**  
             onos:add-multi-to-single-intent [options] ingressDevices egressDevice   
     **ARGUMENTS**  
     **ingressDevices egressDevice**  
                     ingressDevice/Port..ingressDevice/Port egressDevice/Port  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### add-optical-intent

**DESCRIPTION**  
             onos:add-optical-intent  
             Installs optical connectivity intent  
     **SYNTAX**  
             onos:add-optical-intent [options] ingressDevice egressDevice   
     **ARGUMENTS**  
     **ingressDevice**  
                     Ingress Device/Port Description  
     **egressDevice**  
                     Egress Device/Port Description  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### add-point-intent

**DESCRIPTION**  
             onos:add-point-intent  
             Installs point-to-point connectivity intent  
     **SYNTAX**  
             onos:add-point-intent [options] ingressDevice egressDevice   
     **ARGUMENTS**  
     **ingressDevice**  
                     Ingress Device/Port Description  
     **egressDevice**  
                     Egress Device/Port Description  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### add-single-to-multi-intent

**DESCRIPTION**  
             onos:add-single-to-multi-intent  
             Installs connectivity intent between a single ingress device and multiple egress devices  
     **SYNTAX**  
             onos:add-single-to-multi-intent [options] ingressDevice egressDevices   
     **ARGUMENTS**  
     **ingressDevice egressDevices**  
                     ingressDevice/Port egressDevice/Port...egressDevice/Port  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--ipDst**  
                     Destination IP Prefix  
     **-k, --key**  
                     Intent Key  
     **-b, --bandwidth**  
                     Bandwidth  
     **-t, --ethType**  
                     Ethernet Type  
     **-d, --ethDst**  
                     Destination MAC Address  
     **--setEthSrc**  
                     Rewrite Source MAC Address  
     **-s, --ethSrc**  
                     Source MAC Address  
     **--setEthDst**  
                     Rewrite Destination MAC Address  
     **--tcpSrc**  
                     Source TCP Port  
     **-l, --lambda**  
                     Lambda  
     **--ipProto**  
                     IP Protocol  
     **-p, --priority**  
                     Priority  
                     (defaults to 100)  
     **--tcpDst**  
                     Destination TCP Port  
     **--ipSrc**  
                     Source IP Prefix  
     **--help**  
                     Display this help message

### address-bindings

**DESCRIPTION**  
             onos:address-bindings  
             Lists all configured address port bindings.  
     **SYNTAX**  
             onos:address-bindings [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### app

**DESCRIPTION**  
             onos:app  
             Manages application inventory  
     **SYNTAX**  
             onos:app [options] command name   
     **ARGUMENTS**  
     **command**  
                     Command name (activate|deactivate|uninstall)  
     **name**  
                     Application name  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### app-ids

**DESCRIPTION**  
             onos:app-ids  
             Lists application ID information  
     **SYNTAX**  
             onos:app-ids [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### apps

**DESCRIPTION**  
             onos:apps  
             Lists application information  
     **SYNTAX**  
             onos:apps [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### balance-masters

**DESCRIPTION**  
             onos:balance-masters  
             Forces device mastership rebalancing  
     **SYNTAX**  
             onos:balance-masters [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### cfg

**DESCRIPTION**  
             onos:cfg  
             Manages component configuration  
     **SYNTAX**  
             onos:cfg [options] [command] [component] [name] [value]   
     **ARGUMENTS**  
     **command**  
                     Command name (activate|deactivate|uninstall)  
     **component**  
                     Component name  
     **name**  
                     Property name  
     **value**  
                     Property value  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### cluster-devices

**DESCRIPTION**  
             onos:cluster-devices  
             Lists devices of the specified topology cluster in the current topology  
     **SYNTAX**  
             onos:cluster-devices [options] id   
     **ARGUMENTS**  
     **id**  
                     Cluster ID  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### cluster-links

**DESCRIPTION**  
             onos:cluster-links  
             Lists links of the specified topology cluster in the current topology  
     **SYNTAX**  
             onos:cluster-links [options] id   
     **ARGUMENTS**  
     **id**  
                     Cluster ID  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### clusters

**DESCRIPTION**  
             onos:clusters  
             Lists all clusters in the current topology  
     **SYNTAX**  
             onos:clusters [options]  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### cycle-intents

**DESCRIPTION**  
             onos:cycle-intents  
             Installs random intents to test throughput  
     **SYNTAX**  
             onos:cycle-intents [options] ingressDevice egressDevice numberOfIntents [keyOffset]   
     **ARGUMENTS**  
     **ingressDevice**  
                     Ingress Device/Port Description  
     **egressDevice**  
                     Egress Device/Port Description  
     **numberOfIntents**  
                     Number of intents to install/withdraw  
     **keyOffset**  
                     Starting point for first key (default: 1)  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### device-remove

**DESCRIPTION**  
             onos:device-remove  
             Removes an infrastructure device  
     **SYNTAX**  
             onos:device-remove [options] uri   
     **ARGUMENTS**  
     **uri**  
                     Device ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### device-role

**DESCRIPTION**  
             onos:device-role  
             Sets role of the controller node for the given infrastructure device  
     **SYNTAX**  
             onos:device-role [options] uri node role   
     **ARGUMENTS**  
     **uri**  
                     Device ID  
     **node**  
                     Node ID  
     **role**  
                     Mastership role  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### devices

**DESCRIPTION**  
             onos:devices  
             Lists all infrastructure devices  
     **SYNTAX**  
             onos:devices [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### flows

**DESCRIPTION**  
             onos:flows  
             Lists all currently-known flows.  
     **SYNTAX**  
             onos:flows [options] [state] [uri]   
     **ARGUMENTS**  
     **state**  
                     Flow Rule state  
     **uri**  
                     Device ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### get-stats

**DESCRIPTION**  
             onos:get-stats  
             Fetches stats for a connection point  
     **SYNTAX**  
             onos:get-stats [options] connectPoint   
     **ARGUMENTS**  
     **connectPoint**  
                     Device/Port Description  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### groups

**DESCRIPTION**  
             onos:groups  
             Lists all groups in the system  
     **SYNTAX**  
             onos:groups [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### host-remove

**DESCRIPTION**  
             onos:host-remove  
             Removes an end-station host  
     **SYNTAX**  
             onos:host-remove [options] id   
     **ARGUMENTS**  
     **id**  
                     Host ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### hosts

**DESCRIPTION**  
             onos:hosts  
             Lists all currently-known hosts.  
     **SYNTAX**  
             onos:hosts [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### intents

**DESCRIPTION**  
             onos:intents  
             Lists the inventory of intents and their states  
     **SYNTAX**  
             onos:intents [options]  
     **OPTIONS**  
     **-i, --installable**  
                     Output Installable Intents  
     **-j, --json**  
                     Output JSON  
     **-s, --summary**  
                     Intents summary  
     **--help**  
                     Display this help message  
     **-p, --pending**  
                     Show inforamtion about pending intents

### leaders

**DESCRIPTION**  
             onos:leaders  
             Finds the leader for particular topic.  
     **SYNTAX**  
             onos:leaders [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### links

**DESCRIPTION**  
             onos:links  
             Lists all infrastructure links  
     **SYNTAX**  
             onos:links [options] [uri]   
     **ARGUMENTS**  
     **uri**  
                     Device ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### masters

**DESCRIPTION**  
             onos:masters  
             Lists device mastership information  
     **SYNTAX**  
             onos:masters [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### metrics

**DESCRIPTION**  
             onos:metrics  
             Prints metrics in the system  
     **SYNTAX**  
             onos:metrics [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### nodes

**DESCRIPTION**  
             onos:nodes  
             Lists all controller cluster nodes  
     **SYNTAX**  
             onos:nodes [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### partitions

**DESCRIPTION**  
             onos:partitions  
             Lists information about partitions in the system  
     **SYNTAX**  
             onos:partitions [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### paths

**DESCRIPTION**  
             onos:paths  
             Lists all shortest-paths paths between the specified source and destination devices  
     **SYNTAX**  
             onos:paths [options] src dst   
     **ARGUMENTS**  
     **src**  
                     Source device ID  
     **dst**  
                     Destination device ID  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### ports

**DESCRIPTION**  
             onos:ports  
             Lists all ports or all ports of a device  
     **SYNTAX**  
             onos:ports [options] [uri]   
     **ARGUMENTS**  
     **uri**  
                     Device ID  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **-d, --disabled**  
                     Show only disabled ports  
     **-e, --enabled**  
                     Show only enabled ports  
     **--help**  
                     Display this help message

### push-random-intents

**DESCRIPTION**  
             onos:push-random-intents  
             Installs random intents to test throughput  
     **SYNTAX**  
             onos:push-random-intents [options] count   
     **ARGUMENTS**  
     **count**  
                     Number of intents to push  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### push-test-intents

**DESCRIPTION**  
             onos:push-test-intents  
             Installs random intents to test throughput  
     **SYNTAX**  
             onos:push-test-intents [options] ingressDevice egressDevice numberOfIntents [keyOffset]   
     **ARGUMENTS**  
     **ingressDevice**  
                     Ingress Device/Port Description  
     **egressDevice**  
                     Egress Device/Port Description  
     **numberOfIntents**  
                     Number of intents to install/withdraw  
     **keyOffset**  
                     Starting point for first key (default: 1)  
     **OPTIONS**  
     **-i, --install**  
                     Install intents  
     **-j, --json**  
                     Output JSON  
     **-w, --withdraw**  
                     Withdraw intents  
     **--help**  
                     Display this help message

### remove-intent

**DESCRIPTION**  
             onos:remove-intent  
             Removes the specified intent  
     **SYNTAX**  
             onos:remove-intent [options] app id   
     **ARGUMENTS**  
     **app**  
                     Application ID  
     **id**  
                     Intent ID  
     **OPTIONS**  
     **-p, --purge**  
                     Purge the intent from the store after removal  
     **-j, --json**  
                     Output JSON  
     **-s, --sync**  
                     Waits for the removal before returning  
     **--help**  
                     Display this help message

### resource-allocations

**DESCRIPTION**  
             onos:resource-allocations  
             Lists allocations by link  
     **SYNTAX**  
             onos:resource-allocations [options] [srcString] [dstString]   
     **ARGUMENTS**  
     **srcString**  
                     Link source  
     **dstString**  
                     Link destination  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### resource-available

**DESCRIPTION**  
             onos:resource-available  
             Lists available resources by link  
     **SYNTAX**  
             onos:resource-available [options] [srcString] [dstString]   
     **ARGUMENTS**  
     **srcString**  
                     Link source  
     **dstString**  
                     Link destination  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### roles

**DESCRIPTION**  
             onos:roles  
             Lists mastership roles of nodes for each device.  
     **SYNTAX**  
             onos:roles [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### summary

**DESCRIPTION**  
             onos:summary  
             Provides summary of ONOS model  
     **SYNTAX**  
             onos:summary [options]  
     **OPTIONS**  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### topology

**DESCRIPTION**  
             onos:topology  
             Lists summary of the current topology  
     **SYNTAX**  
             onos:topology [options]  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

### wipe-out

**DESCRIPTION**  
             onos:wipe-out  
             Wipes-out the entire network information base, i.e. devices, links, hosts  
     **SYNTAX**  
             onos:wipe-out [options] [please]   
     **ARGUMENTS**  
     **please**  
                     Confirmation phrase  
     **OPTIONS**  
     **-r, --recompute**  
                     Trigger topology re-computation  
     **-j, --json**  
                     Output JSON  
     **--help**  
                     Display this help message

---

[Home : User's Guide](../../apps-and-use-cases/cord-leaf-spine-fabric-with-segment-routing/archived-onfs-spring-open-project/user-guide.md)

---
