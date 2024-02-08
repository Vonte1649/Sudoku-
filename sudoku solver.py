import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

        self.create_board()
        self.create_buttons()

    def create_board(self):
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=3, font=('Helvetica', 12), justify='center')
                entry.grid(row=i, column=j)
                entry.insert(0, str(self.board[i][j]))
                self.entries[i][j] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4)

    def solve_sudoku(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value and not value.isdigit():
                    messagebox.showerror("Error", "Invalid input. Please enter digits only.")
                    return

                self.board[i][j] = int(value) if value else 0

        if self.solve():
            self.update_board()
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0  # Backtrack if the solution is not found

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num, pos):
        row, col = pos

        # Check row
        if num in self.board[row]:
            return False

        # Check column
        if num in [self.board[i][col] for i in range(9)]:
            return False

        # Check box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num:
                    return False

        return True

    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.board[i][j]))


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()