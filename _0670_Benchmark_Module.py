"""
pybench.py: Test speed of one or more Pythons on a set of simple
code-string benchmarks. A function, to allow stmts to vary. 
This system itself runs on both 2.X and 3.X, and may spawn both.

Uses timeit to test either the Python running this script by API
calls, or a set of Pythons by reading spawned command-line outputs
(os.popen) with Python's -m flag to find timeit on module search path.

Replaces $listif3 with a list() around generators for 3.X and an
empty string for 2.X, so 3.X does same work as 2.X. In command-line
mode only, must split multiline statements into one separate quoted 
argument per line so all will be run (else might run/time first line
only), and replace all \t in indentation with 4 spaces for uniformity.

Caveats: command-line mode (only) may fail if test stmt embeds double
quotes, quoted stmt string is incompatible with shell in general, or
command-line exceeds a length limit on platform's shell--use API call
mode or homegrown timer; does not yet support a setup statement: as is,
time of all statements in the test stmt are charged to the total time.
"""

import sys, os, timeit
defnum, defrep = 1000, 5    # May vary per stmt

def runner(stmts, pythons=None, tracecmd=False):
    """
    Main logic: run tests per input lists caller handles usage modes.
    stmts: [(number?, repeat?, stmt-string)], replaces $listif3 in stmt
    pythons: None=this python only, or [(ispy3?, python-executable-path)]
    """
    print(sys.version)
    for (number, repeat, stmt) in stmts:
        # or returns first object that evaluates to true (left to right)
        number = number or defnum
        repeat = repeat or defrep # 0=default

        if not pythons:
            # Run stmt on this python: API call
            # No need to split lines or quote here
            ispy3 = sys.version[0] == '3'
            stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
            best = min(timeit.repeat(stmt, number=number, repeat=repeat))
            # Similar to s but uses repr instead of str
            print('%.4f  [%r]' % (best, stmt[:70]))
        else:
            # Run stmt on all pythons: command line
            # Split lines into quoted arguments
            print('-' * 80)
            print('[%r]' % stmt)
            for (ispy3, python) in pythons:
                stmtl = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmtl = stmtl.replace('\t', ' ' * 4)
                lines = stmtl.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m timeit -n %s -r %s %s' % (python, number, repeat, args)
                print(python)
                if tracecmd: print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())