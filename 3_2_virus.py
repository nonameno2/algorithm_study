n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range (n + 1)]              

for _ in range(m):                                          
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

# dfs
visited = []    
def dfs(start):                                             
    visited.append(start)
    for i in range(n + 1):                                  
        if (graph[start][i] == 1) and (i not in visited):   
            dfs(i)

dfs(1)
print(len(visited) - 1)