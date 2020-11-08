from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3


class App:

    db = 'bookrecord.db'

    # declare book data
    book_author = ""
    book_title = ""
    book_genre = ""
    book_rating = ""
    book_pages = 0

    def __init__(self, window):
        self.win = window
        self.win.title("Book Record App")
        self.win.protocol("WM_DELETE_WINDOW", self.disable_event)

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
        read.title("Book Record App - [Books Read]")
        read.config(background="gold")
        self.disable_button(button)
        self.exit_open_menu(read, button)

        data_key = 0
        self.data_manipulation(read, data_key)

        read.mainloop()

    def open_to_read_window(self, button):
        to_read = Toplevel()
        to_read.title("Book Record App - [Books To Read]")
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

        Label(data_frame, text="Title: ").grid(row=1, column=0)
        self.book_title = Entry(data_frame)
        self.book_title.grid(row=1, column=1)

        Label(data_frame, text="Author: ").grid(row=2, column=0)
        self.book_author = Entry(data_frame)
        self.book_author.grid(row=2, column=1)

        Label(data_frame, text="Genre: ").grid(row=3, column=0)
        self.book_genre = Entry(data_frame)
        self.book_genre.grid(row=3, column=1)

        if data_key != 1:
            Label(data_frame, text="Rating: ").grid(row=4, column=0)
            self.book_rating = Entry(data_frame)
            self.book_rating.grid(row=4, column=1, columnspan=2)

        Label(data_frame, text="Pages: ").grid(row=5, column=0)
        self.book_pages = Entry(data_frame)
        self.book_pages.grid(row=5, column=1, columnspan=2)

        register = Button(opt, text="Register", padx=30, pady=10,
                          command=lambda: self.register_book(opt, data_key, main_table))
        register.grid(row=6, column=1, columnspan=2, pady=10)

        main_table = ttk.Treeview(opt, height=10, columns=(0, 1, 2, 3))
        main_table.grid(row=7, column=2, sticky="nsew", padx=10, pady=10)

        main_table.heading("#0", text="Title", anchor=CENTER)
        main_table.heading("#1", text="Author", anchor=CENTER)
        main_table.heading("#2", text="Genre", anchor=CENTER)
        main_table.heading("#3", text="Rating", anchor=CENTER)
        main_table.heading("#4", text="Pages", anchor=CENTER)

        self.list_books(main_table, data_key)

    # Launches a query to the database
    def query(self, query, parameters=()):
        with sqlite3.connect(self.db) as c:
            cursor = c.cursor()
            result = cursor.execute(query, parameters)
            c.commit()
        return result

    # Validates non null state of the first three fields
    def validate_data(self):
        return len(self.book_title.get()) != 0 and len(self.book_author.get()) != 0 and len(self.book_genre.get()) != 0

    def list_books(self, main_table, data_key):
        data = main_table.get_children()
        for field in data:
            main_table.delete(field)
        if data_key == 0:
            query = "SELECT * FROM books_read ORDER BY title DESC"
        else:
            query = "SELECT * FROM books_to_read ORDER BY title DESC"
        db_rows = self.query(query)
        for row in db_rows:
            main_table.insert('', 0, text=row[1], values=(row[2], row[3], row[4], row[5]))

    def register_book(self, opt, data_key, main_table):
        if self.validate_data() is True:
            if data_key == 0:
                query = "INSERT INTO books_read VALUES(NULL, ?, ?, ?, ?, ?)"
                parameters = (self.book_title.get(), self.book_author.get(), self.book_genre.get(),
                              self.book_rating.get(), self.book_pages.get())
                self.query(query, parameters)
                self.book_title.delete(0, END)
                self.book_author.delete(0, END)
                self.book_genre.delete(0, END)
                self.book_rating.delete(0, END)
                self.book_pages.delete(0, END)
            else:
                query = "INSERT INTO books_to_read VALUES(NULL, ?, ?, ?, NULL, ?)"
                parameters = (self.book_title.get(), self.book_author.get(), self.book_genre.get(),
                              self.book_pages.get())
                self.query(query, parameters)
                self.book_title.delete(0, END)
                self.book_author.delete(0, END)
                self.book_genre.delete(0, END)
                self.book_pages.delete(0, END)

            messagebox.showinfo("Success", f"{self.book_title.get()} has been added successfully.", parent=opt)
        else:
            messagebox.showwarning("Warning", "Fields title, author and genre must not be empty.", parent=opt)
            self.list_books(main_table, data_key)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
