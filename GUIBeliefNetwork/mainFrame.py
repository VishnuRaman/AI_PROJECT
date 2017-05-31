# Edited by Timo 2017/4/17
import ManageNode,Linking,GuiArray
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# canvas
canvas = Canvas(root, width=500,height=300,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

#creating objects - link to the classes in the folder
GA=GuiArray.guiArray(canvas)
#node list calls list from the object GA which references Gui Array class
nodeList=GA.get_nodeList
MN=ManageNode.manageNode()
LK=Linking.Graph()


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


# methods called by buttons
node_id_Dic={}
# draw on the canvas
def drawNode(e):
    #if not means if it's empty then do operation
    #canvas enclosed creates a space around where you click and checks no other objects are in that area
    #if objects are present it wont create a node there
    #if is empty then creates the oval
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        node=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)
      #MN.inc means increase that method by 1 as new node was created
        nodeID=MN.inc()
        num=canvas.create_text(e.x,e.y,text=str(nodeID))
        #num = the number label for the node eg 0,1,2
        #node = the oval shape
        GUIset=[num,node,{}]
        node_id_Dic[node]=nodeID
        GA.addNode(GUIset,nodeID)
        LK.add_vertex(nodeID)

# listen to mouse action
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)
# listen to second click and draw the line on the canvas
def ArcPoint2(e):
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        toNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")
            GA.addArrow(fromNode,toNode,arrow)
            #this method produces the connection and provides a cost
            LK.add_edge(fromNode,toNode,1)
            #inf means infinity so hasnt been assigned a cost/value yet
            #this one shows the individual costs of travel between nodes (the weight variable in the class)
            for v in LK:
                print (str(v.get_id())+' is connected to '+str(LK.vert_dict[v.get_id()]))

            canvas.bind("<Button-1>",ArcPoint1)
# listen to the first click for the line
def ArcPoint1(e):
    #==2 means must only have one node and node number in that range to catch the arrow else cant click
    #provides 1st number for the method above
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
    #global equivalent of instance variable
    #used this so its able to be used by different methods
    #x,y =location and fromNode = the id of the node you pick up - the one you draw FROM
        global x,y,fromNode
        x,y=e.x,e.y
        fromNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
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
        for v in LK:
            print (str(v.get_id())+' is connected to '+str(LK.vert_dict[v.get_id()]))#########
        Delete #takes you to delete def below

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
