# Tic-Tac-Toe with Minimax Algorithm

## Overview
This project implements an AI for Tic-Tac-Toe using the Minimax algorithm. The AI plays optimally and cannot be defeated if both players make the best moves. This project is based on the CS50 course at Harvard University.

## Features
- Implements the Minimax algorithm for optimal play.
- Uses Alpha-Beta Pruning to improve efficiency.
- Determines the best move for a given board state.
- Detects terminal states, possible actions, and the winner.
- Includes a graphical user interface (GUI) using Pygame.

## Installation
Ensure you have Python 3.10 installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

## Usage
Run the game using:

```sh
python runner.py
```

### Controls
- Play against the AI by selecting available cells.
- The AI plays optimally using Minimax.
- The game ends when there is a winner or a tie.

## Implementation Details
- **State Representation**: The board is represented as a 3x3 list.
- **Functions Implemented**:
  - `player(board)`: Determines whose turn it is.
  - `actions(board)`: Returns possible moves.
  - `result(board, action)`: Returns a new board state after a move.
  - `winner(board)`: Checks if there is a winner.
  - `terminal(board)`: Determines if the game is over.
  - `utility(board)`: Assigns utility values (1 for X win, -1 for O win, 0 for tie).
  - `minimax(board)`: Determines the optimal move using Minimax with Alpha-Beta Pruning.

## Strategy & AI Behavior
- The AI uses Minimax to explore all possible moves and chooses the optimal one.
- Alpha-Beta Pruning is applied to enhance performance by eliminating unnecessary searches.
- The AI ensures a tie in optimal play and can win if the opponent makes a mistake.

 
