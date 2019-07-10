'''
# Example: Default Behavior
def gobad(x, y):
    return x / y

def gosouth(x):
    print(gobad(x, 0))

gosouth(1)
'''

# Example: Catching Built-in Exceptions
def kaboom(x, y):
    print(x + y)

try:
    kaboom([1, 2, 3], 'spam')
except TypeError:
    print('Hello TypeError')
print('Error is dead')