from formats import money, commas

print(money(123.456))
print(money(-9999999.99, 15))
X = 99999999999999999999999
print('%s (%s)' % (commas(X), X))