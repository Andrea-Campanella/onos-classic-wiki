# Deploy SONA using Kubernetes Helm Chart

It explains how to deploy SONA using Kubernetes and Helm Chart.

Please note that it is tested with ONOS 1.13.x, and it is NOT tested with 1.14.x version, where ONOS has been separated from Atomix.

SONA helm chart for ONOS 1.14.x will be also available soon.

## **Prerequisite**

### Install Kubernetes

There are many ways to install kubernetes. But, I recommend to use kubespary.

<https://github.com/kubernetes-incubator/kubespray>

### Install Helm

Please refer to <https://docs.helm.sh/using_helm/#installing-helm> to install helm

## **Configuring Kubernetes environment**

SONA is exposed as a service to OpenStack, and SONA itself also uses a service for cluster manager. Therefore, we need to configuration Kubernetes environment to resolve the service.

Please add the following part in head file of resolve.conf (/etc/resolvconf/resolv.conf.d/head)

```
nameserver 10.233.0.3
search default.svc.cluster.local  svc.cluster.local cluster.local
options ndots:5
options timeout:1
```

When you use the default configuration of kubespray to install kubernetes, 10.233.0.3 is used as a DNS server IP address. Otherwise, you can check kube-dns IP address as follows.

```
$ kubectl get svc -n kube-system
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
kube-dns ClusterIP 10.233.0.3 <none> 53/UDP,53/TCP 12d
kubernetes-dashboard ClusterIP 10.233.21.149 <none> 443/TCP 12d
tiller-deploy ClusterIP 10.233.7.167 <none> 44134/TCP 3h"
```

Restart resolve service

```
$ sudo resolvconf -u
```

Now we can use kubernetes service not only in the container also in kubernetes nodes

## **Deploy SONA**

Download SONA-helm codes from <https://github.com/sonaproject/sona-helm>

```
$ git clone https://github.com/sonaproject/sona-helm.git
```

### For single Kubernetes cluster

```
$ helm upgrade onos-sona sona-helm/ -i
```

### For multi-node kubernetes cluster

```
$ helm upgrade onos-sona sona-helm/ -i --set onos.hostNetwork=true
```

If you want to use different ONOS image, please use onos.image.repository value overriding

```
$ helm upgrade onos-sona sona-helm/ -i --set onos.image.repository=<IMAGE NAME> --set onos.image.tag=<IMAGE TAG>
```

ONOS has an issue when it is installed as a container in a multi-node Kubernetes environment. So, I strongly recommend using hostNetwork = true

Another deployment example to set deployment node to specific nodes using node label

```
$ helm upgrade onos sona-helm/ -i --set onos.node_selector.key=openstack-control-plane --set onos.node_selector.value=enabled --set onos.image.tag=stable
```

## **How to check**

Check the helm deployment status using ls command.

Login to the SONA service and check if status of all onos nodes are READY.

```
$ helm ls
NAME     	REVISION	UPDATED                 	STATUS  	CHART     	APP VERSION	NAMESPACE
onos-sona	1       	Wed Aug  8 09:23:33 2018	DEPLOYED	sona-0.1.0	1.0        	default


$ ssh -p 8101 karaf@sona-service
Password authentication
Password:
Welcome to Open Network Operating System (ONOS)!
     ____  _  ______  ____
    / __ \/ |/ / __ \/ __/
   / /_/ /    / /_/ /\ \
   \____/_/|_/\____/___/

Documentation: wiki.onosproject.org
Tutorials:     tutorials.onosproject.org
Mailing lists: lists.onosproject.org

Come help out! Find out how at: contribute.onosproject.org

Hit '<tab>' for a list of available commands
and '[cmd] --help' for help on a specific command.
Hit '<ctrl-d>' or type 'system:shutdown' or 'logout' to shutdown ONOS.

onos> nodes
id=onos-sona-sona-0, address=10.1.1.12:9876, state=READY, version=1.13.2, updated=1d17h ago
id=onos-sona-sona-1, address=10.1.1.2:9876, state=READY, version=1.13.2, updated=1d17h ago *
id=onos-sona-sona-2, address=10.1.1.3:9876, state=READY, version=1.13.2, updated=53m16s ago
onos>
```
