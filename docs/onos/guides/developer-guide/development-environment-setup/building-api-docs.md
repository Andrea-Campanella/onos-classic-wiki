# Building API docs

## Building API Docs

To *read* the current ONOS Java API documentation (javadoc), go to **[api.onosproject.org](http://api.onosproject.org)** .

If you wish to build your own local ONOS Java API documentation bundle, you can use Bazel directly as follows:

**Build ONOS Java API documentation**

```
bazel build //docs:external
```

The above will build the external Java API docs comprising only of those interfaces and classes that are considered part of the ONOS SDK, thus omitting much of the internal implementation classes. The result is available in `bazel-bin/docs/external.jar` file.

If you wish to build the Java API docs for the entire source tree, including all internal implementation classes, you can use the following:

**Build ONOS Java API internal documentation**

```
bazel build //docs:internal
```

Similarly, The result is available in `bazel-bin/docs/internal.jar` file.

Alternatively, you can use the `onos-build-docs` utility, which uses Bazel to generate both internal and external sets of documentation. You can uncompress the jar files in a location of your choice and then open the top-level `index.html` file in your favourite web browser.
