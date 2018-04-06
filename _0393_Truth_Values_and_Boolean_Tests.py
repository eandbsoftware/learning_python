# Comparisons return True or False

print(2 < 3, 3 < 2)
print(bool(2 < 3) == 1, bool(3 < 2) == 0)
print()

# or test returns first operand that evaluates to true, or right operand
# returns left operand if true, otherwise right operand (true or false)
print(2 or 3, 3 or 2)
print([] or 3)
print([] or {})
print()

# and test returns first operand that evaluates to false, or right operand
# returns left operand if false, otherwise right operand (true or false)
print(2 and 3, 3 and 2)
print([] and {})
print(3 and [])
print()

# Comparisons return a bool 
print(type(2 < 3))
# Boolean operators return an operand
print(type(2 and {}))
# Then use bool to turn operand object into bool
print(type(bool(2 and {})))