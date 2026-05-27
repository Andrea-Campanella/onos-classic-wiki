# Service Function Chaining (SFC)

# Team

| Name | Organization | Email |
| --- | --- | --- |
| Patrick Liu | Huawei Technologies | [Partick.Liu@huawei.com](mailto:Partick.Liu@huawei.com) |
| Suchitra H N | Huawei Technologies | [suchitra.hn@huawei.com](mailto:suchitra.hn@huawei.com) |
| Phaneendra Manda | Huawei Technologies | [phaneendra.manda@huawei.com](mailto:phaneendra.manda@huawei.com) |
| Bharat Saraswal | Huawei Technologies | [bharat.saraswal@huawei.com](mailto:bharat.saraswal@huawei.com) |
| Mahesh Poojary | Huawei Technologies | [mahesh.poojary@huawei.com](mailto:mahesh.poojary@huawei.com) |
| Suresh B R | Huawei Technologies | [suresh.b.r@huawei.com](mailto:Suresh.B.R@huawei.com) |

# What is SFC

Service Function Chaining (SFC): When a data stream passes through an ingress or egress point in a physical or virtual network device, using service chain it is possible to program exactly which sequence of actions the data stream is subjected to. This ordered action by set of service functions on the data stream is called a service function chain

# Introduction

This project is part of ONOSFW for OPNFV. The SFC creation is primarily driven by Openstack Neutron. The SFC component in ONOS implements the SFC creation requests from Openstack Neutron. All the required information for creating a service chain are supplied by Neutron using REST based APIs. Using these information, the SFC component prepares the flow rules as per the IETF NSH header and downloads the flow rules into OVS (OVS version 2.5.90 with official NSH Patch - <https://github.com/yyang13/ovs_nsh_patches>)

# Architecture

SFC is implemented as a bundle within the VTN application in ONOSFW.

[Refer to ONOSFW architecture.](onos-framework-onosfw-for-opnfv.md)

# What we do

1. SFC is implemented as a bundle within the VTN application in ONOSFW
2. The processing of REST based APIs from Neutron are implemented in ONOS as part of SFC project
3. REST APIs such as create port-pair(SF), create port-pair-group(SF group), create port-chain, create flow classifier rules are processed in ONOS
4. SFC resources such as SFs, SF groups, flow classifier rules are stored in ONOS for processing the create chain request
5. Interaction with VTN Resouce manager, VTNManager for various API
6. Implement the logic for service chain creation and flow rule download to classifier and SFFs
7. Extend the ONOS-Loxi for NSH header information download to OVS

# Goals

## Emu Release

Implement basic foundation for SFC

Integrate with Openstack Neutron and service the REST based APIs

Interact with VTN Resource Manager and VTN Manager. Store the SFC resources. Define service chain logic in SFC.

Basic flow rule download to classifier and SFF.

Introduce NSH header in the flows for service plane logic in SFC

## Falcon Release

Improvise on the SFC features introduced in Emu release

Add specific use cases to demonstrate importance of SFC

Introduce load balancing among multiple similar SF's within an SF group

## Golden Eye Release

The balancing among multiple flow rules at the classifier based in priority

Modify the chain by adding/deleting a service function

Support SFC proxy for NSH unaware service function

Define rest API to display resources in the chain

Display service topology in the ONOS web UI

# Demo videos

Demo video to show the NSH based service function chaining

Demo video of SFC solution showcased in OPNFV summit 2016

ONOS G release demo video
