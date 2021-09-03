import sys
from collections import Counter

n = int(input())
card = list(map(int, sys.stdin.readline().split()))      
m = int(input())
integer = list(map(int, sys.stdin.readline().split()))   

count = Counter(card)
for i in integer:
    print(count[i], end = " ")
