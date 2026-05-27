# Single Instance Docker deployment

This tutorial assumes that you have docker installed on your system.

You can install it on Ubuntu systems by following the instructions outlined here: <https://docs.docker.com/installation/ubuntulinux/#installation>

## Download the ONOS Docker image

The ONOS docker image is built and published on docker hub (as an automated build). You can simply obtain it by running:

```
docker pull onosproject/onos
```

Please note that this is the latest and greatest ONOS. The build occurs every time code is pushed to GitHub. There are also tagged versions available for previous versions of ONOS.

If instead you prefer a released version

```
docker pull onosproject/onos:2.1.0
```

## Environment Setup

Please do setup you environment with the ONOS developers tools

```
git clone https://gerrit.onosproject.org/onos
```

then follow

```
$ cd onos
$ cat << EOF >> ~/.bash_profile
export ONOS_ROOT="`pwd`"
source ${ONOS_ROOT}/tools/dev/bash_profile
EOF
$ . ~/.bash_profile
$ cd onos
```

## Running the ONOS Docker image

To run ONOS as a single instance:

```
docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos onosproject/onos
```

To run ONOS as a single instance with an external debugger:

```
docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --env JAVA_DEBUG_PORT="0.0.0.0:5005" --name onos onosproject/onos debug
```

To run a released version:

```
docker run -t -d -p 8181:8181 -p 8101:8101 -p 5005:5005 -p 830:830 --name onos onosproject/onos:2.1.0
```

## Operating ONOS

There are two complementary methods: GUI or CLI. Some operations might be only available for one of such methods.

### Accessing the GUI

Point your browser to http://${YOUR\_IP}:8181/onos/ui/login.html and introduce the default ONOS credentials.

### Attaching to the CLI

To connect to the Karaf console (use the default user and credentials in Karaf):

```
docker exec -it onos /bin/bash
# Install SSH for the OS used by the selected ONOS release (e.g., "apk add openssh" or "apt install openssh-server")
ssh -p 8101 -o StrictHostKeyChecking=no karaf@localhost
```

You may now issue any CLI command.

Tips

Type "onos:" and hit the tab key to autocomplete the available commands. Once you have selected a command, you can type it and append "--help" to get specific information on it.
