# Use Case Description

### Overview

On a traditional IP RAN network, a large number of access devices are deployed at the access layer. In current network construction and operating modes, decentralized access routing devices need to be managed node by node, which is time and manpower consuming and also drastically increases the operation and maintenance cost.

To help customers address those challenges, Huawei creatively proposes the SDN-based mobile backhaul solution, which has a centralized control plane as the basic idea. This solution requires only one control center to control all network behaviors. In this solution, topology summarization and path computation are all complete on the control plane, and the access routing devices are required to provide the access function only. Therefore, this solution simplifies access routing devices. All devices at the access layer are managed like one device.

Compared with a traditional IP RAN networks, SDN-based IP RAN solution aims to bring in ease of management and deployment by extracting the control plane from traditional IP-based RAN for mobile backhaul with a centralized SDN control plane. SDN-based mobile backhaul solution provides the following three benefits:

* One: Free service planning, that is, plug-and-play
* Two: Intelligent and rapid service provisioning
* Three: Fast trouble shooting

### Project Goals (Phase 1)

Building SDN-based IP RAN requires solving complex technical and deployment challenges. It requires a carrier grade SDN control plane as well as comprehensive service and other network provisioning/service deployments models on top of the control plane. In this phased project, our initial goals for phase 1 are:

* Demonstrate a SDN controller solution through Integrating ONOS with Huawei in-house built controller(a.k.a SNC)
* Demonstrate Network Provisioning/Service Deployment model (P-C Model) through provision MPLS network and providing L3VPN service.
* Demonstrate how an application to control the network through Intent interface (e.g. connectivity Intent API) and precise control interface (e.g. flow rule API).
* How ONOS to work with Huawei's devices through its southbound provider interface
* Huawei devices and in-house SDN controller(a.k.a SNC) interoperates with ONOS to deliver a resilient SDN-based IP RAN solution.

### Project Background and Milestones

Huawei teamed up with ON.LAB ONOS project development team on this Use case back to August, 2014. The development work was running in parallel with Avocet release development. Our first demo was shown in ONOS Open Source Announcement Webinar, and then on ONOS summit 2014 as well.

* August 2014,  started the project based on ONOS architecture 1.0 code base
* November 2014, ported to ONOS architecture 2.0 code base.
* December 5, 2014,  demoed on ONOS Open Source Announcement Webinar (Avocet Release)
* December 9, 2014,  demoed on ONOS Summit 2014.
* Blackbird Release,  FlowRule Extension code committed.
* Cardinal Release,  MPLS Label Management and Tunnel Manager code contribution are planned
