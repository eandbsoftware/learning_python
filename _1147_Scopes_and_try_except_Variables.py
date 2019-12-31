# # In 2.X the exception reference variable is NOT localized
# try:
#     1 / 0
# except Exception as X:
#     print X
# print X
# print "\n"

# # Using either syntax
# try:
#     1 / 0
# except Exception, X:
#     print X
# print X

# # In 3.X the exception reference name is localized to the except block
# try:
#     1 / 0
# # Invalid syntax in 3.X
# except Exception, X:
#     print X
# print X

# try:
#     1 / 0
# except Exception as X:
#     print(X)
# print(X)

# # Variable is REMOVED after the exception block,
# # even if you are using the name elsewhere!
# X = 99
# try:
#     1 / 0
# except Exception as X:
#     print(X)
# print(X)
# print()

# More extreme policy than for comprehensions
X = 99
{print(X, end=' ') for X in 'spam'}
print(X)

# Use unique variable names in try statement except clauses.
try: 
    1 / 0
except Exception as X:
    print(X)
    Saveit = X
print(Saveit)

