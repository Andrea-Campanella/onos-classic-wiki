# Test Plan - Samples (SAMP*)

Proposed SAMPstartTemplate

Note: add standard license in all TestON case files (author is tracked through Gerrit and GitHub):

```
"""
Copyright 2017 Open Networking Foundation (ONF)

Please refer questions to either the onos test mailing list at <onos-test@onosproject.org>,
the System Testing Plans and Results wiki page at <https://wiki.onosproject.org/x/voMg>,
or the System Testing Guide page at <https://wiki.onosproject.org/x/WYQg>

    TestON is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    TestON is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TestON.  If not, see <http://www.gnu.org/licenses/>.
"""
```

| CASE | Details | **Pass/Fail Criteria** |
| --- | --- | --- |
| 0 | Pull specific ONOS branch, then build ONOS on ONOS Bench. This step is usually skipped, because Jenkins driven automated test environment. Jenkins jobs are to pull and build for flexibility to handle different versions of ONOS. | ONOS is set up propertly. |
| 1 | Set up global test variables. Uninstall all running cells in test environment defined in .topo file. | Test variables are constructed correctly. |
| 2 | Report errors/warnings/exceptions. | N/A (does not assert) |
| 10 | Start ONOS cluster | ONOS CLIs are started and configurations are set. |
| 11 | Start Mininet and assign controllers | Mininet starts correctly, topology is loaded, and switches are assigned successfuly. |
| 12 | Tests using through ONOS CLI handles | N/A (does not assert) |
| 22 | Tests using ONOS REST API handles | N/A (does not assert) |
| 32 | Configure fwd apps and check the connectivity | Fwd is configured and pingall passes. |

Sample tests are for new users to get to know how to use and author a test plan. Test name/class should be "SAMP\*", for example, a starting template sample is ["SAMPstartTemplate\_1node"](https://gerrit.onosproject.org/gitweb?p=OnosSystemTest.git;a=tree;f=TestON/tests/SAMP/SAMPstartTemplate2_1node;h=2ca355dce62c62640eeeaaa4ccb06076774d96a8;hb=HEAD).
