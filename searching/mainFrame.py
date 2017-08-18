from io import TextIOWrapper
from tkinter.simpledialog import askstring

import ManageNode,Linking,GuiArray,Algorithms

import pickle
from tkinter import *
# import Tkinter
import tkinter.filedialog
import tkinter.messagebox


from searching.Algorithms import algorithms
global iter
iter = False
##This produces the frame dimensions of the window we are creating.
#On this window we shall create a canvas where all our visualisations will be drawn.
root = Tk()
##This refers to the top frame which the buttons can be viewed on.
topFrame = Frame(root)
topFrame.pack(fill=X)
##This refers to the second frame which the second row of buttons can be viewed on.
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
##This referst to the bottom frame produced to display the results.
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
##This is the canvas on which all the visualisations are drawn.
#The background is set to a different colour to distinguish it from the other frames.
canvas = Canvas(root, width=800,height=400,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

##These variables are to be used as a reference, when calling methods or objects
# from these classes.
GA=GuiArray.guiArray(canvas)
MN=ManageNode.manageNode()
LK=Linking.Graph()

##This creates a drop down menu list
myMenu = Menu(root)
root.config(menu=myMenu)

##This method is used to save the graphs produced by the user as a .pkl file to be
# loaded when the user returns to the interface at a later point.
def saveFile():
    fileFormats = [('Pickle', "*.pkl")]
    ##This produces a dialog box allowing the user to choose where to save the file on their system.
    filename = tkinter.filedialog.asksaveasfilename(filetypes=fileFormats)

    ##Everything the user has placed onto the canvas is saved into the GA.nodeList dictionary.
    #Everything in this dictionary is called into a new dictionary and this new dictionary is used
    #by pickle.dump and saved into a .pkl file.
    #Once saved, the method is completed and the dialog box is closed.
    if filename:
        newDict = GA.nodeList
        output = open(filename + '_g.pkl', 'wb')
        pickle.dump(newDict, output)
        output.close()

##This is the method used to open a saved .pkl file onto the canvas.

def loadFile():
    fileFormats = [('Pickle', "*.pkl")]
    ##This produces a dialog box displaying the .pkl files saved, for the user to pick one for loading
    openFilename = tkinter.filedialog.askopenfile(filetypes=fileFormats).name

    ##file assigns itself to the filename clicked by the user and is read by the method.
    #The file is read and the dictionary values which were saved in that file are loaded into the dictionary for the canvas which
    #is currently open.
    #Once the method is completed, the reader closes and the dialog box disappears.
    file = open(openFilename, 'rb')
    dict = pickle.load(file)
    file.close()
    GA.nodeList=dict

##This produces a drop down menu titled "File" which allows the user to have access to the save and load options.
fileMenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Load", command=loadFile)

##These are the methods to be called by the drop down menu used for searches.
def chooseBFS():
    global algorithm
    algorithm='BFS'

def chooseDFS():
    global algorithm
    algorithm='DFS'

def chooseUCS():
    global algorithm
    algorithm='UCS'

def chooseAstar():
    global algorithm
    algorithm ='aStar'

##This produces a drop down menu titled "Searches" which allows the user to select a particular search algorithm.
editMenu = Menu(myMenu)
myMenu.add_cascade(label="Searches", menu=editMenu)
editMenu.add_command(label="BFS", command=chooseBFS)
editMenu.add_command(label="DFS", command=chooseDFS)
editMenu.add_command(label="UCS", command=chooseUCS)
editMenu.add_command(label="A*", command=chooseAstar)


##These are the methods to be called by the drop down menu used for iterative searches.
def chooseIBFS():
    global algorithm
    algorithm='BFS'

    global iter
    iter = True

def chooseIDFS():
    global algorithm
    algorithm='DFS'

    global iter
    iter = True

def chooseIUCS():
    global algorithm
    algorithm='UCS'

    global iter
    iter = True

def chooseIaStar():
    global algorithm
    algorithm='aStar'

    global iter
    iter = True

##This produces a drop down menu titled "Iterative Searches" which allows the user to select a particular iterative search algorithm.
editMenu = Menu(myMenu)
myMenu.add_cascade(label="Iterative Searches", menu=editMenu)
editMenu.add_command(label="BFS", command=chooseIBFS)
editMenu.add_command(label="DFS", command=chooseIDFS)
editMenu.add_command(label="UCS", command=chooseIUCS)
editMenu.add_command(label="A*", command=chooseIaStar)

##The following creates all the buttons, entry boxes and text labels seen on the interface
button1 = Button(topFrame,text="Create Node ")
button2 = Button(topFrame,text="Create Arrows")
button3 = Button(topFrame,text="Create Arrows with costs")
button9 = Button(topFrame,text="Add Heuristics")
button4 = Button(topFrame,text="Move")
button5 = Button(topFrame,text="Delete")
button6 = Button(bottomFrame,text="Run")
button7 = Button(topFrame2,text="<<",bg="light blue")
button8 = Button(topFrame2,text=">>",bg="light blue")
text1=Label(topFrame2,text="Start Node")
startNode=Entry(topFrame2, width=2)
text2=Label(topFrame2,text="End Node")
endNode=Entry(topFrame2, width=2)
text3=Label(topFrame2,text="Delay Seconds")
delay=Entry(topFrame2, width=2)
text4=Label(topFrame2,text="Maximum Number of Rows to Search")
it = Entry(topFrame2, width=2)

##This positions all the buttons, entry boxes and text labels seen on the interface.
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button9.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=BOTTOM)
text1.pack(side=LEFT)
startNode.pack(side=LEFT)
text2.pack(side=LEFT)
endNode.pack(side=LEFT)
text3.pack(side=LEFT)
delay.pack(side=LEFT)
text4.pack(side=LEFT)
it.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)
##########################draw grid button - enter row and column no.s
##########################then do like belief net so where they clicked to get ask boxes is top left corner

