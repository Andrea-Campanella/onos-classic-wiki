# Master: Experiment D - Intents Operations Throughput

System Env:

* Server: Dual XeonE5-2670 v2 2.5GHz; 64GB DDR3; 512GB SSD
* 1Gbps NIC
* JAVA\_OPTS="${JAVA\_OPTS:--Xms8G -Xmx8G}"

ONOS Apps:

* drivers, null, intentperf

ONOS Config:

* cfg set org.onosproject.net.intent.impl.compiler.IntentConfigurableRegistrator useFlowObjectives true (when using flow objective intents compiler)
* cfg set org.onosproject.net.intent.impl.IntentManager skipReleaseResourcesOnWithdrawal true

"Constant-Load" Test Conditions:

* NumKeys - 40000, with Flow Obj - 4000

Note:

* Following graphs include results using flow rule stores with both strong consistency and eventual consistency models. The ONOS team is still working on performance improvements for flow rule store with strong consistency.

![](../../../../../assets/unknown-macro-5.png)

![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPFintentEventTp_master_no-neighbors_OldFlow_graph.jpg)![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPFintentEventTp_master_all-neighbors_OldFlow_graph.jpg)

![](../../../../../assets/unknown-macro-5.png)

![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPFintentEventTpWithFlowObj_master_no-neighbors_flowObj_OldFlow_graph.jpg)![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPFintentEventTpWithFlowObj_master_all-neighbors_flowObj_OldFlow_graph.jpg)
