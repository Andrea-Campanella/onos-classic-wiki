# Configuring OVS connection using SSL/TLS with self-signed certificates

To make a SSL/TLS Openflow connection between onos and OVS switches using self-signed certificates, there are five main steps to follow:

1. *Generate SSL key/certificate for onos;*
2. *Copy the onos certificate to the appropriate OVS location so that OVS can accept the certificate from onos;*
3. *Generate SSL key/certificate for OVS;*
4. *Copy the OVS certificate to the appropriate onos location so that onos can accept the certificate from OVS;*
5. *Test the SSL connection.*

The following is an example of the detailed configuration steps.

1. Generating SSL key/certificate for onos. On the host running onos, we generate the SSL key/certificate as the following:
   1. Use "keytool" to generate a .jks keystone:

      ```
      sdn@onosCell1:~/wiki$ keytool -genkey -keyalg RSA -alias onos -keystore onos.jks -storepass 222222 -validity 360 -keysize 2048
      What is your first and last name?
        [Unknown]:  sdn rocks
      What is the name of your organizational unit?
        [Unknown]:  config-guide
      What is the name of your organization?
        [Unknown]:  onosproject.org
      What is the name of your City or Locality?
        [Unknown]:  anycity
      What is the name of your State or Province?
        [Unknown]:  anystate
      What is the two-letter country code for this unit?
        [Unknown]:  us
      Is CN=sdn rocks, OU=config-guide, O=onosproject.org, L=anycity, ST=anystate, C=us correct?
        [no]:  yes
      Enter key password for <onos>
      	(RETURN if same as keystore password):
      sdn@onosCell1:~/wiki$ ls
      onos.jks
      ```
   2. Covert the .jks keystore (which onos uses) to PEM file (which OVS uses) in a 2-step conversions: from .jks to .p12, then to .pem:

      ```
      sdn@onosCell1:~/wiki$ keytool -importkeystore -srckeystore onos.jks -destkeystore onos.p12 -srcstoretype jks -deststoretype pkcs12
      Enter destination keystore password:
      Re-enter new password:
      Enter source keystore password:
      Entry for alias onos successfully imported.
      Import command completed:  1 entries successfully imported, 0 entries failed or cancelled
      sdn@onosCell1:~/wiki$ ls
      onos.jks  onos.p12
      ```

      ```
      sdn@onosCell1:~/wiki$ openssl pkcs12 -in onos.p12 -out onos.pem
      Enter Import Password:
      MAC verified OK
      Enter PEM pass phrase:
      Verifying - Enter PEM pass phrase:
      sdn@onosCell1:~/wiki$ ls
      onos.jks  onos.p12  onos.pem
      ```
   3. Use the certificate portion of the "onos.pem" file to create a new file, called "cacert.pem" - this is the file to be copied over to OVS - it is from "Bag Attributes" to "END CERTIFICATE":

      ```
      sdn@onosCell1:~/wiki$ cat onos.pem
      <Private key here>
      Bag Attributes
          friendlyName: onos
          localKeyID: 54 69 6D 65 20 31 34 35 33 32 34 33 35 32 33 34 31 39
      subject=/C=us/ST=anystate/L=anycity/O=onosproject.org/OU=config-guide/CN=sdn rocks
      issuer=/C=us/ST=anystate/L=anycity/O=onosproject.org/OU=config-guide/CN=sdn rocks
      -----BEGIN CERTIFICATE-----
      MIIDjTCCAnWgAwIBAgIEbbwHKjANBgkqhkiG9w0BAQsFADB3MQswCQYDVQQGEwJ1
      .....
      -----END CERTIFICATE-----
       
      sdn@onosCell1:~/wiki$ cat cacert.pem
      Bag Attributes
          friendlyName: onos
          localKeyID: 54 69 6D 65 20 31 34 35 33 32 34 33 35 32 33 34 31 39
      subject=/C=us/ST=anystate/L=anycity/O=onosproject.org/OU=config-guide/CN=sdn rocks
      issuer=/C=us/ST=anystate/L=anycity/O=onosproject.org/OU=config-guide/CN=sdn rocks
      -----BEGIN CERTIFICATE-----
      MIIDjTCCAnWgAwIBAgIEbbwHKjANBgkqhkiG9w0BAQsFADB3MQswCQYDVQQGEwJ1
      ...
      -----END CERTIFICATE-----
       
      sdn@onosCell1:~/wiki$ ls
      cacert.pem  onos.jks  onos.p12  onos.pem
      ```

      Note: the intermediate key/cert, "onos.p12", and onos.pem, are no longer used and should be discarded.
2. Copy the onos certificate to the appropriate OVS location so that OVS can accept the certificate from onos:  
   1. Copy cacert.pem from your working directory to your OVS installation at "/var/lib/openvswitch/pki/controllerca/cacert.pem". In this case, OVS is running on a host called, "mininet",  than onosCell1:

      ```
      root@mininet:/var/lib/openvswitch/pki/controllerca# ls -al
      total 68
      drwxr-xr-x 6 root root 4096 Jan 19 15:39 .
      drwxr-xr-x 4 root root 4096 Oct  8  2014 ..
      -rw-r--r-- 1 root root 1567 Jan 19 15:39 cacert.pem
      ........
      ```

      Note: beware of where the OVS installation location is depending on how you install OVS. It could be "/var/lib/openvswitch", or "/usr/local/var/lib/openvswitch", or others.
