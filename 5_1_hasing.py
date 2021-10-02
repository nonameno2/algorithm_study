n = int(input())
st = list(input())

def hashing():
    sum = 0
    for i in range(n):
        sum += (ord(st[i]) - 96) * (31** i)
    return sum % 1234567891

print(hashing())
