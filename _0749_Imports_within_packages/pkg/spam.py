# Incompatable behavior.
# This is relative in 2.X and absolute in 3.X
#import eggs

# Works in both 2.X and 3.X
from . import eggs
print(eggs.X)