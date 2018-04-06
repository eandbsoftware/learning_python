"""
pybench_cases.py: Run pybench on a set of pythons and statments.

Select modes by editing this script or using command-line arguments (in
sys.argv): e.g., run a "C:\python27\python pybench_cases.py" to test just
one specific version on stmts, "pybench_cases.py -a" to test all pythons
listed, or a "py -3 pybench_cases.py -a -t" to trace command lines too.
"""

import _0670_Benchmark_Module as pybench, sys

pythons = [
    # (ispy3?, path)
    (1, r'"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe"'),
    (0, r'C:\Python27amd64\python.exe'),
    (0, r'C:\Users\jason\Downloads\pypy3-v5.10.1-win32\pypy3.exe')
]

stmts = [
    # (num, rpt, stmt)
    (0, 0, "[x ** 2 for x in range(1000)]"),                        # Iterations
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),     # \n=multistmt
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),         # \n\t=indent
    (0, 0, "list(x ** 2 for x in range(1000))"),                    #$=list or ''
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),  # string ops
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'")
    ]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)