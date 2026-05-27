#!/bin/bash
echo "starting gluon"
echo "change directory to home"
GLUON_DIR=/home
echo $GLUON_DIR
echo "download gluon git repo"
cd $GLUON_DIR
#sudo git clone https://github.com/openstack/gluon.git
echo "add proton and gluon users"
sudo adduser --system --group proton
sudo adduser --system --group gluon
echo "create gluon and proton working directory"
sudo mkdir /opt/gluon
sudo mkdir /opt/proton
sudo mkdir /etc/gluon
sudo mkdir /etc/proton
echo "change gluon and proton directory ownership"
sudo chown gluon /opt/gluon
sudo chown proton /opt/proton
echo "create gluon.conf and proton.conf files into /etc/gluon and /etc/proton directory respectively"
cd /etc/gluon
sudo touch gluon.conf
sudo chmod 777 gluon.conf
cd /etc/proton
sudo touch proton.conf
sudo chmod 777 proton.conf
echo "append gluon.conf configuration"
sudo cat > /etc/gluon/gluon.conf <<EOF
[DEFAULT]
state_path = /opt/gluon
host=0.0.0.0
debug=True
[api]
host=0.0.0.0
EOF
echo "append proton.conf configuration"
sudo cat > /etc/proton/proton.conf <<EOF
[DEFAULT]
state_path = /opt/proton
EOF
echo "change owner for gluon and proton"
sudo chown gluon /etc/gluon
sudo chmod go+w /etc/gluon
sudo chown proton /etc/proton
sudo chmod go+w /etc/proton
echo "change keystone and oslo_policy version in requirement.txt file"
#cd $GLUON_DIR/gluon
#sudo sed -i 's/keystoneauth1>=2.14.0/keystoneauth1>=2.10.0/' requirements.txt
#sudo sed -i 's/oslo.policy>=1.15.0/oslo.policy>=1.9.0/' requirements.txt
echo "gluon building and installation"
cd $GLUON_DIR/gluon
sudo python setup.py build
sudo python setup.py develop
sudo python setup.py install
echo "copy the startup script to start gluon"
sudo cp $GLUON_DIR/gluon/scripts/proton-server.conf /etc/init
echo "starting proton server"
sudo start proton-server
echo "started proton server successfully"
