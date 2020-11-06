from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, window):
        self.win = window
        self.win.title("Book Register App")
        self.win.protocol("WM_DELETE_WINDOW", self.disable_event)

        # Create options for "books read" and "books to read"
        frame_main = LabelFrame(self.win, text="Select an option: ")
        frame_main.grid(row=0, column=0, columnspan=2, padx=70, pady=40)

        # Select options
        books_read = Button(frame_main, text="Books Read", fg="gray10", bg="gold",
                            padx=65, pady=30, command=self.open_read_window)
        books_read.grid(row=0, column=0, padx=5, pady=5)

        books_to_read = Button(frame_main, text="Books To Read", fg="gray10", bg="goldenrod",
                               padx=65, pady=30, command=self.open_to_read_window)
        books_to_read.grid(row=0, column=1, padx=5, pady=5)

    def disable_event(self):
        pass

    def data_entry(self):
        pass

    def exit_open_menu(self, opt):
        opt.protocol("WM_DELETE_WINDOW", self.disable_event)
        close_menu = Button(opt, text="Close Main Menu", command=self.win.withdraw)
        close_menu.grid(row=0, column=1)

        go_to_menu = Button(opt, text="Go To Main Menu", command=lambda: [self.win.deiconify(), opt.withdraw()])
        go_to_menu.grid(row=0, column=2)

    def open_read_window(self):
        read = Toplevel()
        read.title("Book Register App - [Books Read]")
        self.exit_open_menu(read)
        read.mainloop()

    def open_to_read_window(self):
        to_read = Toplevel()
        to_read.title("Book Register App - [Books To Read]")
        self.exit_open_menu(to_read)
        to_read.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