3. Generate SSL key/certificate for OVS:
   1. On the "mininet" host:

      ```
      admin@mininet:~$ cd /etc/openvswitch
      admin@mininet:/etc/openvswitch$ sudo ovs-pki req+sign sc switch
      sc-req.pem	Wed Jan 20 13:06:16 PST 2016
      	fingerprint 719b77cb8a485f4b86f8fab6da6057298a504131
       
      admin@mininet:/etc/openvswitch$ ls -al
      total 56
      drwxr-xr-x   2 root root  4096 Jan 20 13:06 .
      drwxr-xr-x 124 root root 12288 Jan 20 13:05 ..
      ...
      -rw-r--r--   1 root root  4044 Jan 20 13:06 sc-cert.pem
      -rw-------   1 root root  1679 Jan 20 13:06 sc-privkey.pem
      -rw-r--r--   1 root root  3601 Jan 20 13:06 sc-req.pem
      ...
      ```

      "sc-\* .pem" files were newly generated.
   2. Make OVS to use the new keys:

      ```
      admin@onos-dev:/etc/openvswitch$ sudo ovs-vsctl set-ssl /etc/openvswitch/sc-privkey.pem /etc/openvswitch/sc-cert.pem /var/lib/openvswitch/pki/controllerca/cacert.pem
      ```
4. Copy the OVS certificate to the appropriate onos location so that onos can accept the certificate from OVS:
   1. Copy "sc-cert.pem" (the OVS public key just generated in 4a) to the "onosCell1" host, and import it to onos.jks store with trust:

      ```
      sdn@onosCell1:~/wiki$ ls
      cacert.pem  onos.jks  onos.p12  onos.pem  sc-cert.pem
       
      dn@onosCell1:~/wiki$ keytool -importcert -file sc-cert.pem -keystore onos.jks
      Enter keystore password:
      Owner: CN=sc id:5a3a05bf-9221-46bf-8b71-b526da64772f, OU=Open vSwitch certifier, O=Open vSwitch, ST=CA, C=US
      Issuer: CN=OVS switchca CA Certificate (2015 Nov 24 13:43:42), OU=switchca, O=Open vSwitch, ST=CA, C=US
      Serial number: 8
      Valid from: Wed Jan 20 13:06:16 PST 2016 until: Sat Jan 17 13:06:16 PST 2026
      Certificate fingerprints:
      	 MD5:  70:CF:BC:62:33:EB:C7:FD:16:49:87:04:9E:07:98:9C
      	 SHA1: 66:C3:AB:12:CA:88:F5:A9:47:62:24:9F:50:60:87:F7:A9:D7:CF:97
      	 SHA256: E0:1C:07:45:2F:48:B6:D8:E1:A3:FA:65:7A:8D:9F:82:56:5A:04:4C:97:D4:0C:BC:43:7E:4C:13:80:9B:36:E3
      	 Signature algorithm name: SHA1withRSA
      	 Version: 1
      Trust this certificate? [no]:  yes
      Certificate was added to keystone

      sdn@onosCell1:~/wiki$ keytool -list -keystore onos.jks
      Enter keystore password:
      Keystore type: JKS
      Keystore provider: SUN
      Your keystore contains 2 entries
      onos, Jan 19, 2016, PrivateKeyEntry,
      Certificate fingerprint (SHA1): CB:77:5D:23:AB:84:A0:39:22:B2:E0:AB:B8:91:1D:3B:10:8C:70:1F
      mykey, Jan 20, 2016, trustedCertEntry,
      Certificate fingerprint (SHA1): 66:C3:AB:12:CA:88:F5:A9:47:62:24:9F:50:60:87:F7:A9:D7:CF:97
      ```
   2. Enable onos to use OFTLS by configuring "$ONOS\_HOME/tools/package/bin/onos-service" - in this case we use "onos-install" to start onos:

      ```
      #!/bin/bash
      # -----------------------------------------------------------------------------
      # Starts ONOS Apache Karaf container
      # -----------------------------------------------------------------------------
      # uncomment the following line for performance testing
      #export JAVA_OPTS="${JAVA_OPTS:--Xms8G -Xmx8G -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -XX:+PrintGCDetails -XX:+PrintGCTimeStamps}"
      # uncomment the following line for Netty TLS encryption
      # Do modify the keystore location/password and truststore location/password accordingly
      #export JAVA_OPTS="${JAVA_OPTS:--DenableNettyTLS=true -Djavax.net.ssl.keyStore=/home/ubuntu/onos.jks -Djavax.net.ssl.keyStorePassword=222222 -Djavax.net.ssl.trustStore=/home/ubuntu/onos.jks -Djavax.net.ssl.trustStorePassword=222222}"

      export JAVA_OPTS="${JAVA_OPTS:--DenableOFTLS=true -Djavax.net.ssl.keyStore=/home/sdn/wiki/onos.jks -Djavax.net.ssl.keyStorePassword=222222 -Djavax.net.ssl.trustStore=/home/sdn/wiki/onos.jks -Djavax.net.ssl.trustStorePassword=222222}"
      .....
      ```

      Note: if you want to configure SSL on onos service, e.g. using a tar.gz, you can configure "onos-service" under the node's "/opt/onos/bin" directory.
