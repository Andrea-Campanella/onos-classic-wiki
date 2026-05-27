# RR+

## Team

|  |  |  |
| --- | --- | --- |
| Li Zhenbin | Huawei | [lizhenbin@huawei.com](mailto:lizhenbin@huawei.com) |
| Jiang Rui | Huawei | [henry.jiangrui@huawei.com](mailto:henry.jiangrui@huawei.com) |
| Lu Kai | Huawei | [lukai1@huawei.com](mailto:xushiping7@huawei.com) |
| Name | Organization | Email |
| --- | --- | --- |

## RR+ Introduction

On a traditional IP network, devices calculate their respective paths in a dynamic and distributed manner. The entire network is divided into multiple antonomous systems(ASs), andan Interior Gateway Protocol(IGP) runs on the devices within each AS. The IGP enables devices within an AS to obtaiin the instra-AS network topology and use the same algorithm to calculate routes. Devices in different ASs use Border Gateway Protocol(BGP) to exchange routes. If a link or device fails, the IP network layer triggers route convergence to protect data traffic. However, if you want to manually optimize traffic paths on a traditional IP network, you will encounter the following difficulties.

1. Network traffic cannot be globally adjusted. Traffic can only be partially adjusted device by device, and the real-time effects of traffic adjustment cannot be previewed.
2. The configuration workload is heavy. All routers that the traffic traverses need to be configured.
3. High maintenance skills are required and a quick response to traffic changes cannot be made. After configuring routing policies, you have to observe traffic distribution to determine whether the traffic path are adjusted correctly, In addition, you can respond to traffic distribution changes only after observing these changes.
4. The network maintainablity is poor.The routing policies used to control network routes are complex, posing difficulties to subsequent maintenance.

To address the preceding issues and improve bandwidth usage and service quality, the SDN-based RR+ solution is introduced. The solution not only enables VIP traffic to be reliably transmitted, but also enables traffic to be evenly shared among links to improve bandwidth usage.
