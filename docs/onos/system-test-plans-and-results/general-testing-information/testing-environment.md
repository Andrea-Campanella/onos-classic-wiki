# Testing Environment

## SCPF and USECASE Tests

A 7-node bare-metal server cluster is set aside for all the experiments. Each server has the following specs:

* Dual Intel Xeon E5-2670v2 2.5GHz Processors - 10 real cores/20 hyper-threaded cores per processor.
* 32GB 1600MHz DDR3 DRAM.
* 1Gbps Network interface card.
* Ubuntu 14.04.5 OS.
* Time synchronization amongst cluster nodes using ptpd.

ONOS specific software environment includes:

* Java HotSpot(TM) 64-Bit Server VM; version 1.8.0\_31
* JAVA\_OPTS="${JAVA\_OPTS:--Xms8G -Xmx8G}"
* Additional case-specific ONOS parameters to be described in specific case.

## FUNC and HA Tests

Nodes:

* (1x) 1 Mininet Node + 7 ONOS Nodes

Each node contains the following specifications:

* AMD 2.0GHz Processor - 4 cores
* 8GB DIMM RAM
* Ubuntu 16.04.3 OS

## Segment Routing Tests

Nodes:

* (3x) 1 Mininet Node + 4 ONOS Nodes
* (1x) 1 Mininet Node + 7 ONOS Nodes

Each physical server and all nodes in the same cluster share the following specifications:

* Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz - 32 cores
* 200GB DDR4 RAM
* Ubuntu 16.04.4 OS

## CHO Tests

Nodes:

* (1x) 1 Mininet Node + 3 ONOS Nodes

Each node contains the following specifications:

* AMD 2.0GHz Processor - 4 cores
* 6GB DIMM RAM
* Ubuntu 14.04 OS

## CHO Tests with Hardware Switches

Nodes:

* (1x) 1 Test station + 3 ONOS Nodes

Switches:

* (6x) Accton AS5912-54x
* (2x) Accton AS7712-32X
* (2x) x86-64-accton-as6712-32x-r0
