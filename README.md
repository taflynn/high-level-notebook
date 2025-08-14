# <img src='./images/logo.svg' width=90 style="vertical-align:middle" /> SHAREing: High-level performance assessment notebook

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
`tools` directory.

## Structure of high-level performance assessment

Performance is broken down into 5 main topics
1. Core
2. Intra-node
3. Inter-node
4. GPU
5. I/O

So far, the high-level assessment notebook has implemented high-level metrics
of the **core** and **intra-node** performance topics.

Further details of how to conduct each performance measurement are given in the
notebook, however, below we list the main classes and methods currently
implemented in the high-level assessment.

### Core analysis

Core performance analysis is packaged up into the `core_perf` class, which has
only one method: `core_perf_table`. This method generates a tables which gives
a 'score' of how the memory bandwidth and compute rate perform.

### Intra-node analysis

Intra-node performance analysis is packaged up into the `intra_node_perf`
class, which has three methods:
1. `plot_efficiency_graph` - this generates a figure of the parallel efficiency
   against the core count. It also includes amber and red vertical, dashed
lines, beyond which the parallel efficiency drops below 80% and 60%,
respectively.
2. `plot_time_graph` - this generates a figure of the total runtime against the
   core count.
3. `intra_perf_table` - this generates a table which gives a 'score' of how
   effectively the intra-node parallelism performs.

## Contributions

This performance assessment is intentionally limited as we want to simply
capture the performance of software at a *high level*. However, if you have
ideas of performance metrics which are necessary but missing, or if you find
any faults with the notebook, please raise an issue.

## Acknowledgements

This project has received funding through the UKRI Digital Research
Infrastructure Programme under grant UKRI1801 (SHAREing)

<img src='./images/ukri.png' width=200 style="vertical-align:middle" /> 
