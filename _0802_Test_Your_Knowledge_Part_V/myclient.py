import os, sys
print(f'CWD:\n\t{os.getcwd()}')
print('sys.path:')
[print('\t', repr(p)) for p in sys.path]

# An unqualified import only works if the imported module is in the home directory
# (the first entry on the python path).
# BUT, the home directory depends on whether the code run as a program or interactively!
#   program -> home dir is dir in which the program resides
#   interactively -> home dir is dir from which you launched interactive prompt

# So if I run an unqualified import interactively it will fail to locate the module mymod
# because mymod isn't in c:\users\jason, it is in C:\_Gastelum\Development\Learning_Python_5th_Edition\_0802_Test_Your_Knowledge_Part_V
# Running as a program, a qualified or unqualified import will work.

#import mymod
import _0802_Test_Your_Knowledge_Part_V.mymod as mymod
print(mymod.test(r'C:\_Gastelum\Development\Learning_Python_5th_Edition\_0802_Test_Your_Knowledge_Part_V\mymod.py'))