########################### methods called by buttons
node_id_Dic={}
########################## draw on the canvas

##This method draws the node oval and its ID number onto where the user has clicked on the canvas
def drawNode(e):

    ##If the area encircling where the user has clicked, does not contain an object already, then create an oval and store this with an ID value.
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        oval=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)

        nodeID=MN.inc()
        num=canvas.create_text(e.x,e.y,text=str(nodeID))
###########num = the number label for the node eg 0,1,2
###########node = the oval shape
        GUIset=[num,oval,{}]###################number object / oval object / dictionary for linking
        coordinateSet=[nodeID,e.x,e.y]
        node_id_Dic[oval]=nodeID
        GA.addNode(GUIset,nodeID)
##################ADD EXPLANATIONS FOR THESE
        GA.addCoords(coordinateSet,nodeID)
        LK.add_vertex(nodeID)

##This method listens for the mouse click and upon this it will call the method to draw the node.
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)


###############
################
################
#EXPLAIN THIS IS WITHOUT COSTS BUT WEIGHT =1 FOR ALGS TO WORK AND UNIFORM COSTS
def ArcPoint2(e):
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        toNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")

            weight = 1
            GA.addArrow(fromNode, toNode, arrow, weight)

            # #this method produces the connection and provides a cost

            LK.add_edge(fromNode,toNode,weight)
            #inf means infinity so hasnt been assigned a cost/value yet
            #this one shows the individual costs of travel between nodes (the weight variable in the class)


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

def ArcCostPoint2(e):
        if len(canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)) == 2:
            toNode = node_id_Dic[canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)[
                0]]  # the node is created before num so it is at [0]
            if (fromNode is not toNode) and (LK.check_edge_existed(fromNode, toNode) == False):
                root.config(cursor="")
                arrow = canvas.create_line(x, y, e.x, e.y, arrow="last")
                # use -->  canvas.itemconfig(arrow,fill="red") <-- to change color after created

                # need to change this so text corresponds to the custom entry made by the user
                # do like belief net button
                value = askstring('value', 'Please enter a cost')

                if value == None:
                    value = 0

                weight = int(value)

                if weight is None:
                    print("aaa")

                weightLabel = canvas.create_text(0.5 * (x + e.x), 0.5 * (y + e.y) - 10, text=value)

                GA.addArrow(fromNode, toNode, arrow, weightLabel)

                # #this method produces the connection and provides a cost

                LK.add_edge(fromNode, toNode, weight)
                # inf means infinity so hasnt been assigned a cost/value yet
                # this one shows the individual costs of travel between nodes (the weight variable in the class)


                canvas.bind("<Button-1>", ArcPoint1)

def ArcCostPoint1(e):
        # ==2 means must only have one node and node number in that range to catch the arrow else cant click
        # provides 1st number for the method above
        if len(canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)) == 2:
            # global equivalent of instance variable
            # used this so its able to be used by different methods
            # x,y =location and fromNode = the id of the node you pick up - the one you draw FROM
            global x, y, fromNode
            x, y = e.x, e.y
            fromNode = node_id_Dic[canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)[0]]
            root.config(cursor="cross")
            canvas.bind("<Button-1>", ArcCostPoint2)

def CreateCostArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>", ArcCostPoint1)

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
        #     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))
        Delete #takes you to delete def below

# Delete the node
def Delete(event):
    root.config(cursor="spider")
    canvas.bind("<Button-1>",removeFromCanvas)


AL=Algorithms.algorithms(LK.vert_dict)
#result variable default setting = empty so resultcanvas is printed
result=[]

def AddHeu(e):
    #find the node it clicked on
    #add heuristic to this node
    #store this info somehow
    x = e.x
    y = e.y

    heuLabel= askstring('value', 'Please enter a heuristic')

    heu = int(float(heuLabel)) ############check if this is int or float

    print(heu)

    for i in GA.coordList:
        if GA.coordList[i]:
            if x > GA.coordList[i][1] - 20 and x < GA.coordList[i][1] + 20:


                if y < GA.coordList[i][2] + 10 and y > GA.coordList[i][2] - 10:
                    print("colour test" + str(i))
                    heuset=[heu]
                    GA.addHeu(heuset,i)

