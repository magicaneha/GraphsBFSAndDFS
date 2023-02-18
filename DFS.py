visited=set()
graph= {
    '0':['1','2','3'],
    '1':['2','3'],
    '2':['3'],
    '3':['4'],
    '4':[]
    
}
def dfs(visited,graph,root):
    if root  not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'0')