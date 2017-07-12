from io import TextIOWrapper

import beliefManageNode,beliefLinking,beliefGuiStore

import pickle
from tkinter import *
# import Tkinter
import tkinter.filedialog

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# canvas
canvas = Canvas(root, width=1000,height=600,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

#creating objects - link to the classes in the folder
GA=beliefGuiStore.beliefGuiStore(canvas)
MN=beliefManageNode.beliefManageNode()
LK=beliefLinking.Graph()

#drop down list

# create buttons
button1 = Button(topFrame,text="Create Node")
button2 = Button(topFrame,text="Create Link")
button3 = Button(topFrame,text="Move Node")
button4 = Button(topFrame,text="Delete Node")
button7 = Button(topFrame2,text="Previous step",bg="light blue")
button8 = Button(topFrame2,text="Next step",bg="light blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)

# methods called by buttons
node_id_Dic={}
# draw on the canvas
def drawNode(e):
    #if not means if it's empty then do operation

    #canvas enclosed creates a space around where you click and checks no other objects are in that area
    #if objects are present it wont create a node there

    #if is empty then creates the oval

    if not canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105):
        oval=canvas.create_oval(e.x-50,e.y-40,e.x+50,e.y+40)
      #MN.inc means increase that method by 1 as new node was created
        nodeID=MN.inc()
        num=canvas.create_text(e.x,e.y,text=str(nodeID))
        #num = the number label for the node eg 0,1,2
        #node = the oval shape
        GUIset=[num,oval,{}]#number object / oval object / dictionary for linking
        node_id_Dic[oval]=nodeID
        GA.addNode(GUIset,nodeID)
        LK.add_vertex(nodeID)

# listen to mouse action
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)
# listen to second click and draw the line on the canvas
def ArcPoint2(e):
    if len(canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105))==2:
        toNode=node_id_Dic[canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")#fill="turquoise" can change color
            #use -->  canvas.itemconfig(arrow,fill="red") <-- to change color after created

            GA.addArrow(fromNode, toNode, arrow)

            # #this method produces the connection and provides a cost

            LK.add_edge(fromNode,toNode)

            canvas.bind("<Button-1>",ArcPoint1)
# listen to the first click for the line
def ArcPoint1(e):
    #==2 means must only have one node and node number in that range to catch the arrow else cant click
    #provides 1st number for the method above
    if len(canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105))==2:
    #global equivalent of instance variable
    #used this so its able to be used by different methods
    #x,y =location and fromNode = the id of the node you pick up - the one you draw FROM
        global x,y,fromNode
        x,y=e.x,e.y
        fromNode=node_id_Dic[canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105)[0]]
        root.config(cursor="cross")
        canvas.bind("<Button-1>",ArcPoint2)
# listen to the mouse action
def CreateArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",ArcPoint1)

def moveTo(e):
    #for both lines below so x = location of the node you want to move
    #e.x = location you want to move it to
    #subtract these to get the distance to move the node by

    #selects the location of the node you want to move
    canvas.move(moveTheNode,e.x-x,e.y-y)

    #+1 moves the number associated with that node ie 0,1,2 etc
    canvas.move(moveTheNode+1,e.x-x,e.y-y)

    # move the arrows
    for i in moveArrowTails:
        canvas.move(moveArrowTails[i],e.x-x,e.y-y)

    root.config(cursor="")
    canvas.bind("<Button-1>",moveFrom)
# select the node
def moveFrom(e):
    global x,y
    x,y=e.x,e.y
    n=canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)
    if len(n)==2:
        root.config(cursor="exchange")
        global moveTheNode, moveArrowTails, moveArrowHeads
        #[0] is the ID of the node you want to move
        moveTheNode=n[0]
        moveArrowTails=GA.nodeList[node_id_Dic[n[0]]][2]
        moveArrowHeads={}
        for i in GA.nodeList:
            if node_id_Dic[n[0]] in GA.nodeList[i][2]:
                moveArrowHeads[i]=GA.nodeList[i][2][node_id_Dic[n[0]]]

        #once you click that node, then moves to moveTo method above and moves node
        canvas.bind("<Button-1>",moveTo)
    else:
        canvas.bind("<Button-1>",moveTo)

# Move the object
def Move(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",moveFrom)


def removeFromCanvas(e):
    #checks range to see if both node and number label are in the range where you clicked
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        #[0] is the node ID thats selected
        selectedNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
        GA.deleteNode(selectedNode)
        LK.delete_vertex(selectedNode)
        #this removes the deleted node and arrow out of the array and stores the number of that node into a priority queue
        #so takes no. from top of priority queue when creating next node
        MN.remove(selectedNode)

        # for v in LK.vert_dict:#####
        # print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))
        Delete  #takes you to delete def below

# Delete the node
def Delete(event):
    root.config(cursor="spider")
    canvas.bind("<Button-1>",removeFromCanvas)


def Run(): #next step button produces this so method below
    # canvas - make pop up probability table like video
        resultcanvas = Frame(root)
        resultcanvas.pack(side=BOTTOM)

def NextStep(e):
    #global variable because otherwise cant be called in new methods as it
    #would be a local variable
    #xth is 1st,2nd,3rd,4th etc
    global xTh
    # if xTh<len(AL.getQsLog())-1:
    #     #add 1 to go forward
    #     xTh+=1
    root.update()
def PreStep(e):
    global xTh

    root.update()

button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",Move)
button4.bind("<Button-1>",Delete)
button7.bind("<Button-1>",PreStep)
button8.bind("<Button-1>",NextStep)


root.mainloop()
