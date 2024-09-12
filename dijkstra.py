import heapq

def dijkstra(graph, start):
    # Initialize the priority queue, distances dictionary, and visited set
    priority_queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph} 
    distances[start] = 0
    visited = set()

    while priority_queue:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Update distances to neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
# start_vertex = 'A'
# print(dijkstra(graph, start_vertex))

def dijkstra1(graph, start):
    priority_queue = [(0,start)]
    distances = {vertex:float("infinity") for vertex in graph}
    visited = set()
    distances[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue 
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight 
            if distances[neighbor] > distance: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
print(dijkstra1(graph, start_vertex))