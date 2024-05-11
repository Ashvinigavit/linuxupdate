N = 4
b = [[0]*N for k in range(N)]

def isSafe(i,j):
    for p in range(N):
        if b[i][p] == 1 or b[p][j] ==1 :
            return False
    # Check upper diagonal
    for n in range(N):
        for m in range(N):
            if (n + m)==( i + j) or (n - m)==( i - j):
                if b[n][m]== 1:
                    return False
    return True

def nqueen(noq):
    if noq == 0:
        return False
    for i in range(N):
        for j in range(N):
            if b[i][j] != 1 and isSafe(i,j):
                b[i][j]=1
                if nqueen(noq-1) == True:
                    return True
                b[i][j]=0
            return False

def printBoard(b):
    for i in b;
        print(i)

if nqueen(N):
    printBorad(b)

else:
    print("cant place")