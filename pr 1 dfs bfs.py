# g ={
#     0:[1,4],
#     1 :[0,2,3],
#     2 :[1,3,4],
#     3:[1,2],
#     4:[0,2]
# }

 
# def dfs(g,s):
#     vis1[s] = 1 
#     print(s)
#     for c in g[s]:
#         if not vis1[c]:
#             dfs(g,c)

# vis1 = [0]*5
# dfs(g,0)
# print('--------------BFS----------------')
# def bfs(g,s):
#     q=[s]
#     vis2=[s]
#     while q :
#         cur = q.pop(0)
#         print(cur)
#         for c in g[cur]:
#             if c not in vis2:

#                 q.append(c)
#                 vis2.append(c)
# bfs(g,0)



def dfs(g, s, vis):
    vis[s] = 1
    print(s, end=' ')
    for c in g[s]:
        if not vis[c]:
            dfs(g, c, vis)

def bfs(g, s):
    q = [s]
    vis = [s]
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for c in g[cur]:
            if c not in vis:
                q.append(c)
                vis.append(c)

# ---------- USER INPUT SECTION ----------

g = {}
n = int(input("Enter the number of nodes in the graph: "))

for i in range(n):
    edges = list(map(int, input(f"Enter the adjacent nodes for node {i} (space-separated): ").split()))
    g[i] = edges

start_node = int(input("Enter the starting node for traversal: "))

# ---------- DFS Traversal ----------
print("\nDFS Traversal:")
dfs_vis = [0] * n
dfs(g, start_node, dfs_vis)

# ---------- BFS Traversal ----------
print("\nBFS Traversal:")
bfs(g, start_node)
