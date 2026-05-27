# M-CORD Developer Environment

This document describes the relative open source softwares used in M-CORD. This purpose of the document is for developers to build their own XOS development environment for M-CORD.

## Open source softwares M-CORD needs:

* XOS (lastest master version), WIKI:  <http://guide.xosproject.org/opsguide/>
* Openstack (Kilo version, which is required by XOS)
* ONOS (lastest master version)

     The XOS is for service orchestration. Openstack is used to create networks and vms. ONOS is mainly used for VNF VM connectivities. We run two ONOS, one controls the Fabric, with Segement Routing Application. Another ONOS with application VTN controls the OVS inside each compute node.

* CORD-VTN: [https://wiki.onosproject.org/display/ONOS/CORD+VTN](../cord-central-offices-re-architected-as-datacenters-vcpe-volt-nfaas/cord-vtn.md)
* CORD: Leaf-Spine Fabric with Segment Routing, the Hardware Switch Installation Guide: <https://wiki.onosproject.org/display/ONOS/Hardware+Switch+Installation+Guide>

## Two general ways to setup the M-CORD environment:

    (1) Setup the Openstack, XOS, ONOS separately and manually according to the tutorial of each.

    (2) You also can setup them together automatically according to : <https://github.com/open-cloud/xos/tree/master/xos/configurations/cord-pod>.

**On this page, we do not need those two sections: "Set up external connectivity for VMs" "Inspecting the vSG".**

## Experience running M-CORD on Cloudlab: [www.cloudlab.us](http://www.cloudlab.us):

    I tried the tutorial <https://github.com/open-cloud/xos/tree/master/xos/configurations/cord-pod> on [www.cloudlab.us](http://www.cloudlab.us). After following the second way to setup the environment, you can login in the xos for cord-pod. How to run M-CORD portal of XOS?

    Step 1: prepare the environment to run M-CORD on Cloudlab.

```
$ssh ubuntu@xos
ubuntu@xos:~$ cd xos/xos/configurations/mcord/
ubuntu@xos:~/xos/xos/configurations/mcord$ cp ../cord-pod/admin-openrc.sh .
ubuntu@xos:~/xos/xos/configurations/mcord$ cp ../cord-pod/id_rsa* .
ubuntu@xos:~/xos/xos/configurations/mcord$ cp ../cord-pod/node_key .
```

    Note: the admin-openrc.sh is for xos to talk to openstack.

    Step2: change the RSA key pair name inside mcord.yaml.

        mcord\_public\_key - > id\_rsa.pub

        mcord\_private\_key -> id\_rsa

    Step3: Build M-CORD

```
ubuntu@xos:~$ docker rm -f $(docker ps -aq)
ubuntu@xos:~$ make rebuild_xos
ubuntu@xos:~$ make rebuild_synchronizer
ubuntu@xos:~$ make
```

Then run the follow command line on your local computer with port 8000. Because XOS portal for M-CORD uses 8000.

```
ssh -L 8888:xos:8000 pingping@clnode096.clemson.cloudlab.us
```

### TODO:

(1) add default image, right now, we only have bbu image in the xos, but indeed does not exist on cloudlab.

### Verification:

Right now, you can open your bower with <http://localhost:8888>, and you can see the M-CORD relative services now.

Lets try further, click the "Slices" in the left add a new slice. After creating this slice, then click this slice, you should be able to add an instance inside this slice.

when you create a instance, please choose "nova-compute", others compute nodes are not active on Cloudlab.

Only after you create an instance, the private network of the slice will be really created, you can see the network ID and subnet ID in both "Admin-Only" tab of the network in XOS portal and Openstack.

Note: If you meet any issue, send me email [pingping@onlab.us](mailto:pingping@onlab.us) or chat with me on slack.
