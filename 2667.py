N = int(input()) # size of map
graph = [[0]*(N+2) for _ in range(N+2)]
for i in range(1,N+1):
    graph[i] = [0]+[int(char) for char in input()]+[0]

def DFS(i,j, cnt):
    if i<1 or j<1 or i>N or j>N:
        return
    if graph[i][j] == 0:
        return
    graph[i][j] = 0
    subdivisions[cnt] += 1
    DFS(i-1, j, cnt)
    DFS(i, j-1, cnt)
    DFS(i+1, j, cnt)
    DFS(i, j+1, cnt)

i,j = 1,1
subdivisions = [] #list of subdivisions
cnt = 0 #number of subdivisions
while i<=N and j<=N:
    if graph[i][j] != 0:
        subdivisions.append(0)
        DFS(i,j,cnt)
        cnt += 1
    if j==N:
        i, j = i+1, 0
    else:
        i, j = i, j+1
subdivisions.sort()

print(cnt)
for i in subdivisions:
    print(i)