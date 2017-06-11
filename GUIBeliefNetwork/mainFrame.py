import ManageNode,Linking,GuiArray,Algorithms
from tkinter import *

from GUIBeliefNetwork.Algorithms import algorithms

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
nodeList=GA.get_nodeList
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
button7 = Button(bottomFrame,text="Run",bg="red")
text1=Label(topFrame2,text="Start node")
startNode=Entry(topFrame2, width=2)
text2=Label(topFrame2,text="End node")
endNode=Entry(topFrame2, width=2)

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
            for v in LK.vert_dict:
                print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))



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

AL=Algorithms.algorithms(LK.vert_dict)
result=[]
def Run(event):
    root.config(cursor="")
    if algorithm=='BFS':
        print(AL.bfs(int(startNode.get()),int(endNode.get())))
    elif algorithm=='DFS':
        print(AL.dfs(int(startNode.get()),int(endNode.get())))

    #finds final path for bfs
    finalbfsP = AL.bfs(int(startNode.get()),int(endNode.get()))
    finalbfsPath = str(finalbfsP)

    #calls the queue for bfs
    queueBFS = AL.getQueueLog()

    #finds final path for dfs
    finaldfsP = AL.dfs(int(startNode.get()),int(endNode.get()))
    finaldfsPath = str(finaldfsP)

    #calls the stack for dfs
    stackDFS = AL.getStackLog()

    # canvas

    if not result:#if result is empty then create the labels
        resultcanvas = Canvas(root, width=800, height=100, bg="white")
        resultcanvas.pack(expand=1, fill=BOTH)

        if algorithm=='BFS':

            #final path label
            finalPathLabel=Label(resultcanvas,text="Final path: ")
            finalPathLabel.grid(column=0,row=0)

            #final path for the bfs
            bfsPath = Label(resultcanvas, text=finalbfsPath)
            bfsPath.grid(column=1,row=0)

            #now expanding path label
            expandLabel=Label(resultcanvas,text="Now expanding: ")
            expandLabel.grid(column=0,row=1)

            #node being expanded bfs
            expandString = Label(resultcanvas, text=str(queueBFS[-1][0]))
            expandString.grid(column=1,row=1)

            #queue label
            queueLabel=Label(resultcanvas,text="Queue: ")
            queueLabel.grid(column=0,row=2)

            #bfs queue
            queueString = Label(resultcanvas,text=str(queueBFS[-1][-1]))
            queueString.grid(column=1,row=2)

            #visited label
            visitedLabel=Label(resultcanvas,text="Visited: ")
            visitedLabel.grid(column=0,row=3)

            #nodes that are visited bfs
            visitedString = Label(resultcanvas, text=str(AL.getVisited()))
            visitedString.grid(column=1,row=3)

            result.extend([resultcanvas,finalPathLabel,expandLabel,visitedLabel])
        elif algorithm=='DFS':
            print('dfs')
    else:
        # final path label
        finalPathLabel = Label(resultcanvas, text="Final path: ")
        finalPathLabel.grid(column=0, row=0)

        # final path for the dfs
        dfsPath = Label(resultcanvas, text=finaldfsPath)
        dfsPath.grid(column=1, row=0)

        # now expanding path label
        expandLabel = Label(resultcanvas, text="Now expanding: ")
        expandLabel.grid(column=0, row=1)

        # node being expanded bfs
        expandString = Label(resultcanvas, text=str(stackDFS[-1][0]))
        expandString.grid(column=1, row=1)

        # stack label
        stackLabel = Label(resultcanvas, text="Stack: ")
        stackLabel.grid(column=0, row=2)

        # dfs stack
        stackString = Label(resultcanvas, text=str(stackDFS[-1][-1]))
        stackString.grid(column=1, row=2)

        # visited label
        visitedLabel = Label(resultcanvas, text="Visited: ")
        visitedLabel.grid(column=0, row=3)

        # nodes that are visited bfs
        visitedString = Label(resultcanvas, text=str(AL.getVisited()))
        visitedString.grid(column=1, row=3)

        # print('dfs')

        result.append((resultcanvas,finalPathLabel,expandLabel,visitedLabel))



    # #order of expansion dialogue box
    # expandPbox = resultcanvas.create_rectangle(5, 70, 608, 100)
    # resultcanvas.create_text(73, 85, text="Order of Expansion: ")  # + the array of results from the alg)  # listen to left click on each button



    #if the boxes appeared once then dont let appear a second time

    # visible = True
    #
    # if visible:
    #    removeFromCanvas(resultcanvas)

    #next task = create error messages for when user does wrong thing eg enters goal node higher than nodes shown


button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",Move)
button4.bind("<Button-1>",Delete)
button5.bind("<Button-1>",SetProperty)
button6.bind("<Button-1>",ModifyProbabilityTable)
button7.bind("<Button-1>",Run)


root.mainloop()
