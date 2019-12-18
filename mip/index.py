from pulp import *

v = { 'laptop':8, 'stereo':3, 'cellphone':6, 'watch':11 }
w = { 'laptop':5, 'stereo':7, 'cellphone':4, 'watch':3 }
limit = 14
items = list(sorted(v.keys()))

# create model
m = LpProblem('Knapsack', LpMaximize)

# variables
x = LpVariable.dicts('x', items, lowBound=0, upBound=1, cat=LpInteger)

# objective
m += sum(v[i] * x[i] for i in items)

# constraint
m += sum(w[i] * x[i] for i in items) <= limit

# optimize
m.solve()

# print the value of the variables at the optimum
for i in items:
    print('%s = %d' % (x[i].name, x[i].varValue))

# print the value of the objective
print('Max value = %d' % value(m.objective))