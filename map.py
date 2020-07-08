"""

The map() function executes a specified function for each item in a iterable.
The item is sent to the function as a parameter.

map(function, iterables)

"""

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))


print(x)

print(list(x))


def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))


print(list(x))
