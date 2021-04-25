import tkinter as tk

root = tk.create()
root.title('first')
button = tk.Button(root, text='Ok', width=25, command = root.destroy)
button.pack()
root.mainloop()