# Slicing off newlines
# Make file
path = r"./resources/text_0612.txt"
'''
f = open(path,'w')
f.writelines(['aaa\n', 'bbb\n', 'ccc\n'])
f.close()
'''

content = open(path,'r').readlines()
print(content)

result = [line.rstrip() for line in open(path,'r').readlines()]
print(result)

result = [line.rstrip() for line in open(path,'r')]
print(result)

result = list(map(lambda line: line.rstrip(), open(path,'r')))
print(result)
print()

# Column Projection
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
result = [age for (name, age, job) in listoftuple]
print(result)

result = list(map(lambda x: x[1], listoftuple))
print(result)