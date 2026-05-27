# ONOS Remote Admin Tools

In order to make administration of an ONOS cluster easier, ONOS comes with a small set of tools that the administrator can use to interact with ONOS cluster from a remote platform, which can be either their laptop or some designated administration host.

## Downloading & Installing Admin Tools

The admin tools are available for download as a compressed tar from Maven central or from [Google drive](https://drive.google.com/file/d/1E-OqKNFuzSa_iydN04tNKb7kz9ozAb7z/view?usp=sharing). The `onos-admin-<version>.tar.gz` file can be unrolled at a desired location on the machine(s) from which the ONOS cluster will be remotely administered. The PATH environment variable should be set to include the ONOS admin tools directory, e.g:

```
# This is just an example; use actual path where you unpacked the tools
export PATH=$PATH:~/onos-admin-1.12.1-SNAPSHOT/
```

The admin tools primarily operate either using the ONOS CLI or ONOS REST API. The clients for these are the native ssh command and curl command, respectively. The ONOS CLI (ssh to port `8101`) access is secured using the `onos-user-key` command, and the ONOS REST API (curl to port `8181`) access is secured using `onos-user-password` command. Both of these commands are part of the standard ONOS distribution and are located under the top-level `bin` directory, e.g. `/opt/onos/bin`. See the following section on securing the ONOS cluster.

To simplify the remote administration it is recommended to capture the details about the ONOS cluster being managed by creating a file that will hold definitions of the ONOS cluster instances:

```
# IP addresses of the ONOS cluster nodes
export OC1=10.192.19.101
export OC2=10.192.19.102
export OC3=10.192.19.103
export OC4=10.192.19.104
export OC5=10.192.19.105

# Provide a list of all ONOS instances using the above variables
export ONOS_INSTANCES=“$OC1 $OC2 $OC3 $OC4 $OC5"

# Optionally export ONOS web user/password if non-default ones are used
export ONOS_WEB_USER=onos
export ONOS_WEB_PASS=rocks
```

Save this file under a name that will make it easy to remember which ONOS deployment cluster it refers to.

Then to set the environment to point to that ONOS pod, simply source in the file, e.g.:

```
$ source ~/pod42 # source in pod42 from home directory
```

After this, and after exporting the `PATH` environment variable as indicated above, you should be able to type in the following commands to manage the cluster, e.g.:

```
$ onos # CLI to the first instance $OC1
$ onos 3 # CLI to the third instance $OC3
$ onos ipaddress # CLI to the ONOS at the given IP
$ onos 2 summary # execute “summary” CLI on 2nd instance $OC2
$ onos-diagnostics # collect ONOS diagnostics on the entire cluster
...
```

The above are just a few examples. Any of the ONOS admin commands that are intended to command a specific instance take the numeric argument or IP address as the first argument. These include `onos`, `onos-app`, `onos-netcfg`, etc.

## Securing ONOS Cluster

To configure passwordless CLI access, the operator must run `onos-user-key` tool as follows from each machine in the cluster. This tool is available under the ONOS `bin` directory.

```
$ onos-user-key onos AAAAB3NzaC1yc2EAAAADAQABAAABAQC4pL/Jzlm/jq7ltDVIb4CEIUXxYEK...
```

Similarly, it is recommended to change the default username and password for the REST API using `onos-user-password` tool on each ONOS cluster node as follows:

```
$ onos-user-password onos superSecretPassword
```

By configuring the ONOS cluster in this manner, not only it will become more secure, it will also become more convenient to manage using automated tools without having to enter credentials each time.

## Documentation & Example Usage

The following sections provides a quick overview of the individual administrative tools and their usage.

### onos-diagnostics

The onos-diagnostics tool collects various information from the running ONOS cluster and packages it into one, easy-to-share archive file. This tool is distributed as part of the ONOS software itself (under bin directory), but is also available as part of a small archive of remote tools to administer an ONOS cluster (onos-admin-\*.tar.gz).

In order to run the onos-diagnostics tool, the machine/account from which the tool runs must be allowed to remotely connect to the ONOS CLI. This is accomplished by registering the user’s public RSA/DSA key with each ONOS instance. To make this easier another tool onos-user-key has been provided as part of the base ONOS distribution to modify the ONOS configuration appropriately to make this possible and, equally important, to make the ONOS deployment secure.

Since the tools contacts all ONOS node cluster instances, it needs to know the IP addresses of those machines. To avoid having to specify these IP addresses as part of the command, you can export the ONOS\_INSTANCES environment variable to specify the addresses as a space-separated list. Here’s an example of how to set the variable:

```
$ export ONOS_INSTANCES="10.192.19.111 10.192.19.112 10.192.19.113"
```

The tool also accesses the ONOS REST API to collect logs and for this it requires the REST API username and password credentials. These credentials can be provided either via ONOS\_WEB\_USER and ONOS\_WEB\_PASSWD environment variables or via command options (see usage below)

Once enabled, the onos-diagnostics tool can be run as follows:

```
$ onos-diagnostics
```

There is an option that allows for naming the resulting archive file for differentiation between different cluster instances, e.g.

```
# This will produce archive file /tmp/delta-pod-diags.tar.gz
$ onos-diagnostics -n delta-pod
```

By default onos-diagnostics will use ONOS\_PROFILE to collect the diags. We use the [profiles](https://github.com/opennetworkinglab/onos/blob/master/tools/package/runtime/bin/onos-diagnostics-profile) to customize the behavior of the tool.

The resulting /tmp/\*-diags.tar.gz file will contain all relevant information about the ONOS cluster.

The following is the usage help for the onos-diagnostics tool:

```
usage: onos-diagnostics [-x] [-n name] [-u user] [-p password] [ip1 ip2...]
Environment Variables:
   DIAGS_PROFILE     Profile to be used to collect diags.
                     Availables profiles in onos-diagnostics-profile
   ONOS_INSTANCES    IPs or hostnames of ONOS cluster machines
   ONOS_WEB_USER     username for REST API
   ONOS_WEB_PASS     password for REST API
Example Usages:
   # Collect compressed diagnostics for the cluster.
   # REST API user and password are drawn from environment variables.
   # Collection archive will be named /tmp/onos-diags.tar.gz
   # The cluster node IPs will be drawn from ONOS_INSTANCES variable.
   # Diags profile is drawn from environment variable.
   $ onos-diagnostics
   # Collect diagnostics for the cluster and leave them extracted.
   # Collection directory will be named /tmp/prague-diags/
   # Collection archive will be named /tmp/prague-diags.tar.gz.
   # REST API user name is 'onos' and password is 'rules'.
   # The cluster node IPs will be drawn from ONOS_INSTANCES variable.
   $ onos-diagnostics -x -n prague -u onos -p rules
   # Collect diagnostics for the cluster and store them in JSON files.
   # JSON_CLI_COMMANDS below lists JSON-supported diagnostics commands.
   # Collection archive will be named /tmp/onos-diags.tar.gz
   $ onos-diagnostics -j
   # Collect compressed diagnostics for a cluster.
   # REST API user name is 'onos' and password is 'rules'.
   # Collection archive will be named /tmp/onos-diags.tar.gz
   # The cluster node IPs are listed explicitly.
   $ onos-diagnostics -u onos -p rules 172.17.0.11 172.17.0.12 172.17.0.1
```

### onos-diagnostics-k8s

Alternatively, it is possible to use onos-diagnostics-k8s in Kubernetes enabled environments. The tool will produce the same results of onos-diagnostics and relies only on kubectl commands.

The tools needs to know the names of the pods. To avoid having to specify these names as part of the command, you can export the ONOS\_PODS environment variable to specify the names as a space-separated list. Here’s an example of how to set the variable:

```
$ export ONOS_PODS="onos-0 onos-1 onos-2"
```

The tool needs to know the Karaf home (path from the mount point). To avoid having to specify this path as part of the command, you can export the KARAF\_HOME environment variable:

```
$ export KARAF_HOME="apache-karaf-4.2.8"
```

Once enabled, the onos-diagnostics-k8s tool can be run as follows:

```
$ onos-diagnostics-k8s
```

The following is the usage help for the onos-diagnostics-k8s tool:

```
usage: onos-diagnostics-k8s [-x] [-j] [-n name] [-k karaf_home] [pod1 pod2...]
Environment Variables:
    DIAGS_PROFILE     Profile to be used to collect diags.
                      Availables profiles in onos-diagnostics-profile
    KARAF_HOME        KARAF_HOME inside the ONOS pod (path from the mount point)
    ONOS_PODS         ONOS pods composing the cluster
Example Usages:
    # Collect compressed diagnostics for the cluster.
    # Karaf home is drawn from environment variable.
    # Collection archive will be named /tmp/onos-diags.tar.gz
    # ONOS pods names will be drawn from ONOS_PODS variable.
    # Diags profile is drawn from environment variable.
    $ onos-diagnostics-k8s 
    # Collect diagnostics for the cluster and leave them extracted. 
    # Collection directory will be named /tmp/prague-diags/
    # Collection archive will be named /tmp/prague-diags.tar.gz.
    # Karaf home is '/root/foo/karaf'.
    # ONOS pods names will be drawn from ONOS_PODS variable.
    $ onos-diagnostics-k8s -x -n prague -k karaf
    # Collect diagnostics for the cluster and store them in JSON files.
    # JSON_CLI_COMMANDS below lists JSON-supported diagnostics commands.
    # Collection archive will be named /tmp/onos-diags.tar.gz
    $ onos-diagnostics-k8s -j
    # Collect compressed diagnostics for a cluster.
    # Karaf home is 'karaf'.
    # Collection archive will be named /tmp/onos-diags.tar.gz
    # The pods names are listed explicitly.
    $ onos-diagnostics-k8s -k karaf onos-0 onos-1 onos-2
```

### onos-log-query

Since ONOS Apache Karaf log can be spread across multiple files, i.e. `karaf.log`, `karaf.log.1`, `karaf.log.3`, etc. and since each ONOS cluster node has its own set of such logs, it can be cumbersome to find relevant information in the logs purely manual means. The `onos-log-query` tool has been provided to make log stitching, filtering and collating much easier. The tool can operate on standalong log files, but it works well with information collected via the `onos-diagnostics` tool.

The tool is designed to splice together the different `karaf.log*` files and then to optionally to narrow them to include only the specified date/time interval. This is done using the `-f` and `-t` options. Since the splicing and filtering operation may take some time, the tool stores the processed output into a separate file, which by default is called `query.log`. This name can be changed using the `-n` option. This allows the user to keep results of multiple different queries and it also allows other types of processing to be applied on these files using other external tools without repeatedly incurring the cost of stitching and filtering a potentially very large data-sets.

The simplest way to run the tool is from the root of the directory produced by unrolling the ONOS diagnostics archive, which is where the node-level directories are. For example, to stitch and filter the logs to only focus on the specific duration of output, you could do the following:

```
$ onos-log-query -x -f "2018-04-25 13:04:30" -t "2018-04-25 13:10:00" -n anomaly
```

This will produce stitched and filtered versions of the log for each individual node, as well as a collated version containing merge of all node logs. These files will be called `anomaly.log`; there will be one for each of the nodes in the respective node directory and also the collated one at the top-level directory.

The -f flag specifies the start of the time period (inclusive) and the -t flag specified the end of the tim period (also inclusive). If either is not specified, the logs will be included from the beginning or until the end. The `-x` option indicates that only timestamped log entries should be included, which means stack-traces and other multi-line log entries will be reduced to just the time-stamped line of the log. The -n option allows you to provide a custom name under which your results should be saved; if not specified, the logs will be stored in `query.log` files.

### onos-app

To facilitate remote management of ONOS applications the onos-app tool has been provided as a way to easily upload new application binaries via REST API. Of course, applications can also be listed, uninstalled, activated and deactivated using the CLI, but installation of apps via CLI only allows installing apps via a URL to application binaries located on a web-server elsewhere. The onos-app tools allows uploading application OAR file from the administration machine directly.

The following is the usage:

```
usage: onos-app [options] <node-ip> list
       onos-app [options] <node-ip> {install|install!} <app-file>
       onos-app [options] <node-ip> {reinstall|reinstall!} [<app-name>] <app-file>
       onos-app [options] <node-ip> {activate|deactivate|uninstall} <app-name>
options: [-P port] [-u user] [-p password] [-v]
```

For example, to upload a super duper ONOS app, whose binaries are located locally in a file `~/onos/apps/super-duper-6.28.oar` file, to the ONOS cluster through one of its instances at `10.45.32.69`, you would use the following command:

```
$ onos-app 10.45.32.69 install! ~/onos/apps/super-duper-6.28.oar
```

The `!` postfix in the  `install!` and `reinstall!` commands indicates that the application should also be activated immediately after the installation. Otherwise, the commands mean what their names clearly imply.

### onos-compile-yang

ONOS supports dynamic YANG compilation via GUI and via REST API. To make this even more convenient, the onos-compile-yang command has been provided. Internally, it uses the REST API, but should be far easier to use from the remote Unix shell.

```
usage: onos-compile-yang [-P port] [-u user] [-p password] [-v] \
          <yang-file|zip-file|jar-file|directory>
```

The command allows uploading and compiling an individual `.yang` file, or a collection of yang files located in a given `.zip` file, `.tar.gz` file or even just a plain local directory. YANG compilation will result in generation of Java classes from the included YANG models, compilation of those classes into an ONOS application `.oar` bundle and automatic installation and activation of the application. The newly registered YANG models can be immediately listed via YANG REST API, GUI or CLI commands. The appllication will derive it's name and identifier from the name of the uploaded file or directory. It can be seen among the list of applications installed and active on the running ONOS cluster.

For example, to upload, compile and register `some-funky-model.yang` file, one could do the following:

```
$ onos-compile-yang 10.45.32.69 ~/models/some-funky-model.yang
```

Notice that the ONOS cluster does not need to be rebuilt, stopped or reconfigured in any way. Once can simply dynamically add and remove YANG models at will.

### onos

The onos command is simply a convenience wrapper that allows the administrator to securely open the ssh session to any of the ONOS cluster nodes. As with all the admin commands, one can use either the DNS name, IP address or a numeric index of the ONOS node - provided the OC# environment variables have been properly setup. The following are examples of usage:

```
$ onos 1 summary		# Invoke summary command on the first ONOS instance
$ onos 10.45.32.69		# Open interactive CLI session on the ONOS instance at the specified IP
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

onos>
```

### onos-cfg

......

onos-netcfg

......

onos-create-app

......
