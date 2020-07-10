import sys

T = int(sys.stdin.readline()) #number of test cases
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def BFS(i, j):
    Queue = [(i, j)]
    while Queue:
        i, j = Queue.pop(0)
        for k in range(4):
            ii, jj = i + di[k], j + dj[k]
            if 0 <= ii < M and 0 <= jj < N and graph[ii][jj] == 1:
                Queue.append((ii, jj))
                graph[ii][jj] = 0

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split()) #MxN size farm, K =num of cabbage
    graph = [[0] * N for _ in range(M)]
    for _ in range(K):
        i,j = map(int, sys.stdin.readline().rstrip().split())
        graph[i][j] = 1

    cnt = 0 #num of cabbage worm
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                graph[i][j] = 0
                BFS(i, j)
                cnt += 1
    print(cnt)

#진짜 모르겠다. graph[i][j]=1인 경우를 lst에 다 저장해서 i랑 j로 이중포문 돌리는 거보다
# lst 하나 포문 돌리는 게 더 효율적일 거라고 생각했는데..
# K가 아주 큰 경우 때문인지, 오히려 이중포문 쓰는 게 더 효율적이다.
# 이제는 sys.stdin.readline()은 국룰이다.