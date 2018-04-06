# Statement rule special cases

# Separate multiple statements on a single line with a semi-colon
a = 1; b = 2; print(a + b)

# Make a single statement span multiple lines with a bracketed pair
mylist = [1111,
          2222,
          3333]
print(mylist)

mydict = {
            "a" : 1,
            "b" : 2,
            "c" : 3 
         }

print(mydict['a'])

print(
    'jason'
)

X = (1 + 2 +
    3 + 4)
print(X)

if (1 == 1 and
    2 == 2 and
    3 == 3):
   print(True)

# Blockl rule special cases
if 1 < 2: print(1)

if 1 < 2:
 print('weird')