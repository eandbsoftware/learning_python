def saver(x = []):
    x.append(1)
    print(x)

saver([2])
saver()
saver()
saver()
print()

def saver(x=None):
    if x is None:
        x=[]
    x.append(1)
    print(x)

saver([2])
saver()
saver()
saver()
print()

# If an empty list is passed in, the or operater return the new list local to the function
def saver(x=None):
    x = x or []
    x.append(1)
    print(x)

saver([2])
saver()

empty=[]
saver(empty)
print(empty)
print()

def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
saver()
saver()
