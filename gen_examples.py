import random
import time
MINN = 1
MAXX = 30
RESmin = 0
RESmax = 100
Length = 2
random.seed(random.randint(0, 100000))
for i in range(15):
    t_Length = Length
    t_res = random.randint(MINN, MAXX)
    print(t_res, end=" ")
    while t_Length > 0:
        t_next = random.randint(MAXX * (-1), MAXX)
        if (t_res + t_next) in range(MINN, MAXX):
            if t_next>=0:
                print('+',t_next, end=" ")
            else:
                print(t_next, end=" ")
            t_res = t_res + t_next
            t_Length -= 1

    print("==", t_res, end="!")
    print()
