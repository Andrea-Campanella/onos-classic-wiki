# Gerrit Workflow for System Test Development

This page is adopted from the [ONOS sample Gerrit workflow page](../contributor-guide/contributing-to-the-onos-codebase/sample-gerrit-workflow.md).

Prerequisites

Cloning the project is open to everyone. If you want to contribute to the project, you will need an account with onosproject. This section assumes that a developer has an account with onosproject.org (signup at onosproject.org).

A developer should also be relatively comfortable with the shell. 

## Git

The version control system used by the project is **`git`**. Using git provides a developer with a way to cleanly keep track of and organize their changes, in addition to the ability (among many others) to view and reapply changes made to the code at various points in time. Importantly, git meshes in a way conducive to the ONOS code submission/review process; therefore, it is important for a potential contributor to be fairly comfortable with using it. Those interested in familiarizing themselves with git will find many resources online, including a [full book](http://git-scm.com/book/). 

As git is extremely rich in features, only the relevant functions will be mentioned where they are needed.

## Cloning the project:

```
$ git clone https://gerrit.onosproject.org/OnosSystemTest
```

In order to submit code for review, add your machine's public key to your user setup (after logging on gerrit.onosproject.org) - <https://gerrit.onosproject.org/#/settings/ssh-keys>.

## The Walkthrough

1. ***Create and switch to a new branch***. A branch is a divergence point from the existing code base. Any changes made in a branch are restricted to the branch.

   ```
   $ cd ~/OnosSystemTest
   $ git checkout -b myBranch
   Switched to a new branch 'myBranch'
   ```

   This creates a new branch named 'myBranch', off of the previous branch that we were in. This command will fail if there was already a branch of the same name. The command `git branch`can be used to list all of the branches to check that the name isn't already used. If a branch with the desired name is no longer needed, it may be deleted with `git branch -D <branchName>`and the above commands repeated to re-create a new branch.
2. ***Make changes to the code***. This can be done in any way - IDE, text editor, whatnot.
3. ***Test the*** ***changes*.** Run your modified or new test script.
4. ***Commit the changes.*** Committing creates a snapshot of the changes made to the code so that may be revisited/manipulated later, but only in the branch where the changes were committed. The command `git status`allows one to view the files that were modified.   
   `git add <file>` adds a file to the pool to commit. Once all files are added, `git commit -m "<message>"` creates a snapshot with <message> as its description. `git log` may be used to list all of the commits that have been made, with the most recent commit at top.
5. ***Pull upstream changes.*** The repository on the development machine should be synchronized with the upstream OnosSystemTest source repository. 

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

   $ [modify the file in order to resolve the merge conflicts]
   $ git add [modified_file_name]
   $ git rebase --continue
   Successfully rebased and updated refs/heads/myBranch.
   ```
7. ***Submit code for review.*** Once the branch is synchronized, it may be submitted for review with `git review`.

   ```
   $ git review
   ```

   This submits the changes with the branch name as its topic.

## Amending Submissions

As part of the peer review process, an author of a patch submitted to Gerrit may be asked to amend their submission. To amend a patch:

1. ***Find the change number for the patch.*** This number can be found in the URL of the patch in the Gerrit web interface.   
   For example, if the URL of the link to the change-set is *https://gerrit.onosproject.org/#/c/169/*, the change number is *169.*
2. ***Checkout the change.*** This creates a new branch for the changeset that represents this patch, with the naming convention *review/submitter\_name/branch\_name.*

   ```
   $ git review -d [commit_number]
   ```

   This needs to be done once for the changeset. If more amendments are needed for the patch later, one can simply check the branch out like any other:

   ```
   $ git checkout review/[submitter_name]/[branch_name]
   ```
3. ***Make changes and commit.***Here, we use `git commit --amend`, instead of generating a new message.

   ```
   $ git add [modified file]
   $ git commit --amend
   ```

   Be Careful with Change-Id:

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

---
