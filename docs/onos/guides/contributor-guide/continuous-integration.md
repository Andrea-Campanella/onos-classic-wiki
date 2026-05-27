# Continuous Integration

This section describes the tool chains used in the ONOS CI process.

ONOS runs a *continuous integration* (CI) job whenever a change set is merged into the master branch and whenever a Gerrit review request or rebase is done. The CI job will do a build from scratch, run all of the unit tests and run static analysis tools to check that the submitted change follows the ONOS coding standards.

## Continuous Integration Tool Chain

## Jenkins

ONOS uses the [Jenkins](http://jenkins-ci.org/) system for running and monitoring continuous integration (CI) jobs. When a change is made, Jenkins starts a job to build and test the source tree. Jenkins also launches a nightly build for SonarQube. You can monitor the status of Jenkins jobs using the Jenkins console at [jenkins.onosproject.org](http://jenkins.onosproject.org).

Jenkins integrates several static analysis and code quality tools into its jobs.  Jenkins follows trends on the problems reported by these tools, so we can watch the evolution of the code quality of ONOS over time.

### pmd

pmd is a tool that looks for constructs in code that may be hard to understand, hard to extend, or prone to introducing errors.

### cpd

cpd is a copy/paste detector.  It looks for blocks of identical code that appear in multiple places.

### coverage

Each Jenkins job does a unit test coverage analysis of the source being built.

## Checkstyle

[Checkstyle](http://checkstyle.sourceforge.net/) is a static analysis tool that scans java source code and checks it for compliance with a set of coding standards. It checks for things like white space usage, naming, placement of braces and other code style issues.  Checkstyle is run as part of every maven build of ONOS, and checkstyle violations will fail the build.

## SonarQube

[SonarQube](http://www.sonarqube.org) integrates a set of java code quality analysis tools with a web-based UI to allow easy identification of code problems. Once a day, Jenkins runs a build that triggers SonarQube to generate quality information about the ONOS source.  SonarQube keeps track of runs over time, so we can track the quality of the ONOS code base as it evolves. You can [view the ONOS SonarQube web console](https://sonarqube.onlab.us) to see how we are doing.

SonarQube integrates tools to check unit test coverage, java source code compliance with coding standards, static detection of coding errors like possible null pointer dereferences, and detection of blocks of code that are duplicated. These tools are integrated into one shared web UI and the results are tracked to allow tracking the state of our source code over time.

---

[Previous : Test Environment Setup](../developer-guide/development-environment-setup/development-workflow-options/cells-and-onos-test-scripts.md)  
[Next : Issue Tracking and Submission with JIRA](issue-tracking-and-submission-with-jira.md)

---
