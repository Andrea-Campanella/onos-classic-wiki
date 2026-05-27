# Developer Quick Start

This Quick Start describes a simple "local" workflow where you build and run ONOS on a single development machine.

## Install Bazelisk and other dependencies

First of all, you should install Bazelisk (a wrapper for Bazel), both open-source build tools developed by Google. We will use Bazel to build and run ONOS. We suggest downloading and installing Bazelisk using the instructions at [Installing required tools](development-environment-setup/installing-required-tools.md).

Some other dependencies are required as well. Use your package manager of choice to install these:

**Other dependencies**

```
git
zip
curl
unzip
python # 2.7 required by some development scripts
python3 # Required by Bazel
bzip2 # Needed by legacy GUI build
```

Java Development Kit (JDK)

Do I need to install a JDK? The short answer is NO ![(smile)](../../../assets/smile.svg)

Starting with ONOS 2.2, we no longer require to install a JDK in your system to build and run ONOS when using Bazel, as we use a version of OpenJDK 11 that is shipped with Bazel.

However, you might still need to install a Java Runtime Environment (JRE) or JDK if you want to run some of the development tools (e.g. onos-lib-gen, etc.) or if you want to run ONOS without using Bazel. In this case, we suggest installing Amazon Corretto, a free, easy-to-install, production-grade OpenJDK build from Amazon:

<https://aws.amazon.com/corretto/>

If you plan to build and run a version of ONOS prior to 2.2, you should install JDK 8, otherwise, feel free to install the more recent JDK 11.

## Get ONOS code

To get the source code and build ONOS, run the following commands from a Unix-like terminal (e.g. Linux, MacOS):

**Download ONOS code & Build ONOS**

```
git clone https://gerrit.onosproject.org/onos
cd onos
bazel build onos
```

This will compile and assemble the installable `onos.tar.gz`, which is located in the `bazel-bin` directory.

To run ONOS locally on the development machine, simply run the following command:

**Run ONOS**

```
bazel run onos-local -- clean debug
# 'clean' to delete all previous running status
# 'debug' to enable remote debugging
```

The above command will create a local installation from the `onos.tar.gz` file (re-building it if necessary) and will start the ONOS server in the background. In the foreground, it will display a continuous view of the ONOS (Apache Karaf) log file. Options following the double-dash (–) are passed through to the ONOS Apache Karaf and can be omitted. Here, the `clean` option forces a clean installation of ONOS and the `debug` option means that the default debug port 5005 will be available for attaching a remote Java debugger.

To attach to the ONOS CLI console, run:

**Login into ONOS CLI**

```
tools/test/bin/onos localhost
```

Once connected, you can run various [ONOS CLI](../administrator-guide/interacting-with-onos/the-onos-cli.md) and Apache Karaf commands. For example, to start up OpenFlow and ReactiveForwarding app, you could do the following:

**Activate applications by ONOS CLI**

```
onos> app activate org.onosproject.openflow
onos> app activate org.onosproject.fwd
```

To open your default browser on the [ONOS GUI](../administrator-guide/interacting-with-onos/the-onos-web-gui.md) page, simply type:

**Open ONOS web page**

```
tools/test/bin/onos-gui localhost
```

or alternatively, visit <http://localhost:8181/onos/ui> 

To start up a Mininet network controlled by an ONOS instance that is already running on your development machine, you can use a command like:

**Run mininet controlled by ONOS**

```
sudo mn --controller remote,ip=<ONOS IP address> --topo torus,3,3
```

Note that you should replace `<ONOS IP address>` with the IP address of your development machine where ONOS is running.

To execute ONOS unit tests, including code Checkstyle validation, run the following command:

**Execute ONOS unit tests**

```
bazel query 'tests(//...)' | xargs bazel test		# or use 'ot' alias
```

To get access to a number of aliases (such as those mentioned above) and in general to make your development environment setup more conveniently for ONOS development, please put the following two lines in your `~/.bash_profile` or `~/.bash_aliases`.

**Customize your Bash environment**

```
export ONOS_ROOT=~/onos
source $ONOS_ROOT/tools/dev/bash_profile
```

Congratulations! The above should be enough to get you started. If you like more detailed instructions for importing the ONOS project into an IDE or contributing your changes back to the ONOS project, please consult the [Development Environment Setup](#) section.

## Building ONOS behind a web proxy

Bazel supports building behind a web proxy. Here are the steps to build with a proxy:

**Steps to build ONOS with a web proxy**

```
export HTTPS_PROXY=https://<proxy address>:<proxy port>
export HTTP_PROXY=http://<proxy address>:<proxy port>


bazel build onos --action_env=HTTP_PROXY=$HTTP_PROXY
```
