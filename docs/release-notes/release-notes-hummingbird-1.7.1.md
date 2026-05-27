# Release Notes - Hummingbird 1.7.1

# Hummingbird Release

Version: 1.7.1

Release Date: October 25, 2016

Download [here](../onos/downloads.md)

# Release Content

* Improvements to DPI Statistics Manager & DPI's CLI
* IETF TE Topology Provider
* TE Topology NBI
* Implement RESTCONF client and server
* Several bug fixes

## Bug

* [[ONOS-5306](https://jira.onosproject.org/browse/ONOS-5306)] - NPE in Flows Instructions Decoder
* [[ONOS-5323](https://jira.onosproject.org/browse/ONOS-5323)] - Issue with POST /intents - Causing NPE with null/ wrong(not existence) appId
* [[ONOS-5396](https://jira.onosproject.org/browse/ONOS-5396)] - Issue with Applications REST API- GET /applications/{name}- Causing NPE with wrong/non-existent App Id
* [[ONOS-5496](https://jira.onosproject.org/browse/ONOS-5496)] - [ONOS-YMS-TEST] Restconf issue, post with empty list
* [[ONOS-5497](https://jira.onosproject.org/browse/ONOS-5497)] - [ONOS-YMS-TEST] String Pattern issue
* [[ONOS-5498](https://jira.onosproject.org/browse/ONOS-5498)] - [ONOS-YMS-TEST] For grouping and uses inter file, namespace for leaf is incorrect
* [[ONOS-5519](https://jira.onosproject.org/browse/ONOS-5519)] - Compilation error for pattern with single quotes
* [[ONOS-5536](https://jira.onosproject.org/browse/ONOS-5536)] - [ONOS-YMS-TEST] Get for leaf with decimal64 type is throwing error.
* [[ONOS-5537](https://jira.onosproject.org/browse/ONOS-5537)] - [ONOS-YMS-TEST] Get for leaf with enum is throwing error.
* [[ONOS-5540](https://jira.onosproject.org/browse/ONOS-5540)] - [ONOS-YMS-TEST] Get for leaf which is not posted is throwing error.
* [[ONOS-5543](https://jira.onosproject.org/browse/ONOS-5543)] - [ONOS-YMS-TEST] Get for leaf-list with type binary is not showing any value.

## Story

* [[ONOS-3646](https://jira.onosproject.org/browse/ONOS-3646)] - Move SNMP to release artifacts
* [[ONOS-4458](https://jira.onosproject.org/browse/ONOS-4458)] - Yang buckification
* [[ONOS-4841](https://jira.onosproject.org/browse/ONOS-4841)] - [YANG] YMSU:JSON builder and walker
* [[ONOS-5011](https://jira.onosproject.org/browse/ONOS-5011)] - [RESTCONF] create RESTCONF Protocol Proxy (RPP) module
* [[ONOS-5315](https://jira.onosproject.org/browse/ONOS-5315)] - Redundant DeviceId on JSON for POST - REST API (Flowobjectives and Meters)
* [[ONOS-5538](https://jira.onosproject.org/browse/ONOS-5538)] - [ONOS-YMS-TEST] Simple data type (union of integer and string type)
