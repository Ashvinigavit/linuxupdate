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






Kruskals:
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class UnionFind {
    vector<int>parent;
    vector<int>rank;
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0;i < n;i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionsets(int x, int y) {
        int parX = find(x);
        int parY = find(y);
        if (parX != parY) {
            if (rank[parX] < rank[parY]) {
                parent[parX] = parY;
            }
            else if (rank[parX] > rank[parY]) {
                parent[parY] = parX;
            }
            else {
                parent[parY] = parX;
                rank[parX]++;
            }
        }
    }
};

class Edge {
    int start;int end;int weight;
public:
    Edge() { start = -1;end = -1;weight = -1; }
    Edge(int a, int b, int c) { start = a;end = b;weight = c; }
    int GetStart() { return start; }
    int GetEnd() { return end; }
    int GetWeight() { return weight; }
    void Display(vector<string>namemapper) { cout << namemapper[start] << "-" << namemapper[end] << ":" << weight << endl; }
};

bool IsEdgeSame(Edge a, Edge b) {
    if (a.GetWeight() == b.GetWeight()) {
        if ((a.GetEnd() == b.GetStart() && a.GetStart() == b.GetEnd()) || (a.GetStart() == b.GetStart() && a.GetEnd() == b.GetEnd())) {
            return true;
        }
        return false;
    }
    return false;
}

class Graph {
    int v, e;
    vector<string> namemapper;
    vector<vector<int>>adjMat;
public:
    Graph() {
        cout << "Enter the number of hosts: ";
        cin >> v;
        adjMat.resize(v, vector<int>(v, -1));
        for (int i = 0;i < v;i++) { adjMat[i][i] = 0; }
        namemapper.resize(v);
        string name;
        for (int i = 0;i < v;i++) {
            cout << "Enter hostname " << (i + 1) << ": ";
            cin >> name;
            namemapper[i] = name;
        }
        char ans;
        int weight;string name1, name2;
        do {
            cout << "Do you want to add a connection (y/n): ";
            cin >> ans;
            if (ans != 'y') { break; }
            cout << "Enter hostname 1: ";cin >> name1;cout << endl;
            cout << "Enter hostname 2: ";cin >> name2;cout << endl;
            cout << "Enter path cost: ";cin >> weight;
            int ind1 = IsValidName(name1);
            int ind2 = IsValidName(name2);
            adjMat[ind1][ind2] = weight;
            adjMat[ind2][ind1] = weight;
        } while (ans == 'y');
        DisplayAdjacencyMatrix();
    }

    int IsValidName(string name) {
        for (int i = 0;i < namemapper.size();i++) {
            if (namemapper[i] == name) { return i; }
        }
        return -1;
    }

    void Prims() {
        cout << "Enter the starting vertex: ";
        string start;
        cin >> start;
        int currentIndex = IsValidName(start);
        vector<Edge>edges;Edge edge;UnionFind uf(v);
        vector<Edge>mst;int mstCost = 0;vector<int>verticesCovered;
        verticesCovered.push_back(currentIndex);
        for (int i = 0;i < v - 1;i++) {
            for (int col = 0;col < v;col++) {
                if (adjMat[currentIndex][col] > 0) {
                    edge = Edge(currentIndex, col, adjMat[currentIndex][col]);
                    if (!IsInEdges(edges, edge)) {
                        edges.push_back(edge);
                    }
                }
            }
            sort(edges.begin(), edges.end(), [](Edge a, Edge b) {return a.GetWeight() > b.GetWeight();});
            while (uf.find(edges[edges.size() - 1].GetStart()) == uf.find(edges[edges.size() - 1].GetEnd())) {
                edges.pop_back();
            }
            if (uf.find(edges[edges.size() - 1].GetStart()) != uf.find(edges[edges.size() - 1].GetEnd())) {
                int tempInd = edges.size() - 1;
                uf.unionsets(edges[tempInd].GetStart(), edges[tempInd].GetEnd());
                mst.push_back(Edge(edges[tempInd].GetStart(), edges[tempInd].GetEnd(), edges[tempInd].GetWeight()));
                mstCost += edges[tempInd].GetWeight();
                if (!IsInCoveredVertices(edges[tempInd].GetStart(), verticesCovered)) {
                    currentIndex = edges[tempInd].GetStart();
                    verticesCovered.push_back(currentIndex);
                }
                else {
                    currentIndex = edges[tempInd].GetEnd();
                    verticesCovered.push_back(currentIndex);
                }
                edges.pop_back();
            }
            cout << i << endl;
            for (auto e : edges) {
                e.Display(namemapper);
            }
            cout << endl;
        }

        cout << "MST: " << endl;
        for (auto e : mst) {
            e.Display(namemapper);
        }
        cout << "MST Cost: " << mstCost << endl << endl;
    }
    bool IsInCoveredVertices(int vertex, vector<int>vertices) {
        return find(vertices.begin(), vertices.end(), vertex) != vertices.end();
    }
    void Kruskals() {
        int edgeCount = 0;
        vector<Edge>edges;
        for (int i = 0;i < v;i++) {
            for (int j = i + 1;j < v;j++) {
                if (adjMat[i][j] > 0) {
                    edgeCount += 1;
                    edges.push_back(Edge(i, j, adjMat[i][j]));
                }
            }
        }
        for (int i = 0;i < edges.size();i++) {
            edges[i].Display(namemapper);
        }
        sort(edges.begin(), edges.end(), [](Edge a, Edge b) {return a.GetWeight() < b.GetWeight();});
        cout << "Sorted\n";
        for (int i = 0;i < edges.size();i++) {
            edges[i].Display(namemapper);
        }
        cout << endl << endl;
        UnionFind uf(v);
        vector<Edge>mst;
        int mstCost = 0;
        for (auto e : edges) {
            if (uf.find(e.GetStart()) != uf.find(e.GetEnd())) {
                mst.push_back(Edge(e));
                mstCost += e.GetWeight();
                uf.unionsets(e.GetStart(), e.GetEnd());
                if (mst.size() >= v - 1) {
                    break;
                }
            }
        }
        for (auto e : mst) {
            e.Display(namemapper);
        }
        cout << "Kruskals MST Cost: " << mstCost << endl << endl;
    }


    bool IsInEdges(vector<Edge> edges, Edge edge) {
        for (auto e : edges) {
            if (IsEdgeSame(e, edge)) {
                return true;
            }
        }
        return false;
    }


    void DisplayAdjacencyMatrix() {
        cout << "  ";
        for (int i = 0;i < namemapper.size();i++) {
            cout << namemapper[i] << " ";
        }
        cout << endl;
        for (int i = 0;i < v;i++) {
            cout << namemapper[i] << " ";
            for (int j = 0;j < v;j++) {
                if (adjMat[i][j] == -1) { cout << "X ";continue; }
                cout << adjMat[i][j] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    Graph g;
    g.Prims();
}