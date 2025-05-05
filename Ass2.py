import heapq

class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def is_valid(self, node):
        row, col = node
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0

    def a_star_search(self):
        open_list = []
        heapq.heappush(open_list, (self.heuristic(self.start), self.start))
        g_values = {self.start: 0}
        came_from = {}

        while open_list:
            _, current = heapq.heappop(open_list)
            if current == self.goal:
                return self.reconstruct_path(came_from)

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])

                if self.is_valid(neighbor):
                    g_cost = g_values[current] + 1
                    if neighbor not in g_values or g_cost < g_values[neighbor]:
                        g_values[neighbor] = g_cost
                        heapq.heappush(open_list, (g_cost + self.heuristic(neighbor), neighbor))
                        came_from[neighbor] = current

        return None

    def reconstruct_path(self, came_from):
        path = []
        current = self.goal
        while current != self.start:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        path.reverse()
        return path


# Function to take user input for grid, start, and goal
def get_user_input():
    # Get grid dimensions
    rows = int(input("Enter the number of rows in the grid: "))
    cols = int(input("Enter the number of columns in the grid: "))
    
    # Create the grid
    grid = []
    print("Enter the grid row by row (0 for open space, 1 for wall):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grid.append(row)
    
    # Get start and goal positions
    start_row, start_col = map(int, input("Enter the start position (row col): ").split())
    goal_row, goal_col = map(int, input("Enter the goal position (row col): ").split())

    return grid, (start_row, start_col), (goal_row, goal_col)


# Main menu
def main():
    while True:
        print("\n--- Menu ---")
        print("1. Run A* Algorithm")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            grid, start, goal = get_user_input()
            astar = AStar(grid, start, goal)
            path = astar.a_star_search()

            if path:
                print("Path found:", path)
            else:
                print("No path found.")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
