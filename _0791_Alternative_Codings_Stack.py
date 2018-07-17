'''
_0791_Alternative_Codings_Stack.py: transitively reload nested modules (explicit stack)
'''

import types
from imp import reload
from _0787_Example_Transitive_Module_Reloads import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()
        status(next)
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values() if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    # Unmatched positional arguments are collected into a tuple.
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, '_0791_Alternative_Codings_Stack')