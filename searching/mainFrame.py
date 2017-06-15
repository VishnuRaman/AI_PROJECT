import ManageNode,Linking,GuiArray,Algorithms
from tkinter import *

from searching.Algorithms import algorithms

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# canvas
canvas = Canvas(root, width=800,height=400,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

#creating objects - link to the classes in the folder
GA=GuiArray.guiArray(canvas)
#node list calls list from the object GA which references Gui Array class
MN=ManageNode.manageNode()
LK=Linking.Graph()


#drop down list
myMenu = Menu(root)
root.config(menu=myMenu)


def chooseBFS():
    global algorithm
    algorithm='BFS'

def chooseDFS():
    global algorithm
    algorithm='DFS'

editMenu = Menu(myMenu)
myMenu.add_cascade(label="Run by", menu=editMenu)
editMenu.add_command(label="BFS", command=chooseBFS)
editMenu.add_command(label="DFS", command=chooseDFS)

# create buttons
button1 = Button(topFrame,text="Create Node ")
button2 = Button(topFrame,text="Create Arc")
button3 = Button(topFrame,text="Move")
button4 = Button(topFrame,text="Delete")
button5 = Button(topFrame,text="Set Property")
button6 = Button(topFrame,text="Modify Probability Table",bg="light green")
button7 = Button(bottomFrame,text="Run",bg="green")
text1=Label(topFrame2,text="Start node")
startNode=Entry(topFrame2, width=2)
text2=Label(topFrame2,text="End node")
endNode=Entry(topFrame2, width=2)
text3=Label(topFrame2,text="Delay seconds")
delay=Entry(topFrame2, width=2)
button8 = Button(topFrame2,text="<<",bg="light blue")
button9 = Button(topFrame2,text=">>",bg="light blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=BOTTOM)
text1.pack(side=LEFT)
startNode.pack(side=LEFT)
text2.pack(side=LEFT)
endNode.pack(side=LEFT)
text3.pack(side=LEFT)
delay.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)

# methods called by buttons
node_id_Dic={}
# draw on the canvas
def drawNode(e):
    #if not means if it's empty then do operation
    #canvas enclosed creates a space around where you click and checks no other objects are in that area
    #if objects are present it wont create a node there
    #if is empty then creates the oval
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        oval=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)
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
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        toNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")#fill="turquoise" can change color
            #use -->  canvas.itemconfig(arrow,fill="red") <-- to change color after created

            GA.addArrow(fromNode,toNode,arrow)
            #this method produces the connection and provides a cost
            LK.add_edge(fromNode,toNode,1)
            #inf means infinity so hasnt been assigned a cost/value yet
            #this one shows the individual costs of travel between nodes (the weight variable in the class)

            # for v in LK.vert_dict:#####
            #     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))

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

        # for v in LK.vert_dict:#####
        #     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v].adjacent]))
        Delete #takes you to delete def below

# Delete the node
def Delete(event):
    root.config(cursor="spider")
    canvas.bind("<Button-1>",removeFromCanvas)

def SetProperty(event):
    root.config(cursor="")
    print("SetProperty")

def ModifyProbabilityTable(event):
    print("ModifyProbabilityTable")


AL=Algorithms.algorithms(LK.vert_dict)
#result variable default setting = empty so resultcanvas is printed
result=[]

def Run(event):
    root.config(cursor="")
    global finalPath,xTh,delaytime
    xTh=0

    finalPath = AL.bdfs(int(startNode.get()),int(endNode.get()),algorithm)

    if not delay.get():
        display()
    else:
        delaytime=int(delay.get())
        for i in range(len(AL.getVisitedLog())):
            xTh=i
            display()
            root.update()
            root.after(delaytime*1000)





