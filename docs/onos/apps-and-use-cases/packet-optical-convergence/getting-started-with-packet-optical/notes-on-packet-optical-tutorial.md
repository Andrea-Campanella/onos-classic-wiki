# Notes on Packet Optical Tutorial

Procedures to install and build tools required for the packet optical  tutorial.

1. Download the ONOS tutorial ova which can be found here: [Basic ONOS Tutorial](../../../tutorials/basic-onos-tutorial.md)

2. Import ova to VirtualBox as described.

3. Start VM and log in as user sdn (default).

4. Open a terminal for the following commands.

5. Build Erlang:

sudo apt-get install -y build-essential autoconf libncurses5-dev libssh-dev unixodbc-dev  
cd  
wget <http://erlang.org/download/otp_src_17.5.tar.gz>  
tar zxvf otp\_src\_17.5.tar.gz  
cd otp\_src\_17.5  
./configure  
make  
sudo make install

6. Build Linc-OE:

sudo apt-get install -y git-core bridge-utils libpcap0.8 libpcap-dev libcap2-bin uml-utilities  
cd  
git clone <https://github.com/FlowForwarding/LINC-Switch.git> linc-oe  
cd linc-oe  
sed -i s/3000/300000/ rel/files/vm.args  
cp rel/files/sys.config.orig rel/files/sys.config  
make

7. Build LINC config generator:

cd  
git clone <https://github.com/FlowForwarding/LINC-config-generator.git>  
cd LINC-config-generator  
cp priv/\* .  
make

8.  Copy tutorial files required:

cd ~/onos  
mkdir optical  
wget <https://raw.githubusercontent.com/opennetworkinglab/onos/master/tools/test/topos/opticalUtils.py>  
wget <https://raw.githubusercontent.com/opennetworkinglab/onos/master/tools/test/topos/opticalTest.py>

Steps to run the packet optical tutorial.

1. Start ONOS cluster, GUI and CLI following the procedures described here: [Basic ONOS Tutorial](../../../tutorials/basic-onos-tutorial.md)

2. Run ONOS CLI command summary and note IP address of node.

3. Run ONOS CLI command app activate to activate applications:  drivers,drivers.optical,openflow,proxyarp,optical

4. Run Linc-OE:

cd ~/onos/optical  
export RUN\_PACK\_PATH=~/onos/bin  
sudo -E python opticalTest.py <node IP address>
