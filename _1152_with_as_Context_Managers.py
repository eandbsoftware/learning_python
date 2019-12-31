'''
# Basic Usage
try:
    with open(r'resources\data.txt', 'r') as myfile:
        for line in myfile:
            print(line.rstrip())
        print(f'{myfile.closed=}')
        raise Exception('Bye-bye')
except Exception:
    # Demonstrate the the implicit __exit__ method has closed the file
    print(f'{myfile.closed=}')
    print()

# Equivalent; requires 4 lines of code instead of 1
myfile = open(r'resources\data.txt', 'r')
try:
    for line in myfile:
        print(line.rstrip())
    print(f'{myfile.closed=}')
finally:
    myfile.close()
    print(f'{myfile.closed=}')
print()

# Decimal module example
import decimal
# https://docs.python.org/3.8/library/decimal.html
print(f'{decimal.getcontext().prec=}')
with decimal.localcontext() as ctx:
    print(f'{decimal.getcontext().prec=}')
    ctx.prec = 2
    print(f'{decimal.getcontext().prec=}')
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
    print(x)
print(f'{decimal.getcontext().prec=}')
'''

class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raised an exception! ' + str(exc_type))
            return False

if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test1')
        print('reached')

    with TraceBlock() as action:
        action.message('test2')
        raise TypeError('this string is NOT the exc_value arg of __exit__!')
        print('not reached')