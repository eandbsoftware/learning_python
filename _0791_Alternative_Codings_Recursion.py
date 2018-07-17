'''
_0791_Alternative_Codings_Recursion.py: transitively reload nested modules (alternative coding)
'''

import types
from imp import reload
from _0787_Example_Transitive_Module_Reloads import status, tryreload, tester

def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) == types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)

def reload_all(*args):
    transitive_reload(args, set())

if __name__ == '__main__':
    tester(reload_all, '_0791_Alternative_Codings_Recursion')
