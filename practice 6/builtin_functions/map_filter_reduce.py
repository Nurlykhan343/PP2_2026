from functools import reduce

values = [6, 7, 8, 9, 10]

print(len(values))
print(sum(values))
print(min(values))
print(max(values))
print(sorted(values))

powers = list(map(lambda x: x * x, values))
print(powers)

odd = list(filter(lambda x: x % 2 != 0, values))
print(odd)

result = reduce(lambda x, y: x + y, values)
print(result)