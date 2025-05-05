# BFS Function
def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    print("BFS Traversal:")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()

# DFS Function
def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# Function to build the graph from user input
def build_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ")
        neighbours = input(f"Enter neighbors of {node} (space separated): ").split()
        graph[node] = neighbours

    # Add empty list for any mentioned nodes that were not defined
    for neighbours in graph.values():
        for neighbour in neighbours:
            if neighbour not in graph:
                graph[neighbour] = []

    return graph

# Main Menu
while True:
    print("\n--- Menu ---")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        graph = build_graph()
        start = input("Enter starting node: ")
        bfs(graph, start)

    elif choice == '2':
        graph = build_graph()
        start = input("Enter starting node: ")
        print("DFS Traversal:")
        dfs(graph, start)
        print()

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
