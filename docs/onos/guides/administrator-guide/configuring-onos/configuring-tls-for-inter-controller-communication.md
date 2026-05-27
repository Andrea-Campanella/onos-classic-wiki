# Configuring TLS for inter-controller communication

Inter-controller communication exchanged at the East/West interface does not provide secure communication by default, allowing observation and modification of inter-controller traffic. TLS can and should be enabled for inter-controller communications to ensure communication within an ONOS cluster is secure. Hostnames, IP addresses, and directories in the following commands should be adjusted for your environment.

**Generate a key on each ONOS server**

On each ONOS server, generate a new key with an alias unique to that server:

```
sdn@server:~/onos$ keytool -genkey -keyalg RSA -alias onos-<server hostname>  -keystore apache-karaf-3.0.8/etc/keystore -storepass 222222 -validity 360 -keysize 2048
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
```

**Get the certificates**

The certificate for the newly generated key on each ONOS instance will now need to be distributed among the other ONOS instances. To do this the key should be converted to a .p12 file and then to a PEM file, as follows:

```
sdn@server:~/onos$ keytool -importkeystore -srckeystore apache-karaf-3.0.8/etc/keystore -destkeystore onos.p12 -srcstoretype jks -deststoretype pkcs12
sdn@server:~/onos$ openssl pkcs12 -in onos.p12 -out onos.pem
sdn@server:~/onos$ ls
onos.pem ...
```

The certificate can now be extracted from the PEM file using the following command. The output file for this command should be adjusted to ensure that it is unique for each ONOS server. This will make it easier to manage when transporting certificates between instances.

```
sdn@server:~/onos$ awk 'split_after == 1 {n++;split_after=0} /-----END ENCRYPTED PRIVATE KEY-----/ {split_after=1} {print > "cacert" n ".pem"}' < onos.pem; mv cacert1.pem cert.pemd
sdn@server:~/onos$ mv cert.pem onos-<hostname>-cert.pem
```

**Copy certificates to each ONOS server**

Each ONOS instance in the cluster will need the certificate for every other ONOS instance. The certificates can be copied using the following command. This command should be repeated for each certificate and each instance.

```
sdn@server:~/onos$ scp ./onos-<hostname>-cert.pem sdn@otherserver:~/onos/
```

**Import the certificate**

Each ONOS instance will need the certificates for every other instance in its keystore. The certificates can be imported using the following command:

```
sdn@server:~/onos$ keytool -importcert -file onos-<hostname>-cert.pem -keystore apache-karaf-3.0.8/etc/keystore
…
Trust this certificate? [no]:  yes
Certificate was added to keystore
```

**Modify the ONOS launch script**

The ONOS launch script ‘onos-service’ located in the ‘$ONOS\_ROOT/bin/’ directory contains a line to enable TLS for Netty, the communication framework used for inter-controller communication. Uncomment the line and ensure the ‘keystore’ and ‘truststore’ point to the keystore used in the commands above.

```
export JAVA_OPTS="${JAVA_OPTS:--DenableNettyTLS=true -Djavax.net.ssl.keyStore=/home/sdn/onos/apache-karaf-3.0.8/etc/keystore -Djavax.net.ssl.keyStorePassword=222222 -Djavax.net.ssl.trustStore=/home/sdn/onos/apache-karaf-3.0.8/etc/keystore -Djavax.net.ssl.trustStorePassword=222222}"
```

**Restart ONOS**

With the above steps completed, the ONOS service should be restarted to enable secure inter-controller communication.
