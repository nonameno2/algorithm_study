# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):    
    n = len(progresses)                                                     # length of input
    completion_date = [0] * n                                               # list initialization  
    answer = []
    stack = []                                                              # create stack

    for i in range(n):
        completion_date[i] = math.ceil((100 - progresses[i]) / speeds[i])   # calculate task completion date      
    
        # if the stack is empty or the value of the top stack is less than the current value
        # push the current index onto the stack
        # add the current index to the return list and initializes its value to 0
        if not stack or completion_date[stack[-1]] < completion_date[i]:    
            stack.append(i)                                                 
            answer.append(i)          
            answer[-1] = 0               

        # if the stack is not empty and the value of the element at the top of the stack is greater than or equal to the current value   
        # add 1 to the last value in the list 
        if stack and completion_date[stack[-1]] >= completion_date[i]: 
            answer[-1] += 1
            
    return answer
