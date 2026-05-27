# STC Advanced Topics

# Scenarios

* Defined using simple XML files
  + Allows hierarchical structure and schema validation
  + Has reasonably balanced horizontal aestetics - compared to JSON
* Definition files are located in /tools/test/scenarios
* Scenario can import other scenarios

  + import can be qualified with a namespace
* Comprised of steps or groups with dependencies
* Dependencies can be inherent or injected later
* Defines process flow as an execution DAG

# Steps and Groups

* Step is an individual node in the scenario process flow  
  + associated with some form of executable via exec attribute
* Group is a collection of other groups and steps  
  + used for grouping related sets of steps
  + used for encapsulation and definition of shared dependencies
* Has a name unique within the scope of a scenario  
  + namespace can be used to preserve uniqueness for scenario import
  + Specifies other steps or groups it inherently requires
  + Can be marked as optional using if or unless attributes

# Properties and Environment

* Most attributes support property expansion  
  + specified as ${property}
  + evaluated using values of environment variables or Java properties
* Pass-through properties for downstream steps  
  + @key=value included in output one property per line
  + only supported for exec attribute
* Steps and groups can specify env attribute  
  + value can be a path to a file to be sourced-in
  + value can be “~“ to indicate command exit status should be ignored
* Steps and groups can specify cwd attribute
  + value is the directory to be set before execution of the step command

# Parallel Chains

* Dynamically clones process flow subgraph region
* Used for repeating steps for independent portions of test environment
  + e.g. install, uninstall, collect logs on all ONOS instances concurrently
* Has an iteration variable specified as ${var#} property
* Clones subgraphs for each of var1, var2, … varN
* Stops cloning when varX becomes undefined or empty
* Value N can be abstracted using ${#} special property
* The <parallel> tag itself does not support the name or requires attributes. However, you can wrap the parallel chain in a group tag to get the same effect.

# Sequential Chains

* Dynamically clones process flow subgraph region
* Used for sequencing steps for portions of test environment
  + e.g. process a task for all ONOS instances sequentially
* Has an iteration variable specified as ${var#} property
* Clones subgraphs for each of var1, var2, … varN
* Stops cloning when varX becomes undefined or empty
* Value N can be abstracted using ${#} special property
* Value N-1 can be abstracted using ${#-1} property

# Dependencies

* Inherent dependencies specified as requires attribute of each step and group element  
  + specified as a comma-separated list of step or group names
* Injected dependencies specified as requires attribute of a dependency element  
  + used for chaining steps or groups imported from other scenarios
* Hard dependencies  
  + forces wait and the failure of the predecessor results in the step being skipped
* Soft dependencies - designated by “~” prefix  
  + forces wait but the failure of the  predecessor has no impact
* The "^" requirement is used to indicate the previous step. Note that this only works between a step and a step. If one of the linked steps is within a different group, parallel, or sequential chain then you must specify the requirement by name.
