# 완전탐색과 이분탐색

# 1. 탐색
# 완전탐색, 이분탐색, 깊이우선탐색, 너비우선탐색, 문자열탐색, KMP, BM

# 2. 완전탐색
# 브루트 포스(Brute Force)라고도 불리며 컴퓨터의 빠른 계산 성능을 활용하여
# 가능한 모든 경우의 수를 탐색하는 효율성 관점에서 최악의 방법

# 완전탐색 구현방법
# 반복문, 재귀함수(동적 계획법, 백트래킹, 탐욕법)

# 완전탐색 - 반복문
def solution(trump):
    for i in range(len(trump)):
        if trump[i] == 8:
            return i
        return -1

# 완전탐색 - 재귀함수
def solution(trump, loc):
    if trump[loc] == 8:
        return loc
    else:
        return solution(trump, loc+1)

# 3. 이분탐색

# UPDOWN 게임
# 1 ~ 1000
# 기회는 8번

# 500s

# 501 ~ 1000
# 기회는 7번

# 750

# 이분탐색이란? 이진검색이라고도 표현하며 오름차순으로 정렬된 리스트에서 특정 값의 위치를 찾는 알고리즘
# 중간의 값을 선택하여 찾고자 하는 값과의 크고 작음을 비교하는 방법

# 이분탐색구조

# 이분탐색 예시코드
def solution(trump):
    left = 0
    right = len(trump) - 1
    while(left <= right):
        mid = (left + right) // 2
        if trump[mid] == 8:
            return mid
        elif trump[mid] < 8:
            left = mid + 1
        elif trump[mid] > 8:
            right = mid - 1
    return mid




