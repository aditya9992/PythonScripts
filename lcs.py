def LCS(valString1, valString2):
    m = [str(s) for s in valString1.split()]
    n = [str(s) for s in valString2.split()]

    C = [[0 for x in range(len(valString2)+1)] for y in range(len(valString1)+1)]

    for i,x in enumerate(valString1):
        for j,y in enumerate(valString2):
            if x == y:
                C[i+1][j+1] = C[i][j] + 1
            else:
                C[i+1][j+1] = max(C[i+1][j],C[i][j+1])

    print(C)

    maxstr1 = ""

    x, y = len(valString1),len(valString2)

    while x!= 0 and y!=0:
        if C[x][y] == C[x-1][y]:
            x -= 1
        elif C[x][y] == C[x][y-1]:
            y -= 1
        else:
            #assert valString1[x-1] == valString2[y-1]
            maxstr1 = valString1[x-1] + maxstr1
            x -= 1
            y -= 1

    print(maxstr1)