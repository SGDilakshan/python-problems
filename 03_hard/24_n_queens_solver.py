# Given a n x n chessboard, return all distinct solutions to the N-Queens puzzle.
# The N-Queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens attack each other (no same row, column, or diagonal).

def solve_n_queens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row, path):
        if row == n:
            board = ["".join(row) for row in path]
            results.append(board)
            return

        for col in range(n):
            if is_safe(row, col):
                path[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                place_queen(row + 1, path)

                path[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    results = []
    cols = set()
    diag1 = set()
    diag2 = set()
    empty_board = [['.' for _ in range(n)] for _ in range(n)]

    place_queen(0, empty_board)
    return results


# Example usage
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Solutions for {n}-Queens problem:")
    for board in solutions:
        for row in board:
            print(row)
        print()

