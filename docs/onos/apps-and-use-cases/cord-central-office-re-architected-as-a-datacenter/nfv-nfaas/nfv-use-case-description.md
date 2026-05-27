# NFV Use Case Description

This section provides an overview of the NFV (NFaaS) use case.

## Introduction

***Network Function Virtualization (NFV)*** is a technique that decouples the functions from specialized hardware in the case of devices such as middleboxes, and implements them as software over industry-standard high volume servers. The intended results of NFV are the ease of service deployment and cost reductions.

This use case demonstrates a proposed method for introducing such abstractions through ***Network Function as a Service (NFaaS)***, a scalable and flexible NFV system where the smallest unit of provisioning is a ***service**,* a collection of VMs that provides a specific network functionality.

## Motivation

The primary challenges that network operators face today are the handling of the explosive demand of mobile traffic, and introducing and operationalizing new services while reducing costs. To combat these challenges, service providers strive for:

1. Agility, flexibility, scalability to their network.
2. Reduction of capital expenditure (CAPEX) and operational expenditure (OPEX).
3. Accelerated service implementation speed.
4. Reduced operational complexity and increased visibility of system states.

Service providers have started looking to Network Function Virtualization (NFV)  as a possible solution to the above four criteria, as it promises to bring flexibility and agility to Service Provider networks by moving network functions from dedicated appliances and middle boxes to generic servers.

While NFV can reduce CAPEX because commodity servers may be used efficiently by VMs, it increases OPEX as service providers now have to contend with increased management complexity due to:

* The management and orchestration of a large numbers of VMs on commodity servers
* The management of network function software on the VMs.
* How VMs must be interconnected based on subscriber’s service contract.

Additionally, increased complexity is inevitably linked to configuration errors. A primary cause of such complexity is the need for a provider to consider their NFV infrastructure in terms of VMs and the medium (networks).

One proposed solution is to introduce an abstractive unit for a collection of VMs and their interconnecting network(s). Being able to create and manipulate these units, rather than handling individual components, significantly simplifies operation. NFaaS aims to provide a means to create and manipulate these units in the enhanced form of a *service*.

## The Service Abstraction

Specifically, a *service* is the abstraction of a ***Virtual Network Function (VNF)***, a unit of network functionality running on one or more VMs. In the usual case, multiple VMs are used to provide highly available and performant functions. A *service* can be:

* ***scaled up and down***, by adding and removing VMs, as well as
* ***composed*** with other services by adding connectivity between services, in order to create new ones.

NFaaS refers to these functionalities as ***service scalability*** and ***service composition***.

![](../../../../assets/nfv-service.png)

---

[Return To : NFV (NFaaS)](../nfv-nfaas.md)  
[Home : ONOS Use Cases](../../../apps-and-use-cases.md)

---
