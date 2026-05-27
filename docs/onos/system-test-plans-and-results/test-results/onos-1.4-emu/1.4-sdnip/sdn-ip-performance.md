# SDN-IP Performance

SDNIPperf at 30 Sep 2015 08:19:58
> commit e4efe458a7fd89dda85b6d32c2e50054e4d7a2f6 (HEAD, master)  
> Author: Sho SHIMIZU [sshimizu@us.fujitsu.com]  
> AuthorDate: Wed Aug 26 15:06:55 2015 -0700  
> Commit: Gerrit Code Review [gerrit@onlab.us]  
> CommitDate: Wed Aug 26 22:24:57 2015 +0000  
>   
> Use LF as line separator

### Case 100: Setting up test environment - PASS

* 100.1 Applying cell variable to environment - No Result ![(warning)](../../../../../assets/warning.svg)
* 100.2 Git pull - No Result ![(warning)](../../../../../assets/warning.svg)
* 100.3 Using mvn clean install - No Result ![(warning)](../../../../../assets/warning.svg)
* 100.4 Creating ONOS package - No Result ![(warning)](../../../../../assets/warning.svg)
* 100.5 Installing ONOS package - No Result ![(warning)](../../../../../assets/warning.svg)
* 100.6 Checking if ONOS is up yet - PASS ![(tick)](../../../../../assets/check.svg)

### Case 9: This case is to testing the performance of SDN-IP with single ONOS instance - FAIL

* 9.1 Get devices in the network - No Result ![(warning)](../../../../../assets/warning.svg)
* 9.2 Get links in the network - No Result ![(warning)](../../../../../assets/warning.svg)
* 9.3 Sleep 1200 seconds - No Result ![(warning)](../../../../../assets/warning.svg)
* 9.4 Checking routes installed - FAIL ![(error)](../../../../../assets/error.svg)

+ \*\*\*Routes in SDN-IP are wrong!\*\*\*

* 9.5 Checking MultiPointToSinglePointIntent intents installed - FAIL ![(error)](../../../../../assets/error.svg)

+ \*\*\*MultiPointToSinglePoint intent number is wrong!\*\*\*
