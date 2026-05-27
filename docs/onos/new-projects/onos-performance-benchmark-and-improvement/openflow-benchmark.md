# OpenFlow Benchmark

# Overview

      OpenFlow has a special significance in the SDN process. The following is concerned with the performance of OpenFlow, including the session capacity, Topo performance, cluster mechanism, Packet\_out and Flow\_mod rate as well as the performance of Datapath(Currently ONOS does not support Auxiliary Channels).

      In order to more accurately measure the SDN controller’s OpenFlow protocol performance, we use IXIA commercial tester directly connected to controllers by TCP connection. And we refered to ONF and IETF and BII test methods and use cases.

      We also focus on cluster-related testing, most of the tests below contains single controller mode and cluster controller mode.

      All of the tests based on packet capture, by analyzing the captured messages, we can more accurately obtain the required information. And this makes the results more reliable.The details are described in each use case below.

      In order to truly reflect the performance of the controller, we carry out each test case only to load the necessary features. And in the implementation of the use case test, each done a test, we will clean all the configuration, including IxNetwork and controllers to ensure that each test environment is the same.

      Through the following test methods, not only can measure the performance of ONOS, ODL can also be measured results. In other words, these methods can be used to test SDN controller performance. However, the protocol implementation of different controllers may be different, resulting in the test process may not be too smooth, such as the ODL Datapath test with IxNetwork, Datapath can not be successfully setup.

# Environment

* **Hardware**

  Cpu：E5-2620 v2 @ 2.10GHz \* 2 \* 12

  Ram：96 GB

  Nic：BCM5719 Gigabit Ethernet PCIe \* 4

  Rigid disk：2TB \* 4

  Model：Huawei Tecal RH1288 v2

* **Software**

  OS：Ubuntu 14.04.4 LTS

  Onos：1.6.0

  Karaf：apache-karaf-3.0.7

  Java：1.8.0\_111

  IxNetwork：IxNetwork 8.10.1046.6 EA (patch：8.10.1608.48,8.10-EA-Update(2))
* **Topo**

  **![](http://mail.163.com/js6/s?func=mbox:getMessageData&sid=FAkvSzKQCAcnbMBLOLQQoPxjvSQwOCjJ&mid=178:1tbish2I6VUL+ptR8wAAsT&part=3)**

# Testcases

**[Test 1：OpenFlow Channel Capacity](openflow-benchmark/test-1openflow-channel-capacity.md)**

**[Test 2：OpenFlow Topo Capacity](openflow-benchmark/test-2openflow-topo-capacity.md)**

**[Test 3：The Role Intimation Time for Controller Cluster At Setup](openflow-benchmark/test-3the-role-intimation-time-for-controller-cluster-at-setup.md)**

**[Test 4：Master-Slave Recovery Time for Controller Cluster](openflow-benchmark/test-4master-slave-recovery-time-for-controller-cluster.md)**

**[Test 5：The Role Intimation Time for Controller Cluster After Master Failover](openflow-benchmark/test-5the-role-intimation-time-for-controller-cluster-after-master-failover.md)**

**[Test 6：Packet Out Rate Performance](openflow-benchmark/test-6packet-out-rate-performance.md)**

**[Test 7：Flow Setup Rate at Reactive Mode](openflow-benchmark/test-7flow-setup-rate-at-reactive-mode.md)**

**[Test 8：Flow Setup Rate at Proactive Mode](openflow-benchmark/test-8flow-setup-rate-at-proactive-mode.md)**

**[Test 10：End-to-End Flow Setup Time](openflow-benchmark/test-10end-to-end-flow-setup-time.md)**

**[Test 11：Datapath Failure Recovery Time](openflow-benchmark/test-11datapath-failure-recovery-time.md)**
