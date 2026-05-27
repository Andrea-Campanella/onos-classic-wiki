# Demo AAA/RADIUS Server Testing

This page describes how to test authentication using the ONOS AAA application and a demo RADIUS server. It uses ONOS and a Mininet network to simulate the client side of the authentication process, and OpenRADIUS to implement the RADIUS server. This description is heavily dependent on the ON.Lab network.

The ONOS RADIUS AAA app takes in 802.1X/EAPOL authentication requests from supplicants within its managed network and forwards them on to an external RADIUS server. In this testing environment, we use Mininet hosts in an ONOS managed network as the supplicants, and use the *wpa\_supplicant*Linux command as the client to initiate authentication. Once the host issues the request, the ONOS AAA app receives the packet, and handles communication with the RADIUS server and the supplicant.

# What You Will Need

* An instance of ONOS to run. The AAA app is packaged as part of ONOS
* A Mininet instance
* A FreeRADIUS instance

# OpenRadius Setup

In the ON.Lab office, we have a FreeRADIUS server running on 10.1.128.10 (login ubuntu/ubuntu). This server can be configured to use MD5 or TLS authentication for EAP. To change the EAP type, edit the file /etc/freeradius/eap.conf and modify the default\_eap\_type attribute. A set of self-signed test certificates are deployed on that server. If you deploy your own FreeRADIUS server you can copy the certificates or generate your own. The client side certificates must be copied to the Mininet node running the supplicants; that is covered in the Mininet section below.

# Mininet Setup

Mininet is required to simulate hosts to act as supplicants. The Mininet topology must have at least one switch and one host, and be controlled by the ONOS instance that is running the AAA app.

# ONOS Setup

ONOS must be configured to manage the Mininet network. The AAA application is installed as part of the default ONOS payload and must be available.

# WPA Supplicant Setup

On the Mininet instance, create the following wpa\_supplicant configuration file in /etc/config/wpa\_supplicant.conf:

**wpa\_supplicant configuration**

```
ctrl_interface=/var/run/wpa_supplicant
eapol_version=1
ap_scan=0
fast_reauth=0
network={
        key_mgmt=WPA-EAP
        #eap=TLS
        #eap=MD5
        identity="testuser"
        password="testpassword"
        ca_cert="/etc/cert/cacert.pem"
        client_cert="/etc/cert/client.pem"
        private_key="/etc/cert/client.key"
     	private_key_passwd="whatever"
        eapol_flags=3
}
```

The client side TLS certificates (cacert.pem, client.pem and client.key) have to be copied from the RADIUS server certificates directory (/etc/freeradius/certs) to the local node in /etc/cert.

# Testing Authentication

There are three separate entities that must be used to fully test a RADIUS request: the FreeRADIUS server, the wpa\_supplicant and ONOS.

First, launch the AAA application inside of ONOS:

```
Rays-MacBook-Pro:onos-next ray$ onos
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

onos> app activate org.onosproject.aaa
onos>
```

Now, launch the FreeRADIUS server. It may already be running as a service, but if you want to run it manually with debugging options enabled, you can run it like this:

```
root@cord-radius:/etc/freeradius# freeradius -f -X -xx
```

The last piece is the client side, or supplicant. While inside of Mininet, invoke the *wpa\_supplicant* command to start the authentication process. If the authentication succeeds you will see a completion message from the supplicant tool:

```
mininet> h1 sudo wpa_supplicant -Dwired -ih1-eth0 -c/etc/config/wpa_supplicant.conf
Successfully initialized wpa_supplicant
h1-eth0: Associated with 01:80:c2:00:00:03
h1-eth0: CTRL-EVENT-EAP-STARTED EAP authentication started
h1-eth0: CTRL-EVENT-EAP-PROPOSED-METHOD vendor=0 method=13
h1-eth0: CTRL-EVENT-EAP-METHOD EAP vendor 0 method 13 (TLS) selected
h1-eth0: CTRL-EVENT-EAP-PEER-CERT depth=1 subject='/C=FR/ST=Radius/L=Somewhere/O=Example Inc./emailAddress=admin@example.org/CN=Example Certificate Authority'
h1-eth0: CTRL-EVENT-EAP-PEER-CERT depth=0 subject='/C=FR/ST=Radius/O=Example Inc./CN=Example Server Certificate/emailAddress=admin@example.org'
h1-eth0: CTRL-EVENT-EAP-SUCCESS EAP authentication completed successfully
```

# Useful Debugging Tools

It can be useful sometimes to watch the network traffic between ONOS and the RADIUS server. Run this command on the VM that is running ONOS to see the packets being sent. This command may differ depending on your network configuration:

**tcpdump command**

```
sudo tcpdump -vvv -X -n -i eth1
```
