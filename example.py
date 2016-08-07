from spikefinder import load, score

a = load('a.csv')
b = load('b.csv')

for method in ['corr', 'auc', 'loglik', 'info', 'rank']:
    print('%s: %s' % (method, score(a, b, method=method)))