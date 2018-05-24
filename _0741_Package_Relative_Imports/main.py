import sys
if sys.version_info[0] == 2:
    exec('print sys.version')
elif sys.version_info[0] == 3:
    print(sys.version)
else:
    pass
    
import dir1.mod

# The reference dir1.mod.util doesn't work because mod contains an assignment to dir1.util!
#print(dir1.mod.util.z)

# So mod must get to util THRU dir1!
print(dir1.mod.dir1.util.z)

# But we can also get to util from the top-level script where it naturally lives in the file hierarchy.
# Apparently the package module also gets loaded into the top-level file's namespace.
#print(dir1.util.z)
