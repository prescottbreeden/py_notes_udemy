name = "Chuck"
it = iter(name)

x = [next(it) for i in range(0, len(name))]
print(list(x))

y = [x for x in name]
print(y)
