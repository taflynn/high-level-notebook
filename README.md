# <img src='./images/logo.svg' width=90 style="vertical-align:middle" /> SHAREing: High-level performance assessment notebook

**This repository is in a very early stage of development**

This repository is part of the [SHAREing](https://shareing-dri.github.io/)
project and is focused on conducting high-level performance assessments of
research software. We use a Jupyter notebook as our interface as we see the
notebook as acting as 'workbook' or 'lab notebook' during the high-level
assessment.

## Setup

To use the Jupyter notebook to conduct a high-level assessment, very few Python
dependencies are required and can be installed locally, or in a virtual
environment, by running the command 
```bash
pip install -r requirements.txt
```
Otherwise, the notebook relies on just a few classes which are defined in the
`topics` directory.

## Structure of high-level performance assessment

Performance is broken down into 5 main topics
1. Core
2. Intra-node
3. Inter-node
4. GPU
5. I/O

Further details of how to conduct each performance measurement are given in the
notebook, however, below we list the main classes and methods currently
implemented in the high-level assessment.

### Core analysis

Core performance analysis is packaged up into the `core_perf` class, which has
only one method: `core_perf_table`. This method generates a tables with a score
of the observed compute rate for the application.

### Intra-node analysis

Intra-node performance analysis is packaged up into the `intra_node_perf`
class, which has three methods:
1. `parallel efficiency figure` - this generates a figure of the parallel
   efficiency against the core count. It also includes amber and red vertical,
dashed lines, beyond which the parallel efficiency drops below 80% and 60%,
respectively.
2. `runtimes_figure` - this generates a figure of the total runtime against the
   core count.
3. `intra_node_perf_table` - this generates a table with a score of how
   effectively the intra-node parallelism scales across the available cores.
The core counts and runtimes are read into these methods as lists. For
convenvience the data can be read in as a file, e.g., by using `pandas` like
```bash
# read in data
df = pandas.read_csv('./runtime_data.csv', header=None)

# core count data from first column
number_of_cores = list(df[df.columns[0]]) 
# application runtime data from second column
time = list(df[df.columns[1]])
```
where here we have set up around data with core counts in the first column, and
associated runtimes in the second column.

### Inter-node analysis

Inter-node performance analysis is packaged up into the `inter_node_perf`
class, which has three methods:
1. `parallel efficiency figure` - this generates a figure of the parallel
   efficiency against the node count. It also includes amber and red vertical,
dashed lines, beyond which the parallel efficiency drops below 80% and 60%,
respectively.
2. `runtimes_figure` - this generates a figure of the total runtime against the
   node count.
3. `inter_node_perf_table` - this generates a table with a score of how
   effectively the inter-node parallelism scales across the available nodes.
The node counts and associated runtimes are read into the methods as lists, and
we can again read these in as above using a module such as `pandas`.

### GPU analysis

GPU performance analysis is packaged up into the `gpu_perf` class, which has
only one method: `gpu_perf_table`. This method generates a tables with a
measure of the GPU occupancy.

### I/O analysis

I/O performance analysis is packaged up into the `io_perf` class, which has
only one method: `io_perf_table`. This method generates a table with a score of
the proportion of runtime spent in I/O.

### Summary diagram

Finally, the `summary_perf` class reads in all 5 of the performance metrics and
plots these via `plotly` to create a summary radar plot.

## Contributions

This performance assessment is intentionally limited as we want to simply
capture the performance of software at a *high level*. However, if you have
ideas of performance metrics which are necessary but missing, or if you find
any faults with the notebook, please raise an issue.

## Acknowledgements
The initial development of this notebook was implemented by Ben Clark.  This
project has received funding through the UKRI Digital Research Infrastructure
Programme under grant UKRI1801 (SHAREing). 

<img src='./images/ukri.png' width=200 style="vertical-align:middle" /> 
