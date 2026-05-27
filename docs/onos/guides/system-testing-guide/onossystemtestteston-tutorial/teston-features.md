# TestON Features

* [Retry function](#TestONFeatures-RetryFunction)
* [Skip Case function](#TestONFeatures-SkipCase)
* [Pause Test function](#TestONFeatures-PauseTest)
* [Command line arguments](#TestONFeatures-CommandLineArguments)
* [CHO framework](#TestONFeatures-CHOFramework)

##### Retry Function

Available from driver functions or test cases as utilities.retry, this function allows the test to retry a function when certain conditions are met.

The retry function takes several arguments:

* f - A callable object such as a function
* retValue - Return value(s) of f to retry on. This can be a list or an object.
* args - (Optional) A tuple containing the arguments of f.
* kwargs - (Optional) A dictionary containing the keyword arguments of f.
* sleep - (Optional) Time in seconds to sleep between retries. If random is True, this is the max time to wait. Defaults to 1 second.
* attempts - (Optional) Max number of attempts before returning. If set to 1, f will only be called once. Defaults to 2 trys.
* random - (Optional) Boolean indicating if the wait time is random between 0 and sleep or exactly sleep seconds. Defaults to False.

Example:

```
# Retry on onosdriver's isup function. Will call isup up to 5 times with a 5 second sleep in between attempts.
started = utilities.retry( main.ONOSbench.isup, main.FALSE, kwargs={"node":"10.0.0.1"}, sleep=5, attempts=5 )
```

##### Skip Case

Will skip the rest of the code in a test case. The case results will be determined as normal based on completed assertions unless the result argument is given.

Optional Arguments:

* result - Case insensitive string. Can be 'PASS' or 'FAIL' and will set the case result accordingly.
* msg - Message to be printed when the case is skipped in the reports.

Example:

```
# Init Step
if not result:
	main.skipCase()
# Other steps that require Init Step to succeed
```

##### Pause Test

Stops the test and interfaces with Python Debugger (pdb).

Type 'h' for help, 'n' to step, 'c' to continue, and 'q' to end test.

```
main.stop()
```

##### Command Line Arguments

When running TestON from the command line, the following arguments are supported: logdir, mail, example, tester, testcases, and onoscell.

Example:

```
# The following command only runs cases 0 and 1 in FUNCflow test
$ ./cli.py run FUNCflow testcases 0,1
```

Besides this,TestON CLI now also support "–params" option, followed by "KEY\_1/KEY\_2/.../KEY\_n=VALUE". This will try to modify the corresponding value (<KEY\_1><KEY\_2>...<KEY\_n> VALUE) read by TestON from the test's .params file. It helps when we want to modify .params file for minor configuration changes from time to time.

Example:

```
# The following command will modify the <TEST><flowObj> value read from "SCPFintentEventTp.params" file before the test begins
$ ./cli.py run SCPFintentEventTp --params TEST/flowObj=True
```

It is also supported to specify different .topo and .params files from command line by using "--topo-file" and "--params-file" options.

Example:

```
# The following command will run SRMulticast test with "SRMulticast.topo.flex" topo file
$ ./cli.py run SRMulticast --topo-file SRMulticast.topo.flex --params-file SRMulticast.params.flex
```

##### CHO Framework

CHO (Continuous Hours of Operation) test runs on an experimental framework called CHOTestMonkey inside TestON. Instead of running a predefined sequence of test cases, CHOTestMonkey breaks test cases into atomic test logics called events and provides a highly customizable way to organize and execute these events. With CHOTestMonkey, it becomes much easier and more flexible to maintain various pieces of test logic and assemble them in different ways for different test purposes. Please refer to [CHO Test Tutorial](cho-test-tutorial.md) page for details.
