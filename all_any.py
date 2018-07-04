import sys

people = ["Charlie", "Casey", "Cody", "Carly", "Christina", "Chuck Norris"]
c_names = all([name[0] is 'C' for name in people])
print(c_names)

people.append("Kristy")
c_names2 = all([name[0] is 'C' for name in people])
print(c_names2)

k_names = any([name[0] is 'K' for name in people])
print(k_names)

'''
the above examples use list-comprehension inside the all/any function,
however, there is really no point since we are not actually using the info
contained in the output of the list-comprehension

the alternative is using a generator expression which is just a light-weight
object that contains the components of the list-comprehension but without
the ability to read it or use built-in list functions on them

the above and the below are identical outputs but the expressions use
less memory than the comprehensions
'''

people = ["Charlie", "Casey", "Cody", "Carly", "Christina", "Chuck Norris"]
c_names = all(name[0] is 'C' for name in people)
print(c_names)

people.append("Kristy")
c_names2 = all(name[0] is 'C' for name in people)
print(c_names2)

k_names = any(name[0] is 'K' for name in people)
print(k_names)

# -------------
# More details:
# -------------

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
