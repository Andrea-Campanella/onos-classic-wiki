# Forming a cluster

**For ONOS 1.14 or later, see [Cluster Configuration in Owl (1.14)](forming-a-cluster/cluster-configuration-in-owl-1.14.md)**

Multiple target machines can act together as a unified, coherent distributed system, configured as a cluster. Once ONOS is installed (and runs) on multiple target machines, it’s very easy to form a cluster.

# Form a cluster from a target machine

From one of the target machines, run:

**Form a cluster of three instances, from one of the target machines**

```
/opt/onos/tools/test/bin/onos-form-cluster $TARGET_MACHINE_1_IP $TARGET_MACHINE_2_IP $TARGET_MACHINE_N_IP
```

where *$TARGET\_MACHINE\_X\_IP* is the IP address of the target machines that should form the cluster (including the IP address of the target machine where the commands are run from).
