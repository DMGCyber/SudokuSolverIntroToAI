import time
from itertools import product


class SudokuCSP:
    def __init__(self, puzzle):
        self.grid = puzzle
        self.size = 9
        self.subgrid_size = 3
        self.empty_cell = 0
        self.assignments_basic = 0
        self.assignments_smart = 0

    def is_valid(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False
        # Check column
        if num in [self.grid[r][col] for r in range(self.size)]:
            return False
        # Check 3x3 subgrid
        start_row, start_col = (row // self.subgrid_size) * self.subgrid_size, (
                    col // self.subgrid_size) * self.subgrid_size
        for r, c in product(range(start_row, start_row + self.subgrid_size),
                            range(start_col, start_col + self.subgrid_size)):
            if self.grid[r][c] == num:
                return False
        return True

    def find_empty(self):
        for r, c in product(range(self.size), repeat=2):
            if self.grid[r][c] == self.empty_cell:
                return r, c
        return None

    def find_empty_mrv(self):
        min_remaining_values = float('inf')
        best_cell = None
        for r, c in product(range(self.size), repeat=2):
            if self.grid[r][c] == self.empty_cell:
                possible_values = sum(1 for num in range(1, self.size + 1) if self.is_valid(r, c, num))
                if possible_values < min_remaining_values:
                    min_remaining_values = possible_values
                    best_cell = (r, c)
        return best_cell

    def backtrack_solver(self):
        empty = self.find_empty()
        if not empty:
            return True  # Solved
        row, col = empty
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.assignments_basic += 1
                if self.backtrack_solver():
                    return True
                self.grid[row][col] = self.empty_cell  # Undo assignment
        return False

    def backtrack_solver_smart(self):
        empty = self.find_empty_mrv()
        if not empty:
            return True  # Solved
        row, col = empty
        possible_values = sorted(range(1, self.size + 1), key=lambda num: sum(
            1 for r, c in product(range(self.size), repeat=2) if self.is_valid(r, c, num)))
        for num in possible_values:
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.assignments_smart += 1
                if self.backtrack_solver_smart():
                    return True
                self.grid[row][col] = self.empty_cell  # Undo assignment
        return False

    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def solve(self):
        start_time = time.time()
        success = self.backtrack_solver()
        end_time = time.time()
        print("Basic Solver:")
        if success:
            print("Sudoku solved in", round(end_time - start_time, 4), "seconds")
            self.print_grid()
            print("Total Assignments:", self.assignments_basic)
        else:
            print("No solution exists")

    def solve_smart(self):
        start_time = time.time()
        success = self.backtrack_solver_smart()
        end_time = time.time()
        print("Smart Solver:")
        if success:
            print("Sudoku solved in", round(end_time - start_time, 4), "seconds")
            self.print_grid()
            print("Total Assignments:", self.assignments_smart)
        else:
            print("No solution exists")


# Sample Sudoku puzzles
easy = [[0, 3, 0, 0, 8, 0, 0, 0, 6],
        [5, 0, 0, 2, 9, 4, 7, 1, 0],
        [0, 0, 0, 3, 0, 0, 5, 0, 0],
        [0, 0, 5, 0, 1, 0, 8, 0, 4],
        [4, 2, 0, 8, 0, 5, 0, 3, 9],
        [1, 0, 8, 0, 3, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 7, 0, 0, 0],
        [0, 4, 1, 6, 5, 3, 0, 0, 2],
        [2, 0, 0, 0, 4, 0, 0, 6, 0]]

puzzles = {
    "Easy": [[0, 3, 0, 0, 8, 0, 0, 0, 6],
             [5, 0, 0, 2, 9, 4, 7, 1, 0],
             [0, 0, 0, 3, 0, 0, 5, 0, 0],
             [0, 0, 5, 0, 1, 0, 8, 0, 4],
             [4, 2, 0, 8, 0, 5, 0, 3, 9],
             [1, 0, 8, 0, 3, 0, 6, 0, 0],
             [0, 0, 3, 0, 0, 7, 0, 0, 0],
             [0, 4, 1, 6, 5, 3, 0, 0, 2],
             [2, 0, 0, 0, 4, 0, 0, 6, 0]],

    "Medium": [[3, 0, 8, 2, 9, 6, 0, 0, 0],
               [0, 4, 0, 0, 0, 8, 0, 0, 0],
               [5, 0, 2, 1, 0, 0, 0, 8, 7],
               [0, 1, 3, 0, 0, 0, 0, 0, 0],
               [7, 8, 0, 0, 0, 0, 0, 3, 5],
               [0, 0, 0, 0, 0, 0, 4, 1, 0],
               [1, 2, 0, 0, 0, 7, 8, 0, 3],
               [0, 0, 0, 8, 0, 0, 0, 2, 0],
               [0, 0, 0, 5, 4, 2, 1, 0, 6]],

    "Hard": [[7, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 0, 0, 4, 1, 0, 2, 5, 0],
             [0, 1, 3, 0, 9, 5, 0, 0, 0],
             [8, 6, 0, 0, 0, 0, 0, 0, 0],
             [3, 0, 1, 0, 0, 0, 4, 0, 5],
             [0, 0, 0, 0, 0, 0, 0, 8, 6],
             [0, 0, 0, 8, 4, 0, 5, 3, 0],
             [0, 4, 2, 0, 3, 6, 0, 0, 7],
             [0, 0, 0, 0, 0, 0, 0, 0, 9]],

    "Evil": [[0, 6, 0, 8, 0, 0, 0, 0, 0],
             [0, 0, 4, 0, 6, 0, 0, 0, 9],
             [1, 0, 0, 0, 4, 3, 0, 6, 0],
             [0, 5, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 8, 6, 0, 9, 3, 0, 0],
             [0, 0, 0, 0, 0, 0, 5, 7, 0],
             [0, 1, 0, 4, 8, 0, 0, 0, 5],
             [8, 0, 0, 0, 1, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 5, 0, 4, 0]]
}


for level, puzzle in puzzles.items():
    print(f"\nSolving {level} Sudoku:")
    sudoku_solver = SudokuCSP(puzzle)
    sudoku_solver.solve()
    sudoku_solver.solve_smart()
