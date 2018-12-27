'''
This module runs in 2.X only.
'''
# class C:
#     data = 10
#     def __cmp__(self, other):
#         '''
#         Note that this method will return the same int result (-1, 0, 1) for the same operands.
#         That result is evaluated in the context of the operator expression to obtain a bool.        
#         This is a different paradigm than __gt__ which directly returns a bool.
#         '''
#         result = cmp(self.data, other)
#         return result
        #return 0

#X = C()
# Note that __comp__ returns the same result for both expressions,
# but they are evaluated differently in the context of the operators.
# Ex.: __comp__(10, 5) == 1 means precisely that 10 is greater than 5. 
# Thus, 10 > 5 is true. Conversely, 10 < 5 is false because
# the return value of 1 means precisely that 10 > 5! 
# print(X > 5)
# print(X < 5)
# print()

class D:
    data = 10
    # Fails (initially) in 3.X because of __cmp__ is not invoked for 
    # comparison opeartors not because cmp is no longer a keyword
    def __cmp__(self, other):
        A = (self.data > other)
        B = (self.data < other)
        result =  A - B
        return result

Y = D()
# TypeError in 3.X: > not supported
print(Y > 5)
print(Y < 5)
