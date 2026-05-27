# P4 brigade

**Brigade Members**

* Carmelo Cascone / ONF ([carmelo@opennetworking.org](mailto:carmelo@opennetworking.org)) (brigade lead)
* Andrea Campanella / ONF ([andrea@](mailto:andrea@onlab.us)[opennetworking.org](http://opennetworking.org)[)](http://opennetworking.org)
* Yi Tseng / ONF ([yi@opennetworking.org](mailto:yi@opennetworking.org))
* Jonghwan Hyun / ONF ([jonghwan@](mailto:jonghwan@onlab.us)[opennetworking.org](http://opennetworking.org)[)](http://opennetworking.org)
* Wu Shaoyong / ZTE ([wu.shaoyong@zte.com.cn](mailto:wu.shaoyong@zte.com.cn))
* Jian Tian / ZTE ([tian.jian@zte.com.cn](mailto:tian.jian@zte.com.cn))
* Ke Zhiyong / ZTE ([ke.zhiyong@zte.com.cn](mailto:ke.zhiyong@zte.com.cn))
* Frank Wang / Inspur ([wangpeihui@inspur.com](mailto:wangpeihuixyz@126.com))
* Minh Pham / UTS ([mngpham@gmail.com](mailto:mngpham@gmail.com))
* Tom Tofigh / AT&T ([tofigh@att.com](mailto:Tofigh@att.com))
* Uyen Chau / ONF ([uyen@opennetworking.org](mailto:uyen@opennetworking.org))
* Brian O'Connor / ONF ([brian@opennetworking.org](mailto:uyen@opennetworking.org))
* Esin Karaman / Netsia ([esin.karaman@](mailto:esin.karaman@netsia.com)[netsia.com](http://netsia.com))
* Serkant Uluderya / Netsia ([serkant.uluderya@](mailto:serkant.uluderya@netsia.com)[netsia.com](http://netsia.com))
* Mehmed Mustafa / Netsia ([mehmed.mustafa@](mailto:mehmed.mustafa@netsia.com)[netsia.com](http://netsia.com))
* Ekber Aziz / Netsia ([ekber.aziz@](mailto:ekber.aziz@netsia.com)[netsia.com](http://netsia.com))
* Kevin Chuang / NCTU ([cachuang@cs.nctu.edu.tw](mailto:cachuang@cs.nctu.edu.tw))
* Nate Tang / NCTU ([tangching1204@gmail.com](mailto:tangching1204@gmail.com))
* Iver Liu / NCTU ([iver.quest@gmail.com](mailto:iver.quest@gmail.com))
* Jianwei Mao / FNLab @ BUPT ([maojianwei2020@gmail.com](mailto:maojianwei2020@gmail.com))

## **Brigade Mailing List**

* <https://groups.google.com/a/onosproject.org/forum/#!forum/brigade-p4>

## **Brigade Status**

INACTIVE

P4 development for ONOS is now happening as part of the SD-Fabric project: <https://opennetworking.org/sd-fabric/>

## **Weekly meetings**

Every Tuesday at alternate times: 9:00 AM PST and 10:00 PM US Pacific time.

Find [here](https://docs.google.com/document/d/1EnlIDPC1jsudlX3T805oEHeZEWxiTGuCHQqYH-XNnkk/edit) the next meeting time and agenda.

## ****Contacts****

For any information or to join the brigade please contact Carmelo Cascone ([carmelo@opennetworking.org](mailto:carmelo@opennetworking.org))

## **Background**

P4 is a domain-specific language (DSL) designed to allow the programming of packet forwarding devices. P4 can be used to program different targets such as software switches, FPGA-based NICs or switches based on reconfigurable ASICs. P4 enables **protocol-independent** programmability at different levels, for example:

* Parsing and modification (actions) of new, non-standard headers.
* Configure table properties such as size, type of match (exact, ternary, longest-prefix), counters, etc.
* Stateful processing, i.e. per-packet custom actions that can access and manipulate state maintained by the switch.

P4 allows programming of many devices in a **target-independent** manner, using high-level constructs. In principle, P4 programs should be portable. The same program, when compiled for different targets, should produce the same forwarding behavior. Finally, P4 allows for **reconfigurability in the field**. In other words, once deployed, devices can be reconfigured with a new P4 program to provide support for new forwarding capabilities. 

##### ***Why should ONOS care about a data plane programming language?***

In ONOS we are ultimately interested in the capabilities of networking devices and ways to ease the configuration and control of such capabilities. P4 is becoming the common language spoken by switch vendors and operators to agree on what the data plane can or should do. Indeed, P4 is meant as both a specification language, e.g. to formally specify how a fixed-function switch ASIC works, and a programming language. In its mission to ease the life of operators, and to promote faster innovation in the network, ONOS should be able to understand and potentially speak P4. Understand, to be aware of the capabilities of a given device and to expose higher-level APIs to control them. Speak, to deploy new capabilities, e.g. generating or modifying existing P4 programs, that can be later controlled to satisfy application needs.

##### ***Runtime control of P4 devices***

P4 is not a protocol or device API for runtime control or configuration, i.e. once a P4 program is deployed to a device, P4 doesn’t tell us how that device can be controlled, for example, to add or remove entries in match+action tables, or to read the value of a counter. How can ONOS control a P4-enabled device? [P4Runtime](https://github.com/p4lang/p4runtime) is an effort in the P4 community to create a standard control-plane API portable across targets, they propose a gRPC-based APIs ([p4runtime.proto](https://github.com/p4lang/PI/blob/master/proto/p4/p4runtime.proto)). The brigade will focus on P4Runtime as a southbound control protocol, however, different devices supporting P4 might expose different APIs. Similarly to how ONOS today deals with different flavors of OpenFlow, heterogeneity of control protocol/APIs is abstracted from applications.

## **Scope**

**Short-term focus:**

* ~~Southbound support for P4 Runtime~~ **DONE** - Available starting from ONOS 1.11
* ~~Enable support for existing applications with any P4 program (via manual ONOS-to-P4 mapping)~~ **DONE** - Available starting from ONOS 1.11
* ~~Extend northbound APIs to support protocol-independence (e.g non-standard match/actions in flow rules)~~ **DONE** - Available starting from ONOS 1.11
* ~~Switch configuration via [OpenConfig](http://openconfig.net/) over [gNMI](https://github.com/openconfig/reference/tree/master/rpc/gnmi)~~ **DONE** - Initial support for OpenConfig Interfaces model available starting from ONOS 1.14
* New use cases:

+ ~~Fabric.p4 ([CORD fabric](https://wiki.opencord.org/x/foAT) with P4 switches)~~ **DONE** - Available starting from ONOS 1.14
+ ~~Support for [In-band Network Telemetry (INT)](https://p4.org/assets/INT-current-spec.pdf)~~ **DONE** - Available starting from ONOS 1.14
+ CORD VNFs offloading to HW P4 switches

  - ~~Mobile Serving and Packet Gateway (spgw.p4)~~ **DONE** - Integrated with fabric.p4
  - ~~Residential BNG with PPPoE termination~~**DONE** - Integrated with fabric.p4

**Long-term focus:**

* Rethink northbound APIs to capture enhanced capabilities of programmable data planes
* Services to support incremental reprogramming, i.e. deploy a new P4 program to devices while traffic is flowing.
* Optimize existing P4 programs or auto-generate new ones based on application needs and traffic workload.

## **Learn more**

Here are some pointers to learn more about the work of this brigade and current support for P4 in ONOS:

* **[Next-Gen SDN Tutorial (with hands-on exercises):](https://github.com/opennetworkinglab/ngsdn-tutorial)**
  + Learn about the building blocks of the [NG-SDN architecture](https://www.opennetworking.org/ng-sdn/), such as data plane programming and control via **P4 and P4Runtime**; configuration via **YANG, OpenConfig, and gNMI**; Stratum, and ONOS.
  + Organized around a sequence of hands-on exercises that show how to build an IPv6-based leaf-spine data center fabric using P4, Stratum, and ONOS.
  + Updated May 2020
* **[Advanced ONOS+P4 Tutorial: Building an SRv6-enabled fabric with P4 and ONOS](../../tutorials/advanced-onosp4-tutorial-building-an-srv6-enabled-fabric-with-p4-and-onos.md)**  
  + Requires intermediate knowledge of the P4 language
  + Updated April 2019
* [P4 support in ONOS deep dive](https://docs.google.com/presentation/d/1ji2jSlP2FCX89qQsTdRLykg5-GhQ6AYEWrUkpgm9VF8/edit?usp=sharing) (presented at ONF Connect 2018 - [video](https://vimeo.com/307549630/ff38da82dc))
* [Developer VM and walkthrough of P4Runtime support in ONOS via BMv2](../../guides/developer-guide/appendix-h-onosp4-development-environment.md)
* [P4-based Trellis (CORD fabric), AKA fabric.p4](../../apps-and-use-cases/fabric.p4-trellis-support-by-p4-devices.md) (with [instructions to test on BMv2](../../apps-and-use-cases/fabric.p4-trellis-support-by-p4-devices/try-fabric.p4-with-onos-and-bmv2.md))
  + **[Trellis+P4 tutorial (with hands-on exercises)](https://docs.google.com/presentation/d/1AFPZ_vJW1UNUHxgGWSPB7oOjkW-iRWvXowluIajjKWY/edit?usp=sharing)** (presented at ONF Connect 2018)
* Disaggregating the BNG in SEBA with P4:
  + [Design document](https://docs.google.com/document/d/1v5Dp-a3s183_1SKxMXcnpBPFWiJBHfGK5p7DNy7uPr0/edit)
  + [Demo presented at ONF Connect 2019](https://docs.google.com/presentation/d/1i3112nqKkHoVnX4wGAcYs5VA7YRt8W0-L7MZzsuUJX4/edit#slide=id.g6257a93d01_0_445)
* [Offloading S/PGW VNF to programmable switches using P4](../../../assets/p4-vnf-offloading-ons2018.pdf) (talk at ONS North America 2018)
* **Disaggregating the BNG in SEBA with P4:**
  + [Design document](https://docs.google.com/document/d/1v5Dp-a3s183_1SKxMXcnpBPFWiJBHfGK5p7DNy7uPr0/edit)
  + [Demo presented at ONF Connect 2019](https://docs.google.com/presentation/d/1i3112nqKkHoVnX4wGAcYs5VA7YRt8W0-L7MZzsuUJX4/edit#slide=id.g6257a93d01_0_445)
* [P4Runtime demo with Google's tor.p4](../../../assets/p4-demo-layer123-3-copy.pdf) (presented at L123 SDN NFV World Congress 2017 - [video here](https://www.youtube.com/watch?v=BE_y-Sz0WnQ))
* [ONOS-P4 Brigade Work Days 2017](../events/onos-p4-brigade-work-days-2017.md) (past event)
* **[OUTDATED] [ONOS+P4 tutorial for beginners (with hands-on exercises)](../../tutorials/onosp4-tutorial-for-beginners.md)**  
  + Includes an introduction to P4Runtime, ONOS, and use cases (fabric.p4 and spgw.p4)
  + Updated December 2018

### ONOS support for P4 targets

* [Using ONOS to control Stratum-enabled Intel/Barefoot Tofino-based switches](../../tutorials/using-onos-to-control-stratum-enabled-intelbarefoot-tofino-based-switches.md)
* [Controlling P4Runtime-enabled Mellanox Spectrum switch with ONOS](../../tutorials/controlling-p4runtime-enabled-mellanox-spectrum-switch-with-onos.md)

### To learn more about P4Runtime

* [Announcing P4Runtime – A contribution by the P4 API Working Group](https://p4.org/api/announcing-p4runtime-a-contribution-by-the-p4-api-working-group/) (Blog post)
* [Other P4Runtime resources](https://p4.org/p4-runtime/)

## **How to get involved**

Support for P4 will affect the whole ONOS platform, from the southbound to the northbound. The P4 brigade is looking for members willing to contribute! Subscribe to the [P4 mailing list](https://groups.google.com/a/onosproject.org/forum/#!forum/brigade-p4) and introduce yourself or contact Carmelo Cascone ([carmelo@opennetworking.org](mailto:carmelo@opennetworking.org)) if you are interested.
