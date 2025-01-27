### BASIC IMPLEMENTATION OF ADJACENCY MATRIX
vertex_data = ['A', 'B', 'C', 'D']  # the graph "points" = vertices

adjacency_matrix = [   # storing edges for each vertice
    [0, 1, 1, 1],     
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
]

def print_adjacency_matrix(matrix):
    for row in matrix:
        print(row)
#print_adjacency_matrix(adjacency_matrix)

def print_edges(matrix, vertices):
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if matrix[i][j] != 0:
                print(f"Vertice {vertices[i]} is connected to vertice {vertices[j]}")
#print_edges(adjacency_matrix, vertex_data)

### GRAPH IMPLEMENTATION USING CLASSES  -- UNDIRECTED + UNWEIGHTED
class Graph:
    def __init__(self,size:int):
        self.size = size
        self.adj_matrix = [[0] * size for i in range(size)]
        self.vertices = [''] * size

    def add_vertice(self,vertex, data):
        if vertex >=0 and vertex < self.size:
            self.vertices[vertex] = data

    def add_edge(self, i, j):
        if 0 <= i < self.size and 0 <= j < self.size:
            self.adj_matrix[i][j] = 1
            self.adj_matrix[j][i] = 1  # undirected graph => symetric matrix

    def print_graph(self):
        print("Adjacency matrix:")
        for i in range(self.size):
            connections = []
            for j in range(i + 1, self.size):  # Only look at the upper triangle
                if self.adj_matrix[i][j] > 0:
                    connections.append(self.vertices[j])
            if connections:
                print(f"Vertice {self.vertices[i]} is connected to: {', '.join(connections)}")

graph = Graph(4)
vertex_data = ['A', 'B', 'C', 'D']
for index, data in enumerate(vertex_data):
    graph.add_vertice(index, data)
graph.add_edge(0, 1)  # A - B
graph.add_edge(0, 2)  # A - C
graph.add_edge(0, 3)  # A - D
graph.add_edge(1, 2)  # B - C

graph.print_graph()


### GRAPH IMPLEMENTATION USING CLASSES  -- DIRECTED + WEIGHTED
class Graph:
    def __init__(self,size:int):
        self.size = size
        self.adj_matrix = [[0] * size for i in range(size)]
        self.vertices = [''] * size

    def add_vertice(self,vertex, data):
        if vertex >=0 and vertex < self.size:
            self.vertices[vertex] = data

    def add_edge(self, i, j, w):
        if 0 <= i < self.size and 0 <= j < self.size:
            self.adj_matrix[i][j] = w

    def print_graph(self):
        print("Adjacency matrix:")
        for i in range(self.size):
            connections = []
            for j in range(i + 1, self.size):  # Only look at the upper triangle
                if self.adj_matrix[i][j] > 0:
                    connections.append(self.vertices[j])
            if connections:
                print(f"Vertice {self.vertices[i]} is connected to: {', '.join(connections)}")


graph = Graph(4)
vertex_data = ['A', 'B', 'C', 'D']
for index, data in enumerate(vertex_data):
    graph.add_vertice(index, data)
graph.add_edge(0, 1,3)  # A - B
graph.add_edge(0, 2,2)  # A - C
graph.add_edge(0, 3,4)  # A - D
graph.add_edge(1, 2,1)  # B - C

graph.print_graph()
