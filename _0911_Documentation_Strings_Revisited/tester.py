import docstr
print(docstr.__doc__)
print(docstr.func.__doc__)
print(docstr.spam.__doc__)
print(docstr.spam.method.__doc__)
print()

x = docstr.spam()
x.method()

help(docstr)
