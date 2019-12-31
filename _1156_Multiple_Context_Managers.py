# with open(r'.\resources\script1.py') as f1, open(r'.\resources\script2.py') as f2:
#     for pair in zip(f1, f2):
#         print(pair)

# with open(r'.\resources\script1.py') as f1, open(r'.\resources\script2.py') as f2:
#     for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
#         print(linenum, line1.rstrip(), line2.rstrip(), sep=", ")

# # Equivalent to simplier code below because file objects are closed automatically.
# for pair in zip(open(r'.\resources\script1.py'), open(r'.\resources\script2.py')):
#     print(pair)

# with pattern is useful here to flush outbuffer of fout for immediate access
with open(r'.\resources\script2.py') as fin, open(r'.\resources\upper.py', 'w') as fout:
    for line in fin:
        fout.write(line.upper())
print(open(r'.\resources\upper.py').read())

# In many contexts, files are reclaimed/closed without with/as.
# One use-case of with/as is to force garbage collection/closure at a specific time.
# Another use-case is when you need to force file close on an exception.
# But you may not need to worry about closing a file via with/as if your program is dead anyway. 