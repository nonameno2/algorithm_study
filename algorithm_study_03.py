# 깊이우선탐색과 너비우선탐색



# PART 01
# 깊이우선탐색(DFS)
# Depth First Search의 약자
# 하나의 경우의 수에 대하여 모든 경우의 수를 조사하고 다음 경우의 수를 조사하면서 해를 찾는 과정

# 깊이우선탐색(DFS)의 구조
# 깊이우선탐색(DFS)과 스택
# 깊이우선탐색(DFS) 구현 - 미로찾기
# 깊이우선탐색(DFS) 예시코드 - 미로찾기

while len(stack) > 0:               # 스택에 데이터가 있다면
    now = stack.pop()               # 스택의 가장 마지막 데이터 추출
    if now == dest:                 # 정답 여부 검사
        return True
    x = now[1]
    y = now[0]
    if x - 1 > -1:                  # 왼쪽으로 이동할 수 있다면
        if maps[y][x-1] == 0:
            stack.append[y, x-1]    # 갈 수 있는 길이라면 스택에 추가하고 방문여부를 2로 표시
            maps[y][x-1] = 2
    if x + 1 < hori:                # 오른쪽으로 이동할 수 있다면
        if maps[y][x+1] == 1:
            stack.append[y, x+1]
            maps[y][x+1] = 2
    if y - 1 > -1:                  # 위로 이동할 수 있다면
        if maps[y-1][x] == 1:
            stack.append[y-1, x]
            maps[y-1][x] = 2
    if x + 1 < verti:               # 오른쪽으로 이동할 수 있다면 
        if maps[y+1][x] == 1:
            stack.append[y+1, x]
            maps[y+1][x] = 2
return False                        # 스택에 데이터가 없으면 False



# PART 02
# 너비우선탐색(BFS)
# Breadth First Search의 약자
# 하나의 경우의 수에 대한 다음 단계의 모든 경우의 수를 조사하면서 해를 찾는 과정

# 너비우선탐색(BFS)의 구조
# 너비우선탐색(BFS)과 큐
# 너비우선탐색(BFS) 구현 - 최단경로찾기
# 너비우선탐색(BFS) 예시코드 - 최단경로찾기

while len(queue) > 0:                                           # 큐에 데이터가 있다면
    count = len(queue)                                          # 같은 거리에 있는 큐 데이터 개수
    for time in range(count):                                   # 같은 거리에 있는 큐 개수 만큼 검사
        now = queue.pop(0)
        if now == dest:                                         # 정답이 존재하면 값 반환
            return answer
        for i in data:                                           # 연결된 포인트 완전 탐색
            if i[0] == now and visited[i[1]-1] == False:        # 방문하지 않은 연결된 길이라면 큐에 추가하고 방문 표시
                queue.append(i[1])
                visited[i[1]-1] == True
            elif i[1] == now and visited[i[0]-1] == False:
                queue.append(i[0])
                visited[i[0]-1] == True
    answer+=1                                                   # 거리를 1 더 벌린다
return anser
