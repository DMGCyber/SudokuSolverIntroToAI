import time # This tracks the time it takes for the algorithms
# to solve the sudoku puzzle.
from itertools import product  # Importing product for Cartesian product operations.
# This helps in effeciently finding the empty ccells

class SudokuCSP: # A class to solve the sudoku puzzles using Constraint Satisfaction Problem (CSP).
    # This implements backtracking algorithms to solve a given puzzle.
    def __init__(self, puzzle):
        """
        The init serves as the initializer for
        the Sudoku CSP solver with the given puzzle.
        The Sudoku grid is 9x9 as this was what was laid out in the assignment.
        """
        self.grid = puzzle  # The Sudoku grid
        self.size = 9  # Sudoku grid size as defined by the assignment.
        self.subgrid_size = 3  # The size of the subgrid is 3x3
        self.empty_cell = 0  # Empty cells are represented by 0
        self.assignments_basic = 0  # This tracks the number of assignments
        # (times a number is placed into an empty cell) basic backtracking assignments
        self.assignments_smart = 0  # This tracks the number of assignments
        # (times a number is placed into an empty cell) smart backtracking assignments
    def is_valid(self, row, col, num):
        """
        This checks to see  if placing a number 'num' at a given location of the grid
        `grid[row][col]` is valid.
        :param row: Row index
        :param col: Column index
        :param num: Number to place
        :return: True if valid, False otherwise
        """
        # Check row
        if num in self.grid[row]:
            return False
        # Check column
        if num in [self.grid[r][col] for r in range(self.size)]:
            return False
        # Check 3x3 subgrid
        start_row, start_col = (row // self.subgrid_size) * self.subgrid_size, (col // self.subgrid_size) * self.subgrid_size
        for r, c in product(range(start_row, start_row + self.subgrid_size), range(start_col, start_col + self.subgrid_size)):
            if self.grid[r][c] == num:
                return False
        return True

    def find_empty(self):
        """
        Inspired by AIMA repo (Basic unassigned variable selection)
        Finds the first empty cell in the grid.
        :return: Tuple (row, col) if found, None otherwise
        """
        for r, c in product(range(self.size), repeat=2):
            if self.grid[r][c] == self.empty_cell:
                return r, c
        return None

    def find_empty_mrv(self):
        """
        Inspired by AIMA repo (MRV heuristic for variable selection)
        Finds the empty cell with the fewest legal values (Minimum Remaining Values heuristic).
        :return: Tuple (row, col) if found, None otherwise
        """
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
        """
        Inspired by AIMA repo (Basic Backtracking Search)
        Basic backtracking algorithm to solve Sudoku.
        :return: True if solved, False otherwise
        """
        empty = self.find_empty()
        if not empty:
            return True  # Sudoku solved
        row, col = empty
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.assignments_basic += 1
                if self.backtrack_solver():
                    return True
                self.grid[row][col] = self.empty_cell  # Undo assignment (Backtrack)
        return False

    def backtrack_solver_smart(self):
        """
        Inspired by AIMA repo (Backtracking with MRV heuristic)
        Smart backtracking using MRV heuristic.
        :return: True if solved, False otherwise
        """
        empty = self.find_empty_mrv()
        if not empty:
            return True  # Sudoku solved
        row, col = empty
        possible_values = sorted(range(1, self.size + 1), key=lambda num: sum(
            1 for r, c in product(range(self.size), repeat=2) if self.is_valid(r, c, num)))
        for num in possible_values:
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                self.assignments_smart += 1
                if self.backtrack_solver_smart():
                    return True
                self.grid[row][col] = self.empty_cell  # Undo assignment (Backtrack)
        return False

    def print_grid(self):
        """
        Prints the Sudoku grid in a readable format with extra spacing.
        """
        print("\n".join("  ".join(str(num) if num != 0 else '.' for num in row) for row in self.grid))
        print("\n")

    def solve(self):
        """
        Runs the basic backtracking solver and prints results in a formatted manner.
        """
        start_time = time.time()
        success = self.backtrack_solver()
        end_time = time.time()
        print("\n============================")
        print("        Basic Solver")
        print("============================")
        if success: # If the sudoku puzzle is solved using the basic solving algorithm,
            # the following message will be displayed
            print(f"Sudoku solved in {round(end_time - start_time, 4)} seconds\n")
            self.print_grid()
            print("Total Assignments:", self.assignments_basic, "\n")
        else: # If the sudoku puzzle is not solved using the basic solving algorithm,
            # the following message will be displayed
            print("No solution exists\n")

    def solve_smart(self):
        """
        Runs the smart backtracking solver and prints results in a formatted manner.
        """
        start_time = time.time() # Starts the time for the smart solving algorithm
        success = self.backtrack_solver_smart()
        end_time = time.time() # Ends the time for the smart solving
        print("\n============================")
        print("        Smart Solver")
        print("============================")
        if success: # If the sudoku puzzle is solved using the smart solving algorithm,
            # the following message will be displayed
            print(f"Sudoku solved in {round(end_time - start_time, 4)} seconds\n")
            self.print_grid()
            print("Total Assignments:", self.assignments_smart, "\n")
        else: # If the sudoku puzzle is not solved using the smart solving algorithm,
            # the following message will be displayed
            print("No solution exists\n")



# These are the initial states of the sudoku puzzles
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

import copy # The copy module in  provides functions for creating copies of objects.
# It helps duplicate objects without modifying the original.

for level, puzzle in puzzles.items(): # The for loop iterates over the dictionary puzzles to
    # solve multiple Sudoku puzzles at different difficulty levels.
    print("\n" + "*" * 30) # Displays a header message indicating which difficulty
    # level is currently being solved.
    print(f"       Solving {level} Sudoku")
    print("*" * 30 + "\n") # Another separator below the title

    # Create a copy of the puzzle for the basic solver
    sudoku_solver = SudokuCSP(copy.deepcopy(puzzle)) # copy.deepcopy(puzzle) ensures that the solver gets a
    # fresh copy of the unsolved Sudoku puzzle.
    sudoku_solver.solve() # This calls the solve() method,
    # which uses basic backtracking to solve the Sudoku.

    # Create a new copy for the smart solver to ensure it starts fresh
    sudoku_solver_smart = SudokuCSP(copy.deepcopy(puzzle)) # copy.deepcopy(puzzle) ensures that the solver gets a
    # fresh copy of the unsolved Sudoku puzzle.
    sudoku_solver_smart.solve_smart() # This calls the solve_smart() method, which,
    # uses a smarter algorithm (MRV heuristic + backtracking).

"""
References 

Chatgpt. (n.d.-a). https://chatgpt.com/ 
* Utilized to assist with the structure of the code 
and to make it more elegant and efficient.

Aimacode. (n.d.-b). Aimacode/aima-python: Python implementation of algorithms from Russell and Norvig’s 
“artificial intelligence - A modern approach.” GitHub. https://github.com/aimacode/aima-python 
* This utilized to assist with some of the backtracking functions and algorithms
"""
