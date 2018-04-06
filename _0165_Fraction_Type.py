from fractions import Fraction
from decimal import Decimal
import decimal

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y)
print()

print(x + y)
print(x - y)
print(x * y)
print()

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))
print()

# Same operations run with floating-point objects
a = 1 / 3
b = 4 / 6
print(a)
print(b)
print()

print(a + b)
print(a - b)
print(a * b)
print()

# Getting exact results with Fraction and Decimal
print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print()

# More intuitive than floating-points using rational representation or limiting precision
print(1/3)
print(Fraction(1, 3))
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))
print()

print((1 / 3) + (6 / 12))
print(Fraction(6, 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(Decimal(str(1/3)) + Decimal(str(6/12)))
print()

print(1000.0 / 1234567890)
print(Fraction(1000,1234567890))
print()

# Conversions
# float.as_integer_ratio: float -> Fraction
print((2.5).as_integer_ratio())
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z, type(z))
print(x + z)

# Fraction.from_float: float -> Fraction
print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))

# Fraction -> float
print(float(x))
print(float(z))
print(float(x + z))
print(17 / 6)
print()

# Type mixing
print(x)
# Fraction + int -> Fraction
print(x + 2)
# Fraction + float -> float
print(x + 2.0)
print(x + (1 / 3))
print(x + (4 / 3))
# Fraction + Fraction -> Fraction
print(x + Fraction(4, 3))
print()

# Precision loss
print(4 / 3)
print((4 / 3).as_integer_ratio())
a = x + Fraction(*(4 / 3).as_integer_ratio())
print(a)
print(22517998136852479/13510798882111488)
print(a.limit_denominator(10))
