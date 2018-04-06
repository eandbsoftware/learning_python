'''
# A Simple Interactive Loop
while True:
    reply = input("Enter text: ")
    if reply == 'stop': break
    print(reply.upper())

# Doing Mathk on User Inputs
while True:
    reply = input("Enter age :")
    if reply == 'stop' : break
    print(int(reply)**2)
print('bye!')

# Handling Errors by Testing Inputs
S = '123'
T = 'xxx'
print((S.isdigit(), T.isdigit()))

while True:
    reply = input("Enter text: " )
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply)**2)
print("Bye!")

# Handling Errors with try Statements
while True:
    reply = input("Enter text: ")
    if reply == 'stop' : break
    try:
        num = int(reply)
    except:
        print("Bad!" * 8)
    else:
        print(num**2)
print("Bye!")

# Supporting floating-point numbers
while True:
    reply = input("Enter text: ")
    if reply == 'stop' : break
    try:
        print(float(reply)**2)
    except:
        print("Bad!" * 8)
print("Bye!")        
'''

# Nesting Code Three Levels Deep
while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num**2)
print("Bye!")    