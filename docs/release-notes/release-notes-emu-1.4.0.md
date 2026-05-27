# Release Notes - Emu 1.4.0

# Emu Release

Version: 1.4.0

Release Date: December 16th, 2015

Download [here](../redirect-pages-not-in-main-menu/download-packages-and-tutorial-vms.md)

## Sub-task

* [[ONOS-641](https://jira.onosproject.org/browse/ONOS-641)] - Update IP-related unit tests to include IPv6 as well
* [[ONOS-1080](https://jira.onosproject.org/browse/ONOS-1080)] - Metro ONOS DeviceProvider
* [[ONOS-2004](https://jira.onosproject.org/browse/ONOS-2004)] - Create Platform Functional Test Template
* [[ONOS-2264](https://jira.onosproject.org/browse/ONOS-2264)] - IPv6 system test plan
* [[ONOS-2265](https://jira.onosproject.org/browse/ONOS-2265)] - IPv6 System test Phase-1 Scripts
* [[ONOS-2266](https://jira.onosproject.org/browse/ONOS-2266)] - IPv6 system tests Setup and Framework
* [[ONOS-2277](https://jira.onosproject.org/browse/ONOS-2277)] - Test suite for flows through REST
* [[ONOS-2405](https://jira.onosproject.org/browse/ONOS-2405)] - Create initial Platform test suite
* [[ONOS-2629](https://jira.onosproject.org/browse/ONOS-2629)] - Review and integration of IPv6 Phase 1 scripts
* [[ONOS-2630](https://jira.onosproject.org/browse/ONOS-2630)] - IPv6 System test Phase-2 Script
* [[ONOS-2631](https://jira.onosproject.org/browse/ONOS-2631)] - IPv6 System test Phase-3 Script
* [[ONOS-2761](https://jira.onosproject.org/browse/ONOS-2761)] - setup same testbed with topoloy as Internet2 deployment network
* [[ONOS-2762](https://jira.onosproject.org/browse/ONOS-2762)] - test case0: setup all the softwares
* [[ONOS-2763](https://jira.onosproject.org/browse/ONOS-2763)] - test case1: ping test from 3 bgp peers to BGP speaker
* [[ONOS-2764](https://jira.onosproject.org/browse/ONOS-2764)] - Test case2: point-to-point intents test for each bgp peer and bgp speaker pair
* [[ONOS-2765](https://jira.onosproject.org/browse/ONOS-2765)] - test case3: routes and intents check to all BGP peers
* [[ONOS-2766](https://jira.onosproject.org/browse/ONOS-2766)] - test cast4: ping test in data plane for each route
* [[ONOS-2767](https://jira.onosproject.org/browse/ONOS-2767)] - test case5: cut links to peers one by one, check routes/intents
* [[ONOS-2768](https://jira.onosproject.org/browse/ONOS-2768)] - test case6: bring up the links cut in case5, check routes/intents, repeat case4
* [[ONOS-2769](https://jira.onosproject.org/browse/ONOS-2769)] - test case7: shut down 1 edge switch, check P-2-P and M-2-S intents, ping test
* [[ONOS-2770](https://jira.onosproject.org/browse/ONOS-2770)] - test case8: bring up the switch in case7, check routes/intents, repeat case4
* [[ONOS-2771](https://jira.onosproject.org/browse/ONOS-2771)] - test case9: bring down a switch in best path, check routes/p2p,m2sintents, repeat case4
* [[ONOS-2772](https://jira.onosproject.org/browse/ONOS-2772)] - test case10: bring up the switch in case9, check routes/p2p, m2s intents, repeat case4
* [[ONOS-2775](https://jira.onosproject.org/browse/ONOS-2775)] - test case11: flow status check, no PENDING\_ADD, NO PENDING\_REMOVE
* [[ONOS-2776](https://jira.onosproject.org/browse/ONOS-2776)] - test case12: bring down 1 speaker, check routes/intents, repeat case4
* [[ONOS-2777](https://jira.onosproject.org/browse/ONOS-2777)] - test case13: bring down 1 leader onos, check routes/intents, repeat case4
* [[ONOS-2832](https://jira.onosproject.org/browse/ONOS-2832)] - Define a ArpTable class providing the rules in ARP table
* [[ONOS-2833](https://jira.onosproject.org/browse/ONOS-2833)] - Define a DNATTable providing the rules in DNAT table
* [[ONOS-2834](https://jira.onosproject.org/browse/ONOS-2834)] - Define a L3ForwardTable class providing the rules in L3Forward table
* [[ONOS-2835](https://jira.onosproject.org/browse/ONOS-2835)] - Define a SNATTable class providing the rules in SNAT table
* [[ONOS-2841](https://jira.onosproject.org/browse/ONOS-2841)] - Seperate all private methods of programing flow rules from VTNManager and independently define a class per open flow table to contain all static methods
* [[ONOS-2922](https://jira.onosproject.org/browse/ONOS-2922)] - test case12: point-to-point ping failure test
* [[ONOS-2923](https://jira.onosproject.org/browse/ONOS-2923)] - test case13: ping failure test for each route
* [[ONOS-2924](https://jira.onosproject.org/browse/ONOS-2924)] - Setup Jenkin task
* [[ONOS-2925](https://jira.onosproject.org/browse/ONOS-2925)] - make sure the clean up work
* [[ONOS-3019](https://jira.onosproject.org/browse/ONOS-3019)] - create mininet testbed for multiple instances
* [[ONOS-3089](https://jira.onosproject.org/browse/ONOS-3089)] - Write TestON API driver to create and manage Docker containers
* [[ONOS-3096](https://jira.onosproject.org/browse/ONOS-3096)] - setup jenkin task
* [[ONOS-3104](https://jira.onosproject.org/browse/ONOS-3104)] - Add nicira extension of move action to onos-loxi
* [[ONOS-3105](https://jira.onosproject.org/browse/ONOS-3105)] - Add nicira extension of load action to onos-loxi
* [[ONOS-3153](https://jira.onosproject.org/browse/ONOS-3153)] - Write a PLATdockerTest suite using new TestON Docker API driver
* [[ONOS-3168](https://jira.onosproject.org/browse/ONOS-3168)] - Add nicira extension of move instruction to onos
* [[ONOS-3169](https://jira.onosproject.org/browse/ONOS-3169)] - Add nicira extension of load instruction to onos
* [[ONOS-3170](https://jira.onosproject.org/browse/ONOS-3170)] - Add nicira extension of move interface to TrafficTreatment
* [[ONOS-3171](https://jira.onosproject.org/browse/ONOS-3171)] - Add nicira extension of load interface to TrafficTreatment
* [[ONOS-3172](https://jira.onosproject.org/browse/ONOS-3172)] - Add arp\_tpa Criteria to onos
* [[ONOS-3173](https://jira.onosproject.org/browse/ONOS-3173)] - Add arp\_tpa operation to provider of openflow
* [[ONOS-3174](https://jira.onosproject.org/browse/ONOS-3174)] - Add nicira extension of load operation to provider of openflow
* [[ONOS-3175](https://jira.onosproject.org/browse/ONOS-3175)] - Add nicira extension of move operation to provider of openflow
* [[ONOS-3180](https://jira.onosproject.org/browse/ONOS-3180)] - Add initialize method to add table miss rules
* [[ONOS-3184](https://jira.onosproject.org/browse/ONOS-3184)] - create arp\_tpa selector to onos
* [[ONOS-3185](https://jira.onosproject.org/browse/ONOS-3185)] - Add nicira extension of move instructions to onos
* [[ONOS-3188](https://jira.onosproject.org/browse/ONOS-3188)] - Add the method: Returns the virtualPort associated with the fixedIP.
* [[ONOS-3191](https://jira.onosproject.org/browse/ONOS-3191)] - Add external portnumber in PortNumber class
* [[ONOS-3196](https://jira.onosproject.org/browse/ONOS-3196)] - update the method of addPort and deletePort for OvsdbBridgeConfig class
* [[ONOS-3201](https://jira.onosproject.org/browse/ONOS-3201)] - Add extension of resubmit action to onos-loxi
* [[ONOS-3202](https://jira.onosproject.org/browse/ONOS-3202)] - Add extension of resubmit-table action to onos-loxi
* [[ONOS-3229](https://jira.onosproject.org/browse/ONOS-3229)] - Add the junit test code of TenantId
* [[ONOS-3230](https://jira.onosproject.org/browse/ONOS-3230)] - Add the junit test code of SegmentationId
* [[ONOS-3231](https://jira.onosproject.org/browse/ONOS-3231)] - Add the junit test code of PhysicalNetwork
* [[ONOS-3232](https://jira.onosproject.org/browse/ONOS-3232)] - Add the junit test code of DefaultNeutronNetwork
* [[ONOS-3233](https://jira.onosproject.org/browse/ONOS-3233)] - Add the junit test code of NeutronNetworkId
* [[ONOS-3245](https://jira.onosproject.org/browse/ONOS-3245)] - Add the junit test code of DefaultAllocationPool
* [[ONOS-3246](https://jira.onosproject.org/browse/ONOS-3246)] - Add the junit test code of DefaultHostRoute
* [[ONOS-3247](https://jira.onosproject.org/browse/ONOS-3247)] - Add the junit test code of SubnetId
* [[ONOS-3248](https://jira.onosproject.org/browse/ONOS-3248)] - Add the junit test code of AllowedAddressPair
* [[ONOS-3249](https://jira.onosproject.org/browse/ONOS-3249)] - Add the junit test code of DefaultVirtualPort
* [[ONOS-3250](https://jira.onosproject.org/browse/ONOS-3250)] - Add the junit test code of FixedIp
* [[ONOS-3251](https://jira.onosproject.org/browse/ONOS-3251)] - Add the junit test code of SecurityGroup
* [[ONOS-3252](https://jira.onosproject.org/browse/ONOS-3252)] - Add the junit test code of VirtualPortId
* [[ONOS-3266](https://jira.onosproject.org/browse/ONOS-3266)] - add test plan on this test suite
* [[ONOS-3305](https://jira.onosproject.org/browse/ONOS-3305)] - Decide RPC mechanism
* [[ONOS-3317](https://jira.onosproject.org/browse/ONOS-3317)] - Add a test plan for this test suit
* [[ONOS-3318](https://jira.onosproject.org/browse/ONOS-3318)] - Create jenkins job for this test suite
* [[ONOS-3322](https://jira.onosproject.org/browse/ONOS-3322)] - Sketch out RPC service interface
* [[ONOS-3343](https://jira.onosproject.org/browse/ONOS-3343)] - Implement Scapy in FUNCintent
* [[ONOS-3364](https://jira.onosproject.org/browse/ONOS-3364)] - Update the bug: when neutron delete port and VTNManager monitor the event, get the port information which is null
* [[ONOS-3392](https://jira.onosproject.org/browse/ONOS-3392)] - Add L3 interfaces for ClassifierService class
* [[ONOS-3393](https://jira.onosproject.org/browse/ONOS-3393)] - update the bug: missing of sending local broadcast rules
* [[ONOS-3419](https://jira.onosproject.org/browse/ONOS-3419)] - Add README to all system tests
* [[ONOS-3471](https://jira.onosproject.org/browse/ONOS-3471)] - Modify Optical related Compilers code to allocate resource against Device instead of Link
* [[ONOS-3473](https://jira.onosproject.org/browse/ONOS-3473)] - Add the implementation of method programL3ExPortClassifierRules which assemble the L3 Classifier table rules sended from external port.
* [[ONOS-3474](https://jira.onosproject.org/browse/ONOS-3474)] - Add the implementation of method programL3InPortClassifierRules which assemble the L3 Classifier table rules sended from internal port.
* [[ONOS-3475](https://jira.onosproject.org/browse/ONOS-3475)] - Add the implementation of method programArpClassifierRules which assemble the Arp Classifier table rules.
* [[ONOS-3476](https://jira.onosproject.org/browse/ONOS-3476)] - Add the implementation of L3ForwardService interface.
* [[ONOS-3477](https://jira.onosproject.org/browse/ONOS-3477)] - Add the implementation of DnatService interface.
* [[ONOS-3478](https://jira.onosproject.org/browse/ONOS-3478)] - Add the implementation of SnatService interface.
* [[ONOS-3479](https://jira.onosproject.org/browse/ONOS-3479)] - Add the implementation of ArpService interface.
* [[ONOS-3486](https://jira.onosproject.org/browse/ONOS-3486)] - Add the annotation of port mac when monitor switch added.
* [[ONOS-3487](https://jira.onosproject.org/browse/ONOS-3487)] - Add L3 flows for Classifier table
* [[ONOS-3488](https://jira.onosproject.org/browse/ONOS-3488)] - Add L3 flows for arp table
* [[ONOS-3489](https://jira.onosproject.org/browse/ONOS-3489)] - Add L3 flows for L3forward table
* [[ONOS-3490](https://jira.onosproject.org/browse/ONOS-3490)] - Add L3 flows for L3forward table
* [[ONOS-3491](https://jira.onosproject.org/browse/ONOS-3491)] - Add L3 flows for dnat table
* [[ONOS-3492](https://jira.onosproject.org/browse/ONOS-3492)] - Add L3 flows for snat table
* [[ONOS-3496](https://jira.onosproject.org/browse/ONOS-3496)] - Add README to HA tests
* [[ONOS-3497](https://jira.onosproject.org/browse/ONOS-3497)] - Add README to SDNIP tests
* [[ONOS-3499](https://jira.onosproject.org/browse/ONOS-3499)] - Add the set treatments of ARP\_SPA, ARP\_SHA and ARP\_OP.
* [[ONOS-3514](https://jira.onosproject.org/browse/ONOS-3514)] - Add L3 flows for Classifier table, ARP table, L3forward table, DNAT table and SNAT table.
* [[ONOS-3520](https://jira.onosproject.org/browse/ONOS-3520)] - Add L3 codes for VTNManager class.
* [[ONOS-3532](https://jira.onosproject.org/browse/ONOS-3532)] - Update PORT\_MAC to AnnotationKeys.PORT\_MAC.
* [[ONOS-3583](https://jira.onosproject.org/browse/ONOS-3583)] - Update VTNRSC's bug:null exception
* [[ONOS-3584](https://jira.onosproject.org/browse/ONOS-3584)] - Add the cli of updatting external gateway macadress
* [[ONOS-3585](https://jira.onosproject.org/browse/ONOS-3585)] - Add the cli of setting external port name
* [[ONOS-3596](https://jira.onosproject.org/browse/ONOS-3596)] - update VTN's bug: delete local broadcast flows unsuccessfully.
* [[ONOS-3606](https://jira.onosproject.org/browse/ONOS-3606)] - update vtn's bug: if ovs has a plurality of bridge, the code should filter br-int and get the ports via deviceService.
* [[ONOS-3624](https://jira.onosproject.org/browse/ONOS-3624)] - update vtnweb's bug and add Not-Null constraints of export.

## Bug

* [[ONOS-810](https://jira.onosproject.org/browse/ONOS-810)] - "devices" shows also the port of the hypervisor when using Proxmox
* [[ONOS-867](https://jira.onosproject.org/browse/ONOS-867)] - Sporadic AbstractEventAccumulatorTest unit test failure
* [[ONOS-1636](https://jira.onosproject.org/browse/ONOS-1636)] - ONOS shows devices still active after deactivating org.onosproject.openflow
* [[ONOS-1716](https://jira.onosproject.org/browse/ONOS-1716)] - Occasional test failures in AbstractAccumulatorTest
* [[ONOS-1864](https://jira.onosproject.org/browse/ONOS-1864)] - Topology View still sending events after view has been changed
* [[ONOS-2035](https://jira.onosproject.org/browse/ONOS-2035)] - Handshake errors for NiciraSwitchHandshaker over OF 1.3
* [[ONOS-2139](https://jira.onosproject.org/browse/ONOS-2139)] - Topology View -- selecting a node pins it in place
* [[ONOS-2412](https://jira.onosproject.org/browse/ONOS-2412)] - Inconcinstency between number of devices in the gui and in the cli
* [[ONOS-2626](https://jira.onosproject.org/browse/ONOS-2626)] - ConcurrentModificationException while processing device disconnect
* [[ONOS-2628](https://jira.onosproject.org/browse/ONOS-2628)] - Can't uniquely delete flows installed with REST API
* [[ONOS-2802](https://jira.onosproject.org/browse/ONOS-2802)] - Intent Operation Throughput Performance Regression
* [[ONOS-2854](https://jira.onosproject.org/browse/ONOS-2854)] - bugs and problems in bash\_profile and onos-service shell scripts
* [[ONOS-2885](https://jira.onosproject.org/browse/ONOS-2885)] - Seeing flow install failures for some devices randomly after IPv6 ND enable
* [[ONOS-2890](https://jira.onosproject.org/browse/ONOS-2890)] - Deactivating DHCP app deletes default arp flow installed by ONOS on devices
* [[ONOS-2901](https://jira.onosproject.org/browse/ONOS-2901)] - Topology View - Overlay - Quick Help - T-binding
* [[ONOS-2937](https://jira.onosproject.org/browse/ONOS-2937)] - Reactive forwarding app results in dropped packets in multi-instance setups
* [[ONOS-2939](https://jira.onosproject.org/browse/ONOS-2939)] - SDN-IP throws exception for the OPEN message with bird
* [[ONOS-2966](https://jira.onosproject.org/browse/ONOS-2966)] - ONOS jenkins running out of disk space
* [[ONOS-2978](https://jira.onosproject.org/browse/ONOS-2978)] - SDN-IP MP2SP intents are being recompiled on unrelated host events
* [[ONOS-2979](https://jira.onosproject.org/browse/ONOS-2979)] - java.util.ConcurrentModificationException
* [[ONOS-2999](https://jira.onosproject.org/browse/ONOS-2999)] - NPEs at OpenFlowRuleProvider.executeBatch after deactivate proxyARP
* [[ONOS-3000](https://jira.onosproject.org/browse/ONOS-3000)] - Stopping an onos node of a multi-node cluster causes default flow disappear in BM
* [[ONOS-3023](https://jira.onosproject.org/browse/ONOS-3023)] - Some flow rules are missing in CHO even intents are in INSTALLED state
* [[ONOS-3027](https://jira.onosproject.org/browse/ONOS-3027)] - Can not ping local host if it did not appear in onos CLI
* [[ONOS-3087](https://jira.onosproject.org/browse/ONOS-3087)] - POST HostToHost intents failed in FUNCintentRest
* [[ONOS-3150](https://jira.onosproject.org/browse/ONOS-3150)] - Some devices have all ports disabled
* [[ONOS-3157](https://jira.onosproject.org/browse/ONOS-3157)] - Fix onos-secure-ssh key collision problem
* [[ONOS-3160](https://jira.onosproject.org/browse/ONOS-3160)] - opticalUtil.py does not correctly detect linc-oe devices
* [[ONOS-3178](https://jira.onosproject.org/browse/ONOS-3178)] - create one host,when host go online,onos cli shows two hosts
* [[ONOS-3179](https://jira.onosproject.org/browse/ONOS-3179)] - create many hosts in the same time,some host can not get the flows.
* [[ONOS-3194](https://jira.onosproject.org/browse/ONOS-3194)] - NPE in OFMessageEncoder
* [[ONOS-3220](https://jira.onosproject.org/browse/ONOS-3220)] - Intents View - Key column doesn't sort correctly.
* [[ONOS-3224](https://jira.onosproject.org/browse/ONOS-3224)] - HostToHostIntent installed from GUI does not have non-OPTICAL link type constraint
* [[ONOS-3225](https://jira.onosproject.org/browse/ONOS-3225)] - Deletes tunnel package in vtnsrc bundle
* [[ONOS-3226](https://jira.onosproject.org/browse/ONOS-3226)] - Move FlowClassifierCodec from vtnrsc bundle to vtnweb bundle
* [[ONOS-3228](https://jira.onosproject.org/browse/ONOS-3228)] - Change ConcurrentMap to EventuallyConsistentMap in FlowClassifierManager
* [[ONOS-3258](https://jira.onosproject.org/browse/ONOS-3258)] - Flow does not get properly added when VLAN selector is specified
* [[ONOS-3260](https://jira.onosproject.org/browse/ONOS-3260)] - Caught error, "Service org.onosproject.net.topology.TopologyService not found" when using docker image to form a 3-node cluster
* [[ONOS-3320](https://jira.onosproject.org/browse/ONOS-3320)] - PropertyPanelTest fails in non-English Locale
* [[ONOS-3324](https://jira.onosproject.org/browse/ONOS-3324)] - Ovs del-manager and set-manager again, the vxlan configuration lost
* [[ONOS-3346](https://jira.onosproject.org/browse/ONOS-3346)] - NPE when disallowing a connected device via netcfg
* [[ONOS-3347](https://jira.onosproject.org/browse/ONOS-3347)] - Host is not reattached to its new location after being moved
* [[ONOS-3348](https://jira.onosproject.org/browse/ONOS-3348)] - Periodic NullPointerException with DHCP app
* [[ONOS-3350](https://jira.onosproject.org/browse/ONOS-3350)] - messagesPendingMastership in AbstractOpenFlowSwitch is not threadsafe
* [[ONOS-3359](https://jira.onosproject.org/browse/ONOS-3359)] - DeviceManage NPE if config register for non existent device
* [[ONOS-3362](https://jira.onosproject.org/browse/ONOS-3362)] - Fix triggerProbe method of ovsdbDeviceProvider.
* [[ONOS-3378](https://jira.onosproject.org/browse/ONOS-3378)] - DELETE of /network/configuration/{subjectClassKey} has no effect
* [[ONOS-3379](https://jira.onosproject.org/browse/ONOS-3379)] - Trying to GET a non existent Network Config SubjectClassKey results in a 500 error
* [[ONOS-3401](https://jira.onosproject.org/browse/ONOS-3401)] - OF SSL connection not working - Exception trying SSL connection to onos SB
* [[ONOS-3411](https://jira.onosproject.org/browse/ONOS-3411)] - Device status is not properly updated when deactivating openflow-base
* [[ONOS-3412](https://jira.onosproject.org/browse/ONOS-3412)] - "java.lang.IllegalAccessError: already closed" while terminating ONOS
* [[ONOS-3413](https://jira.onosproject.org/browse/ONOS-3413)] - Gerrit hitting gmail daily email limits
* [[ONOS-3423](https://jira.onosproject.org/browse/ONOS-3423)] - When ONOS gets an out of memory exception it essentially becomes a zombie
* [[ONOS-3453](https://jira.onosproject.org/browse/ONOS-3453)] - Bundles not loaded in all nodes in a cluster
* [[ONOS-3472](https://jira.onosproject.org/browse/ONOS-3472)] - ConsistentMap's key equality should not be influenced by #equals
* [[ONOS-3493](https://jira.onosproject.org/browse/ONOS-3493)] - Sometime the number of ONOS users is not displayed correctly on the ONOS website world map
* [[ONOS-3500](https://jira.onosproject.org/browse/ONOS-3500)] - When ConsistentMap is created with relaxed consistency turned on some map events are not delivered
* [[ONOS-3511](https://jira.onosproject.org/browse/ONOS-3511)] - ONOS if enableOFTLS, only can have single switch connection
* [[ONOS-3512](https://jira.onosproject.org/browse/ONOS-3512)] - Migrate resource CLI commands to new device resource model
* [[ONOS-3547](https://jira.onosproject.org/browse/ONOS-3547)] - Exceptions while processing packets during reactive forwarding pingall
* [[ONOS-3549](https://jira.onosproject.org/browse/ONOS-3549)] - NPE in DHCP during IP renew when no IP range is registered
* [[ONOS-3565](https://jira.onosproject.org/browse/ONOS-3565)] - Intent Installation/Reroute latency test failed at 3-node with exceptions
* [[ONOS-3586](https://jira.onosproject.org/browse/ONOS-3586)] - OF port discovery latency regression
* [[ONOS-3593](https://jira.onosproject.org/browse/ONOS-3593)] - NPE when processing FlowRuleEvent
* [[ONOS-3595](https://jira.onosproject.org/browse/ONOS-3595)] - Intent install/Reroute latency test failed, due to a node not assigned role to null devices
* [[ONOS-3623](https://jira.onosproject.org/browse/ONOS-3623)] - No HOST\_REMOVED event when deleting host after restarting ONOS

## Story

* [[ONOS-302](https://jira.onosproject.org/browse/ONOS-302)] - Topology View: SLRG avoidance path visualization
* [[ONOS-304](https://jira.onosproject.org/browse/ONOS-304)] - Topology Viewer demo app
* [[ONOS-1264](https://jira.onosproject.org/browse/ONOS-1264)] - Complete missing IPv6 functionalities
* [[ONOS-1319](https://jira.onosproject.org/browse/ONOS-1319)] - Secure OpenFlow connection using TLS/SSL
* [[ONOS-1439](https://jira.onosproject.org/browse/ONOS-1439)] - Fix the Cpqd bug of sending the reverse subnet mask in flow stats reply
* [[ONOS-1479](https://jira.onosproject.org/browse/ONOS-1479)] - Topology View: dynamic overlay extensibility
* [[ONOS-1684](https://jira.onosproject.org/browse/ONOS-1684)] - Application Dependencies
* [[ONOS-1703](https://jira.onosproject.org/browse/ONOS-1703)] - Refactor Segment Routing Configuration based on new device config framework
* [[ONOS-1850](https://jira.onosproject.org/browse/ONOS-1850)] - Topology View Overlay: Rendering badges
* [[ONOS-1891](https://jira.onosproject.org/browse/ONOS-1891)] - Modify TestON to support test steps as part of some control/loop structure
* [[ONOS-2126](https://jira.onosproject.org/browse/ONOS-2126)] - Clean up ConfigProvider
* [[ONOS-2179](https://jira.onosproject.org/browse/ONOS-2179)] - Define virtual network model & services
* [[ONOS-2234](https://jira.onosproject.org/browse/ONOS-2234)] - Workaround for LinkDiscovery issue when running multiple ONOS clusters
* [[ONOS-2276](https://jira.onosproject.org/browse/ONOS-2276)] - Test suite for Flow rule-based functionality through REST (Emu#1)
* [[ONOS-2291](https://jira.onosproject.org/browse/ONOS-2291)] - AtomicCounter needs a set method
* [[ONOS-2309](https://jira.onosproject.org/browse/ONOS-2309)] - Fix the ARP storm bug
* [[ONOS-2314](https://jira.onosproject.org/browse/ONOS-2314)] - Wiki snapshot for Drake
* [[ONOS-2321](https://jira.onosproject.org/browse/ONOS-2321)] - IP-Optical port to new network config framework
* [[ONOS-2428](https://jira.onosproject.org/browse/ONOS-2428)] - AtomicCounter needs a CAS (compare-and-set) method
* [[ONOS-2437](https://jira.onosproject.org/browse/ONOS-2437)] - Test suite for networking configuration subsystem through REST (Emu#2)
* [[ONOS-2452](https://jira.onosproject.org/browse/ONOS-2452)] - Install ONOS 1.2 (Cardinal) on AMLight production network
* [[ONOS-2472](https://jira.onosproject.org/browse/ONOS-2472)] - Loxi support for Optical Transport extensions
* [[ONOS-2480](https://jira.onosproject.org/browse/ONOS-2480)] - Make Optical (Linc-oe) testing working on production bench(Emu#1)
* [[ONOS-2493](https://jira.onosproject.org/browse/ONOS-2493)] - As a user I would like to see all the sdn-ip related intents disappear when I deactivate the sdn-ip application in onos
* [[ONOS-2500](https://jira.onosproject.org/browse/ONOS-2500)] - Contribute onosfw project test cases and scripts
* [[ONOS-2522](https://jira.onosproject.org/browse/ONOS-2522)] - ONOS automated tests with FSFW - single instance
* [[ONOS-2587](https://jira.onosproject.org/browse/ONOS-2587)] - Implement the BGP communication between ONOS BGP Speaker and the BGP peers on device using BGP protocol messages on TCP/IP socket.
* [[ONOS-2588](https://jira.onosproject.org/browse/ONOS-2588)] - Implement BGP message parser for parsing BGP protocol messages with encoding and decoding API
* [[ONOS-2589](https://jira.onosproject.org/browse/ONOS-2589)] - Implement BGP LS topology provider and listen on Node and Link changes of BGP Controller.
* [[ONOS-2590](https://jira.onosproject.org/browse/ONOS-2590)] - BGP Global and Peer configurations processing.
* [[ONOS-2591](https://jira.onosproject.org/browse/ONOS-2591)] - BGP Channel Handler to manage each BGP Peer connection from BGP peer
* [[ONOS-2593](https://jira.onosproject.org/browse/ONOS-2593)] - Implement BGP Controller to provide socket handling with each BGP Peer
* [[ONOS-2594](https://jira.onosproject.org/browse/ONOS-2594)] - Implement Channel Handler to manage Session handling with BGP peers
* [[ONOS-2595](https://jira.onosproject.org/browse/ONOS-2595)] - Implement BGP Protocol Request and Response message mapping with its Peer
* [[ONOS-2596](https://jira.onosproject.org/browse/ONOS-2596)] - Implement BGP open protocol Message parsing, Decode and encoding
* [[ONOS-2597](https://jira.onosproject.org/browse/ONOS-2597)] - Implement BGP KeepAlive protocol Message parsing, Decode and encoding
* [[ONOS-2598](https://jira.onosproject.org/browse/ONOS-2598)] - Implement BGP Capabilities parsing, Decode and encoding
* [[ONOS-2599](https://jira.onosproject.org/browse/ONOS-2599)] - Implement BGP Notification protocol Message parsing, Decode and encoding
* [[ONOS-2600](https://jira.onosproject.org/browse/ONOS-2600)] - Implement Basic BGP Update protocol Message parsing and Decode excuding path attributes.
* [[ONOS-2601](https://jira.onosproject.org/browse/ONOS-2601)] - Implement BGP Update protocol Message and parse all basic path attributes.
* [[ONOS-2602](https://jira.onosproject.org/browse/ONOS-2602)] - Implement BGP Update protocol Message with reach and unreach attribute parsing and Decode. (Node and Link NLRI)
* [[ONOS-2603](https://jira.onosproject.org/browse/ONOS-2603)] - Implement BGP Update protocol Message and parse all LinkState attributes of Node and Link.
* [[ONOS-2604](https://jira.onosproject.org/browse/ONOS-2604)] - Implement BGP keepalive and Hold Timer
* [[ONOS-2605](https://jira.onosproject.org/browse/ONOS-2605)] - Implement AdjacencyIn RIB for each of the peer
* [[ONOS-2606](https://jira.onosproject.org/browse/ONOS-2606)] - Implement Local RIB and do the selection process of BGP update.
* [[ONOS-2607](https://jira.onosproject.org/browse/ONOS-2607)] - Implement BGP LS topology provider and listen on Node and Link changes of BGP Controller.
* [[ONOS-2608](https://jira.onosproject.org/browse/ONOS-2608)] - Update Node and Link subsystem of ONOS core on any Node/Link Add, modify or delete to build the Linkstate topology
* [[ONOS-2609](https://jira.onosproject.org/browse/ONOS-2609)] - Unit test the BGP controller and channel Handler.
* [[ONOS-2610](https://jira.onosproject.org/browse/ONOS-2610)] - Unit test the BGP Open message
* [[ONOS-2611](https://jira.onosproject.org/browse/ONOS-2611)] - Unit test the BGP Keelalive mesasge
* [[ONOS-2612](https://jira.onosproject.org/browse/ONOS-2612)] - Unit test the BGP Notification message
* [[ONOS-2613](https://jira.onosproject.org/browse/ONOS-2613)] - Unit test the BGP Update message
* [[ONOS-2614](https://jira.onosproject.org/browse/ONOS-2614)] - Unit test the BGP Timer functionality
* [[ONOS-2615](https://jira.onosproject.org/browse/ONOS-2615)] - Unit test the BGP Adjacency In and Local RIB table.
* [[ONOS-2616](https://jira.onosproject.org/browse/ONOS-2616)] - Unit Test the BGP topology Provider for Node changes.
* [[ONOS-2617](https://jira.onosproject.org/browse/ONOS-2617)] - Unit Test the BGP topology Provider for Link changes.
* [[ONOS-2618](https://jira.onosproject.org/browse/ONOS-2618)] - Integration testing of BGP with BGP peers (Stub test code) for session establishment
* [[ONOS-2619](https://jira.onosproject.org/browse/ONOS-2619)] - Integration testing of BGP with BGP peers (Stub test code) for session management
* [[ONOS-2621](https://jira.onosproject.org/browse/ONOS-2621)] - Documentation work for the Implementation of BGP Linkstate topology provider
* [[ONOS-2649](https://jira.onosproject.org/browse/ONOS-2649)] - CHOtest Enhancements (Emu#1)
* [[ONOS-2719](https://jira.onosproject.org/browse/ONOS-2719)] - Investigate traffic tools for TestON remote Mininet driver to send/receive pkts
* [[ONOS-2752](https://jira.onosproject.org/browse/ONOS-2752)] - ONOSFW L3 Feature
* [[ONOS-2753](https://jira.onosproject.org/browse/ONOS-2753)] - The restful service related to route resource of neutron
* [[ONOS-2755](https://jira.onosproject.org/browse/ONOS-2755)] - The restful service related to floating ip resource of neutron
* [[ONOS-2760](https://jira.onosproject.org/browse/ONOS-2760)] - Functional test for SDN-IP, single instance
* [[ONOS-2773](https://jira.onosproject.org/browse/ONOS-2773)] - Functional test for SDN-IP, multiple instance
* [[ONOS-2774](https://jira.onosproject.org/browse/ONOS-2774)] - Wiki update for Drake -- GUI stuff
* [[ONOS-2794](https://jira.onosproject.org/browse/ONOS-2794)] - Enable PAUSE and EMAIL feature in TestON for debug in middle of execution
* [[ONOS-2798](https://jira.onosproject.org/browse/ONOS-2798)] - GUI Topology - need a microwave dish glyph
* [[ONOS-2799](https://jira.onosproject.org/browse/ONOS-2799)] - Increate ONOS log size to at least 10M
* [[ONOS-2803](https://jira.onosproject.org/browse/ONOS-2803)] - Balance Masters in SCPFstartTopo
* [[ONOS-2804](https://jira.onosproject.org/browse/ONOS-2804)] - Packet deserialization issue should be logged as an error, not as warning
* [[ONOS-2813](https://jira.onosproject.org/browse/ONOS-2813)] - Automated device mastership load balancing.
* [[ONOS-2814](https://jira.onosproject.org/browse/ONOS-2814)] - Support a PersistenceService for storing arbitrary data locally
* [[ONOS-2815](https://jira.onosproject.org/browse/ONOS-2815)] - The abstraction of RouteService used to store route resource
* [[ONOS-2817](https://jira.onosproject.org/browse/ONOS-2817)] - The abstraction of FloatingIpService used to store FloatingIp resource
* [[ONOS-2818](https://jira.onosproject.org/browse/ONOS-2818)] - The implementation of RouteService
* [[ONOS-2820](https://jira.onosproject.org/browse/ONOS-2820)] - The implementation of FloatingIpService
* [[ONOS-2826](https://jira.onosproject.org/browse/ONOS-2826)] - The CLIs of FloatingIpService
* [[ONOS-2827](https://jira.onosproject.org/browse/ONOS-2827)] - The CLIs of RouteInterfaceService
* [[ONOS-2828](https://jira.onosproject.org/browse/ONOS-2828)] - The CLIs of RouteService
* [[ONOS-2829](https://jira.onosproject.org/browse/ONOS-2829)] - Support the capability of check data integrity for subnets
* [[ONOS-2830](https://jira.onosproject.org/browse/ONOS-2830)] - Support the data integrity validation of port resource
* [[ONOS-2831](https://jira.onosproject.org/browse/ONOS-2831)] - Refactor L2 code.
* [[ONOS-2837](https://jira.onosproject.org/browse/ONOS-2837)] - Add L3 table-miss rules when ovs is detected or vanished in VTNManager
* [[ONOS-2838](https://jira.onosproject.org/browse/ONOS-2838)] - Add L3 rules when host is detected or vanished in VTNManager
* [[ONOS-2839](https://jira.onosproject.org/browse/ONOS-2839)] - Create a port used to access into internet via physical port of compute node when compute node is detected
* [[ONOS-2840](https://jira.onosproject.org/browse/ONOS-2840)] - Improve the capability of catching exception when VTNManager applies configration via driver subsystem
* [[ONOS-2842](https://jira.onosproject.org/browse/ONOS-2842)] - Design BGP Link state plugin and BGP Topology provider as SBI in ONOS.
* [[ONOS-2844](https://jira.onosproject.org/browse/ONOS-2844)] - ONOSFW L3 requirements analysis
* [[ONOS-2845](https://jira.onosproject.org/browse/ONOS-2845)] - ONOSFW L3 Design
* [[ONOS-2850](https://jira.onosproject.org/browse/ONOS-2850)] - Web UI - Programmable Dialog
* [[ONOS-2851](https://jira.onosproject.org/browse/ONOS-2851)] - Web UI - create archetype for table-view-based app
* [[ONOS-2852](https://jira.onosproject.org/browse/ONOS-2852)] - Web UI - create archetype for topo-overlay-based app
* [[ONOS-2856](https://jira.onosproject.org/browse/ONOS-2856)] - Platform Test Suite to cover tar.gz install cluster with Docker image (Emu#1)
* [[ONOS-2860](https://jira.onosproject.org/browse/ONOS-2860)] - Add openflowJ extension of move action
* [[ONOS-2866](https://jira.onosproject.org/browse/ONOS-2866)] - Model vendor-neutral disaggregated WSS
* [[ONOS-2876](https://jira.onosproject.org/browse/ONOS-2876)] - Web UI - Set device friendly name
* [[ONOS-2892](https://jira.onosproject.org/browse/ONOS-2892)] - Refactor current FUNC, HA and CHO for robust intent/flow checking (Emu#1)
* [[ONOS-2900](https://jira.onosproject.org/browse/ONOS-2900)] - Add Jenkins post script to move all onos logs to TestStation for preservation(Emu#1)
* [[ONOS-2903](https://jira.onosproject.org/browse/ONOS-2903)] - Openflow Nicira extension
* [[ONOS-2909](https://jira.onosproject.org/browse/ONOS-2909)] - Replace DeviceResourceService with new ResourceService
* [[ONOS-2912](https://jira.onosproject.org/browse/ONOS-2912)] - Explore potential candidates to be replaced with ResourceService
* [[ONOS-2913](https://jira.onosproject.org/browse/ONOS-2913)] - Remove APIs deprecated in Cardinal Release
* [[ONOS-2930](https://jira.onosproject.org/browse/ONOS-2930)] - Model vendor-neutral disaggregated ROADM
* [[ONOS-2932](https://jira.onosproject.org/browse/ONOS-2932)] - Identify use cases for Intent Domain
* [[ONOS-2933](https://jira.onosproject.org/browse/ONOS-2933)] - Design review for Intent Domain
* [[ONOS-2936](https://jira.onosproject.org/browse/ONOS-2936)] - Snapshot wiki for Drake (1.3)
* [[ONOS-2940](https://jira.onosproject.org/browse/ONOS-2940)] - Internet2 deployment tests with FSFW - multiple instances
* [[ONOS-2946](https://jira.onosproject.org/browse/ONOS-2946)] - PacketService CLI commands
* [[ONOS-2947](https://jira.onosproject.org/browse/ONOS-2947)] - Remove IP from existing Host
* [[ONOS-2951](https://jira.onosproject.org/browse/ONOS-2951)] - Design Northbound API, Neutron resource storage in ONOS
* [[ONOS-2952](https://jira.onosproject.org/browse/ONOS-2952)] - Design SFC Manager in ONOS for generating forwarding behavior
* [[ONOS-2953](https://jira.onosproject.org/browse/ONOS-2953)] - Design the forwarding logic for southbound including NSH, OVSDB, Openflow
* [[ONOS-2957](https://jira.onosproject.org/browse/ONOS-2957)] - Need a way to read component configs from a file.
* [[ONOS-2972](https://jira.onosproject.org/browse/ONOS-2972)] - Web UI - Packet Processors tabular view
* [[ONOS-2977](https://jira.onosproject.org/browse/ONOS-2977)] - Add in HA\* test bring down ctrl and check all states (topo, intent, flows) still ok
* [[ONOS-2997](https://jira.onosproject.org/browse/ONOS-2997)] - Re-factor ACL app package name to conform to org.onosproject
* [[ONOS-2998](https://jira.onosproject.org/browse/ONOS-2998)] - Write IEEE newsletter paper on packet/optical
* [[ONOS-3003](https://jira.onosproject.org/browse/ONOS-3003)] - fix nightly SCPFswitchLat failure
* [[ONOS-3008](https://jira.onosproject.org/browse/ONOS-3008)] - re-create vm templates with more disk space
* [[ONOS-3012](https://jira.onosproject.org/browse/ONOS-3012)] - Figure out a proper way to deal with empty instruction
* [[ONOS-3018](https://jira.onosproject.org/browse/ONOS-3018)] - Add missing IPv6-VLAN hosts in to FUNC tiopology
* [[ONOS-3020](https://jira.onosproject.org/browse/ONOS-3020)] - Fix TestON's handling of steps from inside functions or loops
* [[ONOS-3021](https://jira.onosproject.org/browse/ONOS-3021)] - Clean up code style for teston.py
* [[ONOS-3024](https://jira.onosproject.org/browse/ONOS-3024)] - Implement ControllerConfig behaviour for OVS devices
* [[ONOS-3025](https://jira.onosproject.org/browse/ONOS-3025)] - Rework HA minority test to make sure all partitions still have a quorum
* [[ONOS-3026](https://jira.onosproject.org/browse/ONOS-3026)] - enable running reactive routing without BGP
* [[ONOS-3080](https://jira.onosproject.org/browse/ONOS-3080)] - Refactor application architecture of ONOS framework
* [[ONOS-3098](https://jira.onosproject.org/browse/ONOS-3098)] - Better Step Wiki Printing
* [[ONOS-3100](https://jira.onosproject.org/browse/ONOS-3100)] - Test set/get controllers using the ONOS OVSDB plugin
* [[ONOS-3106](https://jira.onosproject.org/browse/ONOS-3106)] - Code for parsing port-pair create request - PortPairCodec
* [[ONOS-3107](https://jira.onosproject.org/browse/ONOS-3107)] - Code for parsing port-pair group create request - PortPairGroupCodec
* [[ONOS-3108](https://jira.onosproject.org/browse/ONOS-3108)] - Code for parsing flow classifier create request - FlowClassifierCodec
* [[ONOS-3109](https://jira.onosproject.org/browse/ONOS-3109)] - Code for parsing port-chain create request - PortChainCodec
* [[ONOS-3110](https://jira.onosproject.org/browse/ONOS-3110)] - Code the port-pair web resource interface for receiving neutron request calling codec for parsing - PortPairWebResource
* [[ONOS-3111](https://jira.onosproject.org/browse/ONOS-3111)] - Code the port-pair-group web resource interface for receiving neutron request calling codec for parsing - PortPairGroupWebResource
* [[ONOS-3112](https://jira.onosproject.org/browse/ONOS-3112)] - Code the port-chain web resource interface for receiving neutron request calling codec for parsing - PortChainWebResource
* [[ONOS-3113](https://jira.onosproject.org/browse/ONOS-3113)] - Code the flow classifier web resource interface for receiving neutron request calling codec for parsing - FlowClassifierWebResource
* [[ONOS-3114](https://jira.onosproject.org/browse/ONOS-3114)] - Create the SFC Service interface
* [[ONOS-3115](https://jira.onosproject.org/browse/ONOS-3115)] - Code the SFC Manager with skeleton methods
* [[ONOS-3116](https://jira.onosproject.org/browse/ONOS-3116)] - Code the data structures in SFC Manager to hold the port pairs, port group and flow classifier
* [[ONOS-3117](https://jira.onosproject.org/browse/ONOS-3117)] - Code the interface logic with VTNResourceManager.
* [[ONOS-3118](https://jira.onosproject.org/browse/ONOS-3118)] - Code the querying and storing of SF-SFF mapping at the SFC Manager
* [[ONOS-3119](https://jira.onosproject.org/browse/ONOS-3119)] - Code the logic of deriving Classification rules from the flow classifier and port chain details
* [[ONOS-3120](https://jira.onosproject.org/browse/ONOS-3120)] - Code the forwarding logic that is required at SFF from the port-chain request details
* [[ONOS-3121](https://jira.onosproject.org/browse/ONOS-3121)] - Code the method with logic for identification of Classifier and all the SFFs along the service chain
* [[ONOS-3122](https://jira.onosproject.org/browse/ONOS-3122)] - Code the logic for Ordering of classifier, SFFs with IP and port information for a particular service chain
* [[ONOS-3128](https://jira.onosproject.org/browse/ONOS-3128)] - Web UI - Traffic overlay as default overlay
* [[ONOS-3129](https://jira.onosproject.org/browse/ONOS-3129)] - Web UI - Intent select and navigate to Topology View with intent monitoring
* [[ONOS-3130](https://jira.onosproject.org/browse/ONOS-3130)] - Create L3VPN YANG File
* [[ONOS-3131](https://jira.onosproject.org/browse/ONOS-3131)] - Create a new project proposal wiki for YANG service model
* [[ONOS-3132](https://jira.onosproject.org/browse/ONOS-3132)] - SDN-IP sometimes can not setup p2p intents when running multiple onos nodes
* [[ONOS-3133](https://jira.onosproject.org/browse/ONOS-3133)] - Write OFC 2016 paper
* [[ONOS-3137](https://jira.onosproject.org/browse/ONOS-3137)] - Sketch out HA for Metro Controller
* [[ONOS-3139](https://jira.onosproject.org/browse/ONOS-3139)] - prepare training documents and environment for developer conf in Shenzhen
* [[ONOS-3144](https://jira.onosproject.org/browse/ONOS-3144)] - Use NetConf to get and set controllers
* [[ONOS-3151](https://jira.onosproject.org/browse/ONOS-3151)] - Add createHandler interface by driver name and deviceid
* [[ONOS-3161](https://jira.onosproject.org/browse/ONOS-3161)] - Unit test the port-pair Web resource and Codec methods
* [[ONOS-3162](https://jira.onosproject.org/browse/ONOS-3162)] - Unit test the port-pair-group Web resource and Codec methods
* [[ONOS-3163](https://jira.onosproject.org/browse/ONOS-3163)] - Unit test the flow classifier Web resource and Codec methods
* [[ONOS-3164](https://jira.onosproject.org/browse/ONOS-3164)] - Unit test the port-chain Web resource and Codec methods
* [[ONOS-3165](https://jira.onosproject.org/browse/ONOS-3165)] - MAC address shouldn't be mandatory in interfaces - network cfg
* [[ONOS-3166](https://jira.onosproject.org/browse/ONOS-3166)] - Write a scapy driver for sending and receiving packets from a mininet host
* [[ONOS-3167](https://jira.onosproject.org/browse/ONOS-3167)] - Mobile-friendly ON.Lab and ONOS website
* [[ONOS-3176](https://jira.onosproject.org/browse/ONOS-3176)] - ONOSFW L3 vtn
* [[ONOS-3177](https://jira.onosproject.org/browse/ONOS-3177)] - ONOSFW L3 vtn
* [[ONOS-3181](https://jira.onosproject.org/browse/ONOS-3181)] - Test suit for scaling topology
* [[ONOS-3192](https://jira.onosproject.org/browse/ONOS-3192)] - interfaces cli commmand shouldn't return ips, mac or vlan if these are null
* [[ONOS-3199](https://jira.onosproject.org/browse/ONOS-3199)] - App Specific Webpages
* [[ONOS-3200](https://jira.onosproject.org/browse/ONOS-3200)] - Unify code formation and fix grammar problem
* [[ONOS-3205](https://jira.onosproject.org/browse/ONOS-3205)] - Migrate LLDP Link Discovery configuration to Network Configuration Service
* [[ONOS-3206](https://jira.onosproject.org/browse/ONOS-3206)] - Refactor LLDPLinkDiscovery
* [[ONOS-3234](https://jira.onosproject.org/browse/ONOS-3234)] - Add ONOSFW L2/L3 UT code
* [[ONOS-3236](https://jira.onosproject.org/browse/ONOS-3236)] - Ovsdb Host's vlanid is null,it should be the default value -1.
* [[ONOS-3237](https://jira.onosproject.org/browse/ONOS-3237)] - Change OvsdbNodeId ovsdb:IP:Port to ovsdb:IP
* [[ONOS-3256](https://jira.onosproject.org/browse/ONOS-3256)] - Write IEEE newsletter paper
* [[ONOS-3257](https://jira.onosproject.org/browse/ONOS-3257)] - Add ovsdb node role state.
* [[ONOS-3262](https://jira.onosproject.org/browse/ONOS-3262)] - Remove dependency on LinkResourceService from ObjectiveTracker
* [[ONOS-3263](https://jira.onosproject.org/browse/ONOS-3263)] - Create reference App that demonstrates all GUI extension techniques
* [[ONOS-3265](https://jira.onosproject.org/browse/ONOS-3265)] - Flows, Ports, Groups views - need Nav-to-Devices view button
* [[ONOS-3269](https://jira.onosproject.org/browse/ONOS-3269)] - Protect a ONOS cluster from cross traffic.
* [[ONOS-3270](https://jira.onosproject.org/browse/ONOS-3270)] - ONOSFW Testing South-North
* [[ONOS-3271](https://jira.onosproject.org/browse/ONOS-3271)] - ONOSFW demo environment set up
* [[ONOS-3272](https://jira.onosproject.org/browse/ONOS-3272)] - ONOSFW deliverables
* [[ONOS-3279](https://jira.onosproject.org/browse/ONOS-3279)] - Support for "shared" semantics in ResourceService
* [[ONOS-3280](https://jira.onosproject.org/browse/ONOS-3280)] - Merge SFC Manager as a bundle in VTN application
* [[ONOS-3281](https://jira.onosproject.org/browse/ONOS-3281)] - Code and UT for SFC Manager interface with FlowRule
* [[ONOS-3282](https://jira.onosproject.org/browse/ONOS-3282)] - Code and UT for SFC Manager interface with Openflow adapter via FlowRule
* [[ONOS-3283](https://jira.onosproject.org/browse/ONOS-3283)] - Code and UT for SFC Manager and ForwardingObjective interaction
* [[ONOS-3284](https://jira.onosproject.org/browse/ONOS-3284)] - Prepare the extensions required in FlowRule
* [[ONOS-3285](https://jira.onosproject.org/browse/ONOS-3285)] - Prepare the table details in OVS patch for classifier
* [[ONOS-3286](https://jira.onosproject.org/browse/ONOS-3286)] - Prepare the table details in OVS patch for Forwarder
* [[ONOS-3287](https://jira.onosproject.org/browse/ONOS-3287)] - Prepare the Match and Action details in classier towrads ingress SFF
* [[ONOS-3288](https://jira.onosproject.org/browse/ONOS-3288)] - Prepare the Match and Action details in SFF towards next SFF
* [[ONOS-3289](https://jira.onosproject.org/browse/ONOS-3289)] - Prepare the Match and Action details in last SFF
* [[ONOS-3290](https://jira.onosproject.org/browse/ONOS-3290)] - Prepare the extensions required in ForwardingObjective
* [[ONOS-3291](https://jira.onosproject.org/browse/ONOS-3291)] - Prepare the extensions required in OpenFlow
* [[ONOS-3292](https://jira.onosproject.org/browse/ONOS-3292)] - Prepare the extensions required in OVS patch
* [[ONOS-3293](https://jira.onosproject.org/browse/ONOS-3293)] - Create an HA test that stops nodes instead of killing them
* [[ONOS-3296](https://jira.onosproject.org/browse/ONOS-3296)] - Support for continuous values in new resource APIs
* [[ONOS-3299](https://jira.onosproject.org/browse/ONOS-3299)] - Analyze E-CORD GUI requirements
* [[ONOS-3306](https://jira.onosproject.org/browse/ONOS-3306)] - Define RPC data model for Device related interfaces
* [[ONOS-3311](https://jira.onosproject.org/browse/ONOS-3311)] - Basic Gerrit reviewers plugin
* [[ONOS-3321](https://jira.onosproject.org/browse/ONOS-3321)] - Application subsystem preDeactivate & postActivate
* [[ONOS-3323](https://jira.onosproject.org/browse/ONOS-3323)] - RPC Service implementation using gRPC
* [[ONOS-3325](https://jira.onosproject.org/browse/ONOS-3325)] - As an operator I want to specify the IP address and ONOS node advertises for clustering purposes
* [[ONOS-3326](https://jira.onosproject.org/browse/ONOS-3326)] - As an operator I would like clustering to select an available IP address for identification
* [[ONOS-3327](https://jira.onosproject.org/browse/ONOS-3327)] - Add persistence service usage to ECMap
* [[ONOS-3328](https://jira.onosproject.org/browse/ONOS-3328)] - Bundle Catalyst using maven-bundle-plugin
* [[ONOS-3329](https://jira.onosproject.org/browse/ONOS-3329)] - Add TUNNEL\_IPV4\_DST to L3ModificationInstruction
* [[ONOS-3331](https://jira.onosproject.org/browse/ONOS-3331)] - Add class TunnelIPv4Criterion
* [[ONOS-3332](https://jira.onosproject.org/browse/ONOS-3332)] - sketch out BigSwitch for super Controller based on ONOS
* [[ONOS-3336](https://jira.onosproject.org/browse/ONOS-3336)] - Implement Mininet driver function that checks the flow tables
* [[ONOS-3341](https://jira.onosproject.org/browse/ONOS-3341)] - Remove ll command from onos commands, since conflicts with ll command in ubuntu
* [[ONOS-3345](https://jira.onosproject.org/browse/ONOS-3345)] - Add processing about Instruction type Extention in GroupModBuilder.
* [[ONOS-3352](https://jira.onosproject.org/browse/ONOS-3352)] - Need to move the method to compare Intents out of the sdn-ip package
* [[ONOS-3353](https://jira.onosproject.org/browse/ONOS-3353)] - Add the entire American map to ONOS
* [[ONOS-3354](https://jira.onosproject.org/browse/ONOS-3354)] - Install slackin on the wiki srv to facilitate the subscription of users to slack
* [[ONOS-3356](https://jira.onosproject.org/browse/ONOS-3356)] - NPE when pushing a net cfg for a device not yet connected
* [[ONOS-3367](https://jira.onosproject.org/browse/ONOS-3367)] - Update HA to use the new Mininet driver function for getting the flow table
* [[ONOS-3368](https://jira.onosproject.org/browse/ONOS-3368)] - Core should protect itself against applications that throw exceptions in packet processors
* [[ONOS-3369](https://jira.onosproject.org/browse/ONOS-3369)] - Exceptions from rest calls that result in a 500 response do not get logged
* [[ONOS-3370](https://jira.onosproject.org/browse/ONOS-3370)] - Separate HostLocationProvider and LLDPLinkProvider from OpenFlow application
* [[ONOS-3387](https://jira.onosproject.org/browse/ONOS-3387)] - Verification mechanism for network configuration
* [[ONOS-3399](https://jira.onosproject.org/browse/ONOS-3399)] - Ensure LINC driver keeps using draft OF optical extensions
* [[ONOS-3405](https://jira.onosproject.org/browse/ONOS-3405)] - change encoding of ethType to Base16 in flows json coding/encoding
* [[ONOS-3406](https://jira.onosproject.org/browse/ONOS-3406)] - Change expected type of element in application post REST API
* [[ONOS-3408](https://jira.onosproject.org/browse/ONOS-3408)] - Retrieve statistics about ONOS commits
* [[ONOS-3409](https://jira.onosproject.org/browse/ONOS-3409)] - Create Epics and Wiki pages for GEANT SDX use-case
* [[ONOS-3410](https://jira.onosproject.org/browse/ONOS-3410)] - let sdn-ip support IPv4/IPv6 default route
* [[ONOS-3420](https://jira.onosproject.org/browse/ONOS-3420)] - QA Nightly Test Hang
* [[ONOS-3436](https://jira.onosproject.org/browse/ONOS-3436)] - Code the ONOS-Loxi extensions for NSH support
* [[ONOS-3437](https://jira.onosproject.org/browse/ONOS-3437)] - Code the classification logic with flow classifier rules
* [[ONOS-3438](https://jira.onosproject.org/browse/ONOS-3438)] - API for getting all flow classifiers
* [[ONOS-3439](https://jira.onosproject.org/browse/ONOS-3439)] - API for getting flow classifier rule
* [[ONOS-3440](https://jira.onosproject.org/browse/ONOS-3440)] - Code the forwarding logic based on Neutron port-chain parameters
* [[ONOS-3442](https://jira.onosproject.org/browse/ONOS-3442)] - Ip Topology subsystem with IpTopology device manager and its store (Device)
* [[ONOS-3443](https://jira.onosproject.org/browse/ONOS-3443)] - Ip Topology subsystem with IpTopology link manager and its store (Link)
* [[ONOS-3455](https://jira.onosproject.org/browse/ONOS-3455)] - Documentation about new resource management APIs
* [[ONOS-3461](https://jira.onosproject.org/browse/ONOS-3461)] - Move specific Device/Port LLDP suppression NetworkConfiguration from apps tree to devices and ports tree
* [[ONOS-3470](https://jira.onosproject.org/browse/ONOS-3470)] - ONOS deployment on sites without Internet access
* [[ONOS-3501](https://jira.onosproject.org/browse/ONOS-3501)] - Check if optical devices support required behaviour for resource query
* [[ONOS-3515](https://jira.onosproject.org/browse/ONOS-3515)] - Ability to configure alternate link-weight function as a default
* [[ONOS-3516](https://jira.onosproject.org/browse/ONOS-3516)] - Ability to inject alternate graph path search algorithm as default
* [[ONOS-3518](https://jira.onosproject.org/browse/ONOS-3518)] - GUI Topology View - extend badging to include hosts
* [[ONOS-3524](https://jira.onosproject.org/browse/ONOS-3524)] - SM-ONOS: Implement scripts to enable Security-Mode
* [[ONOS-3525](https://jira.onosproject.org/browse/ONOS-3525)] - Refactor KShortestPaths search
* [[ONOS-3540](https://jira.onosproject.org/browse/ONOS-3540)] - Update the ON.Lab Github page
* [[ONOS-3552](https://jira.onosproject.org/browse/ONOS-3552)] - Groups are not removed from the store when device disconnects
* [[ONOS-3570](https://jira.onosproject.org/browse/ONOS-3570)] - Setup rack for Atrium
* [[ONOS-3571](https://jira.onosproject.org/browse/ONOS-3571)] - Setup rack for CORD
* [[ONOS-3572](https://jira.onosproject.org/browse/ONOS-3572)] - Hardware maintenance at Stanford for OpenCloud cluster
* [[ONOS-3574](https://jira.onosproject.org/browse/ONOS-3574)] - Unmount monitors/keyboard/KVMs from server room
* [[ONOS-3594](https://jira.onosproject.org/browse/ONOS-3594)] - Web UI - Create new "Loading..." animation from custom frames.
* [[ONOS-3599](https://jira.onosproject.org/browse/ONOS-3599)] - LldpLinkProvider gets ConsistentMapException$Timeout on activate
