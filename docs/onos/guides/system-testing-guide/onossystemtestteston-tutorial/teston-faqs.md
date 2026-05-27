# TestON FAQs

# FAQs about TestON

#### *Could not connect to hosts machine during test?*

1. Carefully check the components in the .topo file. Check the correctness of component's log in information. See this example of a [.topo](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.topo) file.
2. Make sure you can SSH ,without password , to the test bench machine as well as the other machine in your test environment.
3. It is possible that you did not specify the ONOS user in your cell file , by default, the ONOS user would be "sdn" so the host name in your ONOS machine should be named "sdn". In your cell file, you can add "export ONOS\_USER = *nameOfyourHostMachine*" and "export ONOS\_GROUP=*nameOfyourHostMachine*". Check your environment by executing "env" command.

#### *Applying cell to environment could not execute?*

1. Normally you run the bash script to initialize your environment you can access the bash profile at ONOS/tools/dev/ directory. Copy and paste the bash\_profile to your root directory and rename it to .bash\_profile. Edit the .bashrc file in your root directory to execute the profile during log in to the machine by adding ". ~/.bash\_profile" at the end of the file.
2. The cell name may not get recognize by the machine, make sure you have the correct cell name in the [.params](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.params) file.

#### *Running pingall function and could not reach all the host*?

1. In common cases, the pingall reach most of the hosts but not all of it so the pingall would still fail because not all the hosts got pinged.
2. Make sure you assign the correct controller to the switches in your test cases before you actually do pingall. See the [SAMPstartTemplate\_1node](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_1node/SAMPstartTemplate_1node.py) or [SAMPstartTemplate2\_3node](https://github.com/opennetworkinglab/OnosSystemTest/blob/master/TestON/tests/SAMP/SAMPstartTemplate_3node/SAMPstartTemplate_3node.py) on how to properly assigning controller to the switches.
3. Always do a manual check if your current version of ONOS does not have problem regarding its internal application. Some of the commit can be messed up and if pulled to your repository can affect internal application in ONOS such. You can git reset to the older commit of the ONOS and stick with the most stable commit if you are trying on testing since not all commits are different from each other. You might need to fully reinstall ONOS if some of the application won't run during manual testing.
4. Each time you run your test make sure there are no Mininet instance running. Always execute "sudo mn -c" before you run your test.

#### *How to run Mininet during test?*

1. In the .topo file you can modify the  the Mininet components such as the topology, controller etc. by editing the args tag.
2. You can also create your own custom topology using python and pass that file in the startNet function. The startNet function is in the "mininetclidriver.py" in the TestON drivers directory.

#### *Pexpect causing error?*

1. Make sure you installed python packages configObj and pexpect.
2. Try printing the repr() of the pexpect buffer. There are sometimes non-printable characters( color codes, ESC, ...) that will be in the middle of the expected output causing the regex to not match.

**NOTE**: More TestON questions and solutions will be added in the future.

Questions or concerns not featured here? Send us an email at [onos-test@onosproject.org](mailto:onos-test@onosproject.org), or subscribe to the [ONOS Test Google Group](https://groups.google.com/a/onosproject.org/forum/#!forum/onos-test).
