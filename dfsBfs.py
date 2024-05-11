g= {
    0:[1,2]
    1:[0,3,4]
    2:[3,0]
    3:[2,1,4]
    4:[3,1]
}
def dfs(g,s):
    vis[s]=1
    print (s)
    for c in g[s]:
        if not vis[c]:
            dfs(g,c)
#vis=[0]*5
#dfs(g,0)

def bfs(g,s):
    q=[s]
    vis = [s]
    while q:
        cur=q.pop(0)
        print(cur)
        for c in g[cur]:
            if c not in vis:
                vis.append(c)
                q.append(c)
bfs(g,0)