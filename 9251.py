lineOne = input()
lineTwo = input()
lenOne, lenTwo = len(lineOne), len(lineTwo)
lcs = {} #[lcs의 길이, lineTwo에서 lcs의 마지막 원소에 해당하는 index]
for i in range(lenOne):
    for j in range(lenTwo):
        if lineOne[i] == lineTwo[j]:
            if i == 0:
                lcs[0].append([1,j])
                break
            tmp = [1,j]
            lcs.append(tmp)
            for tup in lcs[::-1]:
                if tup[1] < j:
                    lcs.append([tup[0]+1, j])