5. Testing the SSL connection:
   1. Start Mininet/OVS switches, configure switches using ssl connections:

      ```
      admin@mininet:$ sudo mn --topo linear,3 --controller remote
      *** Creating network
      *** Adding controller
      *** Adding hosts:
      h1 h2 h3
      *** Adding switches:
      s1 s2 s3
      *** Adding links:
      (h1, s1) (h2, s2) (h3, s3) (s2, s1) (s3, s2)
      *** Configuring hosts
      h1 h2 h3
      *** Starting controller
      c0
      *** Starting 3 switches
      s1 s2 s3 ...
      *** Starting CLI:
      mininet> sh ovs-vsctl set-controller s1 ssl:192.168.57.101:6653
      mininet> sh ovs-vsctl set-controller s2 ssl:192.168.57.101:6653
      mininet> sh ovs-vsctl set-controller s3 ssl:192.168.57.101:6653
      ```
   2. Check onos log. You should see the following log messages:

      ```
      2016-01-20 13:37:49,154 | INFO  | FelixStartLevel  | Controller                       | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | Starting OpenFlow IO
      2016-01-20 13:37:49,154 | INFO  | FelixStartLevel  | Controller                       | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | OpenFlow Security is enabled
      .....
      2016-01-20 13:49:23,023 | INFO  |  server boss #17 | OpenflowPipelineFactory          | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | OpenFlow SSL enabled.
      ....
      onos-of-ctl - 1.5.0.SNAPSHOT | New switch connection from /192.168.57.110:44568
      2016-01-20 15:05:28,273 | INFO  | ew I/O worker #6 | OFChannelHandler                 | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | Sending OF_13 Hello to /192.168.57.110:44568
      2016-01-20 15:05:28,275 | INFO  | ew I/O worker #6 | OFChannelHandler                 | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | Received port desc reply for switch at [/192.168.57.110:44568 DPID[00:00:00:00:00:00:00:01]]
      2016-01-20 15:05:28,279 | INFO  | ew I/O worker #6 | OFChannelHandler                 | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | Received switch description reply OFDescStatsReplyVer13(xid=4294967289, flags=[], mfrDesc=Nicira, Inc., hwDesc=Open vSwitch, swDesc=2.3.2, serialNum=None, dpDesc=None) from switch at /192.168.57.110:44568
      2016-01-20 15:05:28,280 | INFO  | ew I/O worker #6 | Controller                       | 171 - org.onosproject.onos-of-ctl - 1.5.0.SNAPSHOT | OpenFlow handshaker found for device 1: org.onosproject.driver.handshaker.NiciraSwitchHandshaker [? DPID[00:00:00:00:00:00:00:01]]
      ......
      ```
   3. make sure switches are connected by checking onos console:

      ```
      onos> devices
      id=of:0000000000000001, available=true, role=MASTER, type=SWITCH, mfr=Nicira, Inc., hw=Open vSwitch, sw=2.3.2, serial=None, managementAddress=192.168.57.110, protocol=OF_13, channelId=192.168.57.110:44568
      id=of:0000000000000002, available=true, role=MASTER, type=SWITCH, mfr=Nicira, Inc., hw=Open vSwitch, sw=2.3.2, serial=None, managementAddress=192.168.57.110, protocol=OF_13, channelId=192.168.57.110:44597
      id=of:0000000000000003, available=true, role=MASTER, type=SWITCH, mfr=Nicira, Inc., hw=Open vSwitch, sw=2.3.2, serial=None, managementAddress=192.168.57.110, protocol=OF_13, channelId=192.168.57.110:44619
      ```

Some helpful reference to consult when configuring:

* <http://git.openvswitch.org/cgi-bin/gitweb.cgi?p=openvswitch;a=blob_plain;f=INSTALL.SSL;hb=HEAD>
* <https://floodlight.atlassian.net/wiki/pages/viewpage.action?pageId=5636122>

**New Instructions**

**config/component-cfg.json**

```
{
  "org.onosproject.openflow.controller.impl.OpenFlowControllerImpl": {
    "tlsMode": "strict",
    "keyStore": "/home/user/onos.jks",
    "keyStorePassword": "222222",
    "trustStore": "/home/user/onos.jks",
    "trustStorePassword": "222222"
  }
}
```

**config/network-cfg.json**

```
{
    "devices" : {
        "of:0000000000000001" : {
            "openflow" : {
                "keyAlias" : "mykey"
            } 
        }
    }
}
```
