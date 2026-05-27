# Test Result Graphs

The test results graphs that show up on the [Test Results Wiki Page](../test-results.md) are created using the R programming language, immediately following the conclusion of a scheduled test.

# **Individual Test Results**

## CHO Trend Graphs

![](https://jenkins.onosproject.org/view/QA/job/postjob-Fabric5/lastSuccessfulBuild/artifact/CHO_Events_master_168-maxData_graph.jpg)

CHO graphs are refreshed every hour during a CHO test, and the events, failures, and exceptions are recorded and posted to the wiki.

## Trend Graphs - FUNC, HA, USECASE

![](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/FUNCintent_master_20-builds_graph.jpg)

Each test result (besides SCPF and PLATdockertest) is illustrated as a trend graph, displaying the results of the last 20 builds of the specific test.

The number of *test cases* executed is equal to the sum of passed and failed *test cases*.  Therefore, tests may contain skipped test cases if the executed test cases (sum of passed and failed cases) do not equal the number of planned test cases.

## Trend Graphs - SCPF

![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPF_Front_Page_Switch_Latency_Test_-_Switch_Up_master_50-dates_graph.jpg)

The trend graphs for SCPF display the result of a specific value over 50 builds.

## SCPF Bar Charts

![](https://jenkins.onosproject.org/view/QA/job/postjob-BM/lastSuccessfulBuild/artifact/SCPFswitchLat_master_UpErrBarWithStack.jpg)

Each SCPF test contains detailed results about the variables measured during the test, which is illustrated using stacked and/or error bar graphs.  Depending on the test, stacked bar graphs display latencies or throughput values, with the value at the top of the stack being the sum of all of the bars.  Error bar charts display the top half of the error bars.

# **Overall Test Results**

## Overall Trend

![](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/FUNC_master_overview.jpg)

Similar to the trend graphs of individual tests, these graphs display the results of all  *tests* that are fully passing vs. tests that contain at least one error and the **number of tests run** for the corresponding build number.

## Overall Pie Chart

![](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/ALL_master_build-latest_executed_pieChart.jpg)![](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/ALL_master_build-latest_passfail_pieChart.jpg)

For each test category, the overall pie charts display percentage of passed *test cases* vs. percentage of failed *test cases*, and number of executed test cases vs. number of skipped test cases.

## Build Statistics

![](https://jenkins.onosproject.org/view/QA/job/postjob-VM/lastSuccessfulBuild/artifact/ALL_master_build-latest_test-suite-summary.jpg)

The build statistics graph displays a summary of all test suites as stacked bar graphs, with the stacks containing the percent of passed, failed, and skipped test cases for each test category.

# **Script Design**

Each script is divided into three major steps:

## Data Management

* Imports libraries used throughout the script.  The libraries used are:
  + ggplot2
  + reshape2
  + RPostgreSQL
* Reads CLI arguments and verifies all arguments are present.
* Creates title and filename of graph.
* Obtains test results from databases.

## Organize Data

* Extracts columns from the raw data to be used in the following data frame.
* Constructs data frame that is used in generating the graph.

## Generate Graphs

* Creates the main plot.
* Initializes attributes for formatting the graph.
* Initializes the graph type.
* Exports graph as file to destination specified in the CLI arguments.

# **Graph Customization**

Each graph present on the wiki may be customized.  All graphs may have the branch, name, and build number modified.  However, each script may have specific variables that may also be changed:

## Individual Test Trend Graphs

The total number of builds to show may be set.  The default setting is 20.

## SCPF Trend Graphs

The number of builds to show may be set, as well as whether to show old flow results (supported for branch onos-1.12 or newer).

## Overall Trend Graphs

The tests to include, total number of builds to show, and the title of the graph may be set.

## Overall Pie Charts

The tests to include and the build to show may be set, as well as whether to show passed/failed test cases, or executed/skipped test cases.

## Build Statistics

The title of the graph, build to show, and tests to display may be set.
