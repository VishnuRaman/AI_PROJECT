from tkinter import *
import queue
# def sel():
#     selection = "You selected the option " + str(var.get())
#     label.config(text = selection)
#
# root = Tk()
# var = IntVar()
# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,command=sel)
# R1.pack( anchor = W )
#
# R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
#                 )
# R2.pack( anchor = W )
#
# R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
#                  command=sel)
# R3.pack( anchor = W)
#
# label = Label(root)
# label.pack()
# root.mainloop()
q=queue.PriorityQueue()
q.put((2,-1,'two'))
q.put((0,1,'zero'))
q.put((1,0,'one'))


print(q.get())
print(q.get())
print(q.get())
