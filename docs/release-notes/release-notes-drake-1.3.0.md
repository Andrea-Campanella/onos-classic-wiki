# Release Notes - Drake 1.3.0

# Drake Release

Version: 1.3.0

Release Date: September 18th, 2015

Download [here](../redirect-pages-not-in-main-menu/download-packages-and-tutorial-vms.md)

The focus for Drake has been to enable use case deployments and to improve infrastructure.

## Open Source Project Integrations

* ONF Atrium
* OPNFV Brahmaputra
* Cloudrouter
* OpenStack Neutron ML2 plugin

## Security

* GUI and CLI require username and password login
* REST interfaces require username and password
* TLS support for internode communication
* Configurable HTTPS for GUI & REST API
* Security-Mode ONOS for application security

## Device Configuration

* New configuration subsystem to centralize application config
* NETCONF / Yang model for ACLs
* OVSDB plug-in available

## Infrastructure Improvements

* Adaptive flow statistics subsystem
* PCEP southbound plug-in
* VXLAN tunnel setup
* Initial virtualization steps
* DHCP server app
* Metrics collection subsystem
* Test enhancements for new features and coverage
* OpenFlow meter support
* Multicast improvements to IGMP snooping, PIM-SSM
* GUI topology overlays and better link highlighting
* Northbound structural enhancements

---

## Complete Listing of features and bugs resolved

## Sub-task

