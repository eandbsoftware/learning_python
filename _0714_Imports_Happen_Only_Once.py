# Prints 'hello'
import _0714_simple

# Prints value of spam
print(_0714_simple.spam)

_0714_simple.spam = 2
print(_0714_simple.spam)

# Second import does nothing
import _0714_simple

# spam still equals 2
print(_0714_simple.spam)