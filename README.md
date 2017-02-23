# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: All the possible digits for a box constitute the search space for the box. All the possible constraints for all the boxes constitute the search space. By attaching different constraints to each unit, we reduce the search space. Once search space for a unit is reduced, all the constraints can be applied again to narrow down the constraints further. This can be applied repeatedly till the puzzle is solved, or there is not further narrowing of the space.

Naked twins is actually a constraint that can be applied along with elimination, and only_choice to narrow down the search space. By applying this constraint, the number of iterations required and the number of nodes in the search tree can be narrowed.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We first apply constraint of elimination, only_choice, and naked twins on each of the units to narrow down the search space. the two diagonals are two different units which need to be added to the units in the search space. Once the diagonal units are created and added to the list of units, all the constraints are applied by the engine on the diagonals as well and the solution emerges.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.