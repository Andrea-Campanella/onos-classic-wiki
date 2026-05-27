# OpenstackSwitching Test Cases

## Test Conditions

1. A network node in installed with the L3 agent enabled
2. ONOS cluster with at least three nodes

## Basic VM creation test

| Conditions | Cases | Actions | Results |
| --- | --- | --- | --- |
| N/A | Create VMs | All flow rules are created properly |  |
| VMs are created | Remove VMs | All flow rules for the VMs are removed |  |
| VMs are created | Initialize the app | All flow rules for the VMs are created |  |
| 1. Create VMs 2. Initialize the app | Remove VMs | All flow rules for the VMs are removed |  |

## Router test

| Conditions | Cases | Actions | Results |
| --- | --- | --- | --- |
| VMs are created | 1. Create a router 2. Attach an interface of the subnet of VMs to the router | 1. Flow rules for the router are added to all C-Nodes 2. Flow rules for the VMs and the gateway itself are added to the network node |  |
|  | 3. Remove router | 3. All flow rules for the router in all C-nodes are removed |  |
| No VM is created | 1. Add a router | Flow rules for the router are added in the network nodes |  |
|  | 2. Create a few VMs | Flow rules for the VMs and router are added in the C node  Flow rules for the VMs are added in the network node |  |
|  | 3. Remove the router | Flow rules for the router are removed from the C nodes  All flow rules for the VMs are removed from the network node |  |

## HA Test

| Conditions | Cases | Actions | Results |
| --- | --- | --- | --- |
| one of C-nodes is attached to different ONOS instance | 1. Create a few VMs | 1. Flow rules for the VMs are added |  |
|  | 2. Kill an ONOS instance that a C-node with at least one VM among the VMs created in previous step is connected with | 2. All flow rules should be still there in all C nodes |  |
|  | 3. Remove a VM whose host's master controller is changed | 3. Flow rules for the VM are removed  That is we check that flow rules that are inserted from a controller instance (instance A) can be removed from a new controller instance (instance B) when the instance A is dead. |  |
