from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def astar(self, src, dest):
        open_set = {src}
        closed_set = set()

        g_score = {v: float('inf') for v in self.graph}
        g_score[src] = 0

        f_score = {v: float('inf') for v in self.graph}
        f_score[src] = self.heuristic(src, dest)

        while open_set:
            current = min(open_set, key=lambda v: f_score[v])

            if current == dest:
                # Reconstruct path
                path = [current]
                while current != src:
                    current = min(self.graph[current], key=lambda v: g_score.get(v, float('inf')))
                    path.append(current)
                return path[::-1]

            open_set.remove(current)
            closed_set.add(current)

            for neighbor in self.graph[current]:
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + self.graph[current][neighbor]
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, dest)
                    open_set.add(neighbor)

        return None

    def heuristic(self, u, v):
        # Simple heuristic (Euclidean distance for demonstration purposes)
        return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

# Creating the graph
g = Graph()
print("Enter edges for the graph with weights (format: 'source destination weight'). Enter '#' to stop:")

while True:
    edge = input()
    if edge == '#':
        break
    u, v, weight = map(int, edge.split())
    g.add_edge(u, v, weight)

source_vertex = tuple(map(int, input("Enter the source vertex coordinates (format: 'x y'): ").split()))
dest_vertex = tuple(map(int, input("Enter the destination vertex coordinates (format: 'x y'): ").split()))

shortest_path = g.astar(source_vertex, dest_vertex)

if shortest_path:
    print("\nShortest path from {} to {}:".format(source_vertex, dest_vertex))
    print(shortest_path)
else:
    print("\nNo path found from {} to {}.".format(source_vertex, dest_vertex))
