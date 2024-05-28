from tkinter import *

SCR_SIZE = (600, 400)
prev_x, prev_y = -1, -1
cur_x, cur_y = prev_x, prev_y
canvas_pressed = False

def on_canvas_motion(event: Event, canvas: Canvas) -> None:
    global prev_x, prev_y
    global cur_x, cur_y
    if canvas_pressed:
        if prev_x != -1 and prev_y != -1:
            canvas.create_line(prev_x, prev_y, cur_x, cur_y, fill="red")
    prev_x, prev_y = cur_x, cur_y
    cur_x, cur_y = event.x, event.y

def on_canvas_press(event: Event) -> None:
    global canvas_pressed
    canvas_pressed = True
    print("pres")

def on_canvas_release(event: Event) -> None:
    global canvas_pressed
    canvas_pressed = False
    print("rel")

def main() -> None:
    root = Tk()
    canvas = Canvas(bg="white", width=SCR_SIZE[0], height=SCR_SIZE[1])

    root.geometry(f"{SCR_SIZE[0]}x{SCR_SIZE[1]}")
    root.title("Hello")
    root.resizable(False, False)

    canvas.pack(anchor=CENTER, expand=1)
    canvas.bind("<Motion>", lambda event: (on_canvas_motion(event, canvas)))
    canvas.bind("<ButtonPress>", on_canvas_press)
    canvas.bind("<ButtonRelease>", on_canvas_release)
    root.mainloop()

if __name__ == "__main__":
    main()