def display():
    # canvas
    if not result:#if result is empty then create the labels - ie not shown already
        resultcanvas = Frame(root)
        resultcanvas.pack(side=BOTTOM)

        # buttonDisp = Button(resultcanvas,text="disp",bg="light green")
        # buttonDisp.grid(column=0,row=4)

        if algorithm=='BFS':
            #queue label
            qsLabel=Label(resultcanvas,bg="yellow",text="Queue: ")
            qsLabel.grid(column=0,row=2,sticky=W)
        elif algorithm=='DFS':
            # stack label
            qsLabel = Label(resultcanvas,bg="yellow", text="Stack: ")
            qsLabel.grid(column=0, row=2,sticky=W)
        #final path label
        finalPathLabel=Label(resultcanvas, bg="red", text="Final path: ")
        finalPathLabel.grid(column=0,row=0,sticky=W)
        #final path for the bfs
        finalPathValue = Label(resultcanvas, text=str(finalPath))
        finalPathValue.grid(column=1,row=0,sticky=W)

        #now expanding path label
        expandLabel=Label(resultcanvas,bg="light pink",text="Now expanding: ")
        expandLabel.grid(column=0,row=1,sticky=W)
        #node being expanded bfs
        expandValue = Label(resultcanvas, text=str(AL.getQsLog()[xTh][0]))
        expandValue.grid(column=1,row=1,sticky=W)

        qsValue = Label(resultcanvas,text=str(AL.getQsLog()[xTh][-1]))
        qsValue.grid(column=1,row=2,sticky=W)

        #visited label
        visitedLabel=Label(resultcanvas,bg="brown",text="Visited: ")
        visitedLabel.grid(column=0,row=3,sticky=W)
        #nodes that are visited bfs
        visitedValue = Label(resultcanvas, text=str(AL.getVisitedLog()[xTh]))
        visitedValue.grid(column=1,row=3,sticky=W)
        #notifies the result variable its no longer empty
        result.extend([finalPathValue,expandValue,qsLabel,qsValue,visitedValue])
    else:
        result[0]['text']=str(finalPath)
        if algorithm=='BFS':
            result[2]['text']="Queue: "
        elif algorithm=='DFS':
            result[2]['text']="Stack: "
        result[1]['text']=str(AL.getQsLog()[xTh][0])#expandValue
        result[3]['text']=str(AL.getQsLog()[xTh][1])#qsValue
        result[4]['text']=str(AL.getVisitedLog()[xTh])#visitedValue

    if AL.getQsLog()[xTh][0]==finalPath[-1]:#meet the goal then color the final path
        for a in range(len(finalPath)-1):
            canvas.itemconfig(GA.nodeList[finalPath[a]][2][finalPath[a+1]],fill="red")#final path arrow

    for n in GA.nodeList:
        if n in AL.getVisitedLog()[xTh]:#visited oval
            canvas.itemconfig(GA.nodeList[n][1],fill="brown")
            if n == AL.getQsLog()[xTh][0]:#expanding oval
                canvas.itemconfig(GA.nodeList[n][1],fill="light pink")#now expending oval
        elif n in AL.getQsLog()[xTh][1]:#ovals in queue or stack
            canvas.itemconfig(GA.nodeList[n][1],fill="yellow")
        else:
            canvas.itemconfig(GA.nodeList[n][1],fill="")

        if AL.getQsLog()[xTh][0]!=finalPath[-1]:#meet the goal then color the final path
            for a in GA.nodeList[n][2].values():
               canvas.itemconfig(a,fill="black")#final path arrow


        # for i in the range of range= number of final path nodes
        for i in range(len(finalPath) - 1):
            # nodelist is the dictionary containing all the GUI objects
            # the 1st final path references the start node of the link and the 2nd references the
            # goal node of the link
            # the [2] is the 3rd object (starts at 0) in the nodelist dictionary
            # the +1 allows you to get the next object as it is currently out of the range
            canvas.itemconfig(GA.nodeList[finalPath[i]][2][finalPath[i + 1]], fill="turquoise")

            # canvas.itemconfig(arrow,fill="turquoise")


def NextStep(e):
    global xTh
    if xTh<len(AL.getQsLog())-1:
        xTh+=1
        display()
        root.update()
def PreStep(e):
    global xTh
    if xTh>0:
        xTh-=1
        display()
        root.update()

button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",Move)
button4.bind("<Button-1>",Delete)
button5.bind("<Button-1>",SetProperty)
button6.bind("<Button-1>",ModifyProbabilityTable)
button7.bind("<Button-1>",Run)
button8.bind("<Button-1>",PreStep)
button9.bind("<Button-1>",NextStep)


root.mainloop()
