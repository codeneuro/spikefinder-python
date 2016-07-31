import os
import json
import click
from .. import load, score

@click.argument('files', nargs=2, metavar='<files: ground truth, estimate>', required=True)
@click.command('evaluate', short_help='compare two sets of results', options_metavar='<options>')
def evaluate(files):
    a = load(files[0])
    b = load(files[1])

    scores = score(a, b)

    print(scores)