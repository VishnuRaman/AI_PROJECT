import GuiArray,ManageNode,

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#pop up box - leads to canvas


#canvas
canvas = Canvas(root, width=1000,height=600,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

GA=GuiArray.guiArray(canvas)
MN=ManageNode.manageNode()

#create buttons
button1=Button(bottomFrame,text="Run")

button1.pack(side=BOTTOM)

#square entry boxes

def Run(event):
    root.config(cursor="")

    #produce the lines which lead to the next part for min


    #produce the lines which lead to the top max

    #run the algorithms for min and max and enter the data into the correct spaces on the gui


button1.bind("<Button-1>",Run)

root.mainloop()