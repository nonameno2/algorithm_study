from collections import deque

n, m, v = map(int, input().split())

# (n + 1) x (n + 1) matrix, vertices are initialized to 0
graph = [[0] * (n + 1) for _ in range (n + 1)]              

# vertices connected by edges are weighted by 1
for _ in range(m):                                          
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

# depth-first search
visited = []    
def dfs(graph, start):                                             
    visited.append(start)
    print(start, end = ' ')
    # adjacent edges
    for i in range(n + 1):                                  
        if (graph[start][i] == 1) and (i not in visited):   
            dfs(graph, i)

# breadth-first search
def bfs(graph, start):    
    visited = []                                           
    q = deque()      # deque(append, popleft) : O(1) time complexity   
    visited.append(start)                                  
    q.append(start)
    while q:
        v = q.popleft()
        print(v, end = ' ')    
        # adjacent edges
        for i in range(n + 1):                              
            if (graph[v][i] == 1) and (i not in visited):   
                visited.append(i)
                q.append(i)

dfs(graph, v)
print()
bfs(graph, v)


