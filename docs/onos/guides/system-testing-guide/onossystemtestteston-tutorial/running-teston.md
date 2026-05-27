# Running TestON

In the OnosSystemTest/TestON/bin folder, you may run a test by specifying "run", then the test name:

```
$ ./cli.py run SAMPstartTemplate_1node
```

Alternatively, you may specify your own .params and .topo file in the cli arguments:

```
$ ./cli.py run SAMPstartTemplate_1node --params-file SAMPstartTemplate_1node.params --topo-file SAMPstartTemplate_1node.topo
```

Ensure your .params and .topo file are in the test directory (ie: in OnosSystemTest/TestON/tests/SAMP/SAMPstartTemplate\_1node/ ).

**NOTE:** If you stop a test while running (by ^C or ^D), make sure to clean up before running a new test:

```
$ ./cleanup.sh
```

This will run various scripts to clean up any currently running ONOS, TestON, and Mininet.

## Stuck? Found a bug? Questions?

Visit the [Test Files](teston-files.md) page to learn more about the files necessary to run tests.  Email [us](mailto:onos-discuss@googlegroups.com) if you’re stuck, think you’ve found a bug, or just want to send some feedback. Visit the [guidelines](../../contributor-guide/issue-tracking-and-submission-with-jira/using-jira-to-create-an-issue-bugs-feature-requests-documentation.md) to learn how to efficiently submit a bug report.
