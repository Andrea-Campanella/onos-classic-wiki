# A Beginner's Guide to Contribution

Thanks for your interest in contributing to ONOS.  We know that getting involved in an open source project can feel daunting, so this section provides information to make this jump smoother.  If you have any questions about any of this, please check out the contact information below.

### Types of Contribution

Submitting code as a developer is certainly a way to contribute to a project, but not the only way. There are many aspects to an open source project where contributors can help, including (but not limited to):

* **Development:** Help build ONOS. Opportunities range from coding new features to creating unit tests to bug fixes to making sample applications. [Learn how to get involved with coding](contributing-to-the-onos-codebase.md).
* **Documentation:** Help create clear, concise documentation. Identify and add whatever is missing and fix what is unclear or just plain wrong. [Learn how to get involved with documentation](contributing-to-onos-documentation.md).
* **Deployment:** Help us show the world that ONOS can work in real networks by deploying ONOS and its applications on your network. [Learn how to get involved with deployments](../../community-information/deployments.md).
* **Quality:** Help test ONOS – whether it’s the platform, sample applications or documentation. Work with the Jira issues to ensure that they are clear, complete, and the problems are reproducible. [Learn how to get involved with testing](how-to-contribute-to-system-test.md).
* **User experience and UI:** Help ensure that the ONOS user experience is WOW – not blah! Help create a unique look, feel, and experience for ONOS users. [Learn how to get involved with the UI](../../tutorials/web-ui-tutorials.md).

 There are other ways to contribute to ONOS.  For instance, you may be interested in running a training event in your area.  If there is something you're interested in doing but don't see information about that here, please contact us.

### Contact Information

* **Mailing lists:** Anyone interested in contributing should join [onos-discuss](https://groups.google.com/a/onosproject.org/forum/#%21forum/onos-discuss).This is the primary mailing list for general questions and discussions. There are several other [mailing lists](../../community-information/mailing-lists.md) that you may want to join, such as onos-dev for ONOS developers.
* **Chat:** [Join us on Slack](https://slackin.onosproject.org/) for real-time conversations about ONOS.  There is a general channel as well as channels dedicated to specific topics.  Feel free to stop by and ask questions and introduce yourself.

### Tutorials, Videos and Documentation

The project maintains up-to-date [tutorials](../../tutorials.md) and [videos](../../tutorials/screencasts.md) for both users and contributors. In general, those interested in contribution should at least complete the [Basic ONOS Tutorial](../../tutorials/basic-onos-tutorial.md), as it introduces many of ONOS's features.

In addition to the tutorials, the ONOS Documentation Set provides guides describing various aspects of using and developing on ONOS, as well as its architecture and API documentation (Javadocs). For developers, the recommended way to use the documentation set is:

1. Learn how to install, run, and use ONOS, as per the [Administrator Guide](../administrator-guide.md)
2. Learn how to set up the development/test environment and the usage of JIRA and Gerrit, and testing and coding guidelines as per the [Developer Guide](../developer-guide.md)
3. Reference relevant parts of the [Architecture and Internals Guide](../architecture-and-internals-guide.md), [Javadocs](http://api.onosproject.org), and Developer's Guide Appendices

For step 2. of the above, readers interested in development should refer to [Contributing to the ONOS Codebase](contributing-to-the-onos-codebase.md), and readers interested in the documentation effort should focus on [Contributing to ONOS Documentation](contributing-to-onos-documentation.md).

### Crowd Registration

An account is required to access the various contributor services and access rights, such as JIRA issue creation. An account may be created at <https://www.opennetworking.org/register/>.

[Recover lost username](https://www.opennetworking.org/username-recovery)   
[Recover lost password](https://www.opennetworking.org/password-recovery)

### Project Model

Contributors begin as *submitters*, and may progress to *committer* status. In a similar vein, contributors may work on the existing ONOS codebase and use cases, or, with approval of the technical steering group, introduce their own work as a sanctioned project. [ONOS Governance](https://wiki.onosproject.org/display/ONOSST/Governance) describes the project model that the ONOS Project follows in further detail.

### Current Projects

The ONOS Project is a composite of the ONOS SDN platform itself and the various projects using it (*applications* and *use cases*). Information about the ongoing projects may be found on [Projects]. Many of these projects will have an *Epic* associated with them so that the tasks associated with them may easily be found.

### Proposing a new project or task

Anyone can approach the mailing lists with project ideas and proposals. For example, if a developer has written a new application or a provider for a new protocol, and wishes to contribute it back to ONOS, it is a good idea for them to drop a line on the mailing list for feedback and further suggestions, rather than to submit a pull request without a warning.

### Asking Questions

If you are working on a task, and are stuck, don't be afraid to ask questions - it's certainly in everyone's interest to move the project forward! However, please be sure to search existing documentations and mailing list archives before doing so, or the response you get may consist of a link to a page or something similarly terse. Likewise, If you have log files, or steps for recreating an odd behavior, attach or mention those to your question as well - Just saying "It's broken" without the specifics will just result in a response asking for those materials. 

### Submitting Bug Reports

If you encounter unexpected or incorrect behavior, first make sure that you understand what the correct behavior should be (and why it should be that way), and confirm that you are using the system correctly based on the documentation. Try to isolate the issue as much as possible, by finding the minimum set of steps (or a small, simple piece of code) that can reliably reproduce the problem. Make sure to include a transcript or log of any input steps or output. Finally, to submit the bug report itself, follow the instructions at [Using Jira to create an issue: bugs, feature requests, documentation](issue-tracking-and-submission-with-jira/using-jira-to-create-an-issue-bugs-feature-requests-documentation.md).
