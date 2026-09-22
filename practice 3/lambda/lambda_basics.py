x = lambda a: a + 15
print(x(7))

x = lambda a, b: a * b
print(x(4, 7))

x = lambda a, b, c: a + b + c
print(x(3, 8, 4))


def myfunc(n):
  return lambda a: a * n

mydoubler = myfunc(3)

print(mydoubler(10))
