# Design

# ICONA Architecture

A cluster is a multi-instance ONOS deployment. Each ONOS instance, or node, shares the network state and topology with all other nodes in the same cluster. In a multi-domain scenario we expect that multiple ONOS clusters exchange network information similar to standard multi-domain protocol.

The ICONA module leverages on the ONOS provider subsystem to manage the domain topologies exposed by the remote clusters and to abstract the underlying network view to expose. The communication between remote clusters is provided by an East-West communication interface. ICONA is not bounded to a single mechanism to share and configure the topology, but it allows different type of implementations, leveraging on the ICONA APIs.

![](https://lh6.googleusercontent.com/vWgC3fS3jj6tanwFLWhii01-aOtq5KQvbTHZD4M_xS0Jl831sSFpapUsmU9Dzx5GmuzB5MZTsowUsYUwlBW1RlDoxIxLSdnbtA4AGdcMfdUoKYN1bMoKTRKe6SNDsbkOA_46iriR)

Fig.2

Figure (Fig.2) places ICONA inside the ONOS architecture and the East-West interface allowing clusters to exchange topology information.

In this case Cluster 1 and Cluster 2 are sharing, through ICONA, their topologies as big switches (according to the policies applied towards the other cluster). The outcome, as shown in the figure below (Fig.3), is a topology comprising both the remote and the local topology.

ONOS will be able to distinguish between remote and local elements. Remote elements are properly annotated before being notified to the ONOS core.

![](https://lh5.googleusercontent.com/CU5jR0LO8xFnj-cmoZtYGr-meooPtFG9wEf7QPn0END4pIoMmbaN9LlVGLpj0aGoJLTNVZIuDc_pDk7q-83zL4iIc-Mn9ycdL251tljVk6PRq_zoW995z_ZJucyCxqdutBRwYGVx)

Fig.3

Notice that ICONA does not directly interact with local network elements. In fact local topology events are sensed through the core. For simplicity we distinguish between two kinds of event:

* local event - when the local topology needs to be exposed or changes that are relevant to the other clusters occur and they are to be communicated to the other clusters
* remote event - when a remote cluster communicates for the first time its topology or its exposed topology undergoes some updates

Moreover, the communication between clusters relies on interfaces that can be implemented by different communication mechanisms described in the following.

In order to make ICONA as flexible as possible, its structure is vertically divided into two logical layers (Fig.4):

![](https://lh6.googleusercontent.com/xzDJzA0JTOfzoKD-CnmSLCCOkJU3WYS6FW0T_nVpQIX61dERlifWLoRojA6mG28OJ_b6oFE1ZzAg_2DT7ffzbJY9SHVvkFsmTiGD3K7051suC8gQ3Uy1xG2z1ZLawCd75h8MYWn4)

Fig.4

* the domain provider which interacts with the ONOS core and with the Southbound Bundles (SBs)
* the domain manager
* multiple SBs, each one tied to a specific communication mechanism to use between clusters/domains. Currently, we are implementing a BGP SB and a peer-2-peer REST SB

This will allow ICONA to adapt to different communication mechanisms, just by implementing the SB specific mechanism, without the need of modifying the provider logic.

## Domain Provider

The Domain Provider is the main component of ICONA. It is the component lying between the ONOS core and the SB specific communication mechanisms, and it performs the following functions:

* builds an aggregate form of the local topology to expose to the peer domains. The aggregation follows policies given from configuration (currently only the bigSwitch abstraction is supported)
* receives remote topology elements from the other domains and notify their presence to the core
* handles local topology events which could reflect a change in the topology exposed to the other domains
* receives remote topology updates

The provider is composed by multiple components (Fig.5):

* the IconaTopologyManager is the component in charge of building the aggregated topology to expose to the remote clusters according to the configuration policies. It is also responsible to notify the remotes about relevant local changes.
* three providers components: IconaRemoteDeviceProvider, RemoteIconaLinkProvider and RemoteIconaHostProvider, that are responsible to expose topologies coming from the remote clusters to the ONOS core. To this aim, they export the respective IconaSB{Device | Link | Host}Service which are consumed by the SBs in order to notify the provider. For example, the SB that receives a big switch topology from a remote cluster will call the method addRemoteDevice() of IconaSBDeviceService implemented by the IconaRemoteDeviceProvider

![](https://lh4.googleusercontent.com/yerdp27h-FonlNbmyHv-TsfAH-zlpKUBkF9p_nsdTBJkDOY7fVyUauVyPbTfF9NzfigeNvrjOdObD-LfAR8muiMiBy9t9MqBfEv8nN8i4AFFOCxGigb3fNz1p_stgE8RgnahsDLO)

Fig.5

## Domain Manager

The domain manager (Fig.6)

![](https://lh6.googleusercontent.com/5JYZ5SCqsADNbhGj4Och3k_jQaJqnTHpaFH-FIH3oHiLV1lCId2lduR_8lFkhMOHUFn54qVDFkfCausqqGnFEBSMDf7iHIsBEz9pHu-QNcRKrFXC56K0qEXWQ4Yzdxh70i2feE5M)

Fig.6

## Southbound  Mechanisms

A southbound mechanism is an implementation of how two clusters exchange information about topologies or services. In other words, it is the implementation of the East-West interface between different clusters.

These mechanisms adapt the Domain Provider logic to different specific communication mechanisms, such that the Domain Provider will be able to choose the right southbound mechanism when communicating with another cluster.

The figure below (Fig.7) shows how a cluster (cluster 2) is able to communicate with other clusters exploiting, at the same time, different southbound mechanisms.

![](https://lh5.googleusercontent.com/EshHsglF9fIreNH7PyhCXDLHR-0uLF5IItR_L69kFZmclTn12svGZd8QlWqEvsxtG3M0mFjGqvV2ZkfhL0tshb1lXOldv-MrSqRBiNA-YAvMXe5ycau5QXF5TBqrhwRS94wFpfAd)

Fig.7

# Functionalities

## Topology Management

ICONA  handles local and remote events differently.

A local event is sensed by listeners in the IconaTopologyManager and it is propagated to one or more specific mechanisms. In particular, the IconaTopologyManager uses listeners for sensing local topology events generated by the core and in turn communicates with the southbound modules implementing the Whiteboard Pattern as publisher, by exposing the IconaSBListenerService. Infact a specific mechanism registers the IconaSBListener to the SBManager through which it will receive calls, relative to local topology changes, to propagate to a remote domain (Fig.8). A SB will take care of such information only if it concerns a change affecting a domain whose communication is handled by the SB itself. For example, if cluster A communicates with cluster B through SB X and with cluster C through SB Y, SB X will ignore all calls related to cluster C; this is done in order to let IconaTopologyManager be agnostic w.r.t the specific communication mechanism used with a remote cluster.

![](https://lh4.googleusercontent.com/dcXNAR9vJKvCvAZAG4WG-O3l92bB4qF5NpcEXf5w854xyPEXayfgkLDc_JfW1iK36XvdPhrwGVPnbmrTsKD1-Fxpx2HG7TMfgrTP73eRgeIt1WtMkIvDDse62mhAXDE9m8DjhFj0)

Fig.8

Each ICONA provider component exports a service, called IconaSB{Device | Link | Host}Service, consumed by the SB in order to advertise the provider about the remote event. So, a remote event is forwarded by one specific mechanism to the domain providers (device/host/link providers) through these services. Then, the providers supply an abstraction to ONOS of the remote topology elements.

Once the core has been notified about the event from the provider, the DomainManager notices the presence of new elements and checks the annotations looking for a specific key (the domain Id). If the element is related to ICONA, the DomainManager saves into the DistributedDomainStore the association between the new elements and the proper domain identifier and made the mapping available to the NB apps (Fig.9).

![](https://lh5.googleusercontent.com/foElQOy8GE7AhGPXwDdt0ONwFsimkMTpLWVxSaHPSTA9vrA70V1IP1GBaH3XGdxcpIlb5DTQWqUi_UBr1kf8IBdN-QsLI1vrwMtVk8g-Z18oxHxd8DAg0aakKnIn4UvO65vxdMi6)

Fig.9

## Flows Management

TODO
