a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
                #two forward slashes returns int ans if we are dividing int numbers which is not the case with single forward slash
print(a % b)    # 0 modulo: the remainder after integer division

print()


#EXPRESSION
# in python, an expression is anything that can be calculated to return a value
#an expression can contain multiple expressions
#
for i in range(1, a//b):
    print(i)

print(a + b / 3  - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) /3) - 4) * 12)
print(((a + b) /3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) /b)
