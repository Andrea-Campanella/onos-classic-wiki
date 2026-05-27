# Adding ONOS utility scripts and functions to your environment

ONOS utility scripts are spread across different ONOS root sub-directories.

If you use these scripts frequently, it may be helpful to be able to be able to run them from any directory on your development machine.

If you use `bash`, you can add two lines at the end of your `.bashrc,` `.bash_aliases` or `.profile` file:

**Sourcing ONOS scripts**

```
export ONOS_ROOT=~/onos
source $ONOS_ROOT/tools/dev/bash_profile
```

On Mac and other systems

If you're using a Mac, the file is called bash\_profile. On other systems it might be different.

In general, you can put these instructions in any script that is executed every time at startup.

From now on, you should be able to use the ONOS command utilities directly using their name only, without specifying their path.

For simplicity, some subsequent sections of this development guide will assume you have completed this step.
