# Flow Rule Subsystem

# Introduction

The flow rule subsystem is responsible for managing flow rules in the system and installing them in devices in the network.

This subsystem implements the semantics of a distributed authoritative flow table where the master copy of the flow rules lies with the controller and this is pushed down to the devices. This means that the flow rule subsystem never tries to discover information from the network or tries to work around flows that already exist on devices. If ONOS detects a flow on a device that should not be there according to its authoritative flow table, that flow will be removed.

The general model implemented by the flow rule subsystem is applicable to the group subsystem and metrics subsystem as well.

# Managing Flows

Flows are installed into the flow rule subsystem through the FlowRuleService API. Flows in the system exist in one of the following states:

* PENDING\_ADD – this indicates that the flow rule subsystem has received a request from the application to install the flow rule, but the subsystem has not yet observed that flow on the device. Internally the request is forwarded to the node that is master for the device in question, and this node will use the appropriate FlowRuleProvider to install the flow to the device.
* ADDED – once the flow rule subsystem observes the flow on the device it will transition to this state. The FlowRuleProvider is responsible for reporting information about observed flows to the flow rule subsystem.
* PENDING\_REMOVE – the flow rule subsystem has received a request from the application to remove the flow, but has not yet received confirmation that the flow has been removed from the device. The FlowRuleProvider will be instructed to remove the flow from the device.
* REMOVED – the flow rule subsystem has received confirmation from the FlowRuleProvider that the flow has been removed from the device, and the flow will be removed from the store shortly.
* FAILED – the device indicated that the flow rule installation failed.

The flow rule subsystem supports installing flows in batches which are dependent on one another. This done using the FlowRuleOperations object, which contains a list of stages of FlowRuleOperation. The semantics are that the operations in each stage must be fully completed before the flow rule system can begin working on the subsequent stage.  An example usage of this feature is when you want to install the tail of a path before the head flow rule to prevent traffic from being black-holed while the path is being set up.

# Dataplane reconciliation

Flow rule providers are responsible for collecting statistics on flows installed in the network and reporting these statistics to the flow rule subsystem. The flow rule subsystem uses these reports to ensure that its idea of the authoritative state is still present on the devices on the network.

For example, the OpenFlowRuleProvider periodically queries the flows on the device using OpenFlow FLOW\_STATS\_REQUEST messages. When the device responds with FLOW\_STATS\_REPLIES, the provider sends this information to the flow rule subsystem using the FlowRuleProviderService#pushFlowMetrics() method. If the flow rule subsystem can match those flow metrics to flows in its store, it will update the statistics on those flows. If it sees extraneous flows on the dataplane that aren’t in its store, it will remove those from the dataplane. If it detects that a flow is missing from the dataplane, it will attempt to reinstall it.
