# OnosSystemTest/TestON Framework Architecture Overview

# 

## TestON/Core

The TestON core is where the test is parsed and executed. It is also where the test components are initialized and logging happens. There’s no need to go into the nuances of the architecture because you do not need it to create or run a test. However, it is important to note that because the TestON core handles the parsing of the test cases, exceptions will be be thrown from here rather than the testname.py where the exception probably originated. This is why it is a good idea to incase your code with try-except blocks to make it easier to debug.

## Drivers

The python driver files are a collection of functions that belong to a specific test component, e.g., Mininet1 or ONOScli1. Each function performs a single component’s functionality or some variation of it. For example, there exists a Mininet driver function that calls the pingall command in Mininet and handles all the possible exceptions that might occur with this command. Similar to a dependency file, these are helper or wrapper functions that are commonly used throughout our tests. The main advantages behind a driver function are to encapsulate the components functionality, hide the tediousness of pexpect, and reduce duplicate code. If you are looking to test a specific functionality of ONOS
