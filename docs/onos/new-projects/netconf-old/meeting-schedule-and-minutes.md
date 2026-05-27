# Meeting Schedule and Minutes

# April 16, 2015

**Time**: 9.00-10.00am PST

**Attendees**: Marc De Leenheer, Hiral Amodia, Tofig Tom, Sanjay S, Dharamraj Jhatakia

**Minutes**:

* We quickly surfed through the week's status and JIRA.
* We identified that some JIRA have become duplicate. Marc suggested that we will decide later of what to do about those.
* Marc informed us to update correct epic and sprint information to JIRA so that it is clear to everyone on the progress.
* Development team explained that they are almost near to complete the implementation of Device Provider.
* Next week we should be good to commit the code to ONOS repository for review.

# April 9, 2015

**Time**: 9.00-10.00am PST

**Attendees**: Marc De Leenheer, Hiral Amodia, Tofig Tom, Sanjay S

**Minutes**:

* We quickly surfed through the week's status.
* Development team again put forward their assumptions to Marc about and discussed how the NETCONF plugin will interact with core.
* Marc provided some critical inputs. As the bridge was not properly audible today we requested Marc to put his points in a mail and send to us.
* Marc has send a mail with his inputs which dev team is referring to and changing their design and implementation.

# April 2, 2015

**Time**: 9.00-10.00am PST

**Attendees**: Marc De Leenheer, Hiral Amodia

**Minutes**:

* We quickly scanned through the below four JIRA tickets which were planned for Cardinal Sprint - 1
  + Ticket 1386 : Development environment setup : On track for first sprint. Dev team has done the necessary setup based on the ONOS Wiki guidelines. Currently this ticket is under review process.
  + Ticket 1387 : Test environment setup : In Progress. This ticket was planned for first sprint. However dev team is facing some challanges and hnce it may be moved to next sprint.
  + Ticket 1388 : Connectivity to a NETCONF device : On track for first sprint. Dev team has successfully established connectivity with Conf-D and a CISCO soft device. Currently this ticket is under review process.
  + Ticket 1389 : Generation of the coding framework. On track for first sprint. Dev team has generated the coding framework. Currently it is in review process. Once the review is done, we will reach out to ON Labs team for review and push to git.
* We discussed that for every JIRA ticket we should have :

  + Affects Version : 1.0.0 and 1.1.0
  + ~~Fix Version : 1.2.0~~ This is incorrect: only fill out the fix version when the issue can be closed.
* Success in bringing up ConfD as software server for development and testing purposes
* Class diagrams are in progress

# March 26, 2015

**Time**: 9.00 AM PST to 10.00 AM PST

**Attendees**: Marc De Leenheer, Hiral Amodia, Kapil Aare, Sanjay S

**Minutes**:

* Went through the four stories planned in the first ‘Infrastructure’ Sprint (23-02 to 03-04)
* Discussed on the challenges faced in accessing NETCONF device

  + Kapil will do a call with Ben today to get help in resolving the issues that we are facing in accessing the URL for CISCO VM
  + Hiral proposed that if we identify some CISCO or such NETCONF device, can we reach out to CISCO through this forum to get soft version of that device for our use? Marc was positive in to this suggestion. We will share the device info with Marc.
  + Marc is looking at options for access to a physical device.
* We have shared link of design document Wiki with ONOS Developers group asking for their feedback for the same.

# March 19, 2015

**Time**: 9.00 AM PST to 10.00 AM PST

**Attendees**: Marc De Leenheer, Tofigh Tom, Hiral Amodia, Sanjay S

**Minutes**:

* Went through the design and quick update on the status of project.
* Marc suggested to update contact, call etc details on Wiki and then send the link on ONOS-Dev group for feedback.
* Marc suggested that now we can start putting the development/coding activities in JIRA and start tracking those. As we keep on getting clarity, the Design on Wiki can keep on evolving.
* Tom connected us with Pica8 and AT&T team who has extended their support for test bed to test the plugin.

# March 13, 2015

**Time**: 9.00 AM PST to 10.00 AM PST

**Attendees**: Marc De Leenheer, Tofigh Tom, Hiral Amodia, Kapil Aare, Sanjay S

**Minutes**:

* We quickly went through the status update.
* We utilized our rest of the time for technical discussion around the approach which we are currently taking.
* The discussion turned out to be very useful as it helped clear some critical points for us. Below are some quick updates on the technical discussion that happened.

  1. NETCONF provider should work independently of ONOS.
  2. Netconf as a protocol is stateless. But Netconf provider will not be stateless.
  3. As thought earlier, ONOS will not make a request to NETCONF Provider, instead provider should use ONOS API(‘onos-topo-cfg’ API.) to get the devices list and query those devices by itself.
  4. NETCONF Provider will have its own store to save the NETCONF related details for each device
  5. NETCONF Provider store is an in-memory storage and no need of external Storage system, if needed we can save in to ONOS Store
  6. While Marc was happy with the amount of effort put so far, he helped us set the priority  by putting parsing as a less important thing as of today. Once the architecture is in place, we can discuss around the various coding aspects.
  7. When required ONOS will request for NETCONF details of devices and NETCONF Provider will respond from its memory / from Device
* Virtual Router is not yet ready for us to work. Marc has someone who has started working on it and we can expect it to get done soon.
* Instead of a word document shared on mail, we should start putting in to wiki for a wider audience to look at it and provide inputs.
* Share the document/concerns to ONOS community on ONOS-Dev / ONOS-Discuss mailing lists
* Next week we will have technical call/discussion with Marc with frequency more than once a week. In the week after that(as Marc is busy with conference) we will send a mail to Marc for any needed update and based on Marc’s availability , Kapil can reach out to Marc or Marc will respond on mail with updates.
* Tom extended his help with access to a virtual router/switch.

# March 05, 2015

* The call was cancelled.

# February 26, 2015

**Time**: 9.00 AM PST to 10.00 AM PST

**Attendees**: Marc De Leenheer, Hiral Amodia, Sanjay S

**Minutes**:

* We went through the Weekly Status Report.
* Marc has suggested that he will be able to help with a NETCONF switch next week
* We discussed that GPLV3 license is not compatible to ONOS Apache License and hence we cannot use the NETCONF libraries which are under GPLV3 license. This makes our library search limited to TailF library.
* Marc suggested us to work on exploring TailF library by taking help from a virtual software server.
* Marc gave a quick walkthrough of Netconf JIRA.
* We discussed few technical queries that Sanjay put forth to Marc.

# February 19, 2015

**Time**: 9.00 AM PST to 10.00 AM PST

**Attendees**: Marc De Leenheer, William Snow, Hiral Amodia, Sanjay S

**Minutes**:

* Team explained the areas in which they are doing their learning and knowledge gathering. Also explained the understanding about providers, core layer, services etc and the possible location where they feel the Netconf SB plugin will get hooked.
* Marc helped confirm that team’s approach so far is in correct direction
* We fixed the first Short Term goal to only focus on Device provider as current scope is only ACL data model. This will help concentrate our attempts to a focused area.
* We decided that the First step is to find what libraries are there which speaks/knows netconf protocol. Team will spend another two days around this and we can again re-group on Monday same time to discuss the findings. If we get a breakthrough tomorrow we can talk tomorrow also.
* Bill suggested dev team to Track the progress through JIRA tickets.
