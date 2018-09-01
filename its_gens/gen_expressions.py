import time

g = (num for num in range(1, 10))
print(g)

for n in g:
    print(n)

# generator expressions take up 10th of the memeory
# many instances there is no need for a list to persist in memory
# if all we are doing is making a calculation
print(sum(num for num in range(1, 10)))

gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f'gen time: {gen_time}')
print(f'list time: {list_time}')
