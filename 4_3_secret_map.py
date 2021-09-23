#1
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)
    return answer


#2
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        tmp = str(bin(i|j)[2:])
        tmp = tmp.rjust(n, '0')
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)
    return answer
