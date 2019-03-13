from stack import Stack

class Graph:

    def __init__(self, file_name):
        self.graph = {}
        self.num_vertices = 0

        with open(file_name, 'r') as f:
            for line in f.readlines():
                vertices = line.split()
                for vertex in vertices:
                    if vertex not in self.graph:
                        self.num_vertices += 1
                        self.graph[vertex] = []
                self.graph[vertices[0]].append(vertices[1])
                self.graph[vertices[1]].append(vertices[0])
        print(self.graph)

    def conn_components(self):
        
        conn_components = []
        s = Stack()
        visited = {}

        for vertex in [*self.graph]:
            visited[vertex] = False

        for vertex in [*self.graph]:
            if not visited[vertex]:
                visited[vertex] = True
                s.push(vertex)
                # lists and dictionaries are both mutable which means that if we pass them to a function
                # we are actually passing in the reference to their location in memory and as the result,
                # a change to the object will change all instances of the object.
                self.dfs(vertex, visited, s)
            graph = []           
            while not s.is_empty():
                graph.append(s.pop())
            if graph:
                conn_components.append(graph)

        return conn_components

    def dfs(self, vertex, visited, stack):
        print(vertex)
        for vert_conn in self.graph[vertex]:
            if not visited[vert_conn]:
                visited[vert_conn] = True
                stack.push(vert_conn)
                self.dfs(vert_conn, visited, stack)

    


g = Graph('vertices.txt')
print(g.conn_components())