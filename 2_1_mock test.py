# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answer1[i % len(answer1)] == answers[i]:
            score[0] += 1
        if answer2[i % len(answer2)] == answers[i]:
            score[1] += 1
        if answer3[i % len(answer3)] == answers[i]:
            score[2] += 1
    
    for i, j in enumerate(score):
        if j == max(score):
            answer.append(i + 1)

    return answer
