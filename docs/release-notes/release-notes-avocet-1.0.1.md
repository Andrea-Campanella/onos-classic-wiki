# Release Notes - Avocet 1.0.1

# AVOCET 1.0.1

Version: 1.0.1

Release Date: 22nd Jan, 2015

Download [here](../onos/downloads.md)

## About Avocet 1.0.1

The 1.0.1 release is a bug fix update for Avocet release.

## Resolved Security Issues

* [ONOS-605](https://jira.onosproject.org/browse/ONOS-605)

Handle packets that can't be deserialized properly.

## Bugs fixed

* [ONOS-787](https://jira.onosproject.org/browse/ONOS-787)  
  Fixed bug where ONOS sends actions in DELETE flow mods in OF1.0.
* [ONOS-779](https://jira.onosproject.org/browse/ONOS-779)  
  Protect against null pointers during deserializing
* [ONOS-776](https://jira.onosproject.org/browse/ONOS-776)  
  Updated SDN-IP config to support 64-bit port numbers.
* [ONOS-540](https://jira.onosproject.org/browse/ONOS-540)  
  Add explicit flow rules to receive control packets: ARP, LLDP, BDDP
* [ONOS-537](https://jira.onosproject.org/browse/ONOS-537)   
  Provided maxLen setting to make sure packet data is sent with packet-in message. (OF1.3)
* [ONOS-721](https://jira.onosproject.org/browse/ONOS-721), [ONOS-447](https://jira.onosproject.org/browse/ONOS-447)  
   Add org.osgi.core dependency to pom.xml. Fixes eclipse build issue
* [ONOS-535](https://jira.onosproject.org/browse/ONOS-535)  
  capture and display ip address and port of switches
* [ONOS-539](https://jira.onosproject.org/browse/ONOS-539)  
  Capture port names so CLI can display them
* Related to [ONOS-481](https://jira.onosproject.org/browse/ONOS-481)  
  DistributedFlowRuleStore: always add FlowEntry on batchStore
* [ONOS-478](https://jira.onosproject.org/browse/ONOS-478)  
  DistributedFlowRuleStore: getFlowEntries should never return null
* [ONOS-473](https://jira.onosproject.org/browse/ONOS-473)  
  LinkStores: Concurrent readable {src, dst}Links
* [ONOS-393](https://jira.onosproject.org/browse/ONOS-393)  
   NPE when one of the devices can no longer be found
* [ONOS-607](https://jira.onosproject.org/browse/ONOS-607)

* [ONOS-558](https://jira.onosproject.org/browse/ONOS-558)

* [ONOS-505](https://jira.onosproject.org/browse/ONOS-505)  
  controller port visualized incorrectly into ONOS CLI
* [ONOS-537](https://jira.onosproject.org/browse/ONOS-537)  
  Provided maxLen setting to make sure packet data is sent with packet-in message
* [ONOS-504](https://jira.onosproject.org/browse/ONOS-504)  
  FlowRuleEvent.Type not registered in Kryo
* [ONOS-440](https://jira.onosproject.org/browse/ONOS-440)  
  OpticalPathProvisioner Null pointer exception

* [ONOS-439](https://jira.onosproject.org/browse/ONOS-439)  
  [OpticalLinkProvider.processLink throws Null pointer exception](https://jira.onosproject.org/browse/ONOS-439)
