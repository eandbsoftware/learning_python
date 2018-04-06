# 3.X
'''
print("spam")
print('spam', 'ham', 'eggs')
print()
print('something')
print('')
print('something')
print()

# Format the print string as a single object
print('%s %s %s' % ('spam', 'ham', 'eggs'))
print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))
print('answer: ' + str(42))
'''

# 2.X
print('spam')
print 'spam', 'ham', 'eggs'
# Works in 2.X, but it's a tuple
print('spam', 'ham', 'eggs')

# Prints an empty tuple in 2.X
print()
# Use empty string to force a line-feed
print('')
print 'something'
print('')

# Manual string redirection
fname = r'.\resources\log_0377_2X.txt'
log = open(fname,'a')
print >> log, 1, 2, 3
print >> log, 4, 5, 6
log.close()
print "I'm back"

print open(fname,'r').read()
 
