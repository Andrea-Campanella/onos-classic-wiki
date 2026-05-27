# Collecting System Metrics from CollectD Agent

# Overview

Collecting system metrics (e.g., CPU, memory, disk I/O, etc.) inside JVM usually shows incorrect result.  
To obtain more precise monitoring result, control plane manager provides a way to collect system metrics from third-party monitoring server such as CollectD, ganglia, etc.  
In this tutorial, we will show how to integrate third-party monitoring agent with ONOS to obtain system metrics. 

# Usage

Each monitoring agent typically provides a way to report the collected metric to other system through various interfaces.   
As an example, we provide a [CollectD](https://collectd.org/) plugin which is in charging of reporting all metric values to ONOS through REST API.  
Inside ONOS we defined a set of REST API to receive the reported metrics from third-party monitoring agent.  
The detailed REST API that is used for collecting system metrics is enumerated at the end of this document.

## Prerequisites

Before you start, you will need followings:

* Ubuntu 14.04 64-bit
* 2GB or more RAM
* 2 or more processors

### CollectD Installation

Install CollectD using apt-get.

```
$ sudo apt-get update
$ sudo apt-get install collectd collectd-utils python-pycurl
```

Download CollectD plugin for reporting system metrics to ONOS.

```
$ sudo apt-get install git
$ git clone https://github.com/gunine/write_onos
```

Configure CollectD plugin by copying collectd.conf and modules directory under /etc/collectd/.

```
$ sudo cp collectd.conf /etc/collectd
$ sudo cp -R modules /etc/collectd
```

You may need to modify the collectd.conf file, if you have configured your own id and password to access the ONOS.

Finally, run CollectD service.

```
$ sudo /etc/init.d/collectd start
```

### ONOS Installation and CPMan Activation

Install and run ONOS instance. The detailed procedures can be refer from [here](../../../guides/administrator-guide/installing-and-running-onos.md).

After ONOS has been initialized, we can activate CPMan application to receive system metrics from CollectD.

```
onos > app activate org.onosproject.cpman
```

# REST API for Collecting and Querying System Metrics

## Collector

|  |  |
| --- | --- |
| **POST /collector/cpu\_metrics** | **Collects CPU metrics.** |
| **POST /collector/network\_metrics** | **Collects network I/O metrics include in/out-bound packets/bytes statistics.** |
| **POST /collector/disk\_metrics** | **Collects disk I/O metrics include read and write bytes.** |
| **POST /collector/system\_info** | **Collects system information.** |
| **POST /collector/memory\_metrics** | **Collects memory metrics.** |

## Control Metrics

|  |  |
| --- | --- |
| **GET /controlmetrics/memory\_metrics** | **List memory metrics of all network resources.** |
| **GET /controlmetrics/messages** | **List control message metrics of all devices.** |
| **GET /controlmetrics/**messages/{deviceId}**** | **List control message metrics of a given device.** |
| **GET /controlmetrics/cpu\_metrics** | **List CPU metrics.** |
| **GET /controlmetrics/disk\_metrics** | **List disk metrics of all disk resources.** |
