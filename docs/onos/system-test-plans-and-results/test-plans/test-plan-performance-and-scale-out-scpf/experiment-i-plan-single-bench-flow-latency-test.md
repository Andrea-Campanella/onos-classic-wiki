# Experiment I Plan - Single Bench Flow Latency Test

### Goals:

This test measures the latency and rate when installing and deleting flows via REST API of ONOS. This is an end-to-end performance test from a REST API all the way down to the network.

### Setup and Method:

Currently we only run a single-instance case for this test. We set up a Mininet topology with 63 switches and create 100k flows. The flows are divided into 500 batches with 200 flows per batch. Then we start to posting all the flows to ONOS with multi-threads via REST API. After all the posting, we start to check periodically whether all the flows are added to the switches, and this is done by making sure that none of the flows is in PENDING state. The end-to-end flow add latency is comprised of two parts:

* elapse\_post: beginning of this period is the time when we start posting, and the end is when we finish all the posting.
* post\_to\_confirm: the period starts after all posting jobs finish, and ends when we confirm that all the flows have been added to the data plane.

Similarly, for flow deletion we also measure the latency from posting the deletion requests to all flow deletions are confirmed in the data plane. The latency also contain the following two time slots:

* elapse\_del: beginning of this period is the time when we start posting the deletion requests, and the end is when we finish all the posting.
* del\_to\_confirm: the period starts after all posting jobs finish, and ends when we confirm that all the flows have been removed from the data plane.
