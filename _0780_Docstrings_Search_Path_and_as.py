# Docstrings: Module Documentation at Work
from _0775_Example_Dual_Mode_Code import formats
#print(help(formats))

# Changing the Module Search Path
import sys
print(sys.path)
print()

sys.path.append('c:\\sourcedir')
print(sys.path)
print()

sys.path = [r'd:\temp']
sys.path.append('c:\\lp5e\\examples')
sys.path.insert(0, '..')
# Can't find string module now because we blew away the sys.path list.
print(sys.path)
try:
    import string
except ModuleNotFoundError as ex:
    print(ex)
print()

# The as Extension for import and from
import string as s
from string import ascii_letters as a
import xml.etree.ElementTree as ET