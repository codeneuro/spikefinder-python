# spikefinder-python

> python module for testing spike detection algorithms

WORK IN PROGRESS

This repository contains a module and a CLI for working with spike finding algorithm results. Spike finding is defined as identifying the timing of discrete spiking events from continuous-valued calcium flouresence data. This module is used by the [spikefinder](https://github.com/codeneuro/spikefinder) benchmarking challenge to compare ground truth results to results from submitted algorithms.

The included functions compute evaluation statistics. You can use it to compare ground truth against algorithm results and load result files in standard formats, either as a command line tool, or as a module inside a python project (supports Python 2.7 and 3.4).

If you have any questions about these metrics or want to suggest others, please open an issue or submit a pull request!

## use as a command line tool

To evaluate a pair of results, just pass two `CSV` files as arguments

```
spikefinder evaluate a.csv b.csv
```

## use as a module

You can also use this module inside a Python project, for example

```python
from spikefinder import load, score

a = load('a.csv')
b = load('b.csv')
score(a, b)
```

## methods

#### `spikefinder.load(file)`

Load results from a CSV file.

#### `spikefinder.score(a, b)`

Estimate similarity scores between two results.

## format

Input data should be formatted as comma-separated values in a table, where each row corresponds to a time point and each column corresponds to a neuron, and the header row are integer labels, e.g.

```
0,1,2,3,4,5,6,7,8,9,10
0,0,0,0.0,0,0,0,0,0,0,0
0,0,0,0.0,0,1,0,0,0,0,0
0,0,0,0.0,0,0,0,0,0,0,0
0,0,0,0.0,0,1,0,0,0,0,0
0,0,0,0.0,0,0,0,0,0,0,0
...
0,0,,0,0,0,0,0,0,,0
0,0,,,0,0,0,,0,,0
```

It is fine if different columns have different lengths, just leave these entries empty as in the last two rows of the above example. 

If you have your `time point x neuron` table of results as an array in Python named `mat`, with `nan`s for any missing entries, you can write it to a correctly formatted output file using

```python
from pandas import DataFrame

df = DataFrame(mat)
df.to_csv('filename.csv', index=False)
```
