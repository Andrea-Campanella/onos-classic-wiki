# Installing on a single machine

**This article is to deploy a distribution version in production environment, not for development purpose. For developer, please read ([Developer Quick Start](../../developer-guide/developer-quick-start.md)), and other articles in the [Developer Guide](../../developer-guide.md).**

The following section describes how to install ONOS on a single target machine, running the installation steps locally (on the target machine itself).

Further sections will describe how to install one or more ONOS target machines from a centralized management machine.

The target machine will be able to eventually join other nodes in later steps, to form a cluster.

# Installation

**Before continuing remember to verify if you have all the requirements at [this](requirements.md) link.**

ONOS default packages assume ONOS gets installed under */opt*, so let's first make sure the directory exists and let's move into it

**Move to /opt**

```
sudo mkdir /opt
cd /opt
```

Start downloading the desired version of ONOS in tar.gz format. Choose your favorite from the ONOS website, download section ([http://downloads.onosproject.org](../../../downloads.md)). Copy the file downloaded or download the file directly from the target machine and put it in /opt. For example:

**Download ONOS**

```
sudo wget -c https://repo1.maven.org/maven2/org/onosproject/onos-releases/$ONOS_VERSION/onos-$ONOS_VERSION.tar.gz
```

**Untar the ONOS archive into /opt**

```
sudo tar xzf onos-$ONOS_VERSION.tar.gz
```

**Rename the extracted directory to "onos"**

```
sudo mv onos-$ONOS_VERSION onos
```

# Verify that ONOS works

ONOS can be run directly calling its start-stop script, located under the */opt/onos/bin* directory:

**Running ONOS using its start-stop script**

```
/opt/onos/bin/onos-service start
```

Alternatively, while in the bin directory, run ./onos-service start

The command name might be misleading. In this way, ONOS won't be run as a real Linux service. To do that, please follow [these steps](running-onos-as-a-service.md).
