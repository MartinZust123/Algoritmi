import sys

def prim_mst(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    no_edge = 0
    mst_edges = []
    
    while no_edge < n - 1:
        minimum = sys.maxsize
        x = 0
        y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        mst_edges.append((x, y, graph[x][y]))
        selected[y] = True
        no_edge += 1

    return mst_edges

# Primer grafa predstavljen z matriko sosednosti
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst = prim_mst(graph)
print("Minimalno vpeto drevo (MST):")
for edge in mst:
    print(f"Vozlišče {edge[0]} - Vozlišče {edge[1]}: Teža {edge[2]}")
