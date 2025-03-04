# Back Down Memory Lane: 
## README for Sudoku Solver using Simple & Smart Backtracking

## Synopsis of the Program
This program was a fun challenge, as I had never attempted to complete a Sudoku puzzle before completing this assignment. I still have a long way to go before I can complete puzzles at the speed of this program, but I digress. This Python program solves Sudoku puzzles using Constraint Satisfaction Problem (CSP) approaches. It implements a basic and smart backtracking solver incorporating the Minimum Remaining Values (MRV) heuristic. The implementation is inspired by techniques found in the *Artificial Intelligence: A Modern Approach (AIMA)* GitHub repository. The program solves four Sudoku test puzzles at different difficulty levels: Easy, Medium, Hard, and Evil, as outlined in the assignment. It reports the time taken and the number of value assignments each solving approach makes.

---

## Meeting the Assignment Requirements

### Task 1: Formulating Sudoku as a CSP
In this Sudoku constraint satisfaction problem, each cell in the 9x9 grid represents a variable. The domain of each empty cell consists of possible values ranging from 1 to 9. Several constraints govern the problem:
- Each row must contain unique numbers from 1 to 9.
- Each column must contain unique numbers within the same range.
- Each 3x3 sub-grid must not have repeated numbers.
- Any pre-filled values in the grid must remain unchanged throughout the solving process.

### Task 2: Basic Backtracking Solver
The basic Sudoku solver is implemented as the `backtrack_solver` function, which uses a simple backtracking approach to explore possible number placements recursively. The algorithm systematically assigns values to empty cells, backtracking whenever a conflict arises until a valid solution is found. This method follows the fundamental principles of *Basic Backtracking Search*, as outlined in the AIMA repository.

### Task 3: Smart Backtracking Solver (MRV Heuristic)
The competent Sudoku solver is implemented as the `backtrack_solver_smart` function, which utilizes the Minimum Remaining Values (MRV) heuristic to select the next empty cell with the fewest possible values. This approach, inspired by the *MRV Heuristic for Variable Selection* in AIMA, prioritizes the most constrained variables, reducing the search space and improving efficiency. Additionally, it attempts numbers in an order that minimizes conflicts, further accelerating the solving process.

### Task 4: Reporting and Analysis
The program measures and prints key performance metrics, including:
- The execution time for each solver.
- The number of value assignments made during solving.
- A formatted solution grid for each difficulty level.
These outputs directly compare the basic and smart solvers, highlighting their efficiency and effectiveness in solving Sudoku puzzles.

---

## How to Run the Program
### Prerequisites:
Ensure you have **PyCharm** installed as your Python IDE.

### Steps to Run:
1. Open **PyCharm**.
2. Click on `File > Open` and select the directory containing `Hw2Rev3.py`.
3. Set up your Python interpreter:
   - Go to `File > Settings > Project: [Your Project Name] > Python Interpreter`.
   - Ensure that a valid Python version is selected.
4. Run the script:
   - Open `Hw2Rev3.py` in the editor.
   - Click the **Run** button (green triangle) at the top-right, or right-click anywhere in the script and select **Run 'Hw2Rev3'**.

#### Alternatively, you can use the terminal inside PyCharm:
```bash
python Hw2Rev3.py
```

---

## Expected Output
The program displays the original puzzle and the solutions found using both basic and smart solvers for each puzzle difficulty level. Additionally, it reports the execution time and the number of value assignments made by each solver, allowing for a direct comparison of their performance. An example of the output from the Python program is included below.
******************************
       Solving Easy Sudoku
******************************


============================
        Basic Solver
============================
Sudoku solved in 0.001 seconds

7  3  4  5  8  1  2  9  6
5  8  6  2  9  4  7  1  3
9  1  2  3  7  6  5  4  8
3  6  5  7  1  9  8  2  4
4  2  7  8  6  5  1  3  9
1  9  8  4  3  2  6  5  7
6  5  3  9  2  7  4  8  1
8  4  1  6  5  3  9  7  2
2  7  9  1  4  8  3  6  5


Total Assignments: 143 


============================
        Smart Solver
============================
Sudoku solved in 0.0205 seconds

7  3  4  5  8  1  2  9  6
5  8  6  2  9  4  7  1  3
9  1  2  3  7  6  5  4  8
3  6  5  7  1  9  8  2  4
4  2  7  8  6  5  1  3  9
1  9  8  4  3  2  6  5  7
6  5  3  9  2  7  4  8  1
8  4  1  6  5  3  9  7  2
2  7  9  1  4  8  3  6  5


Total Assignments: 45 

---

## Inspirations for the Functions in My Code
While the program runs efficiently, I cannot take full credit for it. Many of the functions implemented in this program came from the *AIMA-Python* GitHub repository:
- `find_empty` function follows the basic unassigned variable selection approach.
- `find_empty_mrv` implements the Minimum Remaining Values (MRV) heuristic for more efficient variable selection.
- `backtrack_solver` is based on *Basic Backtracking Search*.
- `backtrack_solver_smart` enhances this approach by incorporating the *MRV heuristic*, ultimately improving the solver’s efficiency by prioritizing variables with the fewest possible values.

---

## References
- **Aimacode.** *(n.d.-b).* Aimacode/aima-python: Python implementation of algorithms from Russell and Norvig’s *Artificial Intelligence - A Modern Approach*. [GitHub Repository](https://github.com/aimacode/aima-python)

### Works Consulted
- **ChatGPT.** *(n.d.-a).* [ChatGPT Website](https://chatgpt.com/)
- **Grammarly.** *(n.d.-a).* [Grammarly Demo](https://app.grammarly.com/demo)
