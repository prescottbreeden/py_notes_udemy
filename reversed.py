nuns = [1, 2, 3, 4]
print(nuns)
nuns.reverse()
print(nuns)

print(reversed(nuns))
print(list(reversed(nuns)))

snun = nuns[::-1]
print(snun)

for char in reversed("Hello World"):
    print(char)

print("hello world"[::-1])

print(reversed("hello"))
print(list(reversed("hello")))
print(''.join(list(reversed("hello"))))

for x in reversed(range(0, 11)):
    print(x*2)
