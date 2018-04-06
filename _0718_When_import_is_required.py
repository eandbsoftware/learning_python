from _0718_M import func
from _0718_N import func

# Second import statement overwrites func retrieved from M
func()
print()

# Must use import to qualify name with the name of the enclosing module
import _0718_M, _0718_N
_0718_M.func()
_0718_N.func()
print()

# Or use as
from _0718_M import func as mfunc
from _0718_N import func as nfunc
mfunc()
nfunc()
