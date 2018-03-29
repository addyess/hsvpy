import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Do not press this button", width=40)
button.pack(padx=10, pady=10)
clickcount = 0


def onclick(_):
    global clickcount
    clickcount += 1
    if clickcount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickcount == 2:
        button.configure(text="Gah! Next time, no more button.")
    else:
        button.pack_forget()


button.bind("<ButtonRelease-1>", onclick)
root.mainloop()
