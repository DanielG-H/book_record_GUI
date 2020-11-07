from tkinter import *
from tkinter import ttk

# import sqlite3


class App:
    def __init__(self, window):
        self.win = window
        self.win.title("Book Register App")
        self.win.protocol("WM_DELETE_WINDOW", self.disable_event)

        # instance book data
        self.book_author = ""
        self.book_title = ""
        self.book_genre = ""
        self.book_rating = 0

        # Create options for "books read" and "books to read"
        frame_main = LabelFrame(self.win, text="Select an option: ", bg="bisque4")
        frame_main.grid(row=0, column=0, columnspan=2, padx=70, pady=40)

        # Select options
        books_read = Button(frame_main, text="Books Read", fg="gray10", bg="gold",
                            padx=60, pady=30, command=lambda: self.open_read_window(books_read))
        books_read.grid(row=0, column=0, padx=5, pady=5)

        books_to_read = Button(frame_main, text="Books To Read", fg="gray10", bg="goldenrod",
                               padx=60, pady=30, command=lambda: self.open_to_read_window(books_to_read))
        books_to_read.grid(row=0, column=1, padx=5, pady=5)

        # closes main program
        exit_app = Button(frame_main, text="Exit App", fg="red3", bg="LemonChiffon2",
                          padx=30, pady=30, command=self.win.destroy)
        exit_app.grid(row=0, column=3, padx=5, pady=5)

    def disable_event(self):
        pass

    def exit_open_menu(self, opt, button):
        # prevents exiting the main menu without a button
        opt.protocol("WM_DELETE_WINDOW", self.disable_event)

        exit_frame = LabelFrame(opt, text="Menu Options: ")
        exit_frame.grid(column=2, row=0)

        close_menu = Button(exit_frame, text="Close Main Menu", command=self.win.withdraw)
        close_menu.grid(row=0, column=0, pady=10)

        # goes to main menu and closes the other window
        go_to_menu = Button(exit_frame, text="Go To Main Menu",
                            command=lambda: [self.win.deiconify(), opt.withdraw(), self.enable_button(button)])
        go_to_menu.grid(row=0, column=1, pady=10)

    def open_read_window(self, button):
        read = Toplevel()
        read.title("Book Register App - [Books Read]")
        read.config(background="gold")
        self.disable_button(button)
        self.exit_open_menu(read, button)

        data_key = 0
        self.data_manipulation(read, data_key)

        read.mainloop()

    def open_to_read_window(self, button):
        to_read = Toplevel()
        to_read.title("Book Register App - [Books To Read]")
        to_read.config(background="goldenrod")
        self.disable_button(button)
        self.exit_open_menu(to_read, button)

        data_key = 1
        self.data_manipulation(to_read, data_key)

        to_read.mainloop()

    @staticmethod
    def disable_button(button):
        button.config(state=DISABLED)

    @staticmethod
    def enable_button(button):
        button.config(state=NORMAL)

    # Decides the table to be modified using a data key (indicates option)
    def data_manipulation(self, opt, data_key):
        data_frame = Frame(opt)
        data_frame.grid(row=1, column=2, columnspan=2)

        Label(data_frame, text="Book: ").grid(row=1, column=0)
        Entry(data_frame).grid(row=1, column=1)

        Label(data_frame, text="Author: ").grid(row=2, column=0)
        Entry(data_frame).grid(row=2, column=1)

        Label(data_frame, text="Genre: ").grid(row=3, column=0)
        Entry(data_frame).grid(row=3, column=1)

        if data_key != 1:
            Label(data_frame, text="Rating: ").grid(row=4, column=0)
            Entry(data_frame).grid(row=4, column=1, columnspan=2)

        # command=lambda: self.register(opt, data_key)
        register = Button(opt, text="Register", padx=30, pady=10)
        register.grid(row=5, column=1, columnspan=2, pady=10)

        main_table = ttk.Treeview(opt, height=10, columns=(0, 1, 2))
        main_table.grid(row=6, column=2, sticky="nsew", padx=10, pady=10)

        main_table.heading("#0", text="Book", anchor=CENTER)
        main_table.heading("#1", text="Author", anchor=CENTER)
        main_table.heading("#2", text="Genre", anchor=CENTER)
        main_table.heading("#3", text="Rating", anchor=CENTER)

    # def register(self, opt, data_key):
    #     if data_key == 0:
    #         pass
    #     else:
    #         pass


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
