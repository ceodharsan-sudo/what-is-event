from tkinter import *
root = Tk()
root.title("Length Converter")
def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text="Centimeters: " + str(cm))
entry = Entry(root)
entry.pack()
button = Button(root, text="Convert", command=convert)
button.pack()
result = Label(root, text="")
result.pack()
root.mainloop()