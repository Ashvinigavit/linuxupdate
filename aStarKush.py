from copy import deepcopy
class Matrix:
    def __init__(self,matrix,g,h):
        self.matrix=matrix
        self.g=g
        self.h=h
        self.f=self.g+self.h
    def Display(self):
        print(self.g,self.h)

def IsMatrixSame(matrix1,matrix2):
    return matrix1.matrix==matrix2.matrix and matrix1.f==matrix2.f

class Puzzle:
    def __init__(self):
        self.matrix=[['2','8','3'],['1','6','4'],['7','-','5']]
        self.targetMatrix=[['1','2','3'],['8','-','4'],['7','6','5']]
    
    def CalculateMisplacedTiles(self,matrix):
        cnt=0
        for i in range(3):
            for j in range(3):
                if(self.targetMatrix[i][j]=='-'):
                    continue
                if(self.targetMatrix[i][j]!=matrix[i][j]):
                    cnt+=1
        return cnt
    
    def FindMover(self,matrix):
        for i in range(3):
            for j in range(3):
                if(matrix[i][j]=='-'):
                    return (i,j)
        return (-1,-1)
    
    def GetMoveUp(self):
        mover = self.FindMover(self.matrix)
        if(mover[0]<=0):
            return None
        newMatrix = deepcopy(self.matrix)
        newMatrix[mover[0]][mover[1]],newMatrix[mover[0]-1][mover[1]] = newMatrix[mover[0]-1][mover[1]],newMatrix[mover[0]][mover[1]] 
        return newMatrix
    
    def GetMoveDown(self):
        mover = self.FindMover(self.matrix)
        if(mover[0]>=2):
            return None
        newMatrix = deepcopy(self.matrix)
        newMatrix[mover[0]][mover[1]],newMatrix[mover[0]+1][mover[1]] = newMatrix[mover[0]+1][mover[1]],newMatrix[mover[0]][mover[1]] 
        return newMatrix
    
    def GetMoveLeft(self):
        mover = self.FindMover(self.matrix)
        if(mover[1]<=0):
            return None
        newMatrix = deepcopy(self.matrix)
        newMatrix[mover[0]][mover[1]],newMatrix[mover[0]][mover[1]-1] = newMatrix[mover[0]][mover[1]-1],newMatrix[mover[0]][mover[1]] 
        return newMatrix
    
    def GetMoveRight(self):
        mover = self.FindMover(self.matrix)
        if(mover[1]>=2):
            return None
        newMatrix = deepcopy(self.matrix)
        newMatrix[mover[0]][mover[1]],newMatrix[mover[0]][mover[1]+1] = newMatrix[mover[0]][mover[1]+1],newMatrix[mover[0]][mover[1]] 
        return newMatrix
    
    def IsInOpenList(self,element,openList):
        for i in openList:
            if(IsMatrixSame(i,element)):
                return True
        return False
    
    def Display(self,matrix):
        print("---MATRIX START---")
        for i in range(3):
            for j in range(3):
                print(matrix[i][j],end=" ")
            print()    
        print("---MATRIX END---")
    def Solve(self):
        openList = []
        closedList = [self.matrix]
        self.Display(self.matrix)
        print()
        i=1
        while(self.matrix!=self.targetMatrix):
            moves = []
            moves.append(self.GetMoveUp())
            moves.append(self.GetMoveDown())
            moves.append(self.GetMoveLeft())
            moves.append(self.GetMoveRight())
            moves = [move for move in moves if(move!=None)]
            moves = [Matrix(move,i,self.CalculateMisplacedTiles(move)) for move in moves]
            for move in moves:
                if(not(self.IsInOpenList(move,openList)) and (move.matrix not in closedList)):
                    openList.append(move)
            
            openList.sort(key = lambda x:x.f)
            tempMoves = [i.matrix for i in moves]
            self.matrix = openList[0].matrix
            if(self.matrix not in tempMoves):
                print("backtrack")
            else:
                print("No backtrack")
            currentG = openList[0].g
            currentH = openList[0].h
            currentHeuristic = openList[0].f
            openList.pop(0)
            closedList.append(self.matrix)
            print("Optimal Move")
            self.Display(self.matrix)
            print(currentHeuristic,end="\n\n\n")
            i=currentG+1


puzzle = Puzzle()
puzzle.Solve()