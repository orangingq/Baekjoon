import sys
T = int(sys.stdin.readline())
for _ in range(T):
    orderLst = [char for char in sys.stdin.readline().rstrip()]
    n = int(sys.stdin.readline()) #length of the array
    lst = sys.stdin.readline().strip('[]\n').split(',')
    arr = []
    for i in range(n):
        arr.append(int(lst[i]))
    head, tail = 0, n-1
    reverse, error = False, False
    for order in orderLst:
        if order == 'R':
            reverse = not reverse
        if order == 'D':
            if head > tail:
                error = True
                break
            if not reverse:
                head += 1
            else:
                tail -= 1
    if error:
        print('error')
        continue
    ret = '['
    if not reverse:
        for i in range(head, tail + 1):
            ret += str(arr[i])
            if i < tail:
                ret += ','
    else:
        for i in range(tail, head-1, -1):
            ret += str(arr[i])
            if i > head:
                ret += ','
    ret += ']'
    print(ret)