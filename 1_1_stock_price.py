# 1
def solution(prices):
    n = len(prices)                                         # length of input
    answer = [0] * n                                        # list initialization                            
    stack = []                                              # create stack
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:      # if the stack is not empty and the price of the top stack element is greater than the current price
            time = stack.pop()                              # pop the element at the top of the stack
            answer[time] = i - time                         # period of time
        stack.append(i)                                     # add element(current time) to the top of the stack  
    while stack:                                            # if the stack is not empty 
        time = stack.pop()                                  # pop the element at the top of the stack
        answer[time] = n - time - 1                         # period of time
    return answer
  
  # 2
  def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1 
            else:  
                answer[i] += 1
                break       
    return answer
