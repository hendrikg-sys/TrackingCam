import tkinter as tk

master = tk.Tk()

status = tk.IntVar(0)


def callback_next(event):
    v = status.get()
    status.set(v + 1)
    print(status.get())


def callback_back(event):
    v = status.get()
    status.set(v - 1)
    print(status.get())


next = tk.Button(master, text="next")

back = tk.Button(master, text="back")
back.grid(row=0)
next.grid(row=1)

next.bind("<Button-1>", callback_next)
back.bind("<Button-1>", callback_back)


master.mainloop()
