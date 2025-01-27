# The two most common ways a Graph can be traversed are:
# Depth First Search (DFS)
# Breadth First Search (BFS)
# DFS is usually implemented using a Stack or by the use of recursion (which utilizes the call stack),
# while BFS is usually implemented using a Queue.

### DEPTH FIRST SEARCH -- DFS /// BREDTH FIRST SEARCH -- BFS
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
            for j in range(self.size):
                if self.adj_matrix[i][j] > 0:
                    connections.append(self.vertices[j])
            if connections:
                print(f"Vertice {self.vertices[i]} is connected to: {', '.join(connections)}")


                                ### DEPTH FIRST SEARCH -- DFS
    ## My aproach for DFS - recursive
    def dfs_recursive(self, index_vertice, visited: list):
        visited[index_vertice] = True
        print(self.vertices[index_vertice])
        for j in range(self.size):    # go through all possible neigbour
            if self.adj_matrix[index_vertice][j] == 1 and visited[j] == False:
                self.dfs_recursive(j, visited)

    ## My aproach for DFS - iterative
    def dfs_iterative(self):
        visited = [False] * self.size
        stack = []
        stack.append(self.vertices[0])

        while stack:
            current_vertex = stack.pop()
            index = self.vertices.index(current_vertex)

            if not visited[index]:
                visited[index] = True
                print(f"Visited: {current_vertex}")

                for j in range(self.size - 1, -1, -1):  # Obrácené pořadí
                    if self.adj_matrix[index][j] == 1 and not visited[j]:
                        stack.append(self.vertices[j])

    ## W3SCHOOL APROACH
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertices[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]: # go through all possible neigbour
                self.dfs_util(i, visited)

    def dfs(self, start_vertices):
        visited = [False] * self.size
        start_vertex = self.vertices.index(start_vertices)
        self.dfs_util(start_vertex, visited)


                    ###BREDTH FIRST SEARCH -- BFS
    def bfs(self):
        visited = [False] * self.size
        queue = []
        queue.append(self.vertices[0])
        while queue != []:
            vertice = queue.pop(0)
            index = self.vertices.index(vertice)
            if visited[index] == False:
                visited[index] = True
                print(f"Visited: {vertice}")
                for j in range(self.size):
                    if self.adj_matrix[index][j] == 1 and visited[j] == False:
                        queue.append(self.vertices[j])

print("UNDIRECTED UNWEIGHTED GRAPH")
g = Graph(7)

g.add_vertice(0, 'A')
g.add_vertice(1, 'B')
g.add_vertice(2, 'C')
g.add_vertice(3, 'D')
g.add_vertice(4, 'E')
g.add_vertice(5, 'F')
g.add_vertice(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

print("RECURSIVE DFS // MY APROACH\n")
visited = [False] * g.size
g.dfs_recursive(0, visited)  

print("ITERATIVE DFS // MY APROACH\n")
g.dfs_iterative()


print("DFS // W3SCHOOL\n")
g.dfs('A')

print("\n")

print("BFS\n")
g.bfs()



### TO CREATE DIRECTED GRAPH, SIMPLY MAKE THE MATRIX NOT SYMETRIC
# then all works the same!
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
            #self.adj_matrix[j][i] = 1  # undirected graph => symetric matrix

    def print_graph(self):
        print("Adjacency matrix:")
        for i in range(self.size):
            connections = []
            for j in range(self.size):
                if self.adj_matrix[i][j] > 0:
                    connections.append(self.vertices[j])
            if connections:
                print(f"Vertice {self.vertices[i]} is connected to: {', '.join(connections)}")


                                ### DEPTH FIRST SEARCH -- DFS
    ## My aproach for DFS - recursive
    def dfs_recursive(self, index_vertice, visited: list):
        visited[index_vertice] = True
        print(self.vertices[index_vertice])
        for j in range(self.size):    # go through all possible neigbour
            if self.adj_matrix[index_vertice][j] == 1 and visited[j] == False:
                self.dfs_recursive(j, visited)

    ## My aproach for DFS - iterative
    def dfs_iterative(self):
        visited = [False] * self.size
        stack = []
        stack.append(self.vertices[0])

        while stack:
            current_vertex = stack.pop()
            index = self.vertices.index(current_vertex)

            if not visited[index]:
                visited[index] = True
                print(f"Visited: {current_vertex}")


                for j in range(self.size - 1, -1, -1):  # Obrácené pořadí
                    if self.adj_matrix[index][j] == 1 and not visited[j]:
                        stack.append(self.vertices[j])

    ## W3SCHOOL APROACH
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertices[v], end=' ')

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]: # go through all possible neigbour
                self.dfs_util(i, visited)

    def dfs(self, start_vertices):
        visited = [False] * self.size
        start_vertex = self.vertices.index(start_vertices)
        self.dfs_util(start_vertex, visited)


                    ###BREDTH FIRST SEARCH -- BFS
    def bfs(self):
        visited = [False] * self.size
        queue = []
        queue.append(self.vertices[0])
        while queue != []:
            vertice = queue.pop(0)
            index = self.vertices.index(vertice)
            if visited[index] == False:
                visited[index] = True
                print(f"Visited: {vertice}")
                for j in range(self.size):
                    if self.adj_matrix[index][j] == 1 and visited[j] == False:
                        queue.append(self.vertices[j])


g = Graph(7)

g.add_vertice(0, 'A')
g.add_vertice(1, 'B')
g.add_vertice(2, 'C')
g.add_vertice(3, 'D')
g.add_vertice(4, 'E')
g.add_vertice(5, 'F')
g.add_vertice(6, 'G')

g.add_edge(3, 0)  # D -> A
g.add_edge(3, 4)  # D -> E
g.add_edge(4, 0)  # E -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 5)  # C -> F
g.add_edge(2, 6)  # C -> G
g.add_edge(5, 1)  # F -> B
g.add_edge(1, 2)  # B -> C



print("DIRECTED UNWEIGHTED GRAPH")
print("RECURSIVE DFS // MY APROACH\n")
visited = [False] * g.size
g.dfs_recursive(0, visited)  

print("ITERATIVE DFS // MY APROACH\n")
g.dfs_iterative()


print("DFS // W3SCHOOL\n")
g.dfs('A')

print("\n")

print("BFS\n")
g.bfs()               