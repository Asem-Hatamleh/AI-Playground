import tkinter as tk
from tkinter import messagebox
from queue import Queue
import random

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Function to check if the given state is the goal state
def is_goal(state):
    return state == goal_state

# determine the possible moves that can be made 
def get_moves(state):  
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0: #  تمثل الفراغ 
                if i > 0:
                    moves.append((i - 1, j)) # up 
                if i < 2:
                    moves.append((i + 1, j)) # down 
                if j > 0:
                    moves.append((i, j - 1)) # left 
                if j < 2:
                    moves.append((i, j + 1)) # right 
    return moves

# find the position of 0 
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# representing the move to be made
def make_move(state, move):
    i, j = move # were the 0 will be moved 
    zero_i, zero_j = find_zero(state)
    new_state = [row.copy() for row in state] #  copying each row
    new_state[i][j], new_state[zero_i][zero_j] = new_state[zero_i][zero_j], new_state[i][j] # swaping 
    return new_state



# BFS
def bfs(start_state):
    visited = set() # avoid revisiting state 
    queue = Queue()
    queue.put((start_state, []))
    
    #processes each state in BFS
    while not queue.empty(): 
        current_state, path = queue.get()

        if is_goal(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        for move in get_moves(current_state):
            new_state = make_move(current_state, move)

            if tuple(map(tuple, new_state)) not in visited:
                queue.put((new_state, path + [new_state]))

    return None

# GUI 
class PuzzleSolverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("8-Puzzle Solver")

        #   button    
        self.button_style = {"width": 8, "height": 4, "font": ("Arial", 12)}
        self.master.configure(bg="lightgray")

        self.puzzle_frame = tk.Frame(self.master, bg="lightgray")
        self.puzzle_frame.pack()

        self.puzzle_buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.puzzle_buttons[i][j] = tk.Button(self.puzzle_frame, text="", bg="lightblue",
                                                      activebackground="cyan", **self.button_style,
                                                      command=lambda i=i, j=j: self.move(i, j))
                self.puzzle_buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        #  Solve and Generate buttons 
        self.button_frame = tk.Frame(self.master, bg="lightgray")
        self.button_frame.pack()

        self.solve_button = tk.Button(self.button_frame, text="Solve", command=self.solve, bg="green", fg="white",
                                      activebackground="darkgreen", **self.button_style)
        self.solve_button.pack(side=tk.LEFT, padx=10)

        # Changed the button text and command here
        self.generate_button = tk.Button(self.button_frame, text="Generate", command=self.generate, bg="orange", fg="white",
                                         activebackground="darkorange", **self.button_style)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        self.generate()  #  generate a puzzle when it start

    def move(self, i, j):
        current_value = self.puzzle[i][j]
        if current_value != 0:
            moves = get_moves(self.puzzle)
            if (i, j) in moves:
                self.puzzle = make_move(self.puzzle, (i, j))
                self.update_buttons()

    def solve(self):
        solution = bfs(self.puzzle)
        if solution:
            self.animate_solution(solution)
        else:
            messagebox.showinfo("No Solution", "The puzzle is not solvable.")
            self.generate()  # Regenerate a puzzle  

    # Generate
    def generate(self):
        # Change the initial state  
        self.puzzle = generate_solvable_puzzle()
        self.update_buttons()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                self.puzzle_buttons[i][j].config(text=str(self.puzzle[i][j]))

    def animate_solution(self, solution):
        for move in solution:
            self.puzzle = move
            self.update_buttons()
            self.highlight_moving_index(move)
            self.master.update_idletasks()
            self.master.after(10)  

    def highlight_moving_index(self, state):
        zero_i, zero_j = find_zero(state)
        self.puzzle_buttons[zero_i][zero_j].config(bg="yellow")
        self.master.update_idletasks()
        self.master.after(200)   
        self.puzzle_buttons[zero_i][zero_j].config(bg="lightblue")

def generate_solvable_puzzle():
    goal_state_flat = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(goal_state_flat)

    puzzle = [goal_state_flat[i:i+3] for i in range(0, 9, 3)]
    while not is_solvable(puzzle):  
        random.shuffle(goal_state_flat)
        puzzle = [goal_state_flat[i:i+3] for i in range(0, 9, 3)]

    return puzzle

def is_solvable(puzzle):
    inversion_count = 0
    flatten_puzzle = [number for row in puzzle for number in row]

    for i in range(8):
        for j in range(i + 1, 9):
            if flatten_puzzle[i] > flatten_puzzle[j] and flatten_puzzle[i] != 0 and flatten_puzzle[j] != 0:
                inversion_count += 1

    return inversion_count % 2 == 0

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleSolverApp(root)
    root.mainloop()
