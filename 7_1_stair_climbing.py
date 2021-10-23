import sys 
input = sys.stdin.readline

n = int(input())
stair = []
dp = []
for i in range(n):
    stair.append(int(input()))

def stair_chlimbing(stair):
    if n == 1:
        return stair[0]
    elif n == 2:
        return stair[0] + stair[1]
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, n):
        dp.append(max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i]))
    return dp[-1]

print(stair_chlimbing(stair))
