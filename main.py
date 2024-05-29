from tkinter import *

ROOT_SIZE = (600, 500)
COLORWNDW_SIZE = (200, 150)
CANVAS_SIZE = (575, 400)

prev_x, prev_y, cur_x, cur_y = 0, 0, 0, 0

canvas_pressed = False
colors_window_opened = False

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

def on_colors_window_close(window_obj: Toplevel) -> None:
    global colors_window_opened
    colors_window_opened = False
    window_obj.destroy()

def create_color_window() -> None:
    global paint_color
    global canvas_obj
    global colors_window_opened

    if colors_window_opened:
        return
    
    colors_window_opened = True

    color_window = Toplevel()
    color_window.geometry(f"{COLORWNDW_SIZE[0]}x{COLORWNDW_SIZE[1]}")
    color_window.title("Colors")
    color_window.resizable(False, False)

    red_radio = Radiobutton(color_window, fg="red", text="Red", variable=paint_color, value="red")
    green_radio = Radiobutton(color_window, fg="green", text="Green", variable=paint_color, value="green")
    blue_radio = Radiobutton(color_window, fg="blue", text="Blue", variable=paint_color, value="blue")
    black_radio = Radiobutton(color_window, fg="black", text="Black", variable=paint_color, value="black")
    white_radio = Radiobutton(color_window, fg="gray", text="White", variable=paint_color, value="white")

    red_radio.pack()
    green_radio.pack()
    blue_radio.pack()
    black_radio.pack()
    white_radio.pack()

    color_window.protocol("WM_DELETE_WINDOW", lambda: on_colors_window_close(color_window))

def main() -> None:
    global paint_color
    global canvas_obj

    root = Tk()
    paint_color = StringVar()
    paint_color.set("black")

    root.geometry(f"{ROOT_SIZE[0]}x{ROOT_SIZE[1]}")
    root.title("Paint")
    root.resizable(False, False)
    root.configure(background="gray")

    canvas_obj = Canvas(bg="white", width=CANVAS_SIZE[0], height=CANVAS_SIZE[1])
    canvas_obj.pack(pady=10)
    canvas_obj.bind("<Motion>", on_canvas_motion)
    canvas_obj.bind("<ButtonPress>", on_canvas_press)
    canvas_obj.bind("<ButtonRelease>", on_canvas_release)

    erase_btn = Button(text="Erase All", command=erase_canvas)
    erase_btn.pack(side="right", pady=20, padx=100)
    erase_btn = Button(text="Colors", command=create_color_window)
    erase_btn.pack(side="left", pady=20, padx=100)

    root.mainloop()

if __name__ == "__main__":
    main()