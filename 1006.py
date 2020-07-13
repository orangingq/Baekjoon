import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    enemy = list(map(int, sys.stdin.readline().split() + sys.stdin.readline().split()))
    dicEnemy = {} #a number of enemies as a key, list of corresponding section numbers as a value
    visited = [False]*(2*N)
    for i in range(2 * N):
        if enemy[i] in dicEnemy:
            dicEnemy[enemy[i]].append(i)
        else:
            dicEnemy[enemy[i]] = [i]
    cnt = 0 # number of special platoons
    for value in sorted(dicEnemy, reverse = True): #for loop for each enemy number in decreasing order.
        candidate = {} #list of pairs
        for i in dicEnemy[value]: #for each section number i
            if visited[i]:
                continue
            cnt += 1
            lstii = [(i + N) % (2 * N), i // N * N + (i + 1) % N, i // N * N + (i - 1) % N]
            for ii in lstii:
                if not visited[ii] and enemy[ii] + value <= W:
                    candidate[enemy[ii]] = (i, ii)
        print(value, candidate)
        for maxVal in sorted(candidate, reverse=True): #decide the final pairs from the cadidates
            i, ii = candidate[maxVal]
            if not visited[i] and not visited[ii]:
                visited[i], visited[ii] = True, True
        for i in dicEnemy[value]:
            visited[i] = True
    print(cnt)