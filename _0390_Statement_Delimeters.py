# A Few Special Cases

# Continuation line using open syntatic pairs
L = ["Good",
     "Bad",
     "Ugly"]
print(L)

# Using backslash to continue lines
if 1 == 1 and \
   2 == 2:
    print('olde')

# But using parenthesis is preferred
if (1 == 1 and
    2 == 2):
    print('new')

# Backslash is not recommended
x = 1 + 2 + 3 \
+4
print(x)

# Can wrote more than one noncompound statement on the same line with semicolon
x = 1; y = 2; print(x)

# Adjacent strings concatenate
S = """
aaaa
bbbb
cccc"""
print(repr(S))

S =('aaaa'
    'bbbb'
    'cccc')
print(S)

# Statement body can be moved to header line for simple statements
if 1: print('hello')