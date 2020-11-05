from tkinter import *
from tkinter import ttk


class App:
    def __init__(self, root):
        self.win = root
        self.win.title("Book Register App")

        # Create options for "books read" and "books to read"
        frame_main = LabelFrame(self.win, text="Select an option")
        frame_main.grid(row=0, column=0, columnspan=2, padx=70, pady=40)

        # Select options
        books_read = Button(frame_main, text="Books Read", fg="gray10", bg="gold", padx=65, pady=30)
        books_read.grid(row=0, column=0, padx=5, pady=5)

        books_to_read = Button(frame_main, text="Books To Read", fg="gray10", bg="goldenrod", padx=65, pady=30)
        books_to_read.grid(row=0, column=1, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
