# Contributing to the ONOS Codebase

This section describes, and provides pointers to, the various aspects involved in code contribution to the ONOS project.  If you have questions about any of this, please ask on the [onos-dev mailing list](https://groups.google.com/a/onosproject.org/forum/#%21forum/onos-dev) or [chat with us on Slack](https://slackin.onosproject.org/).

## Getting Started

* A good place to start is getting the source code.  The [ONOS Source Code](../../../getting-onos-2130151.md) documentation has more information about how to do that.
* After that, check out the [tutorials](../../../tutorials-and-walkthroughs-9832212.md) and [screencasts](../../tutorials/screencasts.md) we have that will help you get set up.
* Next, pick a [starter bug](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=81) to work on (you'll need to [register for an account](https://opennetworking.org/register/) on JIRA if you don't already have one).    
  + Starter bugs are relatively easy issues that will help you get familiar with the ONOS code and the community's processes for submitting code (more about community processes is below).
  + To pick a starter bug, scroll through the list of items and find something that looks interesting.  Then assign it to yourself by selecting "Assign to me" under **People****.** Your name should appear under the Assignee field, and you should see a message "ONOS-[number] has been assigned".
  + To verify that you now own the issue, go to the [ONOS Scrum Board](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1). You will be taken to the **Active Sprints** (*swim lane)* of the Scrum board, which shows the progress of all current tasks based on who is working on them. Your name should appear as one of the entries (they are alphabetical, so you may need to scroll a bit), with your new issue under the **To Do** column (the blue entry in the figure below). Selecting the issue will display its details in a sidebar to the right.
  + Once you are ready to work on the task, drag the issue from the **To Do** column to the **In Progress** column. Similarly, once you are finished, drag the issue from In Progress to ***Resolve Issue*** under **Done**. When your changes are accepted by the project, it can be moved to ***Close Issue*** under Done.
* If you have any questions about what to do next after assigning yourself a starter bug, read more about our coding processes below, look in the issue for information about who the Reporter was and you can reach out to them for questions, or you can post on the [onos-dev mailing list](https://groups.google.com/a/onosproject.org/forum/#%21forum/onos-dev) or [chat with us on Slack](https://slackin.onosproject.org/).
* After completing your first starter bug, you may want to pick a [bounty bug](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=82) for a more interesting challenge or you may have a project idea of your own you're interested in contributing.

## Finding Tasks to Work On

### Bug Bounties

[Bug bounties](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=82) are issues that are important to resolve for an upcoming release, but the core team doesn't have bandwidth to address right now.  Once you've become familiar with the ONOS code submission process, we would love if you assigned yourself one of the bounty bugs.  To thank people, we will be sending ONOS swag out to community members who complete a bounty bug.  [Check out the bug bounties on Jira](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=82).

### Backlog Issues

The ONOS project actively maintains a list of backlog issues that are used when planning future sprints.  You are welcome to look at the [backlog of the ONOS Scrum Board](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail) to find an issue there that looks interesting to work on.

## Submitting New Features and Enhancements

Developers are encouraged to build on ONOS and, as much as possible, to contribute their enhancements back to its code base. The ONOS team strives to provide the right balance between enabling and encouraging innovation and creativity, but at the same time maintaining the coherency of ONOS architecture and the code. To that effect, we welcome partners and contributors to follow the process outlined below:

* *Explore and prototype your ideas freely* atop the ONOS code-base.
  + We encourage doing this via quick proof-of-concepts exercises to vet out feasibility and test the concepts, but without investing much effort beyond that.
  + If possible, advertise on [onos-dev](mailto:onos-dev@onosproject.org) mailing list for feedback and potential collaborators.
* *Formulate a brief proposal in writing* to the TST using the [onos-tech-steering-team](mailto:onos-tech-steering-team@onosproject.org) mailing list.
  + If person-to-person discussion is desired, it is suggested to put the item on the agenda for the weekly TST meetings. Preferably, this should be done through [onos-tech-steering-team](mailto:onos-tech-steering-team@onosproject.org) mailing list.
  + Examples of previous [feature proposals](https://wiki.onosproject.org/display/ONOS/Feature+Proposals) are available and may help as a template
  + Technical discussion on the Slack channels can also be conducted.
  + The reason for this interactive phase is to make sure that the proposal is properly aligned with ONOS architecture & technical direction, that it conforms to the overall software design and that the abstractions are properly formed.
  + For larger submissions, the technical steering team would also coordinate with the release planning team to decide which ONOS release the submission should join.
  + For larger submissions the release planning team would also need to determine what support resources will be available for the new features or subsystems.
  + Jira Epic or User Stories would be formulated during this part of the process, for tracking the features and associated activities as part of the identified ONOS release.
* *Submit new or changed Java APIs for review via Gerrit.*
  + It is suggested to use Java interfaces rather than Java classes as this forces the discussion to revolve around the semantics of the contract, rather than implementation specifics. If appropriate, interfaces can easily mutate into classes later.
  + Code-style and Javadoc guidelines should be followed in order to maintain code consistency and quality of documentation.
* *Adjust the Java APIs based on the feedback* from the TST and from the broader ONOS community.
* *Proceed with implementation and submit code for review via Gerrit.*
  + Preferably, this can be done in fairly small and discrete chunks. In our experience, dropping large chunks of code for review, or many small concurrent reviews, leads to longer review cycles.
  + Code-style guidelines and unit test guidelines should be followed in order to maintain code consistency and code quality.
  + Code submissions must be accompanied by unit tests with assertions of expected behaviour and sufficiently high code coverage; minimum coverage is 70%, but goal is 80%+.
  + Care should be taken not to negatively impact the overall system performance and stability.
  + Jira sub-tasks can be used to track progress and to give visibility of the work to the rest of ONOS community.
  + If applicable, features should have CLI & debug support.
  + Submitter is responsible of maintaining code up to date with the master until the change-set has been committed to the codebase.

Clearly for bug fixes and small enhancements, the above process can be significantly abbreviated. However, for larger feature contributions, following this process will greatly increase the chances of success and should make for a smooth experience overall. We look forward to your contributions and to see what exciting ideas and solutions you can build with ONOS!

## Coding Processes and Guidelines

To maintain a level of manageability in the codebase, the project maintains a set of coding and testing processes and guidelines.

### Licensing and Contributor Agreement

 Any code contributed to ONOS source must be released under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) license, i.e. the licensing information must appear in the header of contributed files. The [IDE setup](../developer-guide/development-environment-setup.md) section describes how to configure the IDE to automatically add the licensing information for two IDEs, Eclipse and IntelliJ.

 In addition, code submitters must agree to the project [Contributor License Agreement (CLA)](https://gerrit.onosproject.org/static/cla.html), based on that of the Apache Software Foundation. 

### Coding style

Please read through our [Coding Style Guidelines](contributing-to-the-onos-codebase/code-style-guidelines.md) documentation.  Note that many IDEs may be configured to take care of the formatting aspects of the coding style. 

### Unit tests

Unit tests are a fundamental part of ensuring the stability of ONOS. Any new classes or system components should be accompanied by unit tests. For existing code, any changes that do not alter functionality should pass existing tests; however, existing tests should also be modified to reflect any changes that alter the behavior of a class or interface. Existing tests should not be disabled when new functionality is added, unless the tests are obsolete.

All available unit tests are run as part of a full build process. Contributions should pass all tests and build successfully before being submitted.

Minimum code coverage via unit tests is 70%, but the goal is 80%+. More details can be found in the [Unit Test Guidelines](contributing-to-the-onos-codebase/unit-test-guidelines.md) documentation.

### Code submission

The process of submitting code and amending changesets using the `git` Gerrit plugin is described in the [Sample Gerrit Workflow](contributing-to-the-onos-codebase/sample-gerrit-workflow.md) documentation. As a general rule, please submit early and often, but avoid stacking submissions on top of each other and avoid artificially fragmenting changesets; stacked reviews should not exceed 4.

### Code Review

The ONOS project uses [Gerrit](https://code.google.com/p/gerrit/) for code review. Once submitted, a *changeset* is inspected by ONOS committers. The reviewers of a submitted patch, or *changeset,* depend on several criteria. For example, the reviewers for modifications to the existing codebase will likely include current maintainers of the particular subsystems that the changeset affects. Reviewers of new additions, e.g. applications, subsystems, and providers, will depend on where and how the new changeset will affect the existing codebase, as well as who, if any, has provided guidance during the development process of the changeset. 

### Feedback

The primary mode for feedback is via email. This includes notifications about changeset acceptance and rejection, as well as reviewer comments that should be addressed. Therefore, it is important to 1) be subscribed to the project, and 2) have email notifications configured in user settings. [Git/Gerrit Setup](../developer-guide/development-environment-setup.md) addresses the configuration of Gerrit.  

For a changeset to be accepted, it must receive ***one review with a +2*** (not to be confused with two reviews of +1). A changeset given a -2 will not be accepted.  

More information on Gerrit may be found in the [Gerrit Code Review - A Quick Introduction](https://review.typo3.org/Documentation/intro-quick.html) documentation.

[Previous : Submitting a new feature proposal](issue-tracking-and-submission-with-jira/submitting-a-new-feature-proposal.md)

[Next : Sample Gerrit Workflow](contributing-to-the-onos-codebase/sample-gerrit-workflow.md)

---