def CreateHeu(event):
    root.config(cursor="")
    canvas.bind("<Button-1>", AddHeu)


def Run(event):
    root.config(cursor="")
    global finalPath,xTh,delaytime,iter
    xTh=0
    if iter == True and algorithm in ('BFS', 'DFS', 'UCS', 'aStar'): #algorithm mentioned here =
        # print('ffffff')
        finalPath = AL.iterative(int(startNode.get()),int(endNode.get()),algorithm,int(it.get())) #make a box to gain user input from )
    elif iter==False and algorithm in ('UCS','aStar'):
        # print('gggg')
        finalPath = AL.ucsAStar(int(startNode.get()),int(endNode.get()),algorithm)
    elif iter==False and algorithm in ('BFS', 'DFS'):
        # print('hhhh')
        finalPath = AL.bdfs(int(startNode.get()),int(endNode.get()),algorithm)

    # else:
    #     tkinter.messagebox('error','Please select a search')

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

        if iter==False and algorithm=='BFS':
            #queue label
            qsLabel=Label(resultcanvas,bg="yellow",text="Queue: ")
        elif iter==True and algorithm=='BFS':
            qsLabel=Label(resultcanvas,bg="yellow",text="Queue: ")
        elif iter==False and algorithm=='DFS':
            # stack label
            qsLabel = Label(resultcanvas,bg="yellow", text="Stack: ")
        elif iter==True and algorithm=='DFS':
            qsLabel = Label(resultcanvas,bg="yellow", text="Stack: ")
        elif iter==False and algorithm=='UCS':
            #priotity queue label
            qsLabel=Label(resultcanvas,bg="yellow",text="Priority Queue: ")
        elif iter==True and algorithm=='UCS':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")
        elif iter==False and algorithm=='aStar':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")
        elif iter==True and algorithm=='aSTar':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")

        qsLabel.grid(column=0,row=2,sticky=W)
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
        elif algorithm=='UCS':
            result[2]['text']="Priority queue: "
        result[1]['text']=str(AL.getQsLog()[xTh][0])#expandValue
        result[3]['text']=str(AL.getQsLog()[xTh][1])#qsValue
        result[4]['text']=str(AL.getVisitedLog()[xTh])#visitedValue

    if finalPath == None:
        print("No final path found")

    if not finalPath is None:
        # if AL.getQsLog()[xTh][0]==finalPath[-1]:#meet the goal then color the final path
            print("ddddddd")
        # for i in the range of range= number of final path nodes
        #     for a in range(len(finalPath)-1):
        #         print("hhhhhhh")
                # canvas.itemconfig(GA.nodeList[finalPath[a]][2][finalPath[a+1]][0],fill="red")#final path arrow
                # nodelist is the dictionary containing all the GUI objects
                # the 1st final path references the start node of the link and the 2nd references the
                # goal node of the link
                # the [2] is the 3rd object (starts at 0) in the nodelist dictionary
                # the +1 allows you to get the next object as it is currently out of the range

    for n in GA.nodeList:
        if n in AL.getVisitedLog()[xTh]:#visited oval
            canvas.itemconfig(GA.nodeList[n][1],fill="brown")
            if n == AL.getQsLog()[xTh][0]:#expanding oval
                canvas.itemconfig(GA.nodeList[n][1],fill="light pink")#now expending oval
        elif n in AL.getQsLog()[xTh][1]:#ovals in queue or stack
            canvas.itemconfig(GA.nodeList[n][1],fill="yellow")
        else:
            canvas.itemconfig(GA.nodeList[n][1],fill="")

        if finalPath == None:
            print("have not found final path yet")

        elif AL.getQsLog()[xTh][0] == finalPath[-1]:  # meet the goal then color the final path
                print("ddddddd")
            # for i in the range of range= number of final path nodes
                for a in range(len(finalPath) - 1):
                    print("hhhhhhh")
                    canvas.itemconfig(GA.nodeList[finalPath[a]][2][finalPath[a + 1]][0], fill="red")  # final path arrow

        else:
            # AL.getQsLog()[xTh][0]!=finalPath[-1]:#meet the goal then color the final path
                for a in GA.nodeList[n][2].values():
                   canvas.itemconfig(a[0],fill="black")#final path arrow


def NextStep(e):
    #global variable because otherwise cant be called in new methods as it
    #would be a local variable
    #xth is 1st,2nd,3rd,4th etc
    global xTh
    if xTh<len(AL.getQsLog())-1:
        #add 1 to go forward
        xTh+=1
        display()
        root.update()
def PreStep(e):
    global xTh
    #cant have negative no.s
    if xTh>0:
        #-1 to go back
        xTh-=1
        display()
        root.update()

button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",CreateArc)
button3.bind("<Button-1>",CreateCostArc)
button9.bind("<Button-1>",CreateHeu)
button4.bind("<Button-1>",Move)
button5.bind("<Button-1>",Delete)
button6.bind("<Button-1>",Run)
button7.bind("<Button-1>",PreStep)
button8.bind("<Button-1>",NextStep)


root.mainloop()
