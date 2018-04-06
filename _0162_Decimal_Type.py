from decimal import Decimal
print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.3'))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print()

# Setting precision
import decimal
print(Decimal(1) / Decimal(7))
decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
decimal.getcontext().prec = 1
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print()

print(1999 + 1.33)
decimal.getcontext().prec = 2
pay = Decimal(str(1999 + 1.33))
print(pay)
decimal.getcontext().prec = 10


# Temporarily reset precision using context manager with with
print(Decimal('1.00') / Decimal('3.00'))
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('1.00') / Decimal('3.00'))
print (Decimal('1.00') / Decimal('3.00'))