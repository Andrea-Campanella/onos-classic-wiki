# STC Reference Guide

## *group*

Defines a series of steps that are run together. A reference to a group may be used as a dependency for a group or a step, so the group mechanism is a convenient way to ensure parts of scenarios are executed in the proper order.

### Attributes

* *name* - name used to refer to the group. This string must be unique.
* *requires* - comma-separated list of dependencies for the group. These can be group or step names.
* *unless* - If the string evaluates to a non-null value, the group is not executed.
* *if* - If the string evaluates to a null value, the group is not executed.

## *step*

Defines an action to execute. A reference to a step may be used as a dependency for a group or a step, so the group mechanism is a convenient way to ensure parts of scenarios are executed in the proper order. Execution of a step is successful if the command returns a 0 status code, unless the *env* attribute is used to modify this behavior.

### Attributes

* *name* - name used to refer to the step. This string must be unique.
* *requires* - comma-separated list of dependencies for the step. These can be group or step names.
* *unless* - If the string evaluates to a non-null value, the step is not executed.
* *if* - If the string evaluates to a null value, the step is not executed.
* *delay* - the step pauses this number of seconds before execution of the command starts.
* *exec* - the command to execute for this step.
* *env* - if this string contains an exclamation point ("!") the step fails if the execution of the command **does not** return an error.

# *scenario*

Defines a set of operations to be run as a single unit. Scenarios may be run from the command line using the *stc* tool.

### Attributes

* *name* - name used to refer to the scenario in the *stc* tool. This name is also displayed in the output of the *stc* tool. Names must be unique and not have spaces.
* *description* - string used to describe the scenario. There are no limits on characters that can be used or length of the string.
