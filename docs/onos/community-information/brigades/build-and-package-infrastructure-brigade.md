# Build and Package Infrastructure brigade

**This page should be removed!**

## **Brigade Leads:**

* Viswa KSP – Verizon – Chennai, India
  + [kspviswa.github@gmail.com](mailto:kspviswa.github@gmail.com)

## **Brigade Members:**

* Alexis MUNYANDEKWE - Rennes, France
  + [ndekwe@](mailto:ndekwe@gmail.com)[gmail.com](http://gmail.com)
* Bharath Thiruveedula – Verizon, Hyderabad, India
  + [bharath\_ves@hotmail.com](mailto:bharath_ves@hotmail.com)
* Venkata Narayana Tata – India (Gigamon)  
  + venkat.onos@gmail.com
* Zack Williams - Arizona, USA. CORD project, XOS
  + zdw@[cs.arizona.edu](http://cs.arizona.edu)

## ****Contact the brigade:****

* Slack - <https://onosproject.slack.com/archives/brigade-infra>
* Mailing List - [brigade-infrastructure@onosproject.org](mailto:brigade-infrastructure@onosproject.org)

## **Scope:**

* Make sure that ONOS code-base(s) can be built efficiently, reliably and consistently into a small set of [distributable artifacts](https://docs.google.com/document/d/1Hdl-ZsttECXZEucskoPNghwsv_H68dtnTnRZrDWgVsg/edit#heading=h.20s0gz7qtwhg) to make it easy to distribute and deploy ONOS
* Make sure that ONOS SDK can be built and released efficiently, reliably and consistently as a set of [published artifacts](https://docs.google.com/document/d/1Hdl-ZsttECXZEucskoPNghwsv_H68dtnTnRZrDWgVsg/edit#heading=h.a8x8n7mse3r2) on Maven Central and ONOS project site
* Maintenance of the build and release process documentation
* Maintenance of the corresponding user (network administrator) documentation
* Maintenance of the corresponding developer SDK documentation
* Development and maintenance of the build, test and run-time tool kits for developers, testers and users (network administrators)
* Development and maintenance of the CI process and release process and supporting tools and working with the team managing the infrastructure
* Integration of CI with basic functionality tests (STC) as part of the build & release processes
* Maintenance and upstreaming of Gerrit plugins (Module Owner, Stats, Project Lock)
* Maintenance of [Shared Cells](https://docs.google.com/document/d/1Hdl-ZsttECXZEucskoPNghwsv_H68dtnTnRZrDWgVsg/edit?usp=sharing) Warden
* Investigation (and later execution) of how to disaggregate the ONOS code-base, while continuing the ability to build & release with regular (and frequent) cadence
* Development and maintenance of the ONOS archetypes (Maven + Buck)
* Deprecation and removal of the legacy build framework
* Move artifacts versions to follow semantic versioning

## 

## Work week ( Apr 24 ~ 26, 2017 )

* **Plan & Schedule** - <https://docs.google.com/spreadsheets/d/1F6Xd47G2YJTNjHv5KaqYnkyBrzMvI4w1SZ1-1PaECNs/edit#gid=0>
* **Notes** ( *along with recording links* ) - <https://docs.google.com/document/d/18dGYZDPpC8zwK8xxWyetkzVSLi-dDhFlS8acRbl3Xjk/edit#heading=h.mdcz9k2lc3b9>

## Priority Tasks

### Pre-ONS

* Continue deprecation of legacy build framework

+ Scrub Wiki documentation
+ Update affected screencasts (in progress)
+ Prune CI jobs

* Investigate code-base disaggregation

+ Propose workspace / workflow management tools (e.g. Repo)
+ Propose specific repository divisions
+ Propose workspace directory structure
+ Produce timeline for transition, solicit feedback, present to TST

- Including draining or migration of existing code review backlog

+ Experiment with snapshot/subset of codebase for experience

* Investigate build tool deficiencies

+ Look into Buck deficiencies and ONOS’ fork diffs
+ Look into build in the context of multiple/different workspaces (i.e. full code, standalone app)
+ Investigate other Blaze-related tools to see if they overcome limitations more easily
+ Produce build framework recommendation, solicit feedback, present to TST
+ Start developing fixes for any deficiencies or new features for proposed build tool
+ Experiment with snapshot/subset of codebase for experience

### Post-ONS

* Fix build framework as per suggestions of investigation
* Execute code-base disaggregation plan
* Document workflow for development and release

+ Including full code (build apps, drivers, core together) and standalone (build part against release artifacts)

* Complete deprecation of legacy build framework

+ Remove all but the top-level pom.xml files

* Consider moving publish to entirely standalone Python script (away from Buck)
* Begin work on distribution-specific packages (e.g. deb, RPM, Docker container, tutorial and release VMs, etc.)

Notes

### 

### Run-Time Distribution Artifacts & Formats

* platform neutral onos.tar.gz, onos-test.tar.gz
* various platform specific packages and/or recipes

+ e.g. deb, rpm, Docker, snap, Ansible, Puppet

### SDK Distribution Artifacts

* API jar bundles (+javadocs, +tests)
* Libraries & Utilities jar bundles (+javadocs, +tests)
* Java API docs on [api.onosproject.org](http://api.onosproject.org)
* REST API docs on [rest.onosproject.org](http://rest.onosproject.org) - later
* Archetypes for developing external ONOS apps buildable by Maven and Buck

**Document capturing initial thoughts : <https://docs.google.com/document/d/1Hdl-ZsttECXZEucskoPNghwsv_H68dtnTnRZrDWgVsg/edit>**

**How to get involved:**

* contact [kspviswa.github@gmail.com](mailto:kspviswa.github@gmail.com)
