def countLines(file):
    line_count = 0
    for line in file:
        line_count += 1
    file.seek(0)
    return line_count

def countChars(file):
    char_count = 0
    for line in file:
        char_count += len(line)
    file.seek(0)
    return char_count

def test(name):
    # Open once
    target = open(name, 'r')
    line_count = countLines(target)
    char_count = countChars(target)
    return line_count, char_count

if __name__ == '__main__':
    import os
    print(f'Current working dir:\n\t{os.getcwd()}\n')
    print("Python path:")
    import sys
    [print(f'\t{p}') for p in sys.path]

    # Default uses the file itself is none is given at the command line
    fpath = f'C:\_Gastelum\Development\Learning_Python_5th_Edition\_0802_Test_Your_Knowledge_Part_V\mymod.py'
    if len(sys.argv) > 1:
        fpath = sys.argv[1]

    print(f'\n(lines, chars)\n\t{test(fpath)}')