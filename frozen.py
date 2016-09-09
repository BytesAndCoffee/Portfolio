from pipe import FrozenFunction
from copy import copy


@FrozenFunction
def f(a, b, c):
    a, b, c = map(str, [a, b, c])
    return a + b + c

print(f.parameters)

for p in f.parameters:
    f[p] = 1

g = copy(f)
g.a = 3

print(f())
print(g())
