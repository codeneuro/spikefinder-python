from spikefinder import load, score

a = load('a.csv')
b = load('b.csv')
s = score(a, b)

print('score: %s' % s)