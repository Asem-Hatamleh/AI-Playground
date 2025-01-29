# Minesweeper AI

## Overview
This project is an AI implementation for playing the Minesweeper game, inspired by the CS50 course at Harvard University. The AI uses propositional logic and inference to determine safe moves and identify mines.

## Getting Started
### Prerequisites
Ensure you have Python installed on your system. This project also requires the `pygame` package.

### Installation
1. Download the assignment directory (`minesweeper.zip`) from the E-Learning platform and extract it.
2. Open a terminal in the extracted directory.
3. Run the following command to install the required package:
   ```bash
   pip3 install -r requirements.txt
   ```

## How to Run
To start the Minesweeper AI:
```bash
python runner.py
```
This will launch the graphical interface where you can play manually or let the AI make moves.

## Project Structure
- `runner.py` – Handles the graphical interface of the Minesweeper game.
- `minesweeper.py` – Contains the logic for the Minesweeper game and AI implementation.

## AI Implementation
The AI uses logical inference to determine safe moves and flag mines. It maintains a knowledge base of known information and makes decisions based on:
- Safe moves that are guaranteed to be non-mines.
- Mines that can be inferred with certainty.
- Random moves when no deterministic decision is possible.

### Key Classes
- **`Minesweeper`**: Represents the game board, mines, and player interactions.
- **`Sentence`**: Represents logical statements about a group of cells and the number of mines within them.
- **`MinesweeperAI`**: Implements the AI logic for playing the game.

### Important Functions
#### `Sentence` Class
- `known_mines()`: Returns cells that are definitely mines.
- `known_safes()`: Returns cells that are definitely safe.
- `mark_mine(cell)`: Marks a given cell as a mine and updates the sentence accordingly.
- `mark_safe(cell)`: Marks a given cell as safe and updates the sentence accordingly.

#### `MinesweeperAI` Class
- `add_knowledge(cell, count)`: Updates knowledge based on revealed cells.
- `make_safe_move()`: Chooses a guaranteed safe move.
- `make_random_move()`: Chooses a random move when no safe move is available.

## Game Rules
- Clicking a mine results in losing the game.
- Clicking a safe cell reveals a number indicating adjacent mines.
- The goal is to flag all mines and clear the board without detonating a mine.
- The AI infers mine positions using logical deductions and safe cell identification.

## Notes
- The AI may not always win, as some scenarios require guessing.
- The AI continually updates its knowledge base and refines inferences during the game.
- Additional helper methods can be added for efficiency, but core function signatures should remain unchanged.

## Acknowledgments
This project follows the guidelines of Harvard's CS50 AI course.

## License
This project is for educational purposes and should not be used commercially without permission.

