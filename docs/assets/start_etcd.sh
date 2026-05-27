#!/bin/bash

echo "Start Etcd"
echo "Get Etcd Code into the cureent directory"
curl -L https://github.com/coreos/etcd/releases/download/v3.1.0/etcd-v3.1.0-linux-amd64.tar.gz -o ./etcd-v3.1.0-linux-amd64.tar.gz
echo "untar downloaded etcd file"
tar -zxvf etcd-v3.1.0-linux-amd64.tar.gz
echo "change directory to etcd-v2.3.6"
cd etcd-v3.1.0-linux-amd64
echo "copy etcd and etcdctl to /usr/local/bin"
sudo cp etcd etcdctl /usr/local/bin
echo "create etcd directory to /var"
sudo mkdir /var/etcd
echo "create etcd.conf and etcd.override to /etc/init and chnage permission"
cd /etc/init
sudo touch etcd.conf etcd.override
sudo chmod 777 etcd.conf
sudo chmod 777 etcd.override
echo "appending etcd.conf configuration to etcd file"
sudo cat > /etc/init/etcd.conf <<EOF
description "etcd 2.0 distributed key-value store"
author "Scott Lowe <scott.lowe@scottlowe.org>"
start on (net-device-up
          and local-filesystems
          and runlevel [2345])
stop on runlevel [016]
respawn
respawn limit 10 5
script
  if [ -f "/etc/default/etcd" ]; then
    . /etc/default/etcd
  fi
chdir /var/etcd
exec /usr/local/bin/etcd >>/var/log/etcd.log 2>&1
end script
EOF
echo "appending etcd.override configuration to etcd file"
sudo cat > /etc/init/etcd.override <<EOF
env ETCD_INITIAL_CLUSTER="etcd-01=http://127.0.0.1:2380"
env ETCD_INITIAL_CLUSTER_STATE="new"
env ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-1"
env ETCD_INITIAL_ADVERTISE_PEER_URLS="http://127.0.0.1:2380"
env ETCD_DATA_DIR="/var/etcd"
env ETCD_LISTEN_PEER_URLS="http://127.0.0.1:2380"
env ETCD_LISTEN_CLIENT_URLS="http://127.0.0.1:2379,http://127.0.0.1:2379"
env ETCD_ADVERTISE_CLIENT_URLS="http://127.0.0.1:2379"
env ETCD_NAME="etcd-01"
EOF
echo "change iptable acl policy "
sudo iptables -A INPUT -p tcp -m multiport --ports 2380,2379 -m comment --comment "etcd" -j ACCEPT
echo "remove default etcd file /usr/local/bin"
cd /usr/local/bin
sudo rm -rf default.etcd
echo "starting etcd client into new tab"
gnome-terminal -e "bash -c \"cd /usr/local/bin; exec sudo ./etcd\""
echo "waiting for 5 seconds"
sleep 5
sudo etcdctl member list
sudo etcdctl cluster-health
Ishealthy=$(sudo etcdctl cluster-health | grep "cluster is healthy")
if [ -n $Ishealthy ] ; then
echo "failed to start etcd"
else
echo "etcd successfully started, enjoy it :-)"
fi
