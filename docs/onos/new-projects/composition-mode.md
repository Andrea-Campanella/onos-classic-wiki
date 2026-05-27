# Composition Mode

# Introduction

The goal is to implement the composition feature for ONOS. It will allow ONOS to run multiple applications concurrently and ONOS will automatically resolve conflicts that may arise from these applications. We will support the following three composition operators:

**Parallel operator (+):** The parallel composition of two application P + Q operates by logically (though not necessarily physically) copying the packet, applying P to one copy and Q to the other, and taking the union of the results. For example, let P be a monitoring policy and Q be a routing policy. If P counts packets based on source IP prefix and Q forwards packets based on destination IP prefix, P + Q does both operations on all packets.

**Sequential operator (>>):** The sequential operator enables two controllers to process traffic one after another. For example, let P be a load-balancing policy, and let Q be a routing policy. More specifically, for packets destined to anycast IP address 3.0.0.0, P rewrites the destination IP to a server replica's IP based on source IP prefix, and Q forwards packets based on destination IP prefix. To obtain the combined behavior of P and Q---to first rewrite the destination IP address and then forward the rewritten packet to the correct place—the network administrator uses the policy P >> Q.

**Override operator (|>):**Each controller x provides ONOS with a member policy specifying how x wants the network to process packets. The policy x |> T attempts to apply x's member policy to any incoming packet t. If x's policy does not specify how to handle t, then T is used as a default. For example, suppose one controller x is running an elephant flow routing application and another controller y is running an infrastructure routing application. If we want x to override y for elephant flow packets, y to route all regular traffic, and any packet not covered by either policy to be dropped, we use the policy x |> (y |> drop).

# Components

The implementation will include several components which will be contained in an experimental package on the master branch.

**Policy Interface Definition:** This component exposes an API for the network admin to configure the composition policy. It interprets the composition policy and configures ONOS to perform composition based on the policy.

***FlowRuleService*** **Implementation**: The existing ***FlowRuleManager*** receives flow rules from applications and maintains a flow table for each switch, where the primary partition resides on the same instance as the switch's master. The ***FlowRuleManager*** component will be copied and extended to include the following:

* Implement the policy interface specified above, and maintain the policy tree
* Distribute the policy via the ***ComponentConfigService***
* Maintain a flow table for each application and intermediate node in the policy tree (Note: The root of the tree contains the flow table to be programmed on the switch.)
* Provide the policy to the composition library and use the library to update intermediate tables when flow rules are added to "application" flow tables
* Rebuild and reprogram the intermediate and root flow tables when policy is changed

**Composition Library**: This stateless library (adapted from CoVisor) has access to the application and intermediate flow tables as well as the policy.

**Switch Rule Installation:** This component installs OpenFlow rules to physical switches, sends barrier request messages, and receives barrier reply messages. Since a rule from an application may generate multiple rules for a physical switch, we send confirmation to the application until we receive barrier reply messages for all the generated rules.

# API

**createPolicy(String policy):** We use a string to represent the policy. It will be interpreted by ONOS and is used to configure the composition. Example: createPolicy("Monitor + Router").
