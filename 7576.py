import sys
import time
M, N = map(int, sys.stdin.readline().split())
array = [[] for _ in range(N+1)]
array[0] = ['-1']*(M+2)
ones = [] #Queue
zeros = 0
for i in range(1, N+1):
    array[i] = ['-1'] + list(sys.stdin.readline().split()) + ['-1']
    for j in range(1, M+1):
        if array[i][j] == '1':
            array[i][j] = 0
            ones.append((i,j))
        elif array[i][j] == '0':
            zeros += 1
array.append(['-1']*(M+2))
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
days = 0
cnt = 0
while len(ones) > cnt:
    i,j = ones[cnt]
    cnt += 1
    for k in range(4):
        ii, jj = i+di[k], j+dj[k]
        if array[ii][jj] == '0':
            ones.append((ii,jj))
            array[ii][jj] = array[i][j] + 1
            days = array[ii][jj]
            zeros -= 1
if zeros != 0:
    print(-1)
else:
    print(days)

###start time 이랑 end time 재서 검토할 수 있다. 근데 백준에서 채점되는 시간보다 오래 걸린다.
###원래는 시간초과가 나왔다. list의 pop()은 O(1)이지만, pop(k)은 O(k)이다. 앞으로 다 한 칸씩 당긴다고 한다..