from tkinter import *
from tkinter import messagebox
from constants import *

class View:
    def __init__(self):
        self.__window = Tk()

    @property
    def window(self):
        return self.__window

    def create_label(self, master, text, bg, fg, font_size, width, height, padx):
        return Label(
            master=master,
            text=text,
            bg=bg,
            fg=fg,
            font=(FONT, font_size),
            width=width,
            height=height,
            padx=padx
        )

    def create_entry(self):
        return Entry(self.__window, width=ENTRY_WIDTH, font=(FONT, FONT_SIZE), fg=FG)

    def create_button(self, text, command):
        return Button(
            self.__window,
            text=text,
            font=(FONT, FONT_SIZE),
            bg=BG_BUTTON,
            fg=FG,
            width=BTN_WIDTH,
            borderwidth=BRDR_WIDTH,
            command=command
        )

    def create_frame(master):
        return Frame(
            master=master,
            relief=RAISED,
            width=FRAME_WIDTH,
            height=FRAME_WIDTH,
            bg=BG_BOARD
        )

    def create_window(self):
        window = self.window
        window['bg'] = BG_BASE
        window.title(TITLE)
        window.iconbitmap(default=ICON)

    def show_error(msg):
        messagebox.showerror(ERROR_TITLE, msg)

    def show_info(title, msg):
        messagebox.showinfo(title, msg)

    def show_choice(title, msg):
        res = messagebox.askyesnocancel(title, msg)
        return res
