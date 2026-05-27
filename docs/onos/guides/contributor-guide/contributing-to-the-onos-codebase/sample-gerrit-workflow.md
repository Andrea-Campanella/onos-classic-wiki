# Sample Gerrit Workflow

This section describes a sample workflow for making and submitting changes to the project using `git.`

## Prerequisites

This section assumes that a developer has:

* Gotten ONOS source, as described in [Getting Started](https://wiki.onosproject.org/display/ONOS/Installing+and+Running+ONOS)
* Set up their development environment, as described in [Development Environment Setup](../../developer-guide/development-environment-setup.md)
* Set up their test environment, as described in [Cells and ONOS test scripts](../../developer-guide/development-environment-setup/development-workflow-options/cells-and-onos-test-scripts.md)

A developer should also be relatively comfortable with the shell.

## Git

The version control system used by the project is **`git`**. Using git provides a developer with a way to cleanly keep track of and organize their changes, in addition to the ability (among many others) to view and reapply changes made to the code at various points in time. Importantly, git meshes in a way conducive to the ONOS code submission/review process; therefore, it is important for a potential contributor to be fairly comfortable with using it. Those interested in familiarizing themselves with git will find many resources online, including a [full book](http://git-scm.com/book/). 

As git is extremely rich in features, only the relevant functions will be mentioned where they are needed.

## The Walkthrough

1. ***Create and switch to a new branch***. A branch is a divergence point from the existing code base. Any changes made in a branch are restricted to the branch.

   ```
   $ cd $ONOS_ROOT
   $ git checkout -b myBranch
   Switched to a new branch 'myBranch'
   ```

   This creates a new branch named 'myBranch', off of the previous branch that we were in. Replace 'myBranch' with a name that briefly describes the topic of your change. This command will fail if there was already a branch of the same name. The command `git branch`can be used to list all of the branches to check that the name isn't already used. If a branch with the desired name is no longer needed, it may be deleted with `git branch -D <branchName>`and the above commands repeated to re-create a new branch.
2. ***Make changes to the code***. This can be done in any way - IDE, text editor, whatnot.
3. ***Test the*** ***changes*.** Any changes should be accompanied by unit tests wherever possible and must pass existing unit tests. The project should also be rebuilt and tested against a Mininet network (at the very least).   
     
   * if you have exported the onos bash profile the command *ob* will run all of the unit tests.
4. ***Commit the changes.*** Committing creates a snapshot of the changes made to the code so that may be revisited/manipulated later, but only in the branch where the changes were committed. The command `git status`allows one to view the files that were modified.   
   `git add <file>` adds a file to the pool to commit. Once all files are added, `git commit -m "<message>"` creates a snapshot with <message> as its description. `git log` may be used to list all of the commits that have been made, with the most recent commit at top.
5. ***Pull upstream changes.*** The repository on the development machine should be synchronized with the upstream ONOS source repository. 

   Upstream changes are **always** applied to the master branch. We first switch back to master with `git checkout`, before pulling downloading the changes in the upstream source repository with `git pull`:

   ```
   $ git checkout master
   Switched to branch 'master'
   $ git pull --ff-only origin master
   ```
6. ***Sync the branch with updated master.*** The updates pulled to master must be explicitly applied to the branch intended for code review. This is done by switching back to the development branch and using `git rebase`.

   ```
   $ git checkout myBranch
   Switched to branch 'myBranch'
   $ git rebase -i master
   ```

   The default editor will be opened with the list of commits that have been made to the branch locally since its creation. Saving and closing this file causes the changes from the master branch to be incorporated into the branch. Any merge conflicts (e.g. a file modified in both the local and master branch) will interrupt the process. In `git status`, the conflicting files will appear under "Unmerged paths" as "both modified". If this happens, the file(s) must be edited and committed before the rebase is continued:

   ```
   $ git rebase -i master
   error: could not apply ca081b6... Initial commit for information persistence.

   $ vim core/net/src/main/java/org/onlab/onos/net/device/impl/DeviceManager.java
   $ git add core/net/src/main/java/org/onlab/onos/net/device/impl/DeviceManager.java
   $ git rebase --continue
   Successfully rebased and updated refs/heads/myBranch.
   ```
7. ***Submit code for review.*** Once the branch is synchronized, it may be submitted for review with `git review`. ([usage examples](http://docs.openstack.org/infra/git-review/usage.html))

   ```
   $ git review
   ```

   This submits the changes with the branch name as its topic.

   Commit and submit this branch only once

   If you would like to change your code after submission, please follow the procedure as described in the "Amending Submissions" section below.

   git review fails with Traceback

   If you're using a Mac and *git review* command fails with an error traceback like below:

   Error Traceback

   Traceback (most recent call last):  
     File "/usr/local/bin/git-review", line 11, in <module>  
       sys.exit(main())  
     File "/Library/Python/2.7/site-packages/git\_review/cmd.py", line 1132, in main  
       (os.path.split(sys.argv[0])[-1], get\_version()))  
     File "/Library/Python/2.7/site-packages/git\_review/cmd.py", line 180, in get\_version  
       provider = pkg\_resources.get\_provider(requirement)  
     File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pkg\_resources.py", line 197, in get\_provider  
       return working\_set.find(moduleOrReq) or require(str(moduleOrReq))[0]  
     File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pkg\_resources.py", line 666, in require  
       needed = self.resolve(parse\_requirements(requirements))  
     File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pkg\_resources.py", line 565, in resolve  
       raise DistributionNotFound(req)  # XXX put more info here  
   pkg\_resources.DistributionNotFound: git-review

   try upgrading the git-review package dependency first.

   $ sudo pip install --upgrade setuptools

## Review Responses

The review responses, and what they mean:

| Response Score | Meaning |
| --- | --- |
| -2 | There is something fundamentally blocking about this check-in (e.g. style, design). It cannot be merged as is. |
| -1 | Some issues require addressing. Please update and submit patchset (amend commit) for re-review. |
| 0 | A comment, with no opinion on whether or not to accept the change. |
| +1 | Change looks good, but someone else must approve. |
| +2 | Change looks good, approved. |

(Note that two +1's do ***not*** equal a +2)

Typically, if a module owner +2's a review, he/she will also submit (merge) the change also.

## Amending Submissions

As part of the peer review process, an author of a patch submitted to Gerrit may be asked to amend their submission. To amend a patch:

1. ***Find the change number for the patch.*** This number can be found in the URL of the patch in the Gerrit web interface.   
   For example, if the URL of the link to the change-set is *https://gerrit.onosproject.org/#/c/169/*, the change number is *169.*
2. ***Checkout the change.*** This creates a new branch for the changeset that represents this patch, with the naming convention *review/submitter\_name/branch\_name.*

   ```
   $ git review -d 169
   ```

   This needs to be done once for the changeset. If more amendments are needed for the patch later, one can simply check the branch out like any other:

   ```
   $ git checkout review/[submitter_name]/[branch_name]
   ```
3. ***Make changes and commit.***Here, we use `git commit --amend`, instead of generating a new message.

   ```
   $ git add [modified files]
   $ git commit --amend
   ```

   Becareful with Change-Id:

   Gerrit uses the Change-Id: ... in the commit comment to identify which changeset this commit belongs to.  
   Make sure that you're not modifying the Change-Id: string when you're amending changes to the commit.   
   If you're squashing multiple commits together into a existing changeset, be sure to leave only the Change-Id: you want to use in the commit comment.
4. ***Resubmit.*** This creates a new patchset on the existing review.

   ```
   $ git review
   ```

   If Gerrit returns an error about a missing Change-Id, make sure that there is a `Change-Id:` string at the bottom of the commit message (above the comment blocks):

   ```
   Refactored PeerConnectivityManager for code reuse between the two path types.
    
   Change-Id: Ib05f676d071ef1c545e93244a9ed5ed89672113e
    
   # Please enter the commit message for your changes. Lines starting
   # with '#' will be ignored, and an empty message aborts the commit.
   ```

Once finished and the patch is accepted, the branch can be deleted:

```
$ git branch -D review/[submitter_name]/[branch_name]
```

## Amending Submissions (Rebase to master and/or apply changes)

This option is useful if there are commits in the master that conflict with your changes.

1. Find the checkout.  The checkout link can be found on the patch page in the Gerrit web interface.  In the top right, there is a Download option.  Copy the text in the Checkout field.
2. ***Checkout the patchset.*** This checks out the patch set at the most recent patch number.

   ```
   git fetch ssh://username@gerrit.onosproject.org:userid/onos refs/changes/18/18118/7 && git checkout FETCH_HEAD
   ```
3. ***Rebase.***

   ```
   git fetch origin master
   git rebase origin/master
   ```
4. ***Resolve conflicts.***Resolve all conflicts related to the rebase

   ```
   git status
   # if there are files in red, they need to be modified because there is a conflict
   vi myBrokenFile.txt
   ```
5. ***Add files to prepare for commit.***If there are additional files you would like to add to this review, they can be added in this step

   ```
   git add myBrokenFile.txt
   git add myOtherFile.txt
   ```
6. ***Commit --amend.***

   ```
   # If conflicts were resolved, you will need to --continue the rebase
   git rebase --continue
   # Finally amend your commit
   git commit --amend
   ```
7. ***submit review.***

   ```
   git review
   ```

---

[Previous : Contributing to the ONOS Codebase](../contributing-to-the-onos-codebase.md)  
[Next : Contributing to ONOS Documentation](../contributing-to-onos-documentation.md)

---
