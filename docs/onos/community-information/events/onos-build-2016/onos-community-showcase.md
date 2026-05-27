# ONOS Community Showcase

## **ORGANIZER**: [William Quiviger](https://wiki.onosproject.org/display/AM/William+Quiviger) (ON.Lab) - william AT onlab DOT us

## **SCHEDULE**: Thursday Nov 3 (14:00 - 17:00) and Friday Nov 4 (11:00 - 15:30)

## **LOCATION**: **Room A**

---

### What is it?

The ONOS Commuinty Showcase is a series of talks, presentations and demos by partners, collaborators and contributors of the ONOS Community. 

### **What is the overall goal of the showcase?**

The aim is to provide a platform for members of the ONOS community to share and learn from each other. 

### How will the talks be run?

Each talk will be between 20 and 30 minutes long and will be in the form of slide presentations.

### Who can participate ?

The showcase is open to everyone. Registered participants who have submitted a talk proposal and who have been confirmed as speaker will be appear on the schedule.

### List of confirmed presentations:

* [PCECC as SDN transition solution](https://onosbuild2016.sched.org/event/82kn/onos-community-showcase-pcecc-as-sdn-transition-solution)

Legacy network transition to SDN network need a gradual transition. So PCE as Central Controller(PCECC) help to move control plane of MPLS network and provide programmability and agility to the network

* [Adaptive Flow Monitoring & Selective DPI for ONOS](https://onosbuild2016.sched.org/event/8PJd/onos-community-showcase-adaptive-flow-monitoring-selective-dpi-for-onos)

This talk will introduce the implementation of DPI into ONOS.To cope with the performance and scalability problem of current OpenFlow protocols flow statistics collection mechanism due to the per-flow based polling, AFM & SDPI provide algorithms, protocols, and facilities to collect flow statistics efficiently to reduce the overhead of controllers.  AFM reduces overhead by adjusting flow collection rate adaptive to the characteristics of flow size.  SDPI performs deep packet inspection to some specific flows (e.g., flows for premium service customers) for accurate application analysis or anomaly detection purposes.  In this presentation, Taesang Choi will review the state-of-the-art of traffic flow monitoring for SDN, discuss the associated challenges, introduce the ONOS OPEN-TAM subproject that implements AFM & SDPI functionality, and describe experiences on the deployed use cases and future work.  
The audience is anyone interested in traffic flow monitoring and analysis development for SDN and NFV networks. Especially, SDN network equipment, SDN/NFV NMS/OSS, SDN/NFV orchestrator, and network anomaly detection & analysis solution vendors are the favorable audience.  Attendees can expect information on the SDN/NFV traffic monitoring technology state-of-the-art, main outstanding challenges, and the solution with use case deployment experiences.

* [YANG based NBI/SBI in ONOS](https://onosbuild2016.sched.org/event/8PJe/onos-community-showcase-yang-based-nbisbi-in-onos)

Using YANG, applications are abstracted about the external protocol interaction. Application are requited to model the NBI interface in YANG and  implement the business logic. YANG framework, automates the external world interaction.

Driver / provider to register the device schema to YANG management system and interact with device (SBI) using POJO generated from YANG files.

* [An enhanced PCE for WAN environment](https://onosbuild2016.sched.org/event/82ku/onos-community-showcase-an-enhanced-pce-for-wan-environment)

The objective of this work is to implement an SDN-WAN solution to optimize the allocation of paths connecting geo-distributed data centers. The SDN-WAN architecture adopted in this project leverages PCEP and BGP-LS protocols provided by ONOS. To implement this architecture, we make of use ONOS framework and IOS-XR v Cisco routers. Then, we extend PCE algorithm to enhance the quality of  selected paths. The results demonstrate that our approach improves QoS applications while ensuring load balancing of  the network infrastructure.

* [Agile On-boarding of Virtualized and Disaggregated Services with ONOS Architecture](https://onosbuild2016.sched.org/event/8PKF/onos-community-showcase-agile-on-boarding-of-virtualized-and-disaggregated-services-with-onos-architecture)

Mobility is one of the most ubiquitous technology of today's modern networks.  On boarding end to end mobility services is a complex process.  Doing so in DEVOPS model intensifies the process and resource dynamics.  Agile services creation, onboarding, and full lifecycle management of these mobility services will be critical for commercial success and rapid industry adoption. Virtualized and disaggregated mobility service creation via northbound APIs, service chaining, and orchestration requires an end to end view from DevOps programmable models to service deployment and mechanisms for rapid innovation with new incremental service creation.  This session will explore some of the challenges and successes with e2e integration with ONOS architecture in this realm as the industry collectively moves forward in this new and exciting space.

* [Smart SFC](https://onosbuild2016.sched.org/event/8PKH/onos-community-showcase-smart-sfc)

Smart SFC is an ONOS based application which aims to bring smartness to the current SFC solution by Reducing operators TCO by providing efficient resource utilization, increasing customer satisfaction by enhancing reliability, satisfying customer SLAs by real time resource monitoring and enabling quick provisioning by providing a smart intent GUI framework.

* [Open Orchestration using OPEN-O](https://onosbuild2016.sched.org/event/82l9/onos-community-showcase-open-orchestration-using-open-o)

OPEN-O is a Linux Foundation Collaborative Project that enables operators end-to-end service orchestration over NFV along with SDN and legacy networks. By virtue of where it resides in the stack, open orchestration must inherently integrate with a number of frameworks at the service, control (including ONOS), and infrastructure layers. In this presentation we examine the trends driving open orchestration, the role SDN plays in enabling end-to-end composite services, and provide an overview of the OPEN-O architecture and project. OPEN-O is moving towards its initial release, with ONOS support for WAN SDN Control for a virtualized CPE use case, driven by the world's largest mobile operator (China Mobile, with 826 M mobile subscribers)

* [Field trial plan of disaggregated transport network in NTT Communications](https://onosbuild2016.sched.org/event/8PKO/onos-community-showcase-field-trial-plan-of-disaggregated-transport-network-in-ntt-communications)

NTT Communications plan the field trial of disaggregated transport network controlled by ONOS. For the field trial, we will deploy them in our wide area testbed network environment used for R&D activities to evaluate the ONOS from the perspective of commercial service deployment. Toward the deployment, we have been developed a few of new functions of ONOS with ON.Lab that are required to control disaggregated transport network. In this session, we will show our initial deployment plan and current status, functions of ONOS that have been developed for our deployment, and our future deployment plan.

* [Data Center Virtual Networking Solution: SONA](https://onosbuild2016.sched.org/event/82lF/onos-community-showcase-data-center-virtual-networking-solution-sona)

Now OpenStack is the de-facto solution for data center resource virtualization, and there are many commercial solutions using the OpenStack community version. However, the network stack Neutron still has some limitations such as scalability, which degrades the overall network performance.

We have introduced SONA, which is scalable but simple and multi-tenant support network virtualization solution for OpenStack. Also, we have contributed the full source codes to ONOS. Now it is a key component of COSMOS, which is a SDDC architecture for SKT's All-IT infrastructure. In this talk, I am going to present the architecture, features, and a few simple demos including the entire COSMOS architecture.

* [ONOS Community Showcase: ONOS-based KREONET-S Deployment and VDN Application System](https://onosbuild2016.sched.org/event/8PKs/onos-community-showcase-onos-based-kreonet-s-deployment-and-vdn-application-system)

KREONET-S is a new network project to drive softwarization of KREONET Infrastructure. It is designed to provide end-to-end SDN production network services for advanced researches and applications requiring time-to-research and time-to-collaboration. KREONET-S is currently deployed to softwarize four regional & international network centers in 2016. Especially, international SD-WAN connection between Daejeon in Korea and Chicago in USA was implemented over 100 Gbps optical fiber.

Virtual Dedicate Network (VDN) application on ONOS-based KREONET-S deployment provides dynamic and on-demand virtual network provisioning per user with bandwidths guaranteed. The purpose of VDN application indicates new user interfaces and services along with innovative user experiences, e.g., deterministic network performance and higher security derived from strict virtual network insolation.

In order to accomplish this purpose, VDN application has principal functions as follows: 1) user authentication and authorization based on user types, 2) fast VDN generation for user group by using network abstraction with pruning strategy, unification of multiple links, and an improved spanning tree algorithm 3) exclusive data transmission on isolated VDN environments, 4) network and configuration recovery, and 5) command line interface (CLI) for VDN create/update/delete. Furthermore, we are also developing VDN Web UI for user group-oriented network visibility to visualize each allocated VDN topology and its operational attributes. It can be a good solution to handle new network requirements for various advanced users derived from IoT, cloud, big data, supercomputing, and data-intensive science. In the community showcase track, we are going to show VDN operation demo for ONOS community members.

Based on KREONET-S deployment, in 2016-2017, we will provide VDN environment as a the first production SD-WAN service for KREONET users. We expect that VDN will be a leading practice case for ONOS community, attracting ONOS community member's attention very well.

* [ONOS Community Showcase: An SDN/NFV Based Network Infrastructure for Turkey’s Public Safety](https://onosbuild2016.sched.org/event/8gyW/onos-community-showcase-an-sdnnfv-based-network-infrastructure-for-turkeys-public-safety)

Within the MİLAT project, SDN controller, virtual SDN switch, NFV based network controller, network function forwarding, and supporting functionalities will be developed, which are capable of managing SDN based components and which can be utilized in military, public safety and commercial communication infrastructures.
