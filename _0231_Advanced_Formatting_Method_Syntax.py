# Advanced Formatting Method Examples
import sys
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print()

# Omitting the argument number
print('{:10} = {:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))
print()

# Floating-points
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
print()

# Other bases
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
print('{0:X}, {0:o}, {0:b}'.format(255))
print(bin(255), int('11111111',2), 0b11111111)
print(hex(255), int('FF', 16), 0xFF)
print(oct(255), int('377',8), 0o377)
print()

# Dynamic formatting parameters
# Hardcoded
print('{0:.2f}'.format(1 / 3.0))
print('%.2f' % (1 / 3.0))

# Dynamic
print('{0:.{1}f}'.format(1 / 3.0, 4))
print('%.*f' % (4, 1 / 3.0))
print()

# Built-in format method
print('{0:.2f}'.format(1.2345))
print(format(1.2345, '.2f'))
print('%.2f' % 1.2345)
