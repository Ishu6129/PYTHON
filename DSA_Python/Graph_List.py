class GRAPH:
    def __init__(self,vertex_count):
        self.vertex_count=vertex_count
        self.adj_matrix={v:[] for v in range(vertex_count)}

    def chk(self):
        return 0<=u<self.vertex_count and 0<=v<self.vertex_count

    def add_edge(self,u,v,weight=1):
        if self.chk:
            if (v,weight) not in self.adj_matrix[u]:
                self.adj_matrix[u].append((v,weight))
                self.adj_matrix[v].append((u,weight))
        else:
            print("Invalid Vertex")
    def remove_edge(self,u,v):
        if self.chk:
            self.adj_matrix[u]=[(vertex,weight) for vertex,weight in self.adj_matrix[u] if vertex!=v]
            self.adj_matrix[v]=[(vertex,weight) for vertex,weight in self.adj_matrix[u] if vertex!=u]
        else:
            print("Invalid Vertex")
    def has_edge(self,u,v):
        if self.chk:
            return any(vertex==v for vertex,x in self.adj_matrix[u])
        else:
            print("Invalid Vertex")
    def print_adj_matrix(self):
        for x,y in self.adj_matrix.items():
            print(x,y)
gph=GRAPH(5)
gph.add_edge(0,1)
gph.add_edge(0,1)
gph.add_edge(1,2)
gph.add_edge(1,3)
gph.add_edge(2,3)
gph.print_adj_matrix()
print(gph.remove_edge(1,3))
print(gph.has_edge(1,3))
print(gph.has_edge(4,3))