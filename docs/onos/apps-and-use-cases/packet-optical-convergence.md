# Packet Optical Convergence

To try out some of the features of the use case, or begin developing for it, take a look at [Getting Started with Packet Optical](packet-optical-convergence/getting-started-with-packet-optical.md).

To learn more about the internals of the use case, refer to our [Developer Guide for Packet Optical](packet-optical-convergence/developer-guide-for-packet-optical.md).

For ongoing work on the white box ROADM, jump over to [Open and Disaggregated ROADM](packet-optical-convergence/open-and-disaggregated-roadm.md) page.

For slides, papers, and past demos related to this use case, visit the [Packet Optical Resources](packet-optical-convergence/packet-optical-resources.md).

## Partners

AT&T, NTT Communications, Calient, Cavium, Ciena, Fujitsu, Lumentum, Oplink

## Overview

ONOS (Open Networking Operating System) is purpose-built for service providers. These typically operate large and complex multi-layer networks. ONOS has native support for the most common type of multi-layer network, namely the packet/optical network. It does so by offering an innovative converged topology view, allowing rapid introduction of new services and unprecedented optimization in an environment which has been dominated by a legacy mindset.

## Motivation

Service Provider Networks are complex and multi-layer in nature. Each of these layers, including packet and optical, is provisioned and managed independently. Sometimes, the provisioning and adding of capacity or new services requires order of days if not months. A converged SDN control plane for packet and optical networks can help address all of these inefficiencies. Service providers can optimize across packet and optical layers in real-time for availability and economics, thereby reducing over-provisioning. They can add capacity based on traffic and other considerations in minutes instead of days or months.

Typical optical transport networks are made up of ROADMs (Reconfigurable Optical Add Drop Multiplexers) that switch wavelengths and sub-wavelength circuits (OTN), while multiple IP layer connections are carried over the same wavelength. Provisioning of these optical wavelengths or lambdas is a labor-intensive and manual task that requires physically fibering of tunable lasers to the correct port. Adding on-demand connections or shifting capacity must be planned well in advance, and at significant operational expenses, ultimately creating an optical layer which is static and inflexible.

Additionally, due to this inflexible nature of current transport networks, a great deal of spare packet and optical capacity is deployed to cover all possible failure points. This is combined with the need to support busy hour scenarios with overcapacity to minimize packet loss. Capacity planning and traffic engineering must consider all possible traffic load and failure scenarios because the optical network cannot be reconfigured at will. Furthermore, optical impairments are complex and require careful planning and traffic optimization practices. For example, optical reach must be carefully considered when paths are set up by the path computation elements/Engines.

Our goal is to build an open source solution that allows effective multi-layer network programmability using novel abstractions such as intent-based networking and converged topology graphs.

## Group Communication

Slack channel: #packet-optical

You can create your own Slack account here: <https://slackin.onosproject.org/>

## Project Management

Issues for this use case are tracked on [Jira](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&epics=visible&selectedEpic=ONOS-1) under the *IP-Optical* epic.

## Roadmap

TBD
