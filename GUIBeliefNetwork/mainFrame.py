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
button3 = Button(topFrame,text="Select")
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
def overlaps(x1, y1, x2, y2):
    '''returns overlapping object ids in ovals dict'''
    over_list = [] # make a list to hold overlap objects
    c_object = canvas.find_overlapping(x1, y1, x2, y2)
    if nodeList().__len__()!=0:
        for i in range(nodeList().__len__()):  # iterate over over dict
            for j in range(len(nodeList()[i])):
                if nodeList()[i][j] in c_object:      # if the node is in the overlap tuple
                    over_list.append(nodeList()[i][j])# add the node to the list
    return over_list
def drawNode(e):
    if len(overlaps(e.x-25,e.y-15,e.x+25,e.y+15))==0:
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
    if (len(overlaps(e.x-5,e.y-5,e.x+5,e.y+5))==1):
        toNode=nodeDic[overlaps(e.x-5,e.y-5,e.x+5,e.y+5)[0]]
        if fromNode is not toNode:
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")
            GA.addArrow(fromNode,toNode,arrow)
            canvas.bind("<Button-1>",ArcPoint1)
            LK.connect(fromNode,toNode,1)
            print(LK.dataLinking)
# listen to the first click for the line
def ArcPoint1(e):
    if len(overlaps(e.x-5,e.y-5,e.x+5,e.y+5))==1:
        global x,y,fromNode
        x,y=e.x,e.y
        fromNode=nodeDic[overlaps(e.x-5,e.y-5,e.x+5,e.y+5)[0]]
        root.config(cursor="cross")
        canvas.bind("<Button-1>",ArcPoint2)
# listen to the mouse action
def CreateArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",ArcPoint1)


def moveTo(e):

    nodeList[moveTheNode]=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)
    num=canvas.create_text(e.x,e.y,text=str(MN.get_n()))
# select the node
def select(e):
    if len(overlaps(e.x-5,e.y-5,e.x+5,e.y+5))==1:
        print(nodeDic[overlaps(e.x-5,e.y-5,e.x+5,e.y+5)[0]])
        global moveTheNode
        moveTheNode=nodeDic[overlaps(e.x-5,e.y-5,e.x+5,e.y+5)[0]]
        canvas.bind("<Button-1>",moveTo)

# Move the object
def Move(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",select)


def removeFromCanvas(e):
    if len(overlaps(e.x-5,e.y-5,e.x+5,e.y+5))==1:
        selectedNode=nodeDic[overlaps(e.x-5,e.y-5,e.x+5,e.y+5)[0]]
        print(selectedNode)
        GA.deleteNode(selectedNode)
        GA.deleteArrow(selectedNode)
        MN.remove(selectedNode)
        LK.deleteNode(selectedNode)
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
