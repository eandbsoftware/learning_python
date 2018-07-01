#import 'string'

#x = 'string'
#import x

modname = 'string'

# Running Code Strings - use exec
#exec('import ' + modname)

# Direct Calls: Two Options
# Use __import__ function
#string = __import__(modname)

# Use newer importlib.import_module
import importlib
string = importlib.import_module(modname)

print(string)
