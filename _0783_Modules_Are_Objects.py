'''
mydir.py: a module that lists the namespaces of other modules
'''

from __future__ import print_function # 2.X compatibility

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in sorted(module.__dict__):
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)

def getting_module_attributes():
    import sys
    import xml.etree.ElementTree as ET
    import string

    attribute = string.ascii_letters
    print(attribute)

    attribute = string.__dict__['ascii_letters']
    print(attribute)

    attribute = sys.modules['string'].ascii_letters
    print(attribute)

    attribute = getattr(string, 'ascii_letters')
    print(attribute)
    print()

    attribute = ET.parse
    print(attribute)

    attribute = ET.__dict__['parse']
    print(attribute)

    # Note that when aliasing modules with as, sys.modules stores the fully-qualified name.
    #[print(m) for m in sorted(sys.modules)]
    attribute = sys.modules['xml.etree.ElementTree'].parse
    print(attribute)

    attribute = getattr(ET, 'parse')
    print(attribute)

if __name__ == '__main__':
    import _0783_Modules_Are_Objects as mydir
    listing(mydir)
