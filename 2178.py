import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
di = [1,0,-1,0]
dj = [0,1,0,-1]
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
Queue = [[0,0]]
graph[0][0] = 1
while Queue: #BFS
    i, j = Queue.pop(0)
    for k in range(4):
        ii, jj = i+di[k], j+dj[k]
        if 0 <= ii < N and 0 <= jj < M and graph[ii][jj] == '1':
            Queue.append([ii, jj])
            graph[ii][jj] = graph[i][j] + 1
print(graph[N-1][M-1])

#python이라 그런지 뭔지 모르겠지만 진짜 최대애ㅐ애애애애한 런타임을 줄여야하는 거 같다.
# https://pacific-ocean.tistory.com/265 : path나 visited 리스트를 따로 만들어도 되겠지만, 데이터 타입을 이용해서 graph 하나로 끝냈다.
#https://hongku.tistory.com/276 : input() 대신 sys.stdin.readline()을 사용한다.
