"""
pybench_cases.py: Run pybench on a set of pythons and statments.

Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import _0677_Room_for_improvement_Module as pybench, sys

pythons = [
    # (ispy3?, path)
    (1, r'"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe"'),
    (0, r'C:\Python27amd64\python.exe'),
    (0, r'C:\Users\jason\Downloads\pypy3-v5.10.1-win32\pypy3.exe')
]

stmts = [
    # (num, rpt, setup, stmt)
    (0, 0, "", "[x ** 2 for x in range(1000)]"),
    (0, 0, "", "res=[]\nfor x in range(1000): res.append(x ** 2)"),
    (0, 0, "def f(x):\n\treturn x", "[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x):\n\treturn x", "res=[]\nfor x in 'spam' * 2500:\n\tres.append(f(x))"),
    (0, 0, "L=[1, 2, 3, 4, 5]", "for i in range(len(L)): L[i] += 1"),
    (0, 0, "L=[1, 2, 3, 4, 5]", "i=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")    
    ]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)