from tkinter import *
from classes import *

ROOT_SIZE = (600, 400)
COLORS_SIZE = (200, 130)
CANVAS_SIZE = (575, 300)

current_color: StringVar
colors_window_opened = False

def get_color() -> StringVar:
    return current_color

def set_color(color: str) -> None:
    current_color.set(color)

def colors_window_closed() -> None:
    global colors_window_opened
    colors_window_opened = False

def open_colors_window() -> None:
    global colors_window_opened

    if (colors_window_opened):
        return
    
    window = ColorsWindow(COLORS_SIZE[0], COLORS_SIZE[1], "Colors", current_color, colors_window_closed, set_color)
    colors_window_opened = True

def main() -> None:
    global ROOT_SIZE, COLORS_SIZE, CANVAS_SIZE
    global current_color

    root = Root(ROOT_SIZE[0], ROOT_SIZE[1], "Paint", "gray")

    current_color = StringVar()
    current_color.set("black")

    canvas = PaintCanvas(CANVAS_SIZE[0], CANVAS_SIZE[1], get_color)

    colors_btn = Button(text="Colors", command=open_colors_window)
    colors_btn.pack(after=canvas.obj, side="left", padx=100, pady=20)
    erase_btn = Button(text="Erase All", command=canvas.erase)
    erase_btn.pack(after=canvas.obj, side="right", padx=100, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()