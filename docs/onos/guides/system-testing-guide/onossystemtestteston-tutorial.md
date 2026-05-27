# OnosSystemTest/TestON Tutorial

Architecture Overview

# 

TestON for ONOS: Paxterra’s TestON is made out of a set of drivers that connect to various components. In our case, these components will be ONOS and Mininet, and can be pointed to either the same or different IP addresses. TestON manipulates these components through a set of ssh handles created using Python’s pexpect. The test structure is comprised of a set of different tests, each with a number of test-cases inside. Each test-case returns a pass/fail result and can stand alone in theory. However, more complete tests can be created by running multiple test-cases in series, which will return a percentage pass/fail result of all the containing test-cases. There will be certain test-case combinations that make more sense then others, and they will be placed in a sensible order, but in the end it is up to the user to determine logical sequences that produce meaningful data.

* TestON/Core: The TestON core is where the test is parsed and executed. It is also where the test components are initialized and logging happens. Because TestON core parses test cases, exceptions will be be thrown from TestON core, rather than the test case location in the Python file where the exception probably originated. Encasing test case code with try-except blocks may ease the debugging process when an exception occurs.
* Drivers: The Python driver files are a collection of functions that belong to a specific test component (e.g., Mininet1 or ONOScli1).  Driver functions perform stock or variations of functions from a single component. For example, there exists a Mininet driver function that calls the pingall command in Mininet and handles all the possible exceptions that might occur with this command. Similar to a dependency file, these are helper or wrapper functions that are commonly used throughout our tests. The main advantages behind a driver function are to encapsulate the components functionality, hide the tediousness of pexpect, and reduce duplicate code.

Test Suite File Structure: There are three main files that define a specific test in TestON:

* Topology file ( .topo ) This file defines all the components and options that TestON will use to execute its test. For example, the .topo file would include the login info and Mininet parameters for the machine that was going to host Mininet for the test. At the beginning of the test, TestON will automatically connect all components.
* Parameters file ( .params ) This is a custom file in which commonly configured variables can be placed in order to modularize the test cases.
* Python file ( .py ) This is where all of the test-cases are written. TestON calls upon functions implemented in the respective drivers to create a progression of events that produces a pass/fail outcome.

You can start by:

* [Installing TestON](onossystemtestteston-tutorial/installation.md)
* [Creating your test files](https://wiki.onosproject.org/x/iI8g)
* [Running TestON](onossystemtestteston-tutorial/running-teston.md)
* [Creating your own drivers](onossystemtestteston-tutorial/teston-drivers.md)
