class MyError(Exception):
    pass

def stuff(file):
    raise MyError()

f = open(r'.\resources\data', 'w')
try:
    stuff(f)
finally:
    print('closing...')
    f.close()
print('not reached')