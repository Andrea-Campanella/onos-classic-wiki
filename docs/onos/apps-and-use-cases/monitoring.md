# Monitoring

## Overview

By itself, ONOS is little more than an SDN framework that provides a programmatic API into the network that it controls. In other words, while it provides the ability to manipulate the network, it does not have any logic built into it to do so. Such functions are provided in the form of applications, for simple tasks, and use case proofs of concepts (PoCs) for more complex tasks.

## Applications

An application implements a narrow set of features and interacts with the rest of ONOS through its northbound API. Examples of ONOS applications include network control functions, such as traffic forwarding, and managerial interfaces, like the GUI.

If you are interested in getting started writing your own applications for ONOS, please check out the [Tutorials](../tutorials.md).

The following are a set of built-in ONOS applications. You can click on each the link to find out the usage of the application.

* [Control Plane Management Application](monitoring/control-plane-management-application.md)
* [Ganglia Report and Query Application](monitoring/ganglia-report-and-query-application.md)
* [Graphite Report and Query Application](monitoring/graphite-report-and-query-application.md)
* [InfluxDB Report and Query Application](monitoring/influxdb-report-and-query-application.md)

## Use Cases

Use cases are aimed at tackling complex SDN deployment scenarios faced by the members of the ONOS community. Likewise, their implementations tend to be complex, and usually include combinations of applications, drivers, and at times, system core components and specialized APIs.

Use cases have been (and continue to be) developed for ONOS. Each use case has their own documentation sets, maintained separately from the main body of ONOS documentation, as they have their own development cycles and are governed separately from the ONOS project. Refer to the [Apps and Use Cases](../apps-and-use-cases.md) page for a full listing of the use cases.

---

[Previous : Distributed ONOS](#)  
[Next : Experimental and Proposed Features](#)

---
