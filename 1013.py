import sys
T = int(sys.stdin.readline())
for _ in range(T):
    str = sys.stdin.readline().rstrip()
    i=0
    YES = True
    while i < len(str):
        if i < len(str)-2 and str[i:i+3]=='100':
            j = i+1
            while j < len(str) and str[j]=='0':
                j += 1
            r = j
            while r < len(str)-1 and str[r:r+2]=='11':
                r += 1
            if r == len(str)-1:
                i = r + 1
                continue
            elif r < len(str)-2 and str[r-1:r+3]=='1100': #1.../100...
                i = r
            elif r < len(str)-2 and str[r:r+3]=='101':               #1.../01...
                i = r + 1
            else:
                YES = False
                break
        elif i < len(str)-1 and str[i:i+2] == '01':
            i = i + 2
        else:
            YES = False
            break
    if YES:
        print('YES')
    else:
        print('NO')