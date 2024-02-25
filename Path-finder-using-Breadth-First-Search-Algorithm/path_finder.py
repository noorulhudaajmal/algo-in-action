import queue
import os
import time
import tkinter as tk
from tkinter import messagebox

os.system("")

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#", "#", "#", "#"],
    ["#", " ", "#", " ", "#", " ", " ", "#", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", " ", "#", "#", "#"],
    ["#", " ", "#", "#", "#", " ", " ", " ", "#", "#"],
    ["#", " ", " ", "#", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
]


def find_path(maze, root, canvas):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put(([start_pos]))
    visited = set()

    while not q.empty():
        path = q.get()
        current_pos = path[-1]
        i, j = current_pos

        # print_maze(maze, path) # for console output
        display_maze(canvas, maze, path)

        if maze[i][j] == end:
            path += [current_pos]
            return path

        neighbors = get_neighbors(maze, current_pos)
        for neighbor in neighbors:
            pos_i, pos_j = neighbor
            cell = maze[pos_i][pos_j]
            if (cell == "#") | ((pos_i, pos_j) in visited):
                continue
            q.put((path + [neighbor]))
            visited.add(neighbor)

        # Update the Tkinter window and wait for 0.2 seconds
        root.update()
        time.sleep(0.2)


def print_maze(maze, path):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path:
                print("\033[92mX\033[0m", end=" ")  # Print path in green
            elif cell == "#":
                print("\033[91m#\033[0m", end=" ")  # Print obstacles in red
            else:
                print(cell, end=" ")
        print("\n")
    print("\n")


def display_maze(canvas, maze, path):
    canvas.delete("all")
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x, y = j * 30, i * 30
            if cell == "#":
                canvas.create_rectangle(x, y, x + 30, y + 30, fill="red")
            elif cell == "X":
                canvas.create_rectangle(x, y, x + 30, y + 30, fill="purple")
            elif (i, j) in path:
                canvas.create_oval(x, y, x + 30, y + 30, fill="green")


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == start:
                return (i, j)
    return None


def get_neighbors(maze, current_pos):
    neighbors = []
    i, j = current_pos
    if i > 0:  # UP
        neighbors.append((i - 1, j))
    if i < len(maze) - 1:  # DOWN
        neighbors.append((i + 1, j))
    if j > 0:  # LEFT
        neighbors.append((i, j - 1))
    if j < len(maze[0]) - 1:  # RIGHT
        neighbors.append((i, j + 1))
    return neighbors


def main():
    # Create a Tkinter window
    root = tk.Tk()
    root.title("BFS in Action")
    canvas = tk.Canvas(root, width=len(maze[0]) * 30, height=len(maze) * 30)
    canvas.pack()

    final_path = find_path(maze, root, canvas)
    display_maze(canvas, maze, final_path)

    # Show pop-up message after the window is closed
    messagebox.showinfo("Path found!", f"Shortest path is {len(final_path) - 1} units")


if __name__ == "__main__":
    main()
