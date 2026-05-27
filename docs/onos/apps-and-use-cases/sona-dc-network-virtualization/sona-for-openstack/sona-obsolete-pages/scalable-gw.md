# Scalable GW

A gateway in SONA is a special compute node, which plays role as a connection point to external networks. It performs NAT and PAT for outbound traffics and also exchanges routes with external routers with BGP or OSPF. Scalable gateway provides load balancing and high availability by allowing multiple redundant gateways to the system.

## **Features**

* Provides load balance of outbound traffics among multiple gateways
* Provides fail-over for a gateway failure
* Provides dynamic add or remove of gateway nodes

## **High Level Architecture**

**![](../../../../../assets/screen-shot-2016-04-25-at-12.33.37-pm.png)**

SONA is composed of multiple ONOS applications, and **Scalable Gateway** and **vRouter** are in charge of the North-South connectivity.

![](../../../../../assets/screen-shot-2016-04-25-at-12.10.07-pm.png)

* Scalable Gateway provides a gateway group to OpenstackRouting
* OpenstackRouting takes care of forwarding outbound traffic to the gateway group
* OpenstackRouting takes care of NAT/PAT at the gateways
* vRouter takes care of connectivity between GNODEs and external routers

![](../../../../../assets/screen-shot-2016-04-25-at-12.25.13-pm.png)

* GNODE is composed of two software switches controlled by SONA and vRouter
* br-int which is controlled by SONA, OpenstackRouting module specifically, performs NAT and PAT for N-S packets
* br-router which is controlled by vRouter makes the GNODE as a legacy router and it performs forwarding packets to right port

## **Detailed Architecture**

**![](https://lh6.googleusercontent.com/8C-CgVS5CTPIuXhxf6Kjyd0ONSB6ZOnm_g6sAqdybBG4NHPcJVfiYsBtmL596gnGtUd-X1oId06628EjB7FlPIaz6fwacIx6z7oFw0Kh1UZ48QcAsg40hRpTa7P3McMvjXOz60oze0w)**

* Scalable GW manages the information of GNODEs
* OpenstackRouting requests the information of GNODEs
* Scalable GW provides the load-balancing policy to OpenstackRouting
* Scalable GW handles GNODE fail-over and scale-out

### Upstream Traffic Load Balancing

![](https://lh4.googleusercontent.com/zx--g2beigLII1Ho20o5U8yPc6FkC3uhiBiR3wzvCe_XOLzYInv_LoDQ-MVxGXTcv4UPUVHKi4gevx2yWLFjgedl-wEnO5QbHLyGJooUH1Q010uhr7NK4EXPjUTMONidPuYQOqda34U)

### Gateway Node Fail-Over

![](https://lh3.googleusercontent.com/lmoJOILZH-urfiWlFiOvHlttMhDg4x_-M2cAl6rLUQdXi_A_YpuGyFL5klLKNvR9IlXRdS8hCH0t4oPfpEChHyLtY5gEPrAoGhy0yp-F-t7s_QHuIFwWvciRP2oRyJDbjfIoEVGsDKU)

### Dynamic Gateway Node Scale-Out

![](https://lh3.googleusercontent.com/rRvcMVA5PoYdkxQOBk1qwk3XPdJfE5CQHvuLM5fVYW9S8bmgzeAiQG6OwyaJHREunMjuzsRrDdEIik4YTHbEEt5VNFF39SzcFZYCFJZfcQoJG2-DVAKlH9z4S7D5WZtBqt-bD8oVONw)
