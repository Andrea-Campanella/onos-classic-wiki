# Experiment L Plan - Host Add Latency

### Goals:

The goal of this test is to measure the latency to discover a host for ONOS as a cluster in various sizes.

### Setup and Method:

We scale up ONOS from 1 node to 3,5,7 nodes. For each scale, we setup a Mininet topology with only one switch and one host. We assign the switch to ONOS and activate "proxyarp" app for host discovery. There are two time points we concern in this test. The first is the time when a packet-in message triggered by the host is generated, and we consider the timestamp of that packet as the beginning of the host add process. The second is the time when ONOS generates a Host Event, which we consider as the end of the host add process.

We run 25 iterations (including 5 warmups) to gather statistical results. In each iteration, we sent out an arping message from the host which will then trigger a packet-in sent to ONOS. Before sending the arping, we start tshark to capture packet-in messages sent from the switch, and at the same time we watch the changes of Host Event timestamps recorded in ONOS using “topology-event-metrics” app. By collating those timestamps, we calculate an end-to-end latency by subtracting the packet-in timestamp from the Host Event timestamp.