* [[ONOS-862](https://jira.onosproject.org/browse/ONOS-862)] - Define EdgeService & related API entities
* [[ONOS-863](https://jira.onosproject.org/browse/ONOS-863)] - Implement EdgeManager and related entities
* [[ONOS-865](https://jira.onosproject.org/browse/ONOS-865)] - Update ProxyArpManager and other similar classes to use the EdgeService
* [[ONOS-1270](https://jira.onosproject.org/browse/ONOS-1270)] - IPv6 and SDN-IP: Verify the receiving of IPv6 routes over IPv6 BGP peering
* [[ONOS-1271](https://jira.onosproject.org/browse/ONOS-1271)] - Add missing IPv6-related unit tests
* [[ONOS-1321](https://jira.onosproject.org/browse/ONOS-1321)] - Convert the pingIPv6Hosts function in TestON mininet driver to log the output in a matrix fashion.
* [[ONOS-1322](https://jira.onosproject.org/browse/ONOS-1322)] - Add basic IPv6 Test coverage in CHO tests
* [[ONOS-1447](https://jira.onosproject.org/browse/ONOS-1447)] - Fujitsu hardware installation and configuration
* [[ONOS-1509](https://jira.onosproject.org/browse/ONOS-1509)] - Investigate OpenFlow support for Calient fiber switch
* [[ONOS-1524](https://jira.onosproject.org/browse/ONOS-1524)] - Host & traffic generator installation and config
* [[ONOS-1527](https://jira.onosproject.org/browse/ONOS-1527)] - Select Corsa pipeline
* [[ONOS-1536](https://jira.onosproject.org/browse/ONOS-1536)] - Implement demo script
* [[ONOS-1642](https://jira.onosproject.org/browse/ONOS-1642)] - Test Application for Transactions
* [[ONOS-1687](https://jira.onosproject.org/browse/ONOS-1687)] - Update Functionality test plan with new and modified test cases
* [[ONOS-1807](https://jira.onosproject.org/browse/ONOS-1807)] - Implement mininet driver function to run iperf UDPv4 across given set of hosts
* [[ONOS-1808](https://jira.onosproject.org/browse/ONOS-1808)] - Implement Mininet driver function to run iperf TCPv4 across given set of hosts
* [[ONOS-1919](https://jira.onosproject.org/browse/ONOS-1919)] - Update test application to expose new api for Atomic Counters
* [[ONOS-1920](https://jira.onosproject.org/browse/ONOS-1920)] - Add tests for new atomic counter api
* [[ONOS-1923](https://jira.onosproject.org/browse/ONOS-1923)] - Ciena hardware installation and configuration
* [[ONOS-1924](https://jira.onosproject.org/browse/ONOS-1924)] - Huawei hardware installation and configuration
* [[ONOS-2000](https://jira.onosproject.org/browse/ONOS-2000)] - Create TestON driver for leaders -c cli command
* [[ONOS-2001](https://jira.onosproject.org/browse/ONOS-2001)] - Add tests for leadership candidate correctness
* [[ONOS-2112](https://jira.onosproject.org/browse/ONOS-2112)] - Create a application used to manager virtual network resource.
* [[ONOS-2115](https://jira.onosproject.org/browse/ONOS-2115)] - Create a application named vtn
* [[ONOS-2146](https://jira.onosproject.org/browse/ONOS-2146)] - Move exiting Functionality nightly job in to BM setup
* [[ONOS-2147](https://jira.onosproject.org/browse/ONOS-2147)] - Move existing HA Jenkins job to run on BM setup
* [[ONOS-2158](https://jira.onosproject.org/browse/ONOS-2158)] - the implementation of TenantNetwork
* [[ONOS-2159](https://jira.onosproject.org/browse/ONOS-2159)] - Add to query devices by type api in DeviceService and DeviceStore interfaces
* [[ONOS-2160](https://jira.onosproject.org/browse/ONOS-2160)] - the implementation of vtn app
* [[ONOS-2161](https://jira.onosproject.org/browse/ONOS-2161)] - Add OVSDB adapter api in south bound.
* [[ONOS-2162](https://jira.onosproject.org/browse/ONOS-2162)] - The implementation of OvsdbProviderService
* [[ONOS-2173](https://jira.onosproject.org/browse/ONOS-2173)] - Create Jenkins view and jobs for production tests
* [[ONOS-2174](https://jira.onosproject.org/browse/ONOS-2174)] - Move New Functional Tests to Prod. Testbed
* [[ONOS-2175](https://jira.onosproject.org/browse/ONOS-2175)] - move HA to bm production testbed
* [[ONOS-2176](https://jira.onosproject.org/browse/ONOS-2176)] - create Jenkins job to start CHO
* [[ONOS-2177](https://jira.onosproject.org/browse/ONOS-2177)] - remove static test env links
* [[ONOS-2178](https://jira.onosproject.org/browse/ONOS-2178)] - create posting jobs for wiki
* [[ONOS-2195](https://jira.onosproject.org/browse/ONOS-2195)] - Test how many routes SDN-IP can support --- one onos/sdn-ip/bgp-speaker
* [[ONOS-2196](https://jira.onosproject.org/browse/ONOS-2196)] - improve SDN-IP code to handle 600,000 routes --- one onos/sdnip/bgp-speaker
* [[ONOS-2198](https://jira.onosproject.org/browse/ONOS-2198)] - build test environment with test script --- one onos/sdn-ip/bgp-speaker
* [[ONOS-2199](https://jira.onosproject.org/browse/ONOS-2199)] - build test environment with test script --- multiple onos/sdn-ip/bgp-speaker
* [[ONOS-2200](https://jira.onosproject.org/browse/ONOS-2200)] - Test how many routes SDN-IP can support --- multiple onos/sdn-ip/bgp-speaker
* [[ONOS-2201](https://jira.onosproject.org/browse/ONOS-2201)] - improve SDN-IP code to handle 600,000 routes --- multiple onos/sdnip/bgp-speaker
* [[ONOS-2212](https://jira.onosproject.org/browse/ONOS-2212)] - Packet processor for DHCP requests
* [[ONOS-2213](https://jira.onosproject.org/browse/ONOS-2213)] - Packet builder for DHCP replies
* [[ONOS-2214](https://jira.onosproject.org/browse/ONOS-2214)] - Create DHCP "Server" (i.e. Manager) for handling DHCP logic
* [[ONOS-2215](https://jira.onosproject.org/browse/ONOS-2215)] - DHCP Store for reconciling resource state across network
* [[ONOS-2216](https://jira.onosproject.org/browse/ONOS-2216)] - DHCP Service for observability
* [[ONOS-2217](https://jira.onosproject.org/browse/ONOS-2217)] - DHCP CLI commands
* [[ONOS-2218](https://jira.onosproject.org/browse/ONOS-2218)] - DHCP Config for address ranges, gateway, DNS
* [[ONOS-2219](https://jira.onosproject.org/browse/ONOS-2219)] - Integrate hosts learned through DHCP into topology
* [[ONOS-2242](https://jira.onosproject.org/browse/ONOS-2242)] - implementation of TunnelConfig
* [[ONOS-2243](https://jira.onosproject.org/browse/ONOS-2243)] - The restful api used to syncronize network resource by neutron
* [[ONOS-2244](https://jira.onosproject.org/browse/ONOS-2244)] - The restful api used to syncronize subnet resource by neutron
* [[ONOS-2245](https://jira.onosproject.org/browse/ONOS-2245)] - The restful api used to syncronize port resource by neutron
* [[ONOS-2246](https://jira.onosproject.org/browse/ONOS-2246)] - The implementation of network resource service
* [[ONOS-2247](https://jira.onosproject.org/browse/ONOS-2247)] - The implementation of subnet resource service
* [[ONOS-2248](https://jira.onosproject.org/browse/ONOS-2248)] - The implementation of port resource service
* [[ONOS-2249](https://jira.onosproject.org/browse/ONOS-2249)] - The junit test codes of network resource
* [[ONOS-2250](https://jira.onosproject.org/browse/ONOS-2250)] - The junit test codes of subnet resource
* [[ONOS-2251](https://jira.onosproject.org/browse/ONOS-2251)] - The junit test codes of port resource
* [[ONOS-2252](https://jira.onosproject.org/browse/ONOS-2252)] - The CLIs of network resource
* [[ONOS-2253](https://jira.onosproject.org/browse/ONOS-2253)] - The CLIs of subnet resource
* [[ONOS-2254](https://jira.onosproject.org/browse/ONOS-2254)] - The CLIs of port resource
* [[ONOS-2255](https://jira.onosproject.org/browse/ONOS-2255)] - provider the apis of RFC protocol
* [[ONOS-2256](https://jira.onosproject.org/browse/ONOS-2256)] - Add a new queryDevices API by device type.
* [[ONOS-2258](https://jira.onosproject.org/browse/ONOS-2258)] - impelementation of OvsdbController
* [[ONOS-2260](https://jira.onosproject.org/browse/ONOS-2260)] - The implementation of getDevices by type API of GossipDeviceStore
* [[ONOS-2261](https://jira.onosproject.org/browse/ONOS-2261)] - The implementation of DeviceProvider using OVSDB protocal
* [[ONOS-2262](https://jira.onosproject.org/browse/ONOS-2262)] - The implementation of HostProvider using OVSDB protocal
* [[ONOS-2263](https://jira.onosproject.org/browse/ONOS-2263)] - The implementation of TunnelProvider using OVSDB protocal
* [[ONOS-2282](https://jira.onosproject.org/browse/ONOS-2282)] - Balance mastership test
* [[ONOS-2295](https://jira.onosproject.org/browse/ONOS-2295)] - Make LinkResource an interface
* [[ONOS-2296](https://jira.onosproject.org/browse/ONOS-2296)] - Tagging @Beta for Device Resource related API
* [[ONOS-2297](https://jira.onosproject.org/browse/ONOS-2297)] - Decouple ResourceRequest and ResourceAllocation
* [[ONOS-2298](https://jira.onosproject.org/browse/ONOS-2298)] - Tagging @Beta to the existing resource related types
* [[ONOS-2310](https://jira.onosproject.org/browse/ONOS-2310)] - Provide initial sketch of OVSDB driver
* [[ONOS-2312](https://jira.onosproject.org/browse/ONOS-2312)] - Implement PortConfig
* [[ONOS-2313](https://jira.onosproject.org/browse/ONOS-2313)] - Implement ControllerConfig
* [[ONOS-2331](https://jira.onosproject.org/browse/ONOS-2331)] - Create perf test READMEs
* [[ONOS-2375](https://jira.onosproject.org/browse/ONOS-2375)] - Add tunnelId in TrafficTreatment and TrafficSelector
* [[ONOS-2382](https://jira.onosproject.org/browse/ONOS-2382)] - Sketching a new resource management APIs
* [[ONOS-2387](https://jira.onosproject.org/browse/ONOS-2387)] - Implement new resource management API
* [[ONOS-2393](https://jira.onosproject.org/browse/ONOS-2393)] - the implementation of the netty controller
* [[ONOS-2396](https://jira.onosproject.org/browse/ONOS-2396)] - Host mobility
* [[ONOS-2397](https://jira.onosproject.org/browse/ONOS-2397)] - SDN-IP matching
* [[ONOS-2403](https://jira.onosproject.org/browse/ONOS-2403)] - Implement modification of transport port src/dst in OpenFlow1.3
* [[ONOS-2408](https://jira.onosproject.org/browse/ONOS-2408)] - Data model and utility class about RFC 7047 (ovsdb protocol)
* [[ONOS-2413](https://jira.onosproject.org/browse/ONOS-2413)] - REST api driver function for intents
* [[ONOS-2415](https://jira.onosproject.org/browse/ONOS-2415)] - REST api driver function for ONOS applications
* [[ONOS-2425](https://jira.onosproject.org/browse/ONOS-2425)] - Create a ovsdb app in onos-providers to install south ovsdb adapter.
* [[ONOS-2447](https://jira.onosproject.org/browse/ONOS-2447)] - RFC7047's API and its implementation and five main tables
* [[ONOS-2449](https://jira.onosproject.org/browse/ONOS-2449)] - The rest tables of RFC7047
* [[ONOS-2467](https://jira.onosproject.org/browse/ONOS-2467)] - Create Unit Tests
* [[ONOS-2469](https://jira.onosproject.org/browse/ONOS-2469)] - ARP Replies to "myIP"
* [[ONOS-2484](https://jira.onosproject.org/browse/ONOS-2484)] - Masters CLI Driver Function
* [[ONOS-2488](https://jira.onosproject.org/browse/ONOS-2488)] - Move out of incubator area
* [[ONOS-2499](https://jira.onosproject.org/browse/ONOS-2499)] - update accordingly for ONOS-2408's review recommendation
* [[ONOS-2501](https://jira.onosproject.org/browse/ONOS-2501)] - write NBI test cases
* [[ONOS-2502](https://jira.onosproject.org/browse/ONOS-2502)] - write osvdb related test cases
* [[ONOS-2503](https://jira.onosproject.org/browse/ONOS-2503)] - write NBI-network related scripts
* [[ONOS-2504](https://jira.onosproject.org/browse/ONOS-2504)] - write NBI-subnet related scripts
* [[ONOS-2505](https://jira.onosproject.org/browse/ONOS-2505)] - write NBI-port related scripts
* [[ONOS-2506](https://jira.onosproject.org/browse/ONOS-2506)] - write ovsdb connection related scripts
* [[ONOS-2518](https://jira.onosproject.org/browse/ONOS-2518)] - Add cfgSetIpv6 TestON driver function to onosclidriver
* [[ONOS-2524](https://jira.onosproject.org/browse/ONOS-2524)] - Upgrade nfvsrv01 with 64 more gigs of ram and two 500ssd drivers
* [[ONOS-2525](https://jira.onosproject.org/browse/ONOS-2525)] - Move VMs and containers from pmxeon3 to new pmxeon4 - local drive
* [[ONOS-2526](https://jira.onosproject.org/browse/ONOS-2526)] - Install new proxmox locally on the new pmxeon4
* [[ONOS-2527](https://jira.onosproject.org/browse/ONOS-2527)] - Move VMs and containers from pmxeon2 to pmxeon3 - local drive
* [[ONOS-2528](https://jira.onosproject.org/browse/ONOS-2528)] - Install new proxmox locally on the new pmxeon3
* [[ONOS-2529](https://jira.onosproject.org/browse/ONOS-2529)] - Upgrade proxmox3 with 64 more gigs of ram and two 500ssd drivers
* [[ONOS-2530](https://jira.onosproject.org/browse/ONOS-2530)] - Upgrade pmxeon2 with 64 more gigs of ram and two 500ssd drivers
* [[ONOS-2531](https://jira.onosproject.org/browse/ONOS-2531)] - Upgrade pmxeon1 with 64 more gigs of ram and two 500ssd drivers
* [[ONOS-2532](https://jira.onosproject.org/browse/ONOS-2532)] - Move VMs and containers from pmxeon1 to pmxeon2 - local drive
* [[ONOS-2533](https://jira.onosproject.org/browse/ONOS-2533)] - Install new proxmox locally on the new pmxeon2
* [[ONOS-2534](https://jira.onosproject.org/browse/ONOS-2534)] - Install new proxmox locally on the new pmxeon1
* [[ONOS-2535](https://jira.onosproject.org/browse/ONOS-2535)] - Move VMs and containers from pmamd1 to pmxeons servers - local drive
* [[ONOS-2536](https://jira.onosproject.org/browse/ONOS-2536)] - Move VMs and containers from pmamd2 to pmxeons servers - local drive
* [[ONOS-2537](https://jira.onosproject.org/browse/ONOS-2537)] - Move VMs and containers from pmamd3 to pmxeons servers - local drive
* [[ONOS-2538](https://jira.onosproject.org/browse/ONOS-2538)] - Install new proxmox locally on the new pmamd1
* [[ONOS-2539](https://jira.onosproject.org/browse/ONOS-2539)] - Install new proxmox locally on the new pmamd2
* [[ONOS-2540](https://jira.onosproject.org/browse/ONOS-2540)] - Install new proxmox locally on the new pmamd3
* [[ONOS-2543](https://jira.onosproject.org/browse/ONOS-2543)] - Add the rest of the table factory methods
* [[ONOS-2544](https://jira.onosproject.org/browse/ONOS-2544)] - Monidyf the bug of vsrsion utility class
* [[ONOS-2545](https://jira.onosproject.org/browse/ONOS-2545)] - Add the deserialization of UUID
* [[ONOS-2546](https://jira.onosproject.org/browse/ONOS-2546)] - Modify the bug of conditional judgment
* [[ONOS-2549](https://jira.onosproject.org/browse/ONOS-2549)] - Mininet Topology path fixes to current CHO tests
* [[ONOS-2562](https://jira.onosproject.org/browse/ONOS-2562)] - Update the methods and the exception message of FromJsonUtil class.
* [[ONOS-2563](https://jira.onosproject.org/browse/ONOS-2563)] - Optimize RFC 7047's code
* [[ONOS-2568](https://jira.onosproject.org/browse/ONOS-2568)] - Refactor, verify and improve existing M2S & S2M intent tests in CHO
* [[ONOS-2576](https://jira.onosproject.org/browse/ONOS-2576)] - Move VMs and containers from pmamd4 to pmxeons servers - local drive
* [[ONOS-2580](https://jira.onosproject.org/browse/ONOS-2580)] - Introduce new data type or replace "short" to "int" for TCP/UDP port
* [[ONOS-2583](https://jira.onosproject.org/browse/ONOS-2583)] - The implementation of LinkProvider using OVSDB protocal
* [[ONOS-2633](https://jira.onosproject.org/browse/ONOS-2633)] - modify the bug of ParamUtil class
* [[ONOS-2653](https://jira.onosproject.org/browse/ONOS-2653)] - XOS virtual network between Ceilometer head node and MongoDB sliver
* [[ONOS-2685](https://jira.onosproject.org/browse/ONOS-2685)] - Verify all CHOtests run without any issue in ProdCluster with IPv6 cases included
* [[ONOS-2686](https://jira.onosproject.org/browse/ONOS-2686)] - Update the Jenkins results script to include new IPv6 cases (for wiki posting)
* [[ONOS-2687](https://jira.onosproject.org/browse/ONOS-2687)] - Add new wiki pages for posting Drake release test results
* [[ONOS-2689](https://jira.onosproject.org/browse/ONOS-2689)] - Register a link as resource when the link is added
* [[ONOS-2690](https://jira.onosproject.org/browse/ONOS-2690)] - Register a device as resource when the device is added
* [[ONOS-2691](https://jira.onosproject.org/browse/ONOS-2691)] - Register a port as resource when the port is added
* [[ONOS-2692](https://jira.onosproject.org/browse/ONOS-2692)] - Implement a method to unregister resource(s)
* [[ONOS-2693](https://jira.onosproject.org/browse/ONOS-2693)] - Unregister a link from resources when the link is removed
* [[ONOS-2694](https://jira.onosproject.org/browse/ONOS-2694)] - Unregister a device from resources when the device is removed
* [[ONOS-2695](https://jira.onosproject.org/browse/ONOS-2695)] - Unregister a port from resources when the port is removed
* [[ONOS-2701](https://jira.onosproject.org/browse/ONOS-2701)] - Test if master down, whether slave onos instance can take over
* [[ONOS-2702](https://jira.onosproject.org/browse/ONOS-2702)] - Add code generation for self-registering REST API docs
* [[ONOS-2703](https://jira.onosproject.org/browse/ONOS-2703)] - Add swagger GUI to onos-rest bundle and theme it appropriately
* [[ONOS-2704](https://jira.onosproject.org/browse/ONOS-2704)] - Sweep through existing apps and appropriately modify pom.xml files
* [[ONOS-2705](https://jira.onosproject.org/browse/ONOS-2705)] - Sweep through existing apps and document REST APIs via javadocs
* [[ONOS-2710](https://jira.onosproject.org/browse/ONOS-2710)] - Refactor registration/unregistration of ResourceStore
* [[ONOS-2711](https://jira.onosproject.org/browse/ONOS-2711)] - Replace "short" to new "TpPort" for TCP/UDP/SCTP ports in repository
* [[ONOS-2716](https://jira.onosproject.org/browse/ONOS-2716)] - Handle duplicate resource registration in ResourceStore
* [[ONOS-2717](https://jira.onosproject.org/browse/ONOS-2717)] - Handle duplicate resource unregistration in ResourceStore
* [[ONOS-2728](https://jira.onosproject.org/browse/ONOS-2728)] - Define an interface to make a query for VLAN capability
* [[ONOS-2729](https://jira.onosproject.org/browse/ONOS-2729)] - Define an interface to make a query for MPLS capability
* [[ONOS-2742](https://jira.onosproject.org/browse/ONOS-2742)] - Implement registering VLAN IDs when a link is discovered
* [[ONOS-2743](https://jira.onosproject.org/browse/ONOS-2743)] - Implement registering MPLS labels when a link is discovered
* [[ONOS-2745](https://jira.onosproject.org/browse/ONOS-2745)] - ONOS cli for getting and putting into transactional maps
* [[ONOS-2747](https://jira.onosproject.org/browse/ONOS-2747)] - Basic system tests for transactional maps
* [[ONOS-2758](https://jira.onosproject.org/browse/ONOS-2758)] - REST APIs for DHCP Server
* [[ONOS-2783](https://jira.onosproject.org/browse/ONOS-2783)] - FUNC test results wiki posting for Drake
* [[ONOS-2784](https://jira.onosproject.org/browse/ONOS-2784)] - PERF & SCALE test results wiki posting for Drake
* [[ONOS-2785](https://jira.onosproject.org/browse/ONOS-2785)] - HA test results wiki posting for Drake
* [[ONOS-2786](https://jira.onosproject.org/browse/ONOS-2786)] - OVSDB test results wiki posting for Drake
* [[ONOS-2787](https://jira.onosproject.org/browse/ONOS-2787)] - IPv6 test results wiki posting for Drake
* [[ONOS-2788](https://jira.onosproject.org/browse/ONOS-2788)] - CHO test results wiki posting for Drake
* [[ONOS-2883](https://jira.onosproject.org/browse/ONOS-2883)] - Investigate why IPv6 ping all is slower than IPv4 ping all.

## Bug

* [[ONOS-732](https://jira.onosproject.org/browse/ONOS-732)] - TestON hangs when ssh-ing into a machine for the first time
* [[ONOS-1412](https://jira.onosproject.org/browse/ONOS-1412)] - Links and objects disappearing in the GUI when using Firefox
* [[ONOS-1419](https://jira.onosproject.org/browse/ONOS-1419)] - Cannot select nodes in oblique view
* [[ONOS-1589](https://jira.onosproject.org/browse/ONOS-1589)] - Packet library deserialize methods are not resilient to malformed input
* [[ONOS-1633](https://jira.onosproject.org/browse/ONOS-1633)] - As a user, I would be able to create optical intents, also from the ONOS instances which are not master for a specific switch
* [[ONOS-1679](https://jira.onosproject.org/browse/ONOS-1679)] - Platform independent temporary directory name in ApplicationArchiveTest
* [[ONOS-1680](https://jira.onosproject.org/browse/ONOS-1680)] - ApplicationArchiveTest unit test failure on Windows: cannot purge temporary files
* [[ONOS-1753](https://jira.onosproject.org/browse/ONOS-1753)] - Hosts not appearing when "Show hosts" is toggled upon reloading GUI
* [[ONOS-1946](https://jira.onosproject.org/browse/ONOS-1946)] - TestON does not shutdown cleanly if cleanup is called from a thread
* [[ONOS-2075](https://jira.onosproject.org/browse/ONOS-2075)] - App view -- icons not updating unless view is refreshed from browser
* [[ONOS-2076](https://jira.onosproject.org/browse/ONOS-2076)] - Optical connectivity intents are not triggered by OpticalPathProvisioner
* [[ONOS-2080](https://jira.onosproject.org/browse/ONOS-2080)] - Application view does not properly refresh when control actions are performed
* [[ONOS-2090](https://jira.onosproject.org/browse/ONOS-2090)] - Remove need to parse strings in REST JSON output
* [[ONOS-2091](https://jira.onosproject.org/browse/ONOS-2091)] - Installing OAR app loads the built-in app instead
* [[ONOS-2100](https://jira.onosproject.org/browse/ONOS-2100)] - Device disconnect, mastership and role change without Standby noticed during CHO test
* [[ONOS-2109](https://jira.onosproject.org/browse/ONOS-2109)] - Topology View -- (0,0) Coordinate Bug
* [[ONOS-2110](https://jira.onosproject.org/browse/ONOS-2110)] - cbench test regression - getting initial run with "0" responses
* [[ONOS-2123](https://jira.onosproject.org/browse/ONOS-2123)] - Packet Optical Tutorial seems to have wrong preset configurations
* [[ONOS-2124](https://jira.onosproject.org/browse/ONOS-2124)] - Version number should support two-segment versions, e.g. 1.0
* [[ONOS-2138](https://jira.onosproject.org/browse/ONOS-2138)] - Topology View - behavior toggle not consistent upon refresh
* [[ONOS-2148](https://jira.onosproject.org/browse/ONOS-2148)] - Some ONOS nodes in Intent PURGE\_REQ loop trying to purge a non existent intent
* [[ONOS-2149](https://jira.onosproject.org/browse/ONOS-2149)] - App View -- App Action triggers refresh, but without taking into account sort direction
* [[ONOS-2169](https://jira.onosproject.org/browse/ONOS-2169)] - KryoException: Class not registered: org.onosproject.store.service.Versioned
* [[ONOS-2280](https://jira.onosproject.org/browse/ONOS-2280)] - NPE in ECHostStore when disconnecting topology
* [[ONOS-2281](https://jira.onosproject.org/browse/ONOS-2281)] - Unable to bring up ATT topology using latest ONOS master build
* [[ONOS-2292](https://jira.onosproject.org/browse/ONOS-2292)] - NPE in intent store when submitting batches
* [[ONOS-2299](https://jira.onosproject.org/browse/ONOS-2299)] - CompilerTest failure on Windows
* [[ONOS-2330](https://jira.onosproject.org/browse/ONOS-2330)] - Some intents are stuck in Installing state after adding in CHO test
* [[ONOS-2374](https://jira.onosproject.org/browse/ONOS-2374)] - Add getter method in IpTunnelEndPoint
* [[ONOS-2380](https://jira.onosproject.org/browse/ONOS-2380)] - wipe-out command does not wipe-out intents left in FAILED state
* [[ONOS-2381](https://jira.onosproject.org/browse/ONOS-2381)] - purge-intents command to purge WITHDRAWN intents is not working in master
* [[ONOS-2383](https://jira.onosproject.org/browse/ONOS-2383)] - Fixs the DeviceManager.java white-spacing/line-breaks
* [[ONOS-2386](https://jira.onosproject.org/browse/ONOS-2386)] - Device View -- Group, Flow, and Port buttons are still selectable after closing panel
* [[ONOS-2388](https://jira.onosproject.org/browse/ONOS-2388)] - Add error handling for wrong passwords to the driver connect function
* [[ONOS-2390](https://jira.onosproject.org/browse/ONOS-2390)] - NPEs at removeDeviceInternal after device remove issued
* [[ONOS-2404](https://jira.onosproject.org/browse/ONOS-2404)] - Assignment of HandshakerBehavior does not respect driver annotations
* [[ONOS-2406](https://jira.onosproject.org/browse/ONOS-2406)] - Local identity is established incorrectly as a non-cluster IP address.
* [[ONOS-2409](https://jira.onosproject.org/browse/ONOS-2409)] - Errors in opticalUtils.py module
* [[ONOS-2417](https://jira.onosproject.org/browse/ONOS-2417)] - onos-uninstall does not work on systems without the 'service' command
* [[ONOS-2418](https://jira.onosproject.org/browse/ONOS-2418)] - IPv6 reactive mode not working in latest master
* [[ONOS-2419](https://jira.onosproject.org/browse/ONOS-2419)] - flowTP test Throughput regression
* [[ONOS-2421](https://jira.onosproject.org/browse/ONOS-2421)] - After enabling fwd module ONOS failing to install default flows on some devcies
* [[ONOS-2423](https://jira.onosproject.org/browse/ONOS-2423)] - If IPv6 is enabled first before fwd module one default IPv6 flow is missing
* [[ONOS-2426](https://jira.onosproject.org/browse/ONOS-2426)] - Flows are stuck in PENDING\_ADD after switches reconnect.
* [[ONOS-2432](https://jira.onosproject.org/browse/ONOS-2432)] - Reactive Forwarding: fixBlackhole NPE
* [[ONOS-2433](https://jira.onosproject.org/browse/ONOS-2433)] - Intents stuck in FAILED state due to cascading topology changes.
* [[ONOS-2439](https://jira.onosproject.org/browse/ONOS-2439)] - Fix link discovery defect uncovered when consistent map updates were enabled
* [[ONOS-2463](https://jira.onosproject.org/browse/ONOS-2463)] - Exception when pushing topology config
* [[ONOS-2477](https://jira.onosproject.org/browse/ONOS-2477)] - Links not discovered due to link discoverers missing ports
* [[ONOS-2478](https://jira.onosproject.org/browse/ONOS-2478)] - KryoException: Unable to find class: 10.128.30.12
* [[ONOS-2479](https://jira.onosproject.org/browse/ONOS-2479)] - Sometimes OpenFlow packets get dropped before being sent to switch
* [[ONOS-2481](https://jira.onosproject.org/browse/ONOS-2481)] - Caught exception "Can't install feature onos-drivers"
* [[ONOS-2489](https://jira.onosproject.org/browse/ONOS-2489)] - ONOS tries to push flows before the flow provider is there
* [[ONOS-2490](https://jira.onosproject.org/browse/ONOS-2490)] - FUNCintent test caught "IllegalStateExceptions"
* [[ONOS-2494](https://jira.onosproject.org/browse/ONOS-2494)] - Cannot exit from CLI
* [[ONOS-2495](https://jira.onosproject.org/browse/ONOS-2495)] - Buffer underflow when executing 'device-role' command
* [[ONOS-2511](https://jira.onosproject.org/browse/ONOS-2511)] - Error on OFchannel handler when connecting to 1.3 OVS
* [[ONOS-2512](https://jira.onosproject.org/browse/ONOS-2512)] - Fix the bug that catch the node ip and port is wrong in OvsdbTunnelConfig and OvsdbBridgeConfig
* [[ONOS-2514](https://jira.onosproject.org/browse/ONOS-2514)] - SDN-IP installs too many point-to-point intents for some configurations
* [[ONOS-2516](https://jira.onosproject.org/browse/ONOS-2516)] - Poor flow throughput
* [[ONOS-2547](https://jira.onosproject.org/browse/ONOS-2547)] - modify DefaultIpAddress in OvsdbTunnelConfig and modify drivers.xml
* [[ONOS-2548](https://jira.onosproject.org/browse/ONOS-2548)] - add device type validation when create a tunnel
* [[ONOS-2550](https://jira.onosproject.org/browse/ONOS-2550)] - Fix validation incorrect information bugs of TunnelManager
* [[ONOS-2559](https://jira.onosproject.org/browse/ONOS-2559)] - Can post an network which all parameters are null
* [[ONOS-2560](https://jira.onosproject.org/browse/ONOS-2560)] - Get network by id,can‘t return json message
* [[ONOS-2561](https://jira.onosproject.org/browse/ONOS-2561)] - get the subnet,can’t return the json message
* [[ONOS-2572](https://jira.onosproject.org/browse/ONOS-2572)] - AbstractAccumulator: synchronization problem
* [[ONOS-2573](https://jira.onosproject.org/browse/ONOS-2573)] - Missing flow rules for multi-to-single point intents with no selectors
* [[ONOS-2575](https://jira.onosproject.org/browse/ONOS-2575)] - Network NBI update process successful but return an error code
* [[ONOS-2622](https://jira.onosproject.org/browse/ONOS-2622)] - Fix error of north app and update onos-app-vtnrsc package
* [[ONOS-2623](https://jira.onosproject.org/browse/ONOS-2623)] - add onos-ovsdb-api and onos-ovsdb-rfc dependency to pom.xml
* [[ONOS-2624](https://jira.onosproject.org/browse/ONOS-2624)] - Fix host annotations of host description
* [[ONOS-2688](https://jira.onosproject.org/browse/ONOS-2688)] - After running CHOtest for 2 days some devices have no stby controllers
* [[ONOS-2697](https://jira.onosproject.org/browse/ONOS-2697)] - FUNCintent Crash
* [[ONOS-2707](https://jira.onosproject.org/browse/ONOS-2707)] - Fix bug of process ovsdb table update
* [[ONOS-2708](https://jira.onosproject.org/browse/ONOS-2708)] - Add implementation of getting ovsdb ports or bridges in the ovsdb node.
* [[ONOS-2709](https://jira.onosproject.org/browse/ONOS-2709)] - Fix bug of installing flowrules.
* [[ONOS-2713](https://jira.onosproject.org/browse/ONOS-2713)] - Fix a bug of ovsdb controller and add anotations.
* [[ONOS-2714](https://jira.onosproject.org/browse/ONOS-2714)] - Topology discovery failing in latest master (Aug 21st 2015)
* [[ONOS-2718](https://jira.onosproject.org/browse/ONOS-2718)] - Using error json can post an network
* [[ONOS-2721](https://jira.onosproject.org/browse/ONOS-2721)] - Port NBI post use "port:",But get context is "ports"
* [[ONOS-2722](https://jira.onosproject.org/browse/ONOS-2722)] - After port deleted,get port data returns error
* [[ONOS-2723](https://jira.onosproject.org/browse/ONOS-2723)] - Subnet NBI get with "id" returns an error
* [[ONOS-2724](https://jira.onosproject.org/browse/ONOS-2724)] - Fix bug of apply flowrule and remove flowrule
* [[ONOS-2732](https://jira.onosproject.org/browse/ONOS-2732)] - Unit Test TimeFormaterTest fails on some machines
* [[ONOS-2735](https://jira.onosproject.org/browse/ONOS-2735)] - Post a subnet,the getting json is diffrent from the post json.
* [[ONOS-2736](https://jira.onosproject.org/browse/ONOS-2736)] - The getting json from subnet lost two configurations
* [[ONOS-2749](https://jira.onosproject.org/browse/ONOS-2749)] - Subnet NBI get,allocation\_pools spell error:alloction
* [[ONOS-2750](https://jira.onosproject.org/browse/ONOS-2750)] - Add feature to onos-app-vtn
* [[ONOS-2751](https://jira.onosproject.org/browse/ONOS-2751)] - Add config of OpenVSwitchPipeline to onos-drivers.xml
* [[ONOS-2780](https://jira.onosproject.org/browse/ONOS-2780)] - IPv6 functionality broken and seeing NPE at ProxyArpManager in latest master
* [[ONOS-2793](https://jira.onosproject.org/browse/ONOS-2793)] - Links do not get added to the topology
* [[ONOS-2800](https://jira.onosproject.org/browse/ONOS-2800)] - ONOS shows empy/0.0.0.0 IPs
* [[ONOS-2806](https://jira.onosproject.org/browse/ONOS-2806)] - ONOS doesn't add the end option to DHCP packet in packet-outs
* [[ONOS-2807](https://jira.onosproject.org/browse/ONOS-2807)] - ONOS cannot de-serialize correctly an unknown IGMP packet
* [[ONOS-2808](https://jira.onosproject.org/browse/ONOS-2808)] - Problem parsing IPv6 neighbor discover packet
* [[ONOS-2812](https://jira.onosproject.org/browse/ONOS-2812)] - ONOS shows extra link both in the CLI and in the GUI.
* [[ONOS-2846](https://jira.onosproject.org/browse/ONOS-2846)] - Link Detection Inconsistent
* [[ONOS-2865](https://jira.onosproject.org/browse/ONOS-2865)] - NPE and devices reset on ONOS after a DHCP discover from host
* [[ONOS-2880](https://jira.onosproject.org/browse/ONOS-2880)] - NPE from LLDP Provider
* [[ONOS-2881](https://jira.onosproject.org/browse/ONOS-2881)] - DHCP app assigns address that looks like it is already in use
* [[ONOS-2893](https://jira.onosproject.org/browse/ONOS-2893)] - option file is missed in the tar.gz ONOS package
* [[ONOS-2896](https://jira.onosproject.org/browse/ONOS-2896)] - var folder doesn't exist in the tar.gz package. Logs are not posted until the folder gets manually created. The package should contain the var folder

## Epic

* [[ONOS-2287](https://jira.onosproject.org/browse/ONOS-2287)] - Implement PCEP Tunnel Provider Interfaces to support PCE initiated tunnel creation, tunnel release, tunnel update. Implement synchronization of tunnels in the network to ONOS through PCEP provider
* [[ONOS-2332](https://jira.onosproject.org/browse/ONOS-2332)] - this is part of the work for ONOSFW (short for ONOS framework) in OPNFV. In this subsystem, it will provide interface from ONOS to OpenStack Nuetron.

## Improvement

* [[ONOS-2789](https://jira.onosproject.org/browse/ONOS-2789)] - Add Korea map to ONOS
* [[ONOS-2797](https://jira.onosproject.org/browse/ONOS-2797)] - Add Australian map to ONOS
* [[ONOS-2894](https://jira.onosproject.org/browse/ONOS-2894)] - Since the upstart script is compatible with multiple system, the folder in the ONOS package should be renamed as something else (init?)
* [[ONOS-2895](https://jira.onosproject.org/browse/ONOS-2895)] - DEB and RPM packages should automatically craete a default user "sdn" if it's not already there

## New Feature

* [[ONOS-2483](https://jira.onosproject.org/browse/ONOS-2483)] - Check Master Balance CLI Driver
* [[ONOS-2551](https://jira.onosproject.org/browse/ONOS-2551)] - Add parameter for remove intent timeout
* [[ONOS-2574](https://jira.onosproject.org/browse/ONOS-2574)] - OVSDB Client Merge

## Story

* [[ONOS-102](https://jira.onosproject.org/browse/ONOS-102)] - Stylized login screen
* [[ONOS-452](https://jira.onosproject.org/browse/ONOS-452)] - Topology View: Provide other World Region backgrounds
* [[ONOS-466](https://jira.onosproject.org/browse/ONOS-466)] - FlowRules & Intent formatting in the CLI
* [[ONOS-671](https://jira.onosproject.org/browse/ONOS-671)] - Demonstrate hardware prototype
* [[ONOS-861](https://jira.onosproject.org/browse/ONOS-861)] - EdgePortService subsystem
* [[ONOS-1089](https://jira.onosproject.org/browse/ONOS-1089)] - Implement device resource manager
* [[ONOS-1091](https://jira.onosproject.org/browse/ONOS-1091)] - POC deployment
* [[ONOS-1144](https://jira.onosproject.org/browse/ONOS-1144)] - IpAddress.toString performance needs improvement
* [[ONOS-1147](https://jira.onosproject.org/browse/ONOS-1147)] - FlowRuleBatch\* classes should be removed from onos-api bundle
* [[ONOS-1159](https://jira.onosproject.org/browse/ONOS-1159)] - Secure ONOS Apache Karaf Container
* [[ONOS-1224](https://jira.onosproject.org/browse/ONOS-1224)] - Logout action
* [[ONOS-1244](https://jira.onosproject.org/browse/ONOS-1244)] - IPv6 Functionality Testing (Basic Sanity)
* [[ONOS-1320](https://jira.onosproject.org/browse/ONOS-1320)] - Component configuration event accumulation
* [[ONOS-1379](https://jira.onosproject.org/browse/ONOS-1379)] - As an operator I want to have RPM packages to easily install and deploy ONOS.
* [[ONOS-1437](https://jira.onosproject.org/browse/ONOS-1437)] - Implement MPLS BoS feature in ONOS API
* [[ONOS-1459](https://jira.onosproject.org/browse/ONOS-1459)] - Create TestON driver for ONOS REST commands
* [[ONOS-1507](https://jira.onosproject.org/browse/ONOS-1507)] - Support Calient fiber switch
* [[ONOS-1523](https://jira.onosproject.org/browse/ONOS-1523)] - POC integration testing
* [[ONOS-1533](https://jira.onosproject.org/browse/ONOS-1533)] - EdgePortService packet-out
* [[ONOS-1558](https://jira.onosproject.org/browse/ONOS-1558)] - Performance long test data logging and Jenkins Job automation
* [[ONOS-1571](https://jira.onosproject.org/browse/ONOS-1571)] - As an operator I want to have DEB packages to easly install and deploy ONOS.
* [[ONOS-1600](https://jira.onosproject.org/browse/ONOS-1600)] - Implement host mobility test scenario in Functionality test suite
* [[ONOS-1637](https://jira.onosproject.org/browse/ONOS-1637)] - Move/refactor helper link code to its own file
* [[ONOS-1639](https://jira.onosproject.org/browse/ONOS-1639)] - Test Applications for distributed building blocks
* [[ONOS-1749](https://jira.onosproject.org/browse/ONOS-1749)] - Devices view navigation to selected device
* [[ONOS-1778](https://jira.onosproject.org/browse/ONOS-1778)] - Refactor CHO
* [[ONOS-1787](https://jira.onosproject.org/browse/ONOS-1787)] - System test that can be triggered on new commits
* [[ONOS-1793](https://jira.onosproject.org/browse/ONOS-1793)] - Deprecate onos-core-trivial as a feature and move to src/test
* [[ONOS-1805](https://jira.onosproject.org/browse/ONOS-1805)] - Optical intents cannot be removed
* [[ONOS-1814](https://jira.onosproject.org/browse/ONOS-1814)] - Setup VPN connection to Ciena lab
* [[ONOS-1848](https://jira.onosproject.org/browse/ONOS-1848)] - Topology View Overlay: Title & Summary Pane
* [[ONOS-1849](https://jira.onosproject.org/browse/ONOS-1849)] - Topology View Overlay: Detail Pane
* [[ONOS-1914](https://jira.onosproject.org/browse/ONOS-1914)] - Add system tests for predictable handover of leadership
* [[ONOS-1918](https://jira.onosproject.org/browse/ONOS-1918)] - Add system tests for new AtomicCounter methods
* [[ONOS-1999](https://jira.onosproject.org/browse/ONOS-1999)] - Look at leaders candidate list in Functional and HA tests
* [[ONOS-2021](https://jira.onosproject.org/browse/ONOS-2021)] - Add a test to verify ONOS install (single & multi) via tar.gz file (Platform Test Suite)
* [[ONOS-2047](https://jira.onosproject.org/browse/ONOS-2047)] - Prepare ProxMox VM to run BGP router
* [[ONOS-2054](https://jira.onosproject.org/browse/ONOS-2054)] - Test and debug Fujitsu TL1 provider
* [[ONOS-2055](https://jira.onosproject.org/browse/ONOS-2055)] - Bidirectional flow rules for optical path
* [[ONOS-2057](https://jira.onosproject.org/browse/ONOS-2057)] - Test and debug Ciena TL1 provider
* [[ONOS-2064](https://jira.onosproject.org/browse/ONOS-2064)] - Topology Test suite
* [[ONOS-2067](https://jira.onosproject.org/browse/ONOS-2067)] - Port mapping constraints
* [[ONOS-2074](https://jira.onosproject.org/browse/ONOS-2074)] - App view - refactor all DOM manipulation into directives
* [[ONOS-2078](https://jira.onosproject.org/browse/ONOS-2078)] - Make link load factor in optical connectivity configurable
* [[ONOS-2081](https://jira.onosproject.org/browse/ONOS-2081)] - Integration tests of ProxMox VM, BGP router, and Corsa switch
* [[ONOS-2094](https://jira.onosproject.org/browse/ONOS-2094)] - add Mac and hostname to POST url
* [[ONOS-2096](https://jira.onosproject.org/browse/ONOS-2096)] - Let GUI support tunnel
* [[ONOS-2097](https://jira.onosproject.org/browse/ONOS-2097)] - Ensure updates made via TransactionalMap result in map update notifications
* [[ONOS-2102](https://jira.onosproject.org/browse/ONOS-2102)] - Allow creation of bidirectional optical intents on CLI
* [[ONOS-2108](https://jira.onosproject.org/browse/ONOS-2108)] - System tests for transactional map api - phase 1
* [[ONOS-2111](https://jira.onosproject.org/browse/ONOS-2111)] - This featue is about ONOSFW proposal in OPNFV
* [[ONOS-2116](https://jira.onosproject.org/browse/ONOS-2116)] - implementation of BridageConfig
* [[ONOS-2130](https://jira.onosproject.org/browse/ONOS-2130)] - Align device resources with link resources
* [[ONOS-2135](https://jira.onosproject.org/browse/ONOS-2135)] - Performance improvements with large topologies
* [[ONOS-2144](https://jira.onosproject.org/browse/ONOS-2144)] - Finish REST APIs for flows
* [[ONOS-2145](https://jira.onosproject.org/browse/ONOS-2145)] - PacketService cancelPackets for withdrawing intercept requests
* [[ONOS-2150](https://jira.onosproject.org/browse/ONOS-2150)] - Functionality Test Improvements using New Topology and test Template (Part-2)
* [[ONOS-2151](https://jira.onosproject.org/browse/ONOS-2151)] - REST API to get aggregate statistics for all flows traversing the given link.
* [[ONOS-2154](https://jira.onosproject.org/browse/ONOS-2154)] - Contribute our Loxi changes back upstream
* [[ONOS-2167](https://jira.onosproject.org/browse/ONOS-2167)] - Implement hosts REST API
* [[ONOS-2172](https://jira.onosproject.org/browse/ONOS-2172)] - Merge All Test on Production Test Beds
* [[ONOS-2181](https://jira.onosproject.org/browse/ONOS-2181)] - OVSDB Driver
* [[ONOS-2182](https://jira.onosproject.org/browse/ONOS-2182)] - Investigate how to approach multi-tenancy in ONOS
* [[ONOS-2186](https://jira.onosproject.org/browse/ONOS-2186)] - Topology View Overlay: split traffic visualization into its own overlay
* [[ONOS-2190](https://jira.onosproject.org/browse/ONOS-2190)] - Network configuration implementation
* [[ONOS-2191](https://jira.onosproject.org/browse/ONOS-2191)] - Meter Support and Service
* [[ONOS-2192](https://jira.onosproject.org/browse/ONOS-2192)] - Integrate ACL app submission
* [[ONOS-2194](https://jira.onosproject.org/browse/ONOS-2194)] - let SDN-IP to handle 600,000 routes - one onos/sdn-ip/bgp-speaker
* [[ONOS-2197](https://jira.onosproject.org/browse/ONOS-2197)] - Develop DHCP application as a builtin app
* [[ONOS-2204](https://jira.onosproject.org/browse/ONOS-2204)] - let SDN-IP to handle 600,000 routes - multiple onos/sdn-ip/bgp-speaker
* [[ONOS-2226](https://jira.onosproject.org/browse/ONOS-2226)] - Complete REST API for Intents
* [[ONOS-2229](https://jira.onosproject.org/browse/ONOS-2229)] - Refactor resource management mechanism
* [[ONOS-2230](https://jira.onosproject.org/browse/ONOS-2230)] - Introduce composition at flow objective layer
* [[ONOS-2236](https://jira.onosproject.org/browse/ONOS-2236)] - Re-deploy CORD according to original design
* [[ONOS-2240](https://jira.onosproject.org/browse/ONOS-2240)] - Investigate OTN multiplexing support
* [[ONOS-2257](https://jira.onosproject.org/browse/ONOS-2257)] - the implementation of OvsdbAgent
* [[ONOS-2259](https://jira.onosproject.org/browse/ONOS-2259)] - the implementation of OvsdbClientService
* [[ONOS-2278](https://jira.onosproject.org/browse/ONOS-2278)] - Test suite for OVSDB functionality
* [[ONOS-2283](https://jira.onosproject.org/browse/ONOS-2283)] - Scale up/down network topology test (Scalability test)
* [[ONOS-2301](https://jira.onosproject.org/browse/ONOS-2301)] - Refactor start up template test
* [[ONOS-2305](https://jira.onosproject.org/browse/ONOS-2305)] - ACORD Fabric Design
* [[ONOS-2307](https://jira.onosproject.org/browse/ONOS-2307)] - Discuss with KREONET/KISTI the deployment scenario/plan
* [[ONOS-2316](https://jira.onosproject.org/browse/ONOS-2316)] - ACORD PoC Lab Setup Design
* [[ONOS-2317](https://jira.onosproject.org/browse/ONOS-2317)] - ONOS REST APIs to be integrated with ACORD framework
* [[ONOS-2319](https://jira.onosproject.org/browse/ONOS-2319)] - ACORD PoC Scope finalization
* [[ONOS-2320](https://jira.onosproject.org/browse/ONOS-2320)] - SDN-IP porting to new net config framework
* [[ONOS-2324](https://jira.onosproject.org/browse/ONOS-2324)] - Create OFTests for OLT functionality
* [[ONOS-2328](https://jira.onosproject.org/browse/ONOS-2328)] - Topology View - Multiple Links between devices should be shown spread out
* [[ONOS-2333](https://jira.onosproject.org/browse/ONOS-2333)] - REST API from ONOS to ML2 in Neutron
* [[ONOS-2334](https://jira.onosproject.org/browse/ONOS-2334)] - VTN API
* [[ONOS-2335](https://jira.onosproject.org/browse/ONOS-2335)] - Provision VxLAN though Tunnel Manager - Create
* [[ONOS-2336](https://jira.onosproject.org/browse/ONOS-2336)] - Modify driver connect function (and some related function) to all drivers
* [[ONOS-2340](https://jira.onosproject.org/browse/ONOS-2340)] - Implement PCEP Protocol Request and Response message mapping with PCC
* [[ONOS-2341](https://jira.onosproject.org/browse/ONOS-2341)] - Implement PCE-Initiate message protocol parsing, encoding, decoding
* [[ONOS-2342](https://jira.onosproject.org/browse/ONOS-2342)] - Implement PCE LSP Update message protocol parsing, encoding, decoding
* [[ONOS-2343](https://jira.onosproject.org/browse/ONOS-2343)] - Implement PCC to PCE LSP Status Update message protocol parsing, encoding, decoding
* [[ONOS-2344](https://jira.onosproject.org/browse/ONOS-2344)] - Implement PCE Report message
* [[ONOS-2345](https://jira.onosproject.org/browse/ONOS-2345)] - Implement PCEP Stateful capability
* [[ONOS-2346](https://jira.onosproject.org/browse/ONOS-2346)] - Implement PCE-Open message protocol parsing, encoding, decoding
* [[ONOS-2347](https://jira.onosproject.org/browse/ONOS-2347)] - Implement PCE-Close message protocol parsing, encoding, decoding
* [[ONOS-2348](https://jira.onosproject.org/browse/ONOS-2348)] - Implement PCE-KeepAlive message protocol parsing, encoding, decoding
* [[ONOS-2349](https://jira.onosproject.org/browse/ONOS-2349)] - Implement PCE Error message protocol parsing, encoding, decoding
* [[ONOS-2350](https://jira.onosproject.org/browse/ONOS-2350)] - Implement PCE Openwait timer, KeepWait timer, KeepAlive timer and Dead timer in PCE server
* [[ONOS-2351](https://jira.onosproject.org/browse/ONOS-2351)] - Implement the PCE initiated create tunnel flow between PCE and PCC
* [[ONOS-2352](https://jira.onosproject.org/browse/ONOS-2352)] - Implement the PCE open message flow between PCE and PCC
* [[ONOS-2354](https://jira.onosproject.org/browse/ONOS-2354)] - Implement the PCE Initiated update tunnel flow between PCE and PCC
* [[ONOS-2355](https://jira.onosproject.org/browse/ONOS-2355)] - Implement the PCE report LSP status flow between PCC and PCE
* [[ONOS-2356](https://jira.onosproject.org/browse/ONOS-2356)] - Implement the PCE Label update between PCE and PCC
* [[ONOS-2357](https://jira.onosproject.org/browse/ONOS-2357)] - Implement the PCE Label Reserve message between PCE and PCC
* [[ONOS-2358](https://jira.onosproject.org/browse/ONOS-2358)] - Implement the PCE Label update message parsing, encoding and decoding
* [[ONOS-2359](https://jira.onosproject.org/browse/ONOS-2359)] - Implement the PCE label reserve message parsing, encoding and decoding
* [[ONOS-2360](https://jira.onosproject.org/browse/ONOS-2360)] - Implement the PCE TE Report message parsing, encoding and decoding
* [[ONOS-2361](https://jira.onosproject.org/browse/ONOS-2361)] - Implement the PCEP Tunnel provider to PCEP Tunnel Provider Service interactions
* [[ONOS-2362](https://jira.onosproject.org/browse/ONOS-2362)] - Implement the PCEP Tunnel API Mapper
* [[ONOS-2363](https://jira.onosproject.org/browse/ONOS-2363)] - Unit test code for the PCE protocol messages
* [[ONOS-2364](https://jira.onosproject.org/browse/ONOS-2364)] - Unit test code for the PCE Controller and Channel Handler
* [[ONOS-2365](https://jira.onosproject.org/browse/ONOS-2365)] - Unit test code for the PCEP create, update and delete tunnel code
* [[ONOS-2366](https://jira.onosproject.org/browse/ONOS-2366)] - Integration testing of PCE with PCC (Stub test code) for session establishment
* [[ONOS-2367](https://jira.onosproject.org/browse/ONOS-2367)] - Integration testing of PCE with PCC (Stub test code) for session management
* [[ONOS-2368](https://jira.onosproject.org/browse/ONOS-2368)] - Integration testing of PCE with PCC (Stub test code) for tunnel creation, deletion and updation
* [[ONOS-2369](https://jira.onosproject.org/browse/ONOS-2369)] - Integration testing of PCE with PCC (Stub test code) for tunnel learning and TE link learning
* [[ONOS-2370](https://jira.onosproject.org/browse/ONOS-2370)] - Integration testing of PCE with PCC for Label update message
* [[ONOS-2371](https://jira.onosproject.org/browse/ONOS-2371)] - Documentation work for the Implementation of PCEP Tunnel Provider
* [[ONOS-2372](https://jira.onosproject.org/browse/ONOS-2372)] - Implement the delete tunnel flow between PCE and PCC
* [[ONOS-2376](https://jira.onosproject.org/browse/ONOS-2376)] - modify WiKi to reflect new testing env
* [[ONOS-2384](https://jira.onosproject.org/browse/ONOS-2384)] - Add OpenVSwitchPipeline.java
* [[ONOS-2385](https://jira.onosproject.org/browse/ONOS-2385)] - Topology View -- 5 or more links between devices should number how many there are
* [[ONOS-2391](https://jira.onosproject.org/browse/ONOS-2391)] - Rebuild TopoPerfNext for production platform, portability and stability
* [[ONOS-2392](https://jira.onosproject.org/browse/ONOS-2392)] - Scale and Performance Test - scale topology move to Production
* [[ONOS-2394](https://jira.onosproject.org/browse/ONOS-2394)] - Test in-band management for OLT
* [[ONOS-2395](https://jira.onosproject.org/browse/ONOS-2395)] - Add remaining old functionality to new intent functionality test suite
* [[ONOS-2399](https://jira.onosproject.org/browse/ONOS-2399)] - Check for Changes in Intent Partitions in FUNCintent
* [[ONOS-2411](https://jira.onosproject.org/browse/ONOS-2411)] - REST API Testing - Intent framework
* [[ONOS-2424](https://jira.onosproject.org/browse/ONOS-2424)] - Move Mininet flows related functions from remotemininetdriver to mininetdriver
* [[ONOS-2427](https://jira.onosproject.org/browse/ONOS-2427)] - Create a setup.py with setuptools requirments.txt or setup.sh for TESTON framework
* [[ONOS-2429](https://jira.onosproject.org/browse/ONOS-2429)] - Add support for a weak consistency read option for ConsistentMap
* [[ONOS-2430](https://jira.onosproject.org/browse/ONOS-2430)] - Create system tests for using .oar files
* [[ONOS-2431](https://jira.onosproject.org/browse/ONOS-2431)] - NetworkConfig subsystem unit tests
* [[ONOS-2438](https://jira.onosproject.org/browse/ONOS-2438)] - Scale Test on number of intents/number of FlowRules onos handles
* [[ONOS-2440](https://jira.onosproject.org/browse/ONOS-2440)] - Rework DistributedQueue notification mechanism to take advantage of gauranteed database change notifications
* [[ONOS-2442](https://jira.onosproject.org/browse/ONOS-2442)] - CHO Test enhancements
* [[ONOS-2446](https://jira.onosproject.org/browse/ONOS-2446)] - API to declare resource hierarchy
* [[ONOS-2448](https://jira.onosproject.org/browse/ONOS-2448)] - Automatic tracking of addition/removal resources
* [[ONOS-2453](https://jira.onosproject.org/browse/ONOS-2453)] - Instantiate on GEANT GTS two external routers and two clients
* [[ONOS-2455](https://jira.onosproject.org/browse/ONOS-2455)] - Investigation on OpenStack Ceilometer framework
* [[ONOS-2457](https://jira.onosproject.org/browse/ONOS-2457)] - Integration of OpenStack Ceilometer with ONOS for Network related statistics
* [[ONOS-2459](https://jira.onosproject.org/browse/ONOS-2459)] - Integrate OpenStack Ceilometer with CORD Residential service components (OLT, CPE, BNG)
* [[ONOS-2464](https://jira.onosproject.org/browse/ONOS-2464)] - let SDN-IP to handle large topology size with 600,000 routes
* [[ONOS-2471](https://jira.onosproject.org/browse/ONOS-2471)] - Create a new test called FUNCintentRest
* [[ONOS-2482](https://jira.onosproject.org/browse/ONOS-2482)] - Huawei OVSDB test -level 1
* [[ONOS-2486](https://jira.onosproject.org/browse/ONOS-2486)] - REST API documentation via Swagger UI
* [[ONOS-2487](https://jira.onosproject.org/browse/ONOS-2487)] - Refactor various managers atop AbstractListenerRegistry base
* [[ONOS-2492](https://jira.onosproject.org/browse/ONOS-2492)] - Logging exception case in FUNCintent
* [[ONOS-2513](https://jira.onosproject.org/browse/ONOS-2513)] - Modify the semantic of MP2SP intents introducting the partially failed state
* [[ONOS-2515](https://jira.onosproject.org/browse/ONOS-2515)] - Deploy ONOS 1.3 on ON.Lab network
* [[ONOS-2520](https://jira.onosproject.org/browse/ONOS-2520)] - Add REST API driver functions for flows
* [[ONOS-2523](https://jira.onosproject.org/browse/ONOS-2523)] - Upgrade the ON.Lab virtual infrastructure
* [[ONOS-2542](https://jira.onosproject.org/browse/ONOS-2542)] - Migrate SDN-IP tests to the new QA test suite
* [[ONOS-2553](https://jira.onosproject.org/browse/ONOS-2553)] - Stats website: refactor the code to return json to the frontend
* [[ONOS-2557](https://jira.onosproject.org/browse/ONOS-2557)] - Stats website: investigate on statistics not collected from cdn server in July
* [[ONOS-2577](https://jira.onosproject.org/browse/ONOS-2577)] - Basic assessment ONOS 1.3 on the ON.Lab local network (basic config and check that works).
* [[ONOS-2585](https://jira.onosproject.org/browse/ONOS-2585)] - CHOtest Enhancements (Sprint-3 Drake)
* [[ONOS-2632](https://jira.onosproject.org/browse/ONOS-2632)] - OF-DPA 2.0 pipeline testing
* [[ONOS-2647](https://jira.onosproject.org/browse/ONOS-2647)] - Investigate Ceilometer framework for Notification based data collection
* [[ONOS-2650](https://jira.onosproject.org/browse/ONOS-2650)] - Make Ceilometer framework use MongoDB running in a independent XOS slice instead of head node
* [[ONOS-2666](https://jira.onosproject.org/browse/ONOS-2666)] - Single Virtual IP for Ceilometer to contact in Multi ONOS Instance deployment
* [[ONOS-2668](https://jira.onosproject.org/browse/ONOS-2668)] - XOS Monitoring Dashboard for visualization of meters
* [[ONOS-2669](https://jira.onosproject.org/browse/ONOS-2669)] - vOLT meters to be integrated into Ceilometer framework
* [[ONOS-2672](https://jira.onosproject.org/browse/ONOS-2672)] - vCPE meters to be integrated into Ceilometer framework
* [[ONOS-2675](https://jira.onosproject.org/browse/ONOS-2675)] - vBNG meters to be integrated into Ceilometer framework
* [[ONOS-2683](https://jira.onosproject.org/browse/ONOS-2683)] - Topology View Overlay: Link Rendering
* [[ONOS-2726](https://jira.onosproject.org/browse/ONOS-2726)] - Register VLAN as resource against a link
* [[ONOS-2727](https://jira.onosproject.org/browse/ONOS-2727)] - Register MPLS as resource against a link
* [[ONOS-2734](https://jira.onosproject.org/browse/ONOS-2734)] - Verify IPv6 tests submitted by Critreion and move to production cluster
* [[ONOS-2744](https://jira.onosproject.org/browse/ONOS-2744)] - Floating ONOS cluster IP address
* [[ONOS-2778](https://jira.onosproject.org/browse/ONOS-2778)] - TestON function to skip the rest of a test case
* [[ONOS-2782](https://jira.onosproject.org/browse/ONOS-2782)] - Wiki posting of Test results for Drake release (FUNC, HA, PERF, SCALE, OVSDB, IPV6 & CHO)
* [[ONOS-2792](https://jira.onosproject.org/browse/ONOS-2792)] - Update ProdCHO Jenkins job to use Suibin's new build variables
* [[ONOS-2811](https://jira.onosproject.org/browse/ONOS-2811)] - Build the new storage server for ON.Lab local network
* [[ONOS-2882](https://jira.onosproject.org/browse/ONOS-2882)] - Migrate all local ON.Lab VMs to the new shared storage
* [[ONOS-2884](https://jira.onosproject.org/browse/ONOS-2884)] - Migrate all local ON.Lab containers to the new shared storage
* [[ONOS-2887](https://jira.onosproject.org/browse/ONOS-2887)] - Install Nagios to monitor the local network infrastructure of ON.Lab
* [[ONOS-2906](https://jira.onosproject.org/browse/ONOS-2906)] - Allocate new set of 3 VMs for Madan

## Task

* [[ONOS-2002](https://jira.onosproject.org/browse/ONOS-2002)] - Write cli driver for the command onos:maps
* [[ONOS-2288](https://jira.onosproject.org/browse/ONOS-2288)] - Implement PCEP Tunnel provider interface. Support interfaces such as setup tunnel, release tunnel, update tunnel. Also support response APIs such as tunnel created, tunnel updated, tunnel deleted to PCEP Tunnel Service
* [[ONOS-2289](https://jira.onosproject.org/browse/ONOS-2289)] - Implement the PCEP communication between ONOS PCE Server and the PCE client on device using PCEP protocol messages on TCP/IP socket.
* [[ONOS-2401](https://jira.onosproject.org/browse/ONOS-2401)] - Separate Jenkins test and post jobs
* [[ONOS-2581](https://jira.onosproject.org/browse/ONOS-2581)] - Add codec for tunnel ID
* [[ONOS-2584](https://jira.onosproject.org/browse/ONOS-2584)] - create Jenkins job on OVSDB level-1 test
* [[ONOS-2634](https://jira.onosproject.org/browse/ONOS-2634)] - Review the Implementation and unit test code for PCEP label update message.
* [[ONOS-2635](https://jira.onosproject.org/browse/ONOS-2635)] - Review the Implementation of PcInitate and PcUpdate messages
* [[ONOS-2636](https://jira.onosproject.org/browse/ONOS-2636)] - Review of Implementation of PCEP report messages and unit test code
* [[ONOS-2637](https://jira.onosproject.org/browse/ONOS-2637)] - Review of Implementation of unit test code for PCEP OPEN and ERROR Messages.
* [[ONOS-2638](https://jira.onosproject.org/browse/ONOS-2638)] - Review of Unit test code for PcepTunnelProvider
* [[ONOS-2639](https://jira.onosproject.org/browse/ONOS-2639)] - Review of Implementation of PCEP LabelReserve message
* [[ONOS-2640](https://jira.onosproject.org/browse/ONOS-2640)] - Review of implementation of PCEP TE Report message.
* [[ONOS-2641](https://jira.onosproject.org/browse/ONOS-2641)] - Review of Pcep TunnelProvider implementation
* [[ONOS-2642](https://jira.onosproject.org/browse/ONOS-2642)] - Review of Pcep Controller and PCEP Channel Handler
* [[ONOS-2836](https://jira.onosproject.org/browse/ONOS-2836)] - Define a IPTable class providing the rules in IP table
* [[ONOS-2891](https://jira.onosproject.org/browse/ONOS-2891)] - change line separator
