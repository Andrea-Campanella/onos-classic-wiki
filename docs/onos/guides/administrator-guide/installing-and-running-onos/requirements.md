# Requirements

# Hardware requirements

Hardware requirements are difficult to define, since they can depend by many factors, including the cluster size, the managed network size, the number of messages exchanged with network devices, and so on.

However, we feel confident to say that for a basic execution environment, the following minimum requirements should be satisfied:

* 2 core CPU
* 2 GB RAM
* 10 GB hdd
* 1 NIC (any speed)

# Connectivity requirements

## Internet connectivity

Recent efforts have made it possible to install and run ONOS without the need for Internet connectivity. However, Internet connectivity is a necessary when pre-required software needs to be installed, or when ONOS packages need to be downloaded. Often on the mailing list, installation or execution problems are reported due to lack of Internet connectivity. Despite the community efforts to run ONOS with no need for an Internet connection, this can be caused by external factors. For these reasons Internet connectivity is not mandatory, but strongly suggested where possible on both management and target machines.

## For target machines

Target machines that are part of the same cluster are required to be able to communicate together at the IP layer (to confirm this, you should be able to ping all machines of the cluster from every other machine).

## For management machines

If the management machine needs to be able to operate target machines remotely, it needs to be able to communicate with all of them at the IP layer (to verify this, before starting you should be able to ping all machines in the cluster from the management machine).

## Ports:

ONOS requires the following ports to be open, in order to make the corresponding functionalities available:

* 8181    for REST API and GUI
* 8101    to access the ONOS CLI
* 9876    for intra-cluster communication (communication between target machines)
* 6653    optional, for OpenFlow
* 6640    optional, for OVSDB

# Environment and software requirements

Following is a list of things that need to be installed and configured on your OS before moving forward with the ONOS installation. All commands below are valid for Ubuntu 16.04 LTS. You can Google their equivalent for other OSes.

## Users

Like any other production service, ONOS shouldn’t be run as root. Scripts used to run ONOS as a service (used after in the installation process) require a special unprivileged user (often user 'sdn') configured in the system. The following snippet will allow you to create an sdn user and assign it to an sdn group in one step:

**Add a user sdn**

```
sudo adduser sdn --system --group
```

## Software packages

### Java Versions

ONOS is a Java based platform. It’s strongly suggested to use Oracle Java 1.8 for it. The following snippet will allow you to install Java 1.8 in one step on an Ubuntu machine.

### Java8 (Ubuntu 16 and Older)

Since Oracle had an license update on April 16 2019, anyone who want to download java8 has to register account, the apt methods of installing will not work.

Go to Oracle JDK download website, login and download the tar  ball : jdk-8uxxx-linux-x64.tar.gz

**Install Oracle Java 8**

```
for JavaCommand in java jar java2groovy javac javadoc javafxpackager javah javap javapackager javaws
do
	sudo update-alternatives --install /usr/bin/$JavaCommand $JavaCommand /your_path_extracted_jdk/bin/$JavaCommand 1
done
```

### Java11 (Ubuntu 18 and Newer)

For newer versions of Ubuntu and ONOS is recommended to use Java 11 and set

**Install Oracle Java 11**

```
sudo apt install openjdk-11-jdk
```

**Optional:** you can also set java home for a better performance. For this example you will need to have super user powers, other ways to set java home are available online

**Set java home**

```
sudo su
cat >> /etc/environment <<EOL
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
JRE_HOME=/usr/lib/jvm/java-11-openjdk-amd64/jre
EOL
```

### Curl

**Install curl**

```
sudo apt-get install curl
```
