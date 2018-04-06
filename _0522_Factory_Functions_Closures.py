# A simple factory function
def maker(N):
    def action(X):
        return X**N
    return action

f = maker(2)
print(f)

print(f(3))
print(f(4))
print()

# A different maker
g = maker(3)
print(g(4))
print(f(4))
print()

# A factory function using a lambda expression
def maker(N):
    return lambda X: X**N

h = maker(3)
print(h(4))