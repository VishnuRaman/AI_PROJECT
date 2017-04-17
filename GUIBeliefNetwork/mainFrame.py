# Edited by Timo 2017/4/17
# This is the GUI for belief network
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# create buttons
button1 = Button(topFrame,text="Create Node ")
button2 = Button(topFrame,text="Create Arc")
button3 = Button(topFrame,text="Move")
button4 = Button(topFrame,text="Undo")
button5 = Button(topFrame,text="Set Property")
button6 = Button(topFrame,text="Modify Probability Table",bg="light green")
button7 = Button(bottomFrame,text="Run",bg="red")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=BOTTOM)

# Two global variables used to store the operations
nodeList=[]
arcList=[]
# methods called by buttons

# draw on the canvas
def drawNode(e):
    node=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)
    nodeList.insert(0,node)
# listen to mouse action
def CreateNode(event):
    canvas.bind("<Button-1>",drawNode)
# listen to second click and draw the line on the canvas
def ArcPoint2(e):
   point= canvas.create_oval(e.x-2,e.y-2,e.x+2,e.y+2)
   arcList.insert(0,point)
   arc = canvas.create_line(x,y,e.x,e.y)
   arcList.insert(0,arc)
   nodeList.insert(0,arcList[0])
   canvas.bind("<Button-1>",ArcPoint1)
# listen to the first click for the line
def ArcPoint1(e):
    global x,y
    x,y=e.x,e.y
    point=canvas.create_oval(x-2,y-2,x+2,y+2)
    arcList.insert(0,point)
    canvas.bind("<Button-1>",ArcPoint2)
# listen to the mouse action
def CreateArc(event):
    canvas.bind("<Button-1>",ArcPoint1)

# Move the object
def Move(event):
    print("Select")

# Delete the previous operation
def Delete(event):
    if nodeList.__len__()>0:
        if arcList.__len__()==0 or nodeList[0] != arcList[0]:
            canvas.delete(nodeList[0])
            nodeList.remove(nodeList[0])
        else:
            nodeList.remove(nodeList[0])
            for num in range(0,3):
                canvas.delete(arcList[0])
                arcList.remove(arcList[0])


def SetProperty(event):
    print("SetProperty")

def ModifyProbabilityTable(event):
    print("ModifyProbabilityTable")

def Run(event):
    print("Run")


# canvas
canvas = Canvas(root, width=500,height=300,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

# listen to left click on each button
button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",Move)
button4.bind("<Button-1>",Delete)
button5.bind("<Button-1>",SetProperty)
button6.bind("<Button-1>",ModifyProbabilityTable)
button7.bind("<Button-1>",Run)


root.mainloop()
