print('-------------- terminal break --------------')

file = open('story.txt')
print(file.closed)
print(file.read())
print(file.read())  # cursor is at end of file, prints blank

file.seek(0)
print(file.read())

file.seek(50)
print(file.read())

file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)
print(file.readlines())

file.close()
print(file.closed)

with open('story.txt') as f:
    data = f.read()
    print(data)
