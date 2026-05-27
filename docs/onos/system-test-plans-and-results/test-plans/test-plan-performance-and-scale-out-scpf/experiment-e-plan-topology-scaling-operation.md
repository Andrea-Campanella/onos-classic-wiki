# Experiment E Plan - Topology Scaling Operation

### Goals:

The goal of this test is to measure the latency and capacity for ONOS to discover and maintain the entire data plane topology.

When ONOS is brought up, it takes some time for ONOS to discover the network topology including establishing sessions to switches, downloading default flows, sending and receiving link layer discovery packets, assigning switch mastership, etc. During the discovery process, there are at least three things we concern: correctness, latency and stability. Correctness means the topology discovered by ONOS matches the actual topology in the data plane (e.g. Mininet topology); latency measures how long it takes for ONOS to complete the discovery; stability means the topology information stored in ONOS is stable (e.g. no connection lost). In this test we watch and record all three metrics as we scale up the topology size, until ONOS failed to discover a specific size of topology (the topology information in ONOS is incorrect or unstable).

### Setup and Method:

We start a 3-node ONOS cluster, and use OVS and Mininet to set up a TORUS topology. We scale up the topology from 5x5 to 10x10, and then 15x15, ... until 40x40, which is currently the up limit. After the topology is set, we assign the switches to ONOS cluster and balance the mastership. Then we check if the devices and links stored in ONOS match that in Mininet. If the topologies match, we record the latency for topology discovery and wait for 5 minutes and do another check to make sure that the topology data in ONOS is stable. If both correctness and stability are ensured, we continue to the next topology scale. If either of the two measurements fails, we exit the test.

| Topology Discovery Metrics | Description | Roadmap |
| --- | --- | --- |
| Correctness | Devices and links stored in ONOS match that in Mininet | Now |
| Latency | How long does it take for ONOS to discovery all devices and links in the data plane | Now |
| Stability | Make sure the topology information stored in ONOS is stable | Now |
