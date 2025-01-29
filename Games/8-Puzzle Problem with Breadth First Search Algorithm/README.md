# 8-Puzzle Solver Using BFS

## Overview
This project implements a solution for the 8-Puzzle problem using the Breadth-First Search (BFS) algorithm. Additionally, it includes a graphical user interface (GUI) built with Tkinter to allow users to interactively solve the puzzle.

## 8-Puzzle Problem
The 8-Puzzle is a sliding tile puzzle where the goal is to rearrange tiles into a specified order by swapping an empty space (0) with adjacent tiles. The goal state is:

```
1 2 3
4 5 6
7 8 0
```

## Features
- Implements BFS to find the optimal solution.
- GUI built using Tkinter for an interactive experience.
- Ability to generate a random solvable puzzle.
- Animated solution display.
- Highlights the moving tile during the solving process.

## Installation
Ensure you have Python installed on your system. Then, install the required dependencies:

```sh
pip install tk
```

## Usage
Run the script using:

```sh
python puzzle_solver.py
```

### Controls
- **Generate**: Creates a new solvable puzzle.
- **Solve**: Uses BFS to find the optimal solution and animates the moves.

## Implementation Details
- **State Representation**: The puzzle state is represented as a 3x3 matrix.
- **Moves**: The blank space (0) can move up, down, left, or right.
- **Solvability Check**: Ensures that generated puzzles can be solved.
- **BFS Algorithm**: Finds the shortest path to the goal state.

## Bonus Feature
- A GUI provides a visual representation of the state changes while solving the puzzle, earning an additional bonus mark as per the assignment requirements.

 

