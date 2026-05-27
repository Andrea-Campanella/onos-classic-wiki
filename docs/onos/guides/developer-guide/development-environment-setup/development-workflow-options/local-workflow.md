# Local workflow

This local workflow is simple, quick to start up, and recommended for developers who wish to run a single instance of ONOS, locally on a development machine.

Running ONOS locally

To run ONOS locally on the development machine, simply run the following command:

```
cd $ONOS_ROOT
bazel run onos-local clean debug
```

The above command will create local installation from the `onos.tar.gz` file and will start it in the background. In the foreground, it will display a continuous view of the ONOS (Apache Karaf) log file. Options following the double-dash (–) are passed through to the ONOS Apache Karaf and can be omitted. Here, the `clean` option forces a clean installation of ONOS and the `debug` option means that the default debug port 5005 will be available for attaching a remote debugger.

# Attaching to the ONOS console

To attach to the ONOS CLI console, run:

```
$ONOS_ROOT/tools/test/bin/onos localhost
```

Once connected, you can run various ONOS CLI and Apache Karaf commands.

# Opening the ONOS web GUI

To open your default browser on the ONOS GUI page, simply type:

```
$ONOS_ROOT/tools/test/bin/onos-gui localhost
```

or alternatively visit <http://localhost:8181/onos/ui>
