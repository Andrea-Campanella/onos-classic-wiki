# Contributing to ONOS Documentation

This section describes how to contribute documentation to the project. It also describes the formatting conventions that are used by the pages in the ONOS documentation set.

## Overview

The ONOS documentation set contains the following major items:

* [Tutorials](../../tutorials.md) - Tutorials and Screencasts to get people new to ONOS up-to-speed
* [Guides](../../guides.md) - Main body of documentation for the platform in the form of the [Administrator](../administrator-guide.md), [Developer](../developer-guide.md), [Architecture](../architecture-and-internals-guide.md), [Contributor](../contributor-guide.md), and [System Testing](../system-testing-guide.md) guides
* [Apps and Use Cases](../../apps-and-use-cases.md) - Landing page to each use case's documentation
* [New Projects](../../new-projects.md) - Landing page to each in-progress or experimental feature in various stages of development

There are more sections, but the above set are the sections that a contributors are usually interested in. Except for the use cases, which are maintained by the members of the use cases, most everything else is contributed by the general ONOS community.

## Where should <TOPIC> go?

Often, someone has something that they would like to write about, but isn't sure about where to add their topic(s). The following rules can be followed to get an idea about where to place a certain item:

* If it describes steps for how to build up to a specific, tangible example that can be run, it is a [tutorial](../../tutorials.md).
* If it describes a work-in-progress or a to-be-implemented function related to ONOS itself, it is a [feature proposal](../../new-projects.md).
* If it describes a mature function or feature and focuses on:
  + The design, architecture, and/or implementation, it is part of the [Architecture and Internals Guide](../architecture-and-internals-guide.md).
  + How to extend or modify functionality through code (APIs, classes/interfaces, etc), it is part of the [Developer Guide](../developer-guide.md).
  + How a user can interact with it, it is part of the [Administrator Guide](../administrator-guide.md).
* If it describes anything about a use case, it should be added under [Apps and Use Cases](../../apps-and-use-cases.md). For existing use cases, it is best to consult its members for where the page/topic belongs.

## Documentation section owners

Similar to the [Module Owners](#) for the ONOS code base, parts of the documentation set may have owners associated with them. The section owners are responsible for maintaining the organization and content of the sections that they own, and may be contacted with questions about the pages or the type of content that they maintain.

A contributor may become a section owner by creating a set of pages, working on something associated with a certain section of the docs, or volunteering as an owner of certain content on the mailing list or documentation Slack channel. The current list of section owners are listed in the [Documentation Section Owners](documentation-section-owners.md) page.

## Communication channels

Have questions or want to talk with us about docs?  Join us on one of these channels:

* The [onos-docs channel on Slack](https://onosproject.slack.com/messages/onos-docs/)
* The [onos-doc mailing list](https://groups.google.com/a/onosproject.org/forum/#!forum/onos-doc)

## Meetings

Please join us for our regular community documentation calls.  Details below:

* **Time:** Every other Wednesday at 1 pacific (check the [ONOS Community Calendar](../../community-information/meetings.md) for dates)
* **Dial-in:** <https://www.uberconference.com/davidwboswell>
* **Agenda and Meeting notes:** [ONOS Documentation](../../../onos-documentation-11179280.md)

## Procedure

Like everything else for the project, prominent documentation-related tasks are tracked on the ONOS Project JIRA in the [Documentation epic](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning&selectedIssue=ONOS-3147&epics=visible&selectedEpic=ONOS-2959). Anyone interested in contributing should register for an account for the project Wiki and JIRA. To register, go [here](http://onosproject.org/) and follow the 'Join ONOS' button.

### Working on existing tasks

A potential contributor should take ownership of a ticket if they see a task that they're interested in. A current maintainer (or, if the item is related to an owned part of the docs, likely the section owner) will review the changes, and provide feedback if needed.  [Find a list of documentation tasks that need someone to drive on Jira](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=82) (and once one of these documentation tasks is done, we're happy to thank you with some ONOS swag).

### Adding new content

A contributor interested in adding new content (tutorials, sections in the guides, etc.) should check if a JIRA ticket exists for the task in mind. If not, they should create a new ticket for the task, and take ownership of it. Messages should be sent to [onos-discuss](http://groups.google.com/group/onos-discuss):

* If the content is associated with a section with a section owner
* Initially with ideas for the content (to help de-duplicate effort)
* With link(s) to the new content once it's written (so that reviewers are aware of the content)

There may be several feedback cycles before the new pages are formally linked into the documentation set. It is generally a good idea to follow the [Wiki Formatting Conventions](contributing-to-onos-documentation/wiki-formatting-conventions.md) while adding new content
