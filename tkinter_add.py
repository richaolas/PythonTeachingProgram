import tkinter

def doAdd():
    val1 = int(a.get())
    val2 = int(b.get())
    resultVar.set(str(val1 + val2))

root = tkinter.Tk()
a = tkinter.Entry(root, width=20)
a.pack(side=tkinter.LEFT)

add = tkinter.Label(text='+')
add.pack(side=tkinter.LEFT)

b = tkinter.Entry(root, width=20)
b.pack(side=tkinter.LEFT)

equal = tkinter.Button(text='=', command=doAdd)
equal.pack(side=tkinter.LEFT)

resultVar = tkinter.StringVar()
result = tkinter.Entry(root, width=20, textvariable=resultVar)
result.pack(side=tkinter.LEFT)

root.mainloop()
