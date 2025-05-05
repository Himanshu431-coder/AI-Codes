import heapq


# 1. SELECTION SORT

def selection_sort():
    arr = list(map(int, input("Enter numbers to sort (space-separated): ").split()))
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Sorted Array:", arr)



# 2. PRIM'S ALGORITHM

def prims_algorithm():
    n = int(input("Number of nodes: "))
    e = int(input("Number of edges: "))
    graph = {i: [] for i in range(n)}

    print("Enter edges (format: u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    start = int(input("Start node: "))
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            total_cost += cost
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    print("Total cost of Minimum Spanning Tree:", total_cost)



# 3. KRUSKAL'S ALGORITHM

def kruskal_algorithm():
    n = int(input("Number of nodes: "))
    e = int(input("Number of edges: "))
    edges = []

    print("Enter edges (format: u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            return True
        return False

    edges.sort(key=lambda x: x[2])
    mst_cost = 0
    for u, v, w in edges:
        if union(u, v):
            mst_cost += w

    print("Total cost of Minimum Spanning Tree:", mst_cost)



# 4. DIJKSTRA'S ALGORITHM

def dijkstra_algorithm():
    n = int(input("Number of nodes: "))
    nodes = input("Enter node names (space-separated): ").split()
    graph = {node: [] for node in nodes}

    e = int(input("Number of edges: "))
    print("Enter edges (format: src dest weight):")
    for _ in range(e):
        u, v, w = input().split()
        graph[u].append((v, int(w)))

    start = input("Start node: ")
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]
    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    print("Shortest distances from", start + ":")
    for node in distances:
        print(f"  {node}: {distances[node]}")



# 5. JOB SCHEDULING

class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling():
    n = int(input("Number of jobs: "))
    jobs = []

    print("Enter jobs (format: id deadline profit):")
    for _ in range(n):
        job_id, deadline, profit = input().split()
        jobs.append(Job(job_id, int(deadline), int(profit)))

    jobs.sort(key=lambda job: job.profit, reverse=True)
    max_deadline = max(job.deadline for job in jobs)
    slots = [None] * max_deadline

    total_profit = 0
    scheduled_jobs = []

    for job in jobs:
        for i in range(job.deadline - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job.id
                scheduled_jobs.append(job.id)
                total_profit += job.profit
                break

    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)



# MAIN MENU

def main_menu():
    while True:
        print("\n====== Greedy Algorithms Menu ======")
        print("1. Selection Sort")
        print("2. Prim's Algorithm (MST)")
        print("3. Kruskal's Algorithm (MST)")
        print("4. Dijkstra's Algorithm (Shortest Path)")
        print("5. Job Scheduling (Max Profit)")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            selection_sort()
        elif choice == '2':
            prims_algorithm()
        elif choice == '3':
            kruskal_algorithm()
        elif choice == '4':
            dijkstra_algorithm()
        elif choice == '5':
            job_scheduling()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# RUN PROGRAM

if __name__ == "__main__":
    main_menu()
