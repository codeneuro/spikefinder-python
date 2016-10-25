import os
import json
import click
from numpy import mean
from .. import load, score

@click.argument('files', nargs=2, metavar='<files: ground truth, estimate>', required=True)
@click.command('evaluate', short_help='compare two sets of results', options_metavar='<options>')
def evaluate(files):
    a = load(files[0])
    b = load(files[1])

    scores = {}

    for method in ['corr', 'rank', 'info', 'loglik']:
      allscores = score(a, b, method=method)
      scores[method] = mean(allscores)

    print(scores)