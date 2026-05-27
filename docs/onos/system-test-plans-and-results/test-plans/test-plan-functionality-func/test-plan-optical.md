# Test Plan - Optical

# Optical Functionality Test Suite

### Purpose

This test ensures the functionality of optical application.

### Test Overview

This test uses a mininet optical topology included with the test files.  It has 2 hosts, 2 packet switches and 3 optical switches.

### Test Strategy

The test heavily depends on correct loading of the optical topology.  The correct configuration for 

### Test assumption

* A test bench that has onos package deployed
* Requires at least a single node cluster
* Mininet topology included in the test dependency folder should run without errors
* Stable ONOS build ( v1.3 and up )
* LINC-OE installed

| Test Cases | Passing Criteria |
| --- | --- |
| Compare ONOS and Mininet Topologies | * Topologies seen in Mininet and ONOS should match eachother * Same number of Hosts, Switches, and Links |
| Add and test bidirectional point intents | * Intents can be installed between network nodes * Connectivity between hosts when intents are installed * Intent state is in INSTALLED state for each active instances * All devices that are being used are in ACTIVE state * Each active device is assigned to one master controller * Network topology from Mininet is equivalent to ONOS view for each active instances * Flows should be in its appropriate state before and after an event such as intent installation, rerouting flows etc. * System state is consistent to all active ONOS instance * Every match action given when adding intents should correctly stored in each of intents status * Network nodes ( switch and host ) information are consistent such as MAC, IPs, IDs, Ports. * Completely remove or purge all intents that have been installed |
| Add and test bidirectional host intents |
