# Edited by Timo 2017/4/17
# This is the GUI for belief network
import ManageNode,Linking,GuiArray
from tkinter import *

size=6 #how many nodes allowed
root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# canvas
canvas = Canvas(root, width=500,height=300,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

GA=GuiArray.guiArray(size,canvas)
nodeList=GA.get_nodeList
LK=Linking.Linking(size)
MN=ManageNode.manageNode(size)


# create buttons
button1 = Button(topFrame,text="Create Node ")
button2 = Button(topFrame,text="Create Arc")
button3 = Button(topFrame,text="Move")
button4 = Button(topFrame,text="Delete")
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

# Used to store the operations

nodeDic={}


# methods called by buttons

# draw on the canvas
def drawNode(e):
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        node=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)
        nodeID=MN.inc()
        num=canvas.create_text(e.x,e.y,text=str(nodeID))
        set=[num,node]
        GA.addNode(set,nodeID)
        nodeDic[node]=nodeID

# listen to mouse action
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)
# listen to second click and draw the line on the canvas
def ArcPoint2(e):
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        toNode=nodeDic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.checkLinking(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")
            GA.addArrow(fromNode,toNode,arrow)
            canvas.bind("<Button-1>",ArcPoint1)
            LK.connect(fromNode,toNode,1)
            print(LK.dataLinking)
# listen to the first click for the line
def ArcPoint1(e):
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        global x,y,fromNode
        x,y=e.x,e.y
        fromNode=nodeDic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
        root.config(cursor="cross")
        canvas.bind("<Button-1>",ArcPoint2)
# listen to the mouse action
def CreateArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",ArcPoint1)


def moveTo(e):
    canvas.move(moveTheNode,e.x-x,e.y-y)
    canvas.move(moveTheNode+1,e.x-x,e.y-y)
    root.config(cursor="")
    canvas.bind("<Button-1>",Move)
# select the node
def select(e):
    global x,y
    x,y=e.x,e.y
    n=canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)
    if len(n)==2:
        root.config(cursor="exchange")
        global moveTheNode
        moveTheNode=n[0]
        canvas.bind("<Button-1>",moveTo)
    else:
        canvas.bind("<Button-1>",moveTo)

# Move the object
def Move(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",select)


def removeFromCanvas(e):
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        selectedNode=nodeDic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
        GA.deleteNode(selectedNode)
        GA.deleteArrow(selectedNode)
        LK.deleteNode(selectedNode)
        MN.remove(selectedNode)

        Delete

# Delete the node
def Delete(index):
    root.config(cursor="spider")
    canvas.bind("<Button-1>",removeFromCanvas)



def SetProperty(event):
    root.config(cursor="")
    print("SetProperty")

def ModifyProbabilityTable(event):
    print("ModifyProbabilityTable")

def Run(event):
    print("Run")




# listen to left click on each button
button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",Move)
button4.bind("<Button-1>",Delete)
button5.bind("<Button-1>",SetProperty)
button6.bind("<Button-1>",ModifyProbabilityTable)
button7.bind("<Button-1>",Run)


root.mainloop()
