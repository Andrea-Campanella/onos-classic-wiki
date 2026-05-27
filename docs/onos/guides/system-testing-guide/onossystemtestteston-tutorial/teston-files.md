# TestON Files

# Test files

Test files are located in the [/TestON/tests/](https://github.com/opennetworkinglab/ONLabTest/tree/master/TestON/tests) folder.  Each test contains a set of files defined below:

* [.params](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.params) - This file contains user defined variables, as well as specifies the order of which test cases to run.
* [.topo](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.topo) - This file defines the components and options that TestON will use to execute the test. User name, password, IP addresses, drivers, and/or a Mininet topology are specified in this file. (Please use the **exact** syntax/format in the .topo file. The space character in the xml tags is important even if nothing is defined in the tag. Eg. <COMPONENTS> </COMPONENTS>)
* [.py](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.py) - This is where test cases are written. Test cases call upon functions implemented in their respective drivers to create a progression of events that produce a pass/fail outcome.

The test folder name is the name of the test, as well as the names of the .py, .params, and .topo files.

### SAMPstartTemplate\_1node and SAMPstartTemplate\_3node tests:

These tests demonstrate several simple actions using TestON. The test is successful if all test cases succeed.

* CASE0:   Pulls ONOS code and builds ONOS.  This is usually skipped in the production environment for flexibility to handle testing different versions of ONOS
* CASE1:   Sets up global test variables and removes existing instances of ONOS in the test cell
* CASE2:   Reports errors, warnings, and exceptions in ONOS
* CASE10: Starts ONOS on the cell
* CASE11: Starts Mininet and assign mastership of switches to ONOS controllers
* CASE12: Tests some basic ONOS commands using the ONOS cli handle
* CASE22: Tests some basic ONOS commands using the REST API handle
* CASE32: Configures fwd app and run pingall

### Params File:

Below is the SAMPstartTemplate\_1node**.params** file:

```
<PARAMS>
    <!--
        CASE0: pull onos code - this case should be skipped on Jenkins-driven prod test
        CASE1: setup and clean test env
        CASE2: get onos warnings, errors from log
        CASE10: start a 1-node ONOS
        CASE11: Start Mininet and assign controllers
        CASE12: Sample case of using onos cli
        CASE22: Sample case of using onos rest
        CASE32: Configure fwd app
    -->

    <testcases>0,1,10,11,12,22,2,32</testcases>
    <GIT>
        <pull>False</pull>
        <branch>master</branch>
    </GIT>

    <CASE0>
    </CASE0>

    <CASE1>
        <NodeList>OC1</NodeList>
        <SleepTimers>
            <onosStartup>60</onosStartup>
            <onosCfg>5</onosCfg>
            <mnStartup>15</mnStartup>
            <mnCfg>10</mnCfg>
        </SleepTimers>
    </CASE1>

    <CASE10>
        <numNodes>1</numNodes>
        <Apps>
            org.onosproject.openflow,org.onosproject.fwd
        </Apps>
        <ONOS_Configuration>
            <org.onosproject.net.intent.impl.compiler.IntentConfigurableRegistrator>
                <useFlowObjectives>true</useFlowObjectives>
                <defaultFlowObjectiveCompiler>org.onosproject.net.intent.impl.compiler.LinkCollectionIntentObjectiveCompiler</defaultFlowObjectiveCompiler>
            </org.onosproject.net.intent.impl.compiler.IntentConfigurableRegistrator>
        </ONOS_Configuration>
    </CASE10>

    <CASE11>
        <topo> mn --topo tree,3,3 </topo>
    </CASE11>
    <CASE12>
    </CASE12>
    <CASE22>
    </CASE22>
    <CASE32>
    </CASE32>
</PARAMS>
```

The <testcases> tag defines the order in which the test cases in the .py file are executed. <PARAMS> and <testcases> are mandatory, case sensitive tags.

### Topo File:

Below is the SAMPstartTemplate\_1node**.topo** file:

```
<TOPOLOGY>
    <COMPONENT>
    <!--
        This is a list of all components and their handles in the test setup.
        Even with some handles not used in test cases, we want to define
        all onos cells here, for cases to set up onos cluster.
    -->
        <ONOScell>
            <host>localhost</host>  # ONOS "bench" machine
            <user>sdn</user>
            <password>rocks</password>
            <type>OnosClusterDriver</type>
            <connect_order>1</connect_order>
            <home></home>   # defines where onos home is on the build machine. Defaults to "~/onos/" if empty.
            <COMPONENTS>
                <cluster_name></cluster_name>  # Used as a prefix for cluster components. Defaults to 'ONOS'
                <diff_clihost></diff_clihost> # if it has different host other than localhost for CLI. True or empty. OC# will be used if True.
                <karaf_username></karaf_username>
                <karaf_password></karaf_password>
                <web_user></web_user>
                <web_pass></web_pass>
                <rest_port></rest_port>
                <prompt></prompt>
                <onos_home></onos_home>  # defines where onos home is on the target cell machine. Defaults to entry in "home" if empty.
                <nodes> 1 </nodes>  # number of nodes in the cluster
            </COMPONENTS>
        </ONOScell>

        <Mininet1>
            <host>OCN</host>
            <user>sdn</user>
            <password>rocks</password>
            <type>MininetCliDriver</type>
            <connect_order>2</connect_order>
            <COMPONENTS>
                <home>~/mininet/custom/</home>
                <prompt></prompt>
            </COMPONENTS>
        </Mininet1>

    </COMPONENT>
</TOPOLOGY>
```

The .topo file includes the login info of the machine that will run ONOS and Mininet. In this example, the test runs using two virtual machines with host IP, username, password, and driver that are defined for Mininet and ONOS components. The <type> tag specifies which driver the component will use.  The <connect\_order> tag is the connection order that TestON will execute.  In the .topo file, all tags are required, but driver specific tags may be reordered between the components tags.

**NOTE:** It is important to check the login info carefully for each component as incorrect information would result in a test failure.

### Python File:

The .py file defines the test cases.  All of the TestON tests follow the PEP8 coding style.  Check out our built-in PEP8 code checker at [/TestON/bin/codecheck](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/bin/codecheck).

Test case results should be asserted at the end of the case using the TestON [utilities class](https://github.com/opennetworkinglab/ONLabTest/blob/master/TestON/core/utilities.py).  There are four types of assertions: "equals", "matches", "greater", and "lesser". Below is an example of "equals" assertion in case 10:

**SAMPstartTemplate\_1node.py snippet**

```
main.step( "Start ONOS cluster with basic (drivers) app.")
stepResult = main.ONOSbench.startBasicONOS( nodeList=main.Cluster.getIps(),
                                            opSleep=200,
                                            onosUser=main.ONOScell.karafUser )
utilities.assert_equals( expect=main.TRUE,
                         actual=stepResult,
                         onpass="Successfully started basic ONOS cluster ",
                         onfail="Failed to start basic ONOS Cluster " )
```

### Log and Report Files

There are two ways to specify the log directory path:

1. Augmenting a command line option: --logdir "/path/to/logdirectory"
2. Adding a parameter in the .params file: 'logdir' = '/path/to/logdirectory'

Note: If the log directory path is not specified, the default log path will be used: /TestON/logs/test\_name\_time/

After test execution, there will be three types of log files:

1. test\_name\_time.log - Detailed verbose log of everything that the script does.
2. test\_name\_time.rpt - Summary report of test case results.
3. component\_name.SESSION - Log of all commands/APIs run on this component with response.

## Exploring Further

Now that you have created your test cases, you can now run your test by following the tutorial on [how to run TestON](running-teston.md). You may also improve your test by modifying the current TestON drivers or creating your own test specific drivers. Check the [TestON Drivers](teston-drivers.md) article for more information.

## Stuck? Found a bug? Questions?

Email [us](mailto:onos-discuss@googlegroups.com) if you’re stuck, think you’ve found a bug, or just want to send some feedback. Please have a look at the [guidelines](https://wiki.onosproject.org/display/ONOS/ONOS+Mailing+Lists) to learn how to efficiently submit a bug report.
