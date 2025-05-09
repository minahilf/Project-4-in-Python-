# GUI bnane k lye ek library
import tkinter as tk 

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def Create_grid(canvas):
    # grid k rect ko store kreng
    cells = []

# rows banane ka loop jo 0 se canvas ki height tk bnayega cell 
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        # current row ka rect store horha
        row_cells = []
        # ab col ka loop 
        for col in range(0, CANVAS_WIDTH,CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill = "blue", outline = "black")

            row_cells.append(rect)
        cells.append(row_cells)
    return cells


def erase(event):
    x, y = event.x , event.y
    row  = y // CELL_SIZE
    col  = x // CELL_SIZE

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill = "white")

def main():
    global canvas, grid
    # root main window h
    root = tk.Tk()
    root.title("Erase Canvas")

    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.bind("<B1-Motion>", erase)
    # main window show krha pack 
    canvas.pack()

    grid = Create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()