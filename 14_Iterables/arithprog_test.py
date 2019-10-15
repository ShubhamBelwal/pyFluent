from aritprog_v1 import ArithmeticProgression
from aritprog_v2 import aritprog_gen as v2
from aritprog_v3 import aritprog_gen as v3

print('#'*35)
print('Testing Regular Function v1')
print('#'*35)
ap = ArithmeticProgression(0, 1, 3)
print(list(ap))
ap = ArithmeticProgression(1, .5, 3)
print(list(ap))
ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))

from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1,3), 1)
print(list(ap))

from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('.1'), .3)
print(list(ap))

print('#'*35)
print('Testing Generator Function v1')
print('#'*35)

ap = v2(0, 1, 3)
print(list(ap))
ap = v2(1, .5, 3)
print(list(ap))
ap = v2(0, 1/3, 1)
print(list(ap))

from fractions import Fraction
ap = v2(0, Fraction(1,3), 1)
print(list(ap))

from decimal import Decimal
ap = v2(0, Decimal('.1'), .3)
print(list(ap))

print('#'*35)
print('Testing Generator Factory v1')
print('#'*35)

ap = v3(0, 1, 3)
print(list(ap))
ap = v3(1, .5, 3)
print(list(ap))
ap = v3(0, 1/3, 1)
print(list(ap))

from fractions import Fraction
ap = v3(0, Fraction(1,3), 1)
print(list(ap))

from decimal import Decimal
ap = v3(0, Decimal('.1'), .3)
print(list(ap))