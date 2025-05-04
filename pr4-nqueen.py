 def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
    return not (cols[col] or diags1[row + col] or diags2[row - col + (n - 1)])

def solve_backtracking(row, n, cols, diags1, diags2, board):
    global count, solutions
    if row == n:
        solutions.append([row[:] for row in board])  # Copy the solution
        count += 1
        return

    for col in range(n):
        if is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
            board[row][col] = True
            cols[col] = diags1[row + col] = diags2[row - col + (n - 1)] = True

            solve_backtracking(row + 1, n, cols, diags1, diags2, board)

            board[row][col] = False
            cols[col] = diags1[row + col] = diags2[row - col + (n - 1)] = False

def n_queens_branch_and_bound(n):
    global count, solutions
    board = [[False]*n for _ in range(n)]
    cols = [False]*n
    diags1 = [False]*(2*n - 1)
    diags2 = [False]*(2*n - 1)
    solve_backtracking(0, n, cols, diags1, diags2, board)
    print(f"Found {count} solution(s):\n")
     
    idx = 0
    for sol in solutions:

        print(f"Solution {idx + 1}:")
        print_board(sol)
        idx +=1
    print(f"Total solutions: {count}")

count = 0
solutions = []
n = int(input("Enter the value of N: "))
n_queens_branch_and_bound(n)
