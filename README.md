# spikefinder-python

> python module for testing spike detection algorithms

This repository contains a module and a CLI for working with spike finding algorithm results. It is used by the [spikefinder](https://github.com/codeneuro/spikefinder) benchmarking challenge to compare ground truth results to results from submitted algorithms.

The included functions compute evaluation statistics. You can use it to compare ground truth against algorithm results and load result files in standard formats, either as a command line tool, or as a module inside a python project (supports Python 2.7 and 3.4).

If you have any questions about these metrics or want to suggest others, please open an issue or submit a pull request!

## use as a command line tool

To evaluate a pair of results, just pass two `JSON` files as arguments

```
spikefinder evaluate a.json b.json
```

## use as a module

You can also use this module inside a Python project, for example

```python
from spikefinder import load, score

a = load('a.json')
b = load('b.json')
score(a, b)
```

## methods

#### `spikefinder.load(file)`

Load results from a JSON file.

#### `spikefinder.score(a, b)`

Estimate similarity scores between two results.