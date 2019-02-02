# Changing Strings II
S = 'spammy'
S = S[:3] + 'xx' +  S[-1:]
print(S)

S = 'spammy'
S = S.replace('mm','xx')
print(S)

S = 'aa$bb$cc$dd'
S = S.replace('$','SPAM')
print(S)
print()

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)
print()

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM','EGGS'))
print(S.replace('SPAM','EGGS', 1))
print()

S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)
print()

print('SPAM'.join(['eggs','sausage','ham','toast']))
print()

# Parsing Text
line = 'aaa bbb ccc'
col1 = line[:3]
print(col1)
col3 = line[8:]
print(col3)
cols = line.split()
print(cols)
print()

line = 'bob,hacker,40'
print(line.split(','))
print()

line = "i'mSPAMaSPAMlumberjack"
print(line.split("SPAM")) 
print()

# Other Common String Methods
line = 'The knights who say Ni!\n'
print(line)
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))
print()

print(line.find('Ni') != -1)
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))
print(line[-len(sub):] == sub)