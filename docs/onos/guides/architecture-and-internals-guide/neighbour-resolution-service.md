# Neighbour Resolution Service

The Neighbour Resolution Service provides an abstraction that makes it easy for applications to specify how neighbour discovery packets (e.g. ARP, NDP) should be handled for the slice of traffic that the application is managing.

# Target use cases

Previously applications had the option of implementing their own neighbour message handling themselves on top of the PacketService, or to try and fit their logic into an existing neighbour-handling application such as ProxyARP. Solution one means that many apps contain very similar code to parse and construct neighbour messages etc, even though they only have small differences in the handling logic. Solution two becomes very complicated because multiple use cases have to be managed within a single application, and the logic becomes very complex.

The NeighbourResolutionService aims to solve these problems by allowing an application to specify a NeighbourMessageHandler for a particular connect point or interface. The NeighbourMessageHandler is a small piece of logic that decides how to handle the message, and conveys the result of that decision to the NeighbourResolution framework.  This separates decision logic from mechanisms used to parse and generate packets, and it allows applications to contribute their own handling logic that may read an application-specific config or state, without having to insert this logic into an existing application like ProxyARP.

# NeighbourMessageHandlers

The handler is specific to a switch port or interface, which means an application can register multiple different types of handlers for different ports or interfaces if it needs different neighbour message handling for them. For example, the SDN-IP application has different neighbour message handling logic for ports where external peers are connected versus ports where the internal BGP speaker is connected. This also allows multiple applications to specify neighbour message handling at the same time, so long as they don’t conflict in the connect points or interfaces that they add their handers for. There should be a somewhat natural division of connect points or interfaces for different applications, because different applications are interested in handling different slices of the traffic.

# Handler Registration

A handler must be registered with the NeighbourResolutionService for a particular connect point or interface. This means that the message handler will receive packets that come in to the system from that connect point or interface. Handlers are advised to be stateless, and therefore it is possible to register the same handler instance at multiple connect points or interfaces.

A handler registered for a connect point will receive all packets that come to the control plane (e.g. via OpenFlow packet-ins) from that connect point. A handler registered for an interface will receive all packets coming to the control plane from that interface. This means they must come from the connect point that the interface references, and the packet headers must match the parameters of the interface. For example, if the interface has a VLAN configured, then only packets coming through the connect point with that particular VLAN tag will be delivered to the neighbour message handler. Likewise, if the interface has an IP address configured then only neighbour messages that target that configured IP address will be delivered to a handler registered for that interface.

# Handler implementation

NeighbourMessageHandlers operate on a higher layer abstraction than the packet-ins and packet-outs that previous neighbour message logic was forced to operate on. The handler receives a NeighbourMessageContext as its argument. This context provides access to fields of the incoming packets that the handler may be interested in in a protocol-agnostic way, so the handler doesn’t have to reconcile the differences between ARP and NDP. The original incoming packet is also available if the handler is interested in a field that is not available through the context API. The handler can easily see whether the message was a request or a reply, as it is common to require different logic for these different types of messages.

Apart from information about the incoming packet, the context API also provides mechanisms for the handler to specify the decision it has made. There are currently four different decisions a handler can make: reply, forward, flood, and drop. When the handler calls these APIs, the framework takes care of performing the appropriate action. If none of these actions are appropriate for a handler, it is free to implement its own result (but it may require more code to formulate an output packet, etc.). New actions may be added to the framework if they are general enough to apply in a range of situations.

To summarise, an application that is interested in using the NeighbourResolutionService to simplify its neighbour message processing must do two things:

1. Implement one or more NeighbourMessageHandlers, which receiving incoming neighbour messages (abstracted in a NeighbourMessageContext), decide how to handle the messages and then convey their decision to the framework (again using NeighbourMessageContext APIs).
2. Register their handler(s) at the appropriate connect point or interface such that they will receive the traffic that they are interested in.

# References

Please refer to the following APIs for Javadoc:

```
NeighbourResolutionService
NeighbourMessageContext
```

A good application to look at for developers looking to see an example of the neighbour resolution service in use is the ProxyARP application (ProxyARP does handle NDP messages as well). The ProxyARP application responds to ARP or NDP requests on behalf of a target host if the target host is known to ONOS (i.e. it is present and active in the Host store). ProxyARP considers the network to be a single IP network, therefore if it receives a request for which the target host is not known, it will flood the request out every edge port in the network (apart from the input port) in the hope that the host exists in the network and will reply.

# CLI

There is a CLI command that allows users to view the neighbour handler registrations that are held by the service. The CLI command is ‘`neighbour-handlers`’.
