import sys
'''
# The Python "hello world" Program
print('hello world')

sys.stdout.write('hello world\n')

# Manual stream redirection
sys.stdout = open(r'.\resources\log_0375.txt','a')
print(1, 2, 3, flush=True)


# Automatic stream redirection
# Assign alternative file to sys.stdout
temp = sys.stdout
path = r'.\resources\log_0376.txt'
sys.stdout = open(path,'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()
sys.stdout = temp

print('back here')
print(open(path,'r').read())

# Use file key word arg of print
path = r'.\resources\log_0377.txt'
log = open(path,'a')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)
print(open(path, 'r').read())

# Printing to stderr
sys.stderr.write(('Bad!' * 8) + '\n')
print('Bad!' * 8, file=sys.stderr)
print('stderr and stdout go to the same place apparently')
'''

# Equivalence between printing and file write methods
X, Y = 1, 2
# Print the easy way
print(X, Y)
# Print the hard way
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

# Redirect to text file
path1 = r'.\resources\temp1_0378.txt'
print(X, Y, file=open(path1,'w'))
# Send to file manually
path2 = r'.\resources\temp2_0378.txt'
open(path2,'w').write(str(X) + ' ' + str(Y) + '\n')

# Read bytes back
print(open(path1,'rb').read())
print(open(path2,'rb').read())