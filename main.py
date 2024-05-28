from tkinter import *

MAINSCR_SIZE = (400, 300)
COLORSCR_SIZE = (200, 130)

prev_x, prev_y, cur_x, cur_y = 0, 0, 0, 0

canvas_pressed = False

canvas_obj: Canvas

def on_canvas_motion(event: Event) -> None:
    global prev_x, prev_y
    global cur_x, cur_y
    global paint_color
    global canvas_obj

    if canvas_pressed:
        canvas_obj.create_line(prev_x, prev_y, cur_x, cur_y, fill=paint_color.get())
    prev_x, prev_y = cur_x, cur_y
    cur_x, cur_y = event.x, event.y

def erase_canvas() -> None:
    global canvas_obj
    canvas_obj.delete("all")

def on_canvas_press(event: Event) -> None:
    global canvas_pressed
    canvas_pressed = True
    print("pres")

def on_canvas_release(event: Event) -> None:
    global canvas_pressed
    canvas_pressed = False
    print("rel")

def create_color_window() -> None:
    global paint_color
    global canvas_obj

    paint_color = StringVar()
    paint_color.set("black")

    color_window = Toplevel()
    color_window.geometry(f"{COLORSCR_SIZE[0]}x{COLORSCR_SIZE[1]}")
    color_window.title("Control")
    color_window.resizable(False, False)

    red_radio = Radiobutton(color_window, fg="red", text="Red", variable=paint_color, value="red")
    green_radio = Radiobutton(color_window, fg="green", text="Green", variable=paint_color, value="green")
    blue_radio = Radiobutton(color_window, fg="blue", text="Blue", variable=paint_color, value="blue")
    black_radio = Radiobutton(color_window, fg="black", text="Black", variable=paint_color, value="black")

    erase_btn = Button(color_window, text="Erase", command=erase_canvas)

    red_radio.pack()
    green_radio.pack()
    blue_radio.pack()
    black_radio.pack()
    erase_btn.pack()

def main() -> None:
    global paint_color
    global canvas_obj
    root = Tk()

    root.geometry(f"{MAINSCR_SIZE[0]}x{MAINSCR_SIZE[1]}")
    root.title("Paint")
    root.resizable(False, False)

    canvas_obj = Canvas(bg="white", width=MAINSCR_SIZE[0], height=MAINSCR_SIZE[1])
    canvas_obj.pack()
    canvas_obj.bind("<Motion>", lambda event: on_canvas_motion(event))
    canvas_obj.bind("<ButtonPress>", on_canvas_press)
    canvas_obj.bind("<ButtonRelease>", on_canvas_release)

    create_color_window()
    root.mainloop()

if __name__ == "__main__":
    main()