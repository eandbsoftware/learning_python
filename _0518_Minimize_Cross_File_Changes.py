import first
'''
# Cross-file change
print(first.X)
first.X = 88
print(first.X)
'''
# Using accessor function
print(first.X)
first.setX(77)
print(first.X)
