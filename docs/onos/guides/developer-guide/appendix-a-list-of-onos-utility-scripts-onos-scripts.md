# Appendix A : List of ONOS Utility Scripts (onos-* scripts)

The following is a comprehensive list of the ONOS test/development scripts, located in *$ONOS\_ROOT/tools/test/bin*. The conventions followed here are:

* 'option' implies that the parameters are optional, unless specified otherwise
* <node-ip> is an IP address or hostname of a cell machine. This parameter is usually optional, unless specified. When omitted, the default is the value set in `$OCI`.
* 'notes' denotes remarks regarding the command, including bugs.

Please refer to [Development Environment Setup](development-environment-setup.md) and [Cells and ONOS test scripts](development-environment-setup/development-workflow-options/cells-and-onos-test-scripts.md) for information about cells, `OC` variables, and other conventions used here.

## Installation/configuration

#### *onos-install [-f] [-n] [<node-ip>]*

Installs ONOS bits on the designated cell machine.

options:

* + **-f**  : forces an uninstall. Presently, install also includes *onos-push-bits* and *onos-config* within.
  + **-n** : installation of *onos.conf* upstart configuration file will be suppressed and ONOS will not be started. Otherwise, if the option is not specified, ONOS will be ignited as a Linux daemon as the last step of the installation process.

#### *onos-package -[TDR] | --[tar|deb|rpm]*

Packages ONOS into different formats. Running the command without parameters has the same effect of running it with the --tar parameter.

options:

* + **-D, --deb**  : Creates a .deb ONOS package in /tmp
  + **-T, --tar** : Creates a .tar.gz ONOS package in /tmp
  + **-R, --rpm** : Creates a .rpm file in /tmp (this works just on centos/fedora/redhat like machines)

notes:

* + --deb only works on Debian/Ubuntu.
  + --rpm only works on on CentOS/Fedora/Redhat.

#### *onos-uninstall [<node-ip>]*

Uninstall ONOS from the designated cell machine, stopping it if needed.

#### *onos-push-bits* *[<node-ip>]*

Pushes bits produced by *onos-package* to the designated cell machine.

notes:

* + This is not yet available as a separate command.

#### *onos-config [<node-ip>]*

Configures the specified ONOS instance according to the cell definition.

notes:

* + This command is part of *onos-install*, but is provided separately should reconfiguration be needed.

## Remote CLI Monitoring

#### *onos [-w] [<node-ip> [<onos-cli-command>]]*

Attaches to the Command-line client to ONOS from a shell on the development machine.

options:

* + **-w**: Executes *onos-wait-for-start.* This option is only relevant to Linux cell machines.

notes:

* + Presently, this requires Apache Karaf to be installated the development machine; this requirement should go away eventually.

#### *onos-watch [<node-ip> [<onos-cli-command>,<onos-cli-command>,...]]*

Continuously executes the specified ONOS CLI commands using the system *watch* command. Default commands are *summary,intents,flows,hosts.*

#### *onos-batch [<node-ip> [<onos-cli-command>,<onos-cli-command>,...]]*

Executes the specified ONOS CLI commands using the Karaf console batch mode. Default commands are *summary,intents,flows,hosts.*

## Process Management

#### *onos-service [<node-ip | --cell> [stop|start|restart|status]]*

Allows remote management of the ONOS upstart daemon on the designated cell machine at <node-ip> or all cell machines.

options:

* + **-h**, **--help** : print usage
  + **<node-ip>**: the hostname or IP address of the target machine. Incompatible with *--cell*.
  + **--cell**: execute on all machines in the current cell

#### *onos-remove-raft-logs*

Stops ONOS on all cell machines and wipes the durable states stored in each machine's Raft log

#### *onos-wait-for-start [<node-ip>]*

Waits for ONOS instance to reach run-level 100, i.e. to be fully started.

#### *onos-kill [<node-ip>]*

Remotely, and unceremoniously, kills the ONOS instance running on the specified cell machine.

#### *onos-die [<node-ip>]*

Remotely, and unceremoniously, kills the ONOS instance running on the specified cell machine, and stops the upstart job to avoid ONOS from automatically reviving.

#### *onos-log [<node-ip>]*

Remotely watches the ONOS log on the specified cell machine. It operates through re-installs where the entire ONOS directory is removed. Also available under short-cut *ol.*

#### *onos-check-logs [<node-ip>]*

