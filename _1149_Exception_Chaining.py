# # Propagating Exceptions with raise
# try:
#     raise IndexError('spam')
# except IndexError:
#     print('propagating')
#     raise

# # Python 3.X Exception Chaining: raise from
# # https://stackoverflow.com/questions/24752395/python-raise-from-usage
# try:
#     1 / 0
# except Exception as E:
#     # 'The above exception was the direct cause of the following exception'
#     #raise TypeError('from something') from E
    
#     # 'During the handling of the above exception, another exception occurred'
#     #raise TypeError('from nothing')
    
#     # Just the most recent exception
#     raise TypeError('None') from None
    
# try:
#     1 / 0
# except:
#     badname

# try:
#     try:
#         raise IndexError('one')
#     except Exception as E:
#         raise TypeError('two') from E
# except Exception as E:
#     raise SyntaxError('three') from E

# try:
#     try:
#         1 / 0
#     except:
#         badname
# except:
#     open('nonesuch')

# try:
#     try:
#         raise IndexError('one')
#     except Exception as E:
#         raise SyntaxError('two') from E
# except Exception as E:
#     print(f'{E=}')
#     print(f'{E.__cause__=}')

# print 'Python 2.7'