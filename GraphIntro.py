#Graph initalization 

class Graph:
    def __init__(self,edges) -> None:
        self.edges=edges
        self.graph_dict={}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        #print("Graph Dict",self.graph_dict)
    def getPath(self,start,end,path=[]):
        path = path + [start]
        if start not in self.graph_dict:
            return []
        if start==end:
            return [path]
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.getPath(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    def getShortestPath(self,start,end,path=[]):
        path=path+[start]
        if start not in self.graph_dict:
            return None
        
        if start==end:
            return path  
        paths=[]  
        shortestPath=None
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.getShortestPath(node,end,path) 
                if new_path:
                    if shortestPath is None or len(new_path)<len(shortestPath):
                        shortestPath=new_path
        return shortestPath

routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
routeGraph=Graph(routes)
start= "Mumbai"
end= "New York"


print (f"paths between {start} and {end} value:",routeGraph.getPath(start,end))
print (f"\nShortest path between {start} and {end} value:",routeGraph.getShortestPath(start,end))