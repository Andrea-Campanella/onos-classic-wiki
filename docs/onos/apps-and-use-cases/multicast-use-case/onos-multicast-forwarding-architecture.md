# ONOS Multicast Forwarding Architecture

# ONOS MFWD Architecture

The ONOS MFWD multicast architecture is composed of 4 primary functionalities: the *Mulitcast Route Table* that maintains Multicast ASM (\*, G) and SSM (S, G) forwarding state within the ONOS controller, the *MulticastForwarding* module which responds to live multicast data traffic, the *MulticastIntentManager* responsible for interacting with the *ONOS IntentService* which in turn establishes paths through the network. Finally we have the *MFWD CLI & REST* *API*which allow external operators and applications to examine and modify existing mfwd state.

The following paragraphs we will breakdown each of the components and provide a couple graphics to help visualize these relationships.

## [Multicast Route Table (MRT)](file:///C:/Users/Rusty/appdata/local/temp/20.html#multicast-route-table-mrt)

The *Multicast Route Table (MRT)* which may also be referred to at times as the *Multicast Routing Information Base (MRIB)*, is essentially the repository for *Multicast Routes* maintained by ONOS.

The *MRT* manages the set(s) of *multicast routes* (forwarding state) on behalf of external inputs that include:

* Active multicast data via *ONOS Packet Service*
* Interactive operator inputs via ONOS CLI Service
* External applications via the ONOS REST Service
* Future modules include
  + PIM-SSM Emulation
  + IGMPv3 Proxy

### [Multicast Route Table implementation](file:///C:/Users/Rusty/appdata/local/temp/20.html#multicast-route-table-implementation)

The multicast route table is java class defined in the following file exposing the corresponding API:

* **McastRouteTable.java**
  + Private members:
    - mribv4 - Set of IPv4 routes
    - mribv6 - set
  + McastRouteTable.getInstance() - Single instance of the MRT
  + getMrib4() / getMrib6() - retrieve the actual IPv4 & IPv6 tables
  + storeGroup(McastRouteGroup group) - store a multicast group
  + removeGroup(McastRouteGroup) - remove the associated group
  + addRoute(String source, String group) - store either a (\*, G) or (S, G)
  + addRoute(IpPrefix sourcePrefix, IpPrefix groupPrefix) - same as above
  + removeRoute(String source, String group) - remove corresponding route
  + removeRoute(IpPrefix sourcePrefix, IpPrefix groupPrefix) - same as above
  + findMcastGroup(IpPrefix group) - find a specific Mcast Group
  + findMcastSource(IpPrefix source, IpPrefix group) - find a specific (s, g)
  + findBestMatch(IpPrefix source, IpPrefix group) - find the best match
  + printMcastRouteTable() - used by the cli 'mcast-show'
  + toString() - summary string.

### [Multicast Routes](file:///C:/Users/Rusty/appdata/local/temp/20.html#multicast-routes)

The multicast routes are divided into two categories: a *group route (\*, G)*, also known as Any Source Multicast (ASM). There are also *source routes (S, G)* also known as Source Specific Multicast (SSM).

Structure of Multicast Routes are comprised of the follow Java classes and Interfaces. For the official MFWD API refer to the ONOS API documents. The class can be found with the corresponding java file.

* *McastRoute* Interface that defines the public API of all McastRoutes

  + getGaddr() - get the IP multicast address
  + getSaddr() - get the IP unicast address. 0/0 for (\*, G)
  + addIngressPoint(ConnectPoint ingress)
  + getIngressPoint()
  + addEgressPoint(ConnectPoint egressPoint) add individual egress points
  + getEgressPoints() - get the set of egress points
  + setIntents(SinglePointToMultipointIntent p2mp, MultipointToSinglePointIntent mp2p) - set the P2MP & MP2P intents
  + getP2MPIntentKey() - gets P2MP the intent
  + getMP2PIntentKey() - get the P2MP intent
  + toString()
* *McastRouteBase* implements *McastRouteBase*

  + Implement all of the functionality common to both (\*, G) and (S, G) routes.
