# Release Notes - Cardinal 1.2.2

# Cardinal Release

Version: 1.2.2

Release Date: 1st September, 2015

Download [here](../onos/downloads.md)

This revision includes several minor bug fixes and some improvements related to deployments.

## Sub-task

* [[ONOS-2434](https://jira.onosproject.org/browse/ONOS-2434)] - Setup environment on VirtualBox
* [[ONOS-2435](https://jira.onosproject.org/browse/ONOS-2435)] - Execute manual tests

## Bug

* [[ONOS-1412](https://jira.onosproject.org/browse/ONOS-1412)] - Links and objects disappearing in the GUI when using Firefox
* [[ONOS-2404](https://jira.onosproject.org/browse/ONOS-2404)] - Assignment of HandshakerBehavior does not respect driver annotations
* [[ONOS-2406](https://jira.onosproject.org/browse/ONOS-2406)] - Local identity is established incorrectly as a non-cluster IP address.
* [[ONOS-2417](https://jira.onosproject.org/browse/ONOS-2417)] - onos-uninstall does not work on systems without the 'service' command
* [[ONOS-2426](https://jira.onosproject.org/browse/ONOS-2426)] - Flows are stuck in PENDING\_ADD after switches reconnect.
* [[ONOS-2433](https://jira.onosproject.org/browse/ONOS-2433)] - Intents stuck in FAILED state due to cascading topology changes.
* [[ONOS-2463](https://jira.onosproject.org/browse/ONOS-2463)] - Exception when pushing topology config
* [[ONOS-2477](https://jira.onosproject.org/browse/ONOS-2477)] - Links not discovered due to link discoverers missing ports
* [[ONOS-2479](https://jira.onosproject.org/browse/ONOS-2479)] - Sometimes OpenFlow packets get dropped before being sent to switch
* [[ONOS-2514](https://jira.onosproject.org/browse/ONOS-2514)] - SDN-IP installs too many point-to-point intents for some configurations

## Story

* [[ONOS-1535](https://jira.onosproject.org/browse/ONOS-1535)] - Deploy ONOS 1.2-SNAPSHOT on a virtual slice on GEANT GTS testbed
* [[ONOS-2208](https://jira.onosproject.org/browse/ONOS-2208)] - Internet2: successfuly test ONOS 1.2.1 on the mininet instance provided by Internet2
* [[ONOS-2337](https://jira.onosproject.org/browse/ONOS-2337)] - PCEP Channel Handler to manage each PCC client
* [[ONOS-2338](https://jira.onosproject.org/browse/ONOS-2338)] - Implement PCEP Controller to provide socket handling with each PCC
* [[ONOS-2339](https://jira.onosproject.org/browse/ONOS-2339)] - Implement Channel Handler to manage Session handling with PCC
* [[ONOS-2353](https://jira.onosproject.org/browse/ONOS-2353)] - Implement the PCE close message parsing, encoding and decoding
* [[ONOS-2365](https://jira.onosproject.org/browse/ONOS-2365)] - Unit test code for the PCEP create, update and delete tunnel code
* [[ONOS-2513](https://jira.onosproject.org/browse/ONOS-2513)] - Modify the semantic of MP2SP intents introducting the partially failed state

## Task

* [[ONOS-2290](https://jira.onosproject.org/browse/ONOS-2290)] - Implement PCEP message parser for parsing PCEP protocol messages with encoding and decoding API
