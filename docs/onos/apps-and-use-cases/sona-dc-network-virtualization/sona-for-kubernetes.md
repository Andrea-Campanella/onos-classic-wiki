# SONA for Kubernetes

# SONA-CNI for Kubernetes

1. An extension work of SONA
   1. SONA originally aims to support OpenStack network only
   2. With SONA-CNI, SONA starts to support Kubernetes Network as well
2. A pure SDN based overlay solution
   1. NOT rely on kube-proxy → OpenvSwitch handles L3 load balancing
   2. NOT rely on iptables or IPVS → OpenvSwitch handles L2/L3 connectivity
3. Support all Kubernetes networking models
   1. POD IP
   2. Service IP (Cluster IP)
   3. NodePort
   4. Network Policy
4. Fully compatible with Kubernetes CNI, no changes to Kubernetes
5. Support multiple tunneling protocols
   1. VxLAN, GRE and GENEVE
6. Aim provide line-rate performance
   1. Leverages ovs-dpdk or SmartNIC (OVS embedded) Dada-Plane Acceleration (DPA) technologies
7. Provide container to container traffic visibility (TODO)
   1. Telemetry, vTap, etc.
8. Minimum requirements
   1. OpenvSwitch 2.6.X with Kernel module installed (ConnTrack, Stateful NAT)
   2. ONOS 1.15 latest
9. Supported OS
   1. CentOS, RHEL
   2. Ubuntu
