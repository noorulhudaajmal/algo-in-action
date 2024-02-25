import os
import time
import tkinter as tk
from tkinter import messagebox


sudoku_board = [
    [3, 2, 0, 0, 0, 0, 0, 8, 9],
    [0, 6, 8, 0, 5, 2, 7, 3, 4],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 8, 3, 2, 0, 1, 5, 9, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [2, 1, 4, 7, 8, 0, 3, 5, 0],
    [5, 3, 0, 0, 0, 0, 9, 0, 8]
]


root = tk.Tk()
root.title("Sudoku Solution using Backtracking")
canvas = tk.Canvas(root, width=9 * 50, height=9 * 50)
canvas.pack()


def is_valid(board, current_pos, num):
    row, column = current_pos

    # checking in the current row
    for i, value in enumerate(board[row]):
        if i == row:
            continue
        if value == num:
            return False

    # checking in the current column
    for i in range(len(board)):
        if i == column:
            continue
        if board[i][column] == num:
            return False

    # checking in the square
    box = (row // 3, column // 3)
    for i in range(box[0] * 3, box[0] * 3 + 3):
        for j in range(box[1] * 3, box[1] * 3 + 3):
            if (i, j) == (row, column):
                continue
            if board[i][j] == num:
                return False

    return True


def solve_board(board):
    pos = find_empty_cell(board)
    if not pos:
        return board
    else:
        x, y = pos
    for i in range(1, 10):
        if is_valid(board, pos, i):
            board[x][y] = i
            display_board(board, (x, y))
            # Update the Tkinter window and wait for 0.2 seconds
            root.update()
            if solve_board(board):
                return board
            # reset and back-tracking
            board[x][y] = 0

    return None


def display_board(board, pos):
    canvas.delete("all")
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            x, y = j * 50, i * 50
            if num != 0:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="white")
                canvas.create_text(x + 25, y + 25, text=num, fill="black")
            else:
                canvas.create_rectangle(x, y, x + 50, y + 50, fill="gray")
            if (i + 1) % 3 == 0 and i != 8:
                canvas.create_line(0, y + 50, 450, y + 50, fill="black", width=4)
            if (j + 1) % 3 == 0 and j != 8:
                canvas.create_line(x + 50, 0, x + 50, 450, fill="black", width=4)
    x, y = pos
    x *= 50
    y *= 50
    canvas.create_rectangle(y, x, y + 50, x + 50, outline="green", width=5)


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(value, end=" ")
        print("\n")


def find_empty_cell(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:
                return i, j
    return None


def main():
    print_board(sudoku_board)
    sol = solve_board(sudoku_board)
    print("\nSolved Board:")
    print_board(sol)


if __name__ == "__main__":
    main()
