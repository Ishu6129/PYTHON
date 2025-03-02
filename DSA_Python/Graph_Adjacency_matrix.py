class GRAPH:
    def __init__(self,vertex_count):
        self.vertex_count=vertex_count
        self.adj_matrix=[ [0]*vertex_count for e in range (vertex_count) ]

    def chk(self):
        return 0<=u<self.vertex_count and 0<=v<self.vertex_count

    def add_edge(self,u,v,weight=1):
        if self.chk:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
    def remove_graph(self,u,v):
        if self.chk:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")
    def has_edge(self,u,v):
        if self.chk:
            return self.adj_matrix[u][v]>0
        else:
            print("Invalid Vertex")
    def print_adj_matrix(self):
        for i in self.adj_matrix:
            print(*i)
            # print(" ".join(map(str,i)))

            
gph=GRAPH(5)
gph.add_edge(0,1)
gph.add_edge(1,2)
gph.add_edge(1,3)
gph.add_edge(2,3)
gph.add_edge(3,4)
gph.print_adj_matrix()