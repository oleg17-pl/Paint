from tkinter import *
from typing import Callable

class Root:
    def __init__(self, width: int, height: int, title: str, bg: str) -> None:
        self.obj = Tk()
        self.obj.geometry(f"{width}x{height}")
        self.obj.title(title)
        self.obj.configure(background=bg)
        self.obj.resizable(False, False)
    
    def mainloop(self) -> None:
        self.obj.mainloop()

class ColorsWindow:
    def __init__(self, width: int, height: int, title: str, color: StringVar, close_func: Callable, set_color_func: Callable) -> None:
        self.obj = Toplevel()
        self.obj.geometry(f"{width}x{height}")
        self.obj.title(title)
        self.obj.resizable(False, False)

        self.close_callback = close_func
        self.color_callback = set_color_func

        self.color = color

        red_radio = Radiobutton(self.obj, fg="red", text="Red", variable=self.color, value="red")
        green_radio = Radiobutton(self.obj, fg="green", text="Green", variable=self.color, value="green")
        blue_radio = Radiobutton(self.obj, fg="blue", text="Blue", variable=self.color, value="blue")
        black_radio = Radiobutton(self.obj, fg="black", text="Black", variable=self.color, value="black")
        white_radio = Radiobutton(self.obj, fg="gray", text="White", variable=self.color, value="white")

        self.color_callback(self.color.get())
        red_radio.pack()
        green_radio.pack()
        blue_radio.pack()
        black_radio.pack()
        white_radio.pack()

        self.obj.protocol("WM_DELETE_WINDOW", self.__close)

    def __close(self) -> None:
        self.close_callback()
        self.obj.destroy()

class PaintCanvas:
    def __init__(self, width: int, height: int, get_color_func: Callable) -> None:
        self.obj = Canvas(bg="white", width=width, height=height)
        self.obj.pack(pady=10)
        self.obj.bind("<Motion>", self.__motion)
        self.obj.bind("<ButtonPress>", self.__press)
        self.obj.bind("<ButtonRelease>", self.__release)

        self.getColor = get_color_func
        self.prev_x = 0
        self.prev_y  = 0
        self.cur_x = 0
        self.cur_y = 0
        self.pressed = False

    def __press(self, event: Event) -> None:
        self.pressed = True

    def __release(self, event: Event) -> None:
        self.pressed = False

    def __motion(self, event: Event) -> None:
        if self.pressed:
            self.obj.create_line(self.prev_x, self.prev_y, self.cur_x, self.cur_y, fill=self.getColor().get())
        self.prev_x, self.prev_y = self.cur_x, self.cur_y
        self.cur_x, self.cur_y = event.x, event.y

    def erase(self) -> None:
        self.obj.delete("all")