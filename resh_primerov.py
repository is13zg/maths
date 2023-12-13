import sys

data = list(map(str.strip, sys.stdin))
for ex in data:
    ex_old= ex
    ex = ex.replace("-", "-")
    ex = ex.replace(":", "/")
    ex = ex.replace("=", "")
    ex = ex.strip()
    res = eval(ex)
    print(ex_old, res)
