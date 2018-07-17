'''
Transitively reload nested modules (2.X and 3.X).
Call reload_all with one or more imported module obects.
'''

import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        attobjs = module.__dict__.values()
        for attrobj in attobjs:
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)

def reload_all(*args): #: types.ModuleType):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):
    import importlib, sys
    if len(sys.argv) > 1:
        modname = sys.argv[1]
    # Must import itself so it has a reference to its module to pass to reload_all
    module = importlib.import_module(modname)
    reloader(module)

if __name__ == '__main__':
    tester(reload_all, '_0787_Example_Transitive_Module_Reloads')