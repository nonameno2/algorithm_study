import sys
fac = [1, 2, 6, 24, 120]

while(True):
    n = sys.stdin.readline().strip()[::-1]
    if n == '0':
        break
    else:
        print(sum([fac[i] * int(n[i]) for i in range(len(n))]))
