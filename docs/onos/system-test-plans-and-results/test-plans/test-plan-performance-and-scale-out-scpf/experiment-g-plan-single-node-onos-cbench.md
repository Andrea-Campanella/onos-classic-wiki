# Experiment G Plan - Single-node ONOS Cbench

### Goals:

It is important to measure how quick an SDN controller processes and responds to packet-in messages sent from OpenFlow switches. In this test we use Cbench as the tool to measure packet-out rate of ONOS.

### Setup and Method:

We start a single-node ONOS and run Cbench on the same machine. We activate "fwd" app which responds to packet-in messages. The Cbench command we run is:

```
cbench -c localhost -p 6633 -m 1000 -l 70 -s 16 -M 100000 -w 10 -D 5000 -t
```

* "-m 1000" means 1000 ms per test
* "-l 70" means 70 loops
* "-s 16" means simulating 16 switches
* "-M 100000" means 100000 unique MAC addresses per switch
* "-w 10" means 10 warmups
* "-D 5000" means 5 seconds delay after received features\_reply messages
