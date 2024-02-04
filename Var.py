#Variable

print('#Int')
a = 333
print(type(a))

print('#String')
b = "Demo"
print(type(b))

print('#Float')
c = 3.5
print(type(c))

print("========================================")
# import Decimal lib
from decimal import*

# Lấy tối đa 30 chữ số phần nguyên của decimal
getcontext().prec = 40
#getcontext().prec = 3

# chỉ cần 1 biến là decimal thì cả biểu thức là decimal
d = Decimal(12)/5

print(10/3)
print(Decimal(10)/Decimal(3))
print(10/Decimal(3))

print(type(d))

print("========================================")
from fractions import *

frac1 = Fraction(5,2)
frac2 = Fraction(2,3)


print(frac1+frac2)
print(type(frac1+frac2))


print("========================================")

cc = complex(2,5)

print(cc)
print(cc.real)
print(cc.imag)