Remotely checks the ONOS logs to make sure they contain no *ERROR* or *Exception* messages.

#### *onos-push-update-bundle <bundle-name-pattern>*

Remotely copies the bundle with matching name to all of the cell’s machines and triggers its dynamic update without restarting Apache Karaf container. Also available under short-cut *pub*, e.g. *pub cli.*

## Cell Machine Management

#### *onos-push-keys [<node-ip>]*

Pushes user’s *.ssh/id\_rsa.pub* key to the remote cell machine and installs it for enabling password-less access.

notes:

* + This may require the user to enter the password twice; once to copy and the second time to install the keys. Once installed, passwordless access should be enabled.

#### *onos-verify-cell*

Remotely checks that passwordless access via ssh/scp works against all machines within the cell.

#### *onos-patch-vm**<node-ip> <hostname>*

Patches the *hostname* and */etc/hosts* of the cell machine specified by <node-ip> to be set to <hostname>.

options:

* + **<node-ip>** : the hostname or IP address of the target machine. Required.
  + **<hostname>** : the hostname to set for the given <node-ip>. Required.

notes:

* + if your machine appears to have a funky hostname, this is due to an old defect in this tool. To fix the hostname, simply repatch the VM using this same tool.

#### *onos-ssh [<node-ip> <command>]]*

Logs in via ssh to the remote cell machine using the standard user (sdn).

notes:

* + This is intended primarily for troubleshooting and diagnostics. Most of the testing should be done directly from the developer’s machine or test driver machine.

## Miscellaneous

#### *onos-start-network*

Remotely starts the *Solar* topology on the cell’s mininet machine against all controllers configured in the cell.

#### *onos-gui*  *[<node-ip>]*

Launches the ONOS gui in the default browser. The current GUI is *onos-gui*, which listens on *http://<node-ip>:8181/onos/ui* .

notes: 

* + Presently, this depends on the use of open command on OS/X, but it can be made to work using gnome-open to work on Ubuntu/Debian as well.
  + In the future this command will launch the main ONOS GUI.

 

#### *onos-fetch-logs [<node-ip | --cell>]*

Collects ONOS/karaf logs from designated cell machine at <node-ip> or all cell machines, to current directory.

options:

* + **-h**, **--help** : print usage
  + **<node-ip>**: the hostname or IP address of the target machine. Incompatible with *--cell*
  + **--cell**: execute on all machines in the current cell

#### onos-group [help | <command>]

Sends a command to all ONOS instances in the current cell. Currently supported commands are:

install [-f|-n], kill, patch-vm, push-keys, uninstall

These commands invoke the utility whose name is the command name prefixed with *onos-*, e.g. `onos-install` for *install*.

options:

* + **<command>**  : A command to send to the instances.
  + **help** : Displays this message and exits.

notes:

* + Hitting <TAB> will display the options for onos-group.
  + This is currently an initial cut, so commands that take inputs (e.g. push-keys) may not look streamlined.

## Shell Aliases

The following are the aliases exported by the ONOS development environment *bash\_profile*.

| alias | command |
| --- | --- |
| mci | 'mvn clean install' |
| mcis | 'mvn clean install -DskipTests -Dcheckstyle.skip -U -T 1C' |
| mis | 'mvn install -DskipTests -Dcheckstyle.skip -U -T 1C' |
| ob | 'onos-build' |
| obi | 'onos-build -Dmaven.test.failure.ignore=true' |
| obs | 'onos-build-selective' |
| obd | 'onos-build-docs' |
| op | 'onos-package' |
| ot | 'onos-test' |
| ol | 'onos-log' |
| ow | 'onos-watch' |
| oi | 'setPrimaryInstance' |
| pub | 'onos-push-update-bundle' |
| tl | '$ONOS\_ROOT/tools/dev/bin/onos-local-log' |
| tlo | 'tl | grep --colour=always -E -e "org.onlab|org.onosproject"' |
| ll | 'less $KARAF\_LOG' |
| pp | 'python -m json.tool' |
| docs | 'open $ONOS\_ROOT/docs/target/site/apidocs/index.html' |
| gui | 'onos-gui' |
| sshctl | 'onos-ssh' |
| sshnet | 'onos-ssh $OCN' |

---

Previous : Further Resources  
[Next : Appendix B : REST API](appendix-b-rest-api.md)

---
