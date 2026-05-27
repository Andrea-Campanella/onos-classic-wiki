# Deployment brigade

**Brigade Leads:**

* Luca Prete / ON.Lab ([luca@onlab.us](mailto:luca@onlab.us))

**Brigade Members:**

* Alaitz Mendiola / University of the Basque Country / GEANT
* Brian O'Connor / ON.Lab ([bocon@onlab.us](mailto:bocon@onlab.us))
* Chun-Ming Ou / NCTU
* Carolina Fernández / i2CAT
* Dongkyun Kim / KREONET
* Huai-Wen Hsu / NCTU
* Himal Kumar / UNSW
* Humberto Galiza / AmLight
* Itzik Ashkenazi / Technion - Israel Institute of Technology
* Jeronimo Bezerra / AmLight-FIU
* Jordi Ortiz / University of Murcia
* Pier Luigi Ventre / CNIT / Università Roma Tor Vergata / GEANT
* Priyanka Chopra / Verizon
* Raghu Ram / Verizon
* Wei-Cheng Wang / NCTU
* Wu Shaoyong / ZTE Corporation
* Yi Tseng / NCTU
* Yong-Hwan Kim / KREONET
* Phil Huang / Edgecore

**Contact the brigade:** [brigade-deployments@onosproject.org](mailto:brigade-deployments@onosproject.org)

**Mailing list archive:** <https://groups.google.com/a/onosproject.org/forum/#!forum/brigade-deployments>

**Brigade JIRA stories (backlog):** <https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning&quickFilter=106>

**Meeting notes:** [https://docs.google.com/document/d/1TuXM7UI9rV9w4T4iv7ikINzzYM4HPnuruRCxuTSKe4k/edit#](https://docs.google.com/document/d/1TuXM7UI9rV9w4T4iv7ikINzzYM4HPnuruRCxuTSKe4k/edit)

**Brigade goal:**

The ultimate high level goal of this brigade should be creating a concrete stack of software that can be deployed in networks, around the world. The stack should provide Layer 1-3 functionalities, convergence of packet-optical resources, compatibility with the MEF standards for the allocation and the management of Layer2 VPNs, compatibility with the NSI framework - commonly used by RENs for multi-domain resource provisioning.

Many other groups will focus their attention on future architectures, pure development tasks and PoCs - which are absolutely needed. Here we want to deploy what we do, now or very soon :)

**Scope:**

* Short-term focus in 2016:
  + Let ONOS run concurrently applications to provision L2 circuits ([VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md)) and L3 services through BGP ([SDN-IP](../../apps-and-use-cases/sdn-ip.md)) (Work already in progress - looking for help)
  + Refactor the ProxyARP application to avoid code duplication while enabling different applications to plugin their ProxyARP logic easily (Work already in progress lead by Jonathan Hart ([jono@onlab.us](mailto:jono@onlab.us)) - looking for help)
  + Possibly integrate the features of [Castor](../../new-projects/castor-project.md) (developed by AARNET) and [SDX-L2](../../new-projects/gant-sdx/sdx-l2-application.md) (developed by GEANT) into [VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md)
  + Possibly integrate the features of [Castor](../../new-projects/castor-project.md) and [SDX-L3](../../new-projects/gant-sdx/sdx-l3-application.md) (developed by GEANT) into [SDN-IP](../../apps-and-use-cases/sdn-ip.md)
  + Related deployment activities at the RENs + integration with specific vendors
  + Deployment activities
  + Demo results at [ONOS Build 2016](https://onosbuild2016.sched.org/)
* Long-term focus in 2017:
  + Integrate - at least for demo/field trial purposes - the recently developed [BoD app](../../new-projects/bod-dynpac-application.md) (for NSI integration)
  + Integrate [packet-optical](../../apps-and-use-cases/packet-optical.md) to manage optical resources (already developed at ON.Lab) with [VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md) and [SDN-IP](../../apps-and-use-cases/sdn-ip.md)
  + Use MEF standards into [VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md)
  + Integrate [E-CORD](https://wiki.opencord.org/display/CORD/Enterprise+CORD) and [VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md), so that [VPLS](../../apps-and-use-cases/virtual-private-lan-service-vpls.md) can dynamically connect multiple
  + More deployment activities

**Achievements:**

* J release:
  + New VPLS application
  + VPLS and SDN-IP working together
  + Refactoring of SDX-L2/L3
* K release:
  + Significant improvements to the intent framework and southbound system to support deployments
  + VPLS refactoring
  + Intent framework and VPLS working with OFDPA pipeline (i.e. Accton switch)
  + GEANT NOC testing on Corsa devices ONOS + SDX-L2/L3 + VPLS + SDN-IP
  + ONOS deployed in JGN-X
  + New VPLS app deployed in NCTU

**Meeting at ON.Lab in September**

We all know that work together in the same room, and why not - have a beer and socialize :) - helps a lot! We'd like to start this initiative inviting all the participants at ON.Lab in September, to work together for a week.

**The brigade will meet at ON.Lab from Monday, Sept 19th 2016 to Friday Sept 23rd 2016.**

Attendees:

* Alaitz Mendiola / University of the Basque Country / GEANT
* Jeronimo Bezerra / AmLight - FIU
* Yong-Hwan Kim / KISTI
* Chun-Ming Ou / NCTU (arriving earlier on the 12nd)
* Yi Tseng / NCTU (arriving earlier on the 12nd)
* Huai-Wen Hsu / NCTU (arriving earlier on the 12nd)
* Wei-Cheng Wang (arriving earlier on the 12nd)
* Himal Kumar / UNSW

During this week we plan to:

* Teach you how the Intent framework, ProxyARP, VPLS and SDN-IP work (depending on your interest)
* Learn from you what your applications do and how they do it
* Collect requirements: understand how the new software stack will look like and what are the tasks needed (basically populate our backlog)
* Do pair-programming
* Put you directly in contact with ONOS core developers
* Divide us in group and take the ownership of different tasks
* Meet one each other and socialize

**Demo video:** at the end of the week, the brigade gave a demo of what has been achieved. The video of the demo is available on YouTube, at **<https://youtu.be/28yeJ9Ruf-8>**

**How to get involved:**

Deployments are transverse to the entire ONOS platform. The area of code to touch is quite vast and problems to tackle are many. The deployment brigade is always looking for new members willing to contribute! Beginner or expert, network guy or developer..it doesn't matter. We'll find a right spot for you in the brigade! Contact us at [brigade-deployments@onosproject.org](mailto:brigade-deployments@onosproject.org) for more info!
