# A win for map and a rare los for PyPy
import _0670_Benchmark_Module as pybench, sys

pythons = [
    # (ispy3?, path)
    (1, r'"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\python.exe"'),
    (0, r'C:\Python27amd64\python.exe'),
    (0, r'C:\Users\jason\Downloads\pypy3-v5.10.1-win32\pypy3.exe')
]

stmts = [
    # Use function calls: map wins
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
    # Sets and dicts
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
    # Pathological: 300k digits
    (1, 1, "len(str(2 ** 1000000))"),
    # The impact of function calls revisited
    (0, 0, "def f(x): return x\n[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x): return x\nres=[]\nfor x in 'spam' * 2500: res.append(f(x))"),
    (0, 0, "def f(x): return x\n$listif3(map(f, 'spam' * 2500))"),
    (0, 0, "def f(x): return x\nlist(f(x) for x in 'spam' * 2500)")
    ]

tracecmd = '-t' in sys.argv
pythons = pythons if '-a' in sys.argv else None
pybench.runner(stmts, pythons, tracecmd)

