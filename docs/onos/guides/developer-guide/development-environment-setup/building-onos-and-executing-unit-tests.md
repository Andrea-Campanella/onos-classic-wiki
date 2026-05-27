# Building ONOS and executing unit tests

> Ensure the [prerequisite tools](installing-required-tools.md) are installed first

To get the source code and build ONOS, all you need to do it run the following commands from Unix-like terminal (e.g. Linux, MacOS):

**Build ONOS 1.14 or newer**

```
$ cd $ONOS_ROOT
$ bazel build onos
```

This will compile all source code assemble the installable `onos.tar.gz`, which is located in the `bazel-out` directory.

Or for legacy ONOS versions:

**Build ONOS 1.13 or older**

```
$ $ONOS_ROOT/tools/build/onos-buck build onos --show-output
```

This will compile all source code assemble the installable `onos.tar.gz`, which is located in the `buck-out` directory. Note the`--show-output` option, which can be omitted, will display the path to this file.

To execute ONOS unit tests, including code Checkstyle validation, run the following command:

**Run unit tests for ONOS 1.14 or newer**

```
$ cd $ONOS_ROOT
$ bazel query 'tests(//...)' | xargs bazel test
```

Or for legacy ONOS versions:

**Run unit test for ONOS 1.13 or older**

```
$ $ONOS_ROOT/tools/build/onos-buck test
```
