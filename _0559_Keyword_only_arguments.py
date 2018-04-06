# Kewyord-only arguments appear after *args
def kwonly(a, *b, c):
    print(a, b, c)
kwonly(1, 2, c=3)
kwonly(a=1, c=3)
#kwonly(1, 2, 3)
print()

# Does not accept variable-length argument list but still expects
# all arguments following the * to be passed as keywords
def kwonly(a, *, b, c):
    print(a, b, c)
kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
#kwonly(1, 2, 3)
#kwonly(1)
print()

# Can still use defaults
def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)
kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)
#kwonly(1, 2)
print()

# Keyword-only arguments with defaults are optional,
# but those without defaults effectively become required keywords
def kwonly(a, *, b, c='spam'):
    print(a, b, c)
kwonly(1, b='eggs')
#kwonly(1, c='eggs')
#kwonly(1, 2)
print()

def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)
kwonly(3, c=4)
kwonly(3, c=4, b=5)
#kwonly(3)
#kwonly(1, 2, 3)