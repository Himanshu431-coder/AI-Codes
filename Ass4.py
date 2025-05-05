def print_solution(solution):
    for row in solution:
        print(row)
    print()


#  BACKTRACKING 
def is_safe_bt(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_bt(board, row, n, solutions):
    if row == n:
        solutions.append(["".join("Q" if cell else "." for cell in r) for r in board])
        return
    for col in range(n):
        if is_safe_bt(board, row, col, n):
            board[row][col] = 1
            solve_bt(board, row+1, n, solutions)
            board[row][col] = 0

def n_queens_backtracking(n):
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_bt(board, 0, n, solutions)
    return solutions


#  BRANCH AND BOUND 
def solve_bnb(row, n, col_used, diag1, diag2, board, solutions):
    if row == n:
        solutions.append(["".join("Q" if i == col else "." for i in range(n)) for col in board])
        return
    for col in range(n):
        if not col_used[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
            board[row] = col
            col_used[col] = diag1[row - col + n - 1] = diag2[row + col] = True
            solve_bnb(row + 1, n, col_used, diag1, diag2, board, solutions)
            col_used[col] = diag1[row - col + n - 1] = diag2[row + col] = False

def n_queens_branch_and_bound(n):
    board = [-1] * n
    solutions = []
    col_used = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)
    solve_bnb(0, n, col_used, diag1, diag2, board, solutions)
    return solutions


# MAIN MENU 
def main():
    print("N-Queens Problem Solver")
    print("1. Solve using Backtracking")
    print("2. Solve using Branch and Bound")
    choice = input("Enter your choice (1 or 2): ")

    n = int(input("Enter the value of N (number of queens): "))
    if n < 1:
        print("N must be at least 1.")
        return

    if choice == "1":
        print("\nSolving using Backtracking...\n")
        solutions = n_queens_backtracking(n)
    elif choice == "2":
        print("\nSolving using Branch and Bound...\n")
        solutions = n_queens_branch_and_bound(n)
    else:
        print("Invalid choice.")
        return

    print(f"Total solutions found: {len(solutions)}\n")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_solution(sol)

if __name__ == "__main__":
    main()
