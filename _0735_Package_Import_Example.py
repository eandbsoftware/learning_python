# 1. You CAN import just a directory;
# 2. but by default, you don't get access to sub-modules in that directory (i.e., nested directories or module files), only variables assigned in it's __init__.py file
# 3. import will always yield a module
# 4. from...import MAY yield a module, or NOT;
# 5. and you won't know from just looking at the import statement

import dir1.dir2.mod
print()

# Second import statement does not reload module
#import dir1.dir2.mod

'''
# Use reload to reload
from imp import reload
reload(dir1)
print()

reload(dir1.dir2)
print()
'''

print(dir1)
print(dir1.dir2)
print(dir1.dir2.mod)
print()

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)


# from Versus import with Packages
'''
from dir1.dir2 import mod
print(mod.z)
'''

'''
from dir1.dir2.mod import z
print(z)
'''

'''
import dir1.dir2.mod as mod
print(mod.z)
'''

'''
from dir1.dir2.mod import z as modz
print(modz)
'''