* *McastRouteGroup* extends *McastRouteBase*

  + Implements functionality unique to (\*, G) routes
  + private members
    - *sources*: container for all (S, G) entries that share the same multicast group address G.
  + findSource(IpPrefix saddr) - find a specific source for this group (S, G)
  + getSources() - get all sources that belong to this specific group
  + addSource(McastRouteSource src) - add a new source to this group
  + removeSource(IpPrefix sourcePrefix) - remove a specific source from this group
  + removeSources() - remove all sources from this group.
* *McastRouteSource* extends *McastRouteBase*

  + Implements functionality unique to (S, G) entries
  + N/A

#### [How the MRT Stores Multicast routes](file:///C:/Users/Rusty/appdata/local/temp/20.html#how-the-mrt-stores-multicast-routes)

The MRT maintains a set of *McastRouteGroup* groups corresponding to each IPv4 or IPv6 group MFWD is maintaining state for.

The **McastRouteGroup** serves two purposes, first to maintain forwarding state for (\*, G) ASM as well as a parent container for all McastRouteSource (S, G) routes that share the same multicast group address G.

#### [ConnectPoints](file:///C:/Users/Rusty/appdata/local/temp/20.html#connectpoints)

*ConnectPoints* are an ONOS construct consisting of a switch name and port number. For the purpose of multicast we use the *ConnectPoints* to determine where multicast data enters (ingress) the SDN network, as well as the *set* of *ConnectPoints* the multicast data leaves (egress) the network.  Egress ConnectPoints will have a receiver attached to that connect point or forward multicast traffic into a network outside of the given SDN segment.

*McastRouteBase*, the parent of both (\*, G) and (S, G) routes allow a single ingress *ConnectPoint* and set of *egressConnectPoints.* The corresponding API will allow various connect points to be added and removed from the route base.

*Note:* in the case of (\*, G) the ingress ConnectPoint maybe NULL due to the fact that, by definition, the source of the multicast group is not known.  How *Any Source Multicast* is handled is dependent upon the use case and the specific implementation.  Currently we don't have any requirements to provide ASM support, however MFWD was designed as to *not preclude* ASM support.

Both *McastRouteGroup* and *McastRouteSource* leverage the base class implementation of ingress and egress management functions, both classes provide additional functionality required for their respective needs.

## [Multicast Intent Manager](file:///C:/Users/Rusty/appdata/local/temp/20.html#multicast-intent-manager)

The *McastIntentManager* is responsible for registering with the ONOS *IntentService*, formulating and changing intents based on specific McastRoute State. The intent manager is also responsible for withdrawing intents and cleaning up after MFWD when the application is deactivated.

The *McastIntentManager* will register a *SinglePointToMultiPointIntent* for each multicast route which is used to forward multicast state.

The *McastIntentManager* relies on the following ONOS services:

* IntentService
* TrafficSelector
* TrafficTreatment

The *McastIntentManager.java* provides the following:

* *McastIntentManager* class
  + activate() / deactivate() Karaf / felix components
  + McastIntentManager.getInstance() - get the singleton instance
  + setIntent(McastRouteBase mroute) - create and set intents for this route
  + withdrawIntents(McastRouteBase mroute) - withdraw intents
  + withdrawAllIntents() - clean up all intents when MFWD has been deactivated

## [Multicast Forwarding](file:///C:/Users/Rusty/appdata/local/temp/20.html#multicast-forwarding)

The *MulticastForwarding* module is responsible for handling live multicast data.  For incoming multicast packets that do not match an existing multicast forwarding entry, the module will create a multicast forwarding entry with the ingress ConnectPoint with no egress ConnectPoints.  The state will be ready when and if receivers indicate interest.

When live multicast data arrives for which an entry does exist, if that entry also has one or more egress ConnectPoints, the entry is completed with the ingress ConnectPoint and handed to the MulticastIntentManager, which subsequently creates a SinglePointToMultiPointIntent that then is used to install the corresponding flow paths through the relevant switches.

flow in the OpenFlow switch and hence are passed upstream to the controller.

If no multicast forwarding state exists, the *McastForwarding* module will create multicast state.
