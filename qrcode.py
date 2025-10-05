import segno
from tkinter import *
from tkinter import ttk
import os

def show_message():
    qrcode = segno.make_qr(entry.get())
    qrcode.save(
        "qrcode.png",
        scale=5,
    )
    os.startfile(r'qrcode.png')

root = Tk()
root.title("qrcode tool")
root.geometry("250x200")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

root.mainloop()
