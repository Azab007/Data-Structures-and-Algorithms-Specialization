# python3

# python3
import queue
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity +=flow


# def read_data():
#     vertex_count, edge_count = map(int, input().split())
#     graph = FlowGraph(vertex_count)
#     for _ in range(edge_count):
#         u, v, capacity = map(int, input().split())
#         graph.add_edge(u - 1, v - 1, capacity)
#     return graph

def max_flow(graph, from_, to):
    flow = 0
    while True:
        has_path, path, X = bfs(graph, from_, to)
        if not has_path:
            return flow
        for id in path:
            graph.add_flow(id, X)
        flow += X
    return flow

def bfs(graph, from_, to):
    X = float('inf')
    has_path = False
    path = []
    q = queue.Queue()
    n = graph.size()
    visited = [False] * n
    parent = [(None, None)] * n
    visited[from_] = True
    q.put(from_)
    while not q.empty():
        curFromNode = q.get()
        for id in graph.get_ids(curFromNode):
            curEdge = graph.get_edge(id)
            if visited[curEdge.v] == False and curEdge.capacity > 0:
                visited[curEdge.v] = True
                parent[curEdge.v] = (curFromNode, id)
                q.put(curEdge.v)
                if curEdge.v == to:
                    while True:
                        path.insert(0, id)
                        curX = graph.get_edge(id).capacity
                        X = min(X, curX)
                        if curFromNode == from_:
                            break
                        curFromNode, id = parent[curFromNode]
                    has_path = True
                    return has_path, path, X
    return has_path, path, X


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        self.graph = FlowGraph(n + m + 2)

        for i in range(len(adj_matrix)):
            if 1 in adj_matrix[i]:
                flight_node = i + 1
                self.graph.add_edge(0, flight_node, 1)
                for j in range(len(adj_matrix[i])):
                    if adj_matrix[i][j] == 1:
                        crew_node = len(adj_matrix) + 1 + j
                        self.graph.add_edge(flight_node, crew_node, 1)
        for j in range(len(adj_matrix[0])):
            crew_node = len(adj_matrix) + 1 + j
            self.graph.add_edge(crew_node, n + m + 1, 1)
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        max_flow(self.graph, 0, n+m+1)
        for edge in self.graph.edges:
            if edge.flow == 1 and edge.u != 0 and edge.v != n+m+1:
                matching[edge.u-1] = edge.v - n - 1
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
