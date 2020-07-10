n = int(input()) # number of computers
m = int(input()) #number of edges
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    i, j = map(lambda x: int(x), input().split(' '))
    graph[i][j] = 1
    graph[j][i] = 1

def DFS(i):
    if visited[i] == True:
        return
    visited[i] = True
    for j in range(1, n+1):
        if graph[i][j] == 1:
            DFS(j)

DFS(1)
cnt = 0
for i in range(2, n+1):
    if visited[i] == True:
        cnt += 1
print(cnt)
