import random
import time

MINN = 2
MAXX = 80
RESmin = 0
RESmax = 100
Length = 4
random.seed(random.randint(0, 100000))
from get_divisors import get_all_divisors2

for i in range(25):
    t_Length = Length
    t_res = random.randint(MINN, MAXX)
    print(t_res, end=" ")
    divisors = get_all_divisors2(t_res)
    while t_Length > 0:
        if ((random.randint(0, 1)) and (divisors != [])):
            # 1 : div
            t_next = random.choice(divisors)
            print(':', t_next, end=" ")
            t_res = t_res // t_next
            t_Length -= 1
            divisors = get_all_divisors2(t_res)
        else:
            # 2 : mul

            t_next = random.randint(MINN, MAXX)
            if (t_res * t_next) in range(MINN, MAXX):
                print('x', t_next, end=" ")
                t_Length -= 1
                t_res = t_res * t_next
                divisors = get_all_divisors2(t_res)

    print("==", t_res, end="!")
    print()
