from itertools import permutations

def solution(n):
    s = set()
    for i in range(len(n)):
        s |= set(map(int, map("".join, permutations(list(n), i + 1))))    # set of numbers that can be made      
    s -= set(range(0, 2))                                               # remove 0 and 1

    # sieve of Eratosthenes
    for i in range(2, int(max(s) ** 0.5 + 1)):
        s -= set(range(i * 2, max(s) + 1, i))                               # remove non prime numbers from s

    return len(s)
