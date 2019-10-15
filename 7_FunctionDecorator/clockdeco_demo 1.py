from clockdeco import clock
import time
from functools import lru_cache

# @lru_cache()
@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*'*40, 'calling factorial(6)')
    print('6! = ',factorial(30))