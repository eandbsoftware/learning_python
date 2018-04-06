# Names matched by position from left to right by default
def f(a, b, c):
    print(a, b, c)
f(1, 2, 3)

# Keywords
f(c=3, b=2, a=1)
f(1, c=3, b=2)
#f(b=2, c=3, 1)
print()

# Defaults
def f(a, b=2, c=3):
    print(a, b, c)
f(1)
f(a=1)
f(1, 4)
f(1, 4, 5)
f(1, c=6)
print()

# Combining keywords and defaults
def func(spam, eggs, toast=0, ham=0):
    print(spam, eggs, toast, ham)
func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)
print()

L = [9]
# Multiple values for argument 'b'
#f(1, b=2, *L)
f(1, c=3, *L)
f(1, *L, c=3)

f(1, *L, 3)

