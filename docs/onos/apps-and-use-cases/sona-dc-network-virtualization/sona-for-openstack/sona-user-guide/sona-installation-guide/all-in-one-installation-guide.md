# All-in-one Installation Guide

The following guide describes how to install SONA and OpenStack in one node using devstack.

Limitation

In All-in-one installation mode, the gateway is NOT installed because compute node and gateway node require their own OVS. However, you can add gateway nodes after installing all-in-one SONA.

# How to install

1. Download Devstack (Currently we supports pike, queens, and rocky snapshot)

   ```
   $ git clone -b stable/queens https://git.openstack.org/openstack-dev/devstack
   ```

   SONA All-in-one version also supports OpenStack ocata/pike/queens version.
2. Create local.conf

   **local.conf**

   ```
   [[local|localrc]]
   HOST_IP=10.1.1.26
   SERVICE_HOST=10.1.1.26
   RABBIT_HOST=10.1.1.26
   DATABASE_HOST=10.1.1.26
   Q_HOST=10.1.1.26

   ADMIN_PASSWORD=nova
   DATABASE_PASSWORD=$ADMIN_PASSWORD
   RABBIT_PASSWORD=$ADMIN_PASSWORD
   SERVICE_PASSWORD=$ADMIN_PASSWORD
   SERVICE_TOKEN=$ADMIN_PASSWORD

   DATABASE_TYPE=mysql

   # Log
   USE_SCREEN=True
   SCREEN_LOGDIR=/opt/stack/logs/screen
   LOGFILE=/opt/stack/logs/xstack.sh.log
   LOGDAYS=1
   # Images
   FORCE_CONFIG_DRIVE=True

   # Networks
   Q_ML2_TENANT_NETWORK_TYPE=vxlan
   Q_ML2_PLUGIN_MECHANISM_DRIVERS=onos_ml2
   Q_ML2_PLUGIN_TYPE_DRIVERS=flat,vlan,vxlan
   ML2_L3_PLUGIN=onos_router
   NEUTRON_CREATE_INITIAL_NETWORKS=False
   enable_plugin networking-onos https://github.com/openstack/networking-onos.git stable/queens
   ONOS_MODE=allinone

   # Services
   ENABLED_SERVICES=n-cpu,placement-client,neutron,key,nova,n-api,n-cond,n-sch,n-novnc,n-cauth,placement-api,g-api,g-reg,q-svc,horizon,rabbit,mysql


   NOVA_VNC_ENABLED=True
   VNCSERVER_PROXYCLIENT_ADDRESS=$HOST_IP
   VNCSERVER_LISTEN=$HOST_IP

   LIBVIRT_TYPE=qemu

   # Branches
   GLANCE_BRANCH=stable/queens
   HORIZON_BRANCH=stable/queens
   KEYSTONE_BRANCH=stable/queens
   NEUTRON_BRANCH=stable/queens
   NOVA_BRANCH=stable/queens
   ```

   You just need to change IP address in local.conf as in normal SONA installation guide. Also, please use the master branch of networking-onos in sonaproject. All changes will be upstreamed to the OpenStack repository very soon.
3. Install Devstack

   ```
   ~/devstack$ ./stack.sh
   ```
4. Done!  
   Now you can create virtual networks and VMs using either CLI or horizon UI.
5. Gateway install (Optional)  
   If you want to test North-South traffic, you can add gateway nodes as in the SONA installation guide ([SONA Installation Guide](../sona-installation-guide.md)).

# How to check

After installation of devstack, please check if all default SONA flow rules are installed in br-int bridge of OVS.

```
~/devstack$ sudo ovs-ofctl dump-flows br-int -O openflow13
OFPST_FLOW reply (OF1.3) (xid=0x2):
 cookie=0xb0000bb4b9281, duration=255323.201s, table=0, n_packets=4, n_bytes=1344, send_flow_rem priority=42000,udp,tp_src=68,tp_dst=67 actions=CONTROLLER:65535
 cookie=0xb0000c00eeaf2, duration=255323.201s, table=0, n_packets=3, n_bytes=126, send_flow_rem priority=40000,arp actions=CONTROLLER:65535
 cookie=0xb00001461d721, duration=255323.318s, table=0, n_packets=42, n_bytes=3772, send_flow_rem priority=0 actions=goto_table:10
 cookie=0xb0000e8f1b0d8, duration=255323.317s, table=10, n_packets=12, n_bytes=936, send_flow_rem priority=0 actions=goto_table:20
 cookie=0xb00007314ee8c, duration=255323.326s, table=20, n_packets=42, n_bytes=3772, send_flow_rem priority=0 actions=goto_table:30
 cookie=0xb00000d2ffa7a, duration=255323.219s, table=30, n_packets=30, n_bytes=2836, send_flow_rem priority=30000,dl_dst=fe:00:00:00:00:02 actions=goto_table:40
 cookie=0xb00007a117617, duration=255323.317s, table=30, n_packets=12, n_bytes=936, send_flow_rem priority=0 actions=goto_table:50
```

Also, you can login to ONOS and check the openstack nodes status as below. Please note that ONOS is installed as a container. The login password is 'karaf'.

```
~/devstack$ ssh -p 8101 karaf@localhost
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

onos> openstack-
openstack-delete-peer-router         openstack-floatingips                openstack-networks                   openstack-node-check
openstack-node-init                  openstack-nodes                      openstack-peer-routers               openstack-ports
openstack-purge-rules                openstack-purge-states               openstack-routers                    openstack-security-groups
openstack-sync-rules                 openstack-sync-states                openstack-update-peer-router         openstack-update-peer-router-vlan
onos> openstack-nodes
Hostname            Type           Integration Bridge      Management IP           Data IP             VLAN Intf           Uplink Port    State
compute-01          COMPUTE        of:00000000000000a1     10.1.1.26               10.1.1.26                                              COMPLETE
Total 1 nodes
onos>
```
