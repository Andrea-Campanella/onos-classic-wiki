# Experiment M Plan - Mastership Failover Latency

### Goals:

To test the latency for an ONOS node being killed, instance deactivated, and role request as ONOS scales.

### Setup and Method:

The test scales ONOS from 3, 5, and 7 nodes.  A Mininet topology with 5 switches and 5 hosts is created for each scale.

There are 75 total iterations; 5 iterations being a warmup, and 20 iterations recording the results.  Each iteration consists of the following procedure:

| Sub-Step # | Description |
| --- | --- |
| 1 | Assign mastership to ONOS node 0. |
| 2 | Kill ONOS node 0. |
| 3 | Stop ONOS node 0. |
| 4 | Obtain latencies from 'events' output. The command 'events -a' is sent to the ONOS CLIs that are up. Instance deactivated and master changed times are obtained and latencies are calculated. |
| 5 | Obtain latencies from tshark output. Role request time is obtained and latency is calculated. |
| 6 | Verifying that the data are valid before recording the data. Ensures that there are no negative numbers or other unusual results. |
| 7 | Restart ONOS node 0 and check status of restart. |
| 8 | Checking ONOS nodes, and if ONOS CLI 0 has restarted. |
