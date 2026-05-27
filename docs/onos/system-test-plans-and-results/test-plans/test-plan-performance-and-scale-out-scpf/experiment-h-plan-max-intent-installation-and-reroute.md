# Experiment H Plan - Max Intent Installation and ReRoute

### Goals:

The goal of this test is to measure intent installation and reroute capacity of ONOS. We divide the test into two sub tests: max intent installation test aims to find out how many intents can be installed on ONOS, and max intent reroute test aims to find out the maximum number of intents that can be successfully rerouted by ONOS.

### Setup and Method:

We scale up ONOS from 1 node to 3,5,7 nodes. For a specific ONOS scale, we set up a Mininet reroute topology with 8 switches, assign them to ONOS cluster and balance mastership. Then we use "push-test-intents" CLI command to install intents to ONOS. Each time we push a batch of intents to ONOS for installation, we check whether all the intents and related flows are correctly installed. If yes, we continue to push the next intent batch, otherwise we stop the test and regard the current intent number as the capacity of intent installation.

TBD: Max Intent Reroute method

| Sub Tests | Description | Roadmap |
| --- | --- | --- |
| Max Intent Installation | Measure maximum number of intents that can be installed by ONOS | now |
| Max Intent Reroute | Measure maximum number of intents that can be successfully rerouted by ONOS | 1.8 or later |
