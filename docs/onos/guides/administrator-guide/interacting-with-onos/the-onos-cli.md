# The ONOS CLI

This section describes ONOS's Karaf-based CLI.

## Overview

The ONOS CLI is an extension of Karaf's CLI. As a result, it is capable of leveraging features such as programmatic extensibility, the ability to load and unload bundles (among others), and SSH access.

## Accessing the CL**I**

To access the CLI directly **from a target machine**, refer to [these](../installing-and-running-onos/accessing-the-cli-and-gui.md) instructions.

If you're deploying ONOS **from a management machine**, the *`onos`* command can be used to attach to a remote ONOS instance (i.e. without logging in first). For example, to access the CLI of an ONOS running on a target machine at 192.168.56.30:

```
$ onos 192.168.56.30
```

Both **Ctrl-D** and `logout` exits the CLI.

## ONOS Commands

ONOS supplies a set of its own commands.**`help onos`** lists the available commands:

```
onos> help onos
COMMANDS
onos:add-flows                  Installs a flow rules                                                                                                                                                                                           
onos:add-host-intent            Installs host-to-host connectivity intent                                                                                                                                                                       
onos:add-multi-to-single-intent Installs point-to-point connectivity intent                                                                                                                                                                     
onos:add-node                   Adds a new controller cluster node
onos:add-optical-intent         Installs optical connectivity intent 
 
...
```

The commands can be invoked as either `onos:<command>` or `<command>` by itself. Some of these commands have further descriptions that can be seen with `help onos:<command>.`

```
onos> help onos:add-flows
DESCRIPTION
        onos:add-flows

	    Installs a flow rules

SYNTAX
        onos:add-flows [options] flowPerDevice numOfRuns 

ARGUMENTS
        flowPerDevice
                Number of flows to add per device
        numOfRuns
                Number of iterations
OPTIONS
        --help
                Display this help message
        -j, --json
                Output JSON
```

[Appendix A](../appendix-a-cli-commands.md) provides a listing of the currently available CLI commands.

## Bundle Management

Karaf's CLI commands are useful for managing the bundles (modules) that comprise the running ONOS instance. For example, **`list`** can be used to show all loaded modules:

```
onos> list
START LEVEL 100 , List Threshold: 50 
 ID | State  | Lvl | Version          | Name
------------------------------------------------------------------------------
 37 | Active |  80 | 0.0.0            | samples                               
 41 | Active |  80 | 2.6              | Commons Lang                          
 42 | Active |  80 | 3.3.2            | Apache Commons Lang                   
...
156 | Active |  80 | 1.1.0.SNAPSHOT   | onos-core-common                      
157 | Active |  80 | 1.1.0.SNAPSHOT   | onos-core-dist                        
158 | Active |  80 | 1.1.0.SNAPSHOT   | onos-core-serializers                 
159 | Active |  80 | 1.1.0.SNAPSHOT   | onlab-netty                           
168 | Active |  80 | 1.1.0.SNAPSHOT   | onos-app-proxyarp 
onos>
```

[Appendix C](../../developer-guide/appendix-c-source-tree-organization.md) provides a listing of the available ONOS bundles for the stable release.

---

[Previous : Interacting with ONOS](../interacting-with-onos.md)  
[Next : The ONOS Web GUI](the-onos-web-gui.md)

---
