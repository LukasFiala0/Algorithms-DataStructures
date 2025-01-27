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
            self.adj_matrix[j][i] = w

    def print_graph(self):
        print("Adjacency matrix:")
        for i in range(self.size):
            connections = []
            for j in range(self.size):
                if self.adj_matrix[i][j] > 0:
                    connections.append(self.vertices[j])
            if connections:
                print(f"Vertice {self.vertices[i]} is connected to: {', '.join(connections)}")


g = Graph(7)

g.add_vertice(0, 'A')
g.add_vertice(1, 'B')
g.add_vertice(2, 'C')
g.add_vertice(3, 'D')
g.add_vertice(4, 'E')
g.add_vertice(5, 'F')
g.add_vertice(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

g.print_graph()