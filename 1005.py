import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = [0]+list(map(int, sys.stdin.readline().split()))
    next = [[0] for _ in range(N+1)]
    history = time[:]
    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        next[X].append(Y) #an edge from X to Y
        next[Y][0] += 1 #next[i][0] means the number of indegree of i.
    Queue = []
    for i in range(1, N+1):
        if next[i][0] == 0:
            Queue.append(i)
    W = int(sys.stdin.readline())
    while Queue:   #topological sort
        e = Queue.pop(0)
        for i in next[e][1:]:
            history[i] = max(history[i], history[e] + time[i])
            next[i][0] -= 1 #eliminate the edge from e to i.
            if next[i][0] == 0: #if the number of indegree of i becomes 0, add to the Queue.
                Queue.append(i)
        if e == W:
            print(history[W])
            break
