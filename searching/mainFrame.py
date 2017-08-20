from io import TextIOWrapper
from tkinter.simpledialog import askstring

import ManageNode,Linking,GuiArray,Algorithms

import pickle
from tkinter import *
# import Tkinter
import tkinter.filedialog
import tkinter.messagebox
from searching.Algorithms import algorithms

##This variable distinguishes if the user has selected an iterative search and is false by default.
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
canvas = Canvas(root, width=800,height=400,bg="old lace")
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
global algorithm
algorithm='none'
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
button2 = Button(topFrame,text="Create Individual Arrows")
button3 = Button(topFrame,text="Create Individual Arrows with costs")
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

##This dictionary stores the nodes and their associated nodeID values.
node_id_Dic={}

##This method draws the node oval and its ID number onto where the user has clicked on the canvas.
def drawNode(e):

    ##If the area encircling where the user has clicked, does not contain an object already, then create an oval and store this with an ID value.
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        oval=canvas.create_oval(e.x-20,e.y-10,e.x+20,e.y+10)

        ##The node ID is assigned to each object drawn and increases by 1 for each object.
        ##num is the label shown on the canvas displaying the node ID for that node.
        nodeID=MN.inc()
        num=canvas.create_text(e.x,e.y,text=str(nodeID))

        ##GUIset contains the nodeID, the oval it's associated to and the dictionary of nodeIDs it has any connections to.
        GUIset=[num,oval,{}]
        ##coordinateSet contains the nodeID and the coordinates clicked by the user when creating the node on the canvas.
        coordinateSet=[nodeID,e.x,e.y]
        ##This adds the nodeID and its associated node to the dictionary to store it
        node_id_Dic[oval]=nodeID
        ##This calls the method to store the GUIset data into a dictionary next to its relevant nodeID
        GA.addNode(GUIset,nodeID)
        ##This calls the method to store the coordinateSet data into a dictioanry next to its relevajt
        GA.addCoords(coordinateSet,nodeID)
        LK.add_vertex(nodeID)

##This method listens for the mouse click and upon this it will call the method to draw the node.
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)

##This method allows the user draw connections between each node.
def ArcPoint2(e):
    ##This statement checks if a node is within a 50 coordinate radius of where the user has clicked.
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        ##This tells us the nodeID of the node we want to draw the arrow towards.
        toNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
        ##This checks that the two node arguments entered are not the same node and if so, a connection is created.
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            ##This produces the arrow showing the connection where the four arguments taken in are:
            #the x and y coordinates of the start node (stored from the ArcPoint1 method) and the x and y coordinates of
            #where the user has clicked for this method.
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")

            ##A default weight of 1 is applied to all the connections to make them of uniform cost.
            #This is not displayed on the interface.
            weight = 1

            ##This adds the arrow into a dictionary to store which nodes have connections and to which nodes they are connected to.
            GA.addArrow(fromNode, toNode, arrow, weight)

           ##This method produces the cost for each connection.
            LK.add_edge(fromNode,toNode,weight)
            canvas.bind("<Button-1>",ArcPoint1)

##This method listens for the first mouse click from the user making the connection.
def ArcPoint1(e):
    ##if within a 50coordinate radius from where the user clicks only one node is found, then that node is stored
    #as the start node for the connection.
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
    ##global is equivalent of an instance variable and means this variable can be used/called by different methods.
       global x,y,fromNode
    ##These are the coordinates of where the user has clicked to begin their connection.
    #Using these coordinates, the nodeID is obtained.
       x,y=e.x,e.y
       fromNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
       root.config(cursor="cross")
       canvas.bind("<Button-1>",ArcPoint2)

##This method listens for the users mouse click and then proceeds to begin method ArcPoint1.
def CreateArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",ArcPoint1)

##This method allows the user draw connections between each node and add custom costs.
def ArcCostPoint2(e):
    ##If within a 50coordinate radius from where the user clicks only one node is found.
    if len(canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)) == 2:
        ## This node is stored as the final node for the connection.
            toNode = node_id_Dic[canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)[0]]
            ##This checks that the node stored as the start node is not the same as the final node stored and
            #this also checks that the connection does not already exist.
            if (fromNode is not toNode) and (LK.check_edge_existed(fromNode, toNode) == False):
                root.config(cursor="")
                ##This produces the arrow connecting the nodes.
                arrow = canvas.create_line(x, y, e.x, e.y, arrow="last")
                ##This produces the dialog box asking the user to enter a custom cost.
                value = askstring('value', 'Please enter a cost')
                ##If the user does not enter a value, a default cost of 0 is produced for the connection.
                if value == None:
                    value = 0

                weight = int(value)

                if weight is None:
                    print("NO WEIGHT ENTERED")
                ##This produces the label on the interface displaying each cost.
                weightLabel = canvas.create_text(0.5 * (x + e.x), 0.5 * (y + e.y) - 10, text=value)
                ##This calls method to store the connections and their costs into a dictionary.
                GA.addArrow(fromNode, toNode, arrow, weightLabel)

                ##This method produces the connection and provides the cost.
                LK.add_edge(fromNode, toNode, weight)
                canvas.bind("<Button-1>", ArcPoint1)

##This method listens for the first mouse click from the user making the connection.
def ArcCostPoint1(e):
        ##if within a 50coordinate radius from where the user clicks only one node is found, then that node is stored
        # as the start node for the connection.
        if len(canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)) == 2:
            ##global is equivalent of an instance variable and means this variable can be used/called by different methods.
            global x, y, fromNode
            ##These are the coordinates of where the user has clicked to begin their connection.
            #Using these coordinates the nodeID is obtained.
            x, y = e.x, e.y
            fromNode = node_id_Dic[canvas.find_enclosed(e.x - 50, e.y - 50, e.x + 50, e.y + 50)[0]]
            root.config(cursor="cross")
            canvas.bind("<Button-1>", ArcCostPoint2)

            global weight

##This method listens for the users mouse click and then proceeds to begin method ArcCostPoint1.
def CreateCostArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>", ArcCostPoint1)

##This method is called when the user wants to move a node from one location to another on the canvas.
#This method tells the node where to move to.
def moveTo(e):
    ##e.x and e.y are the coordinates you wish to move the node to and x and y are the nodes current coordinates,
    #By subtracting the two coordinates we can gain the distance the user wishes to travel the node by.
    canvas.move(moveTheNode,e.x-x,e.y-y)

    ##This is the same method but applies to the number displayed inside the node oval.
    canvas.move(moveTheNode+1,e.x-x,e.y-y)

    ##This method moves the arrows associated with the node being moved.
    for i in moveArrowTails:
        canvas.move(moveArrowTails[i],e.x-x,e.y-y)

    root.config(cursor="")
    canvas.bind("<Button-1>",moveFrom)

##This method is called when the user wishes to move a node and this method identifies which
#node the user wants to move and its current location to be moved from.
def moveFrom(e):
    ##x and y are the current coordinates of the node the user wants to move.
    global x,y
    x,y=e.x,e.y
    ##This checks a node is present within the area on the canvas that the user clicked.
    n=canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)
    if len(n)==2:
        root.config(cursor="exchange")
        global moveTheNode, moveArrowTails, moveArrowHeads
        ##This is the nodeID of the node the user wishes to move.
        moveTheNode=n[0]
        ##This takes the information regarding any connections associated with that nodeID
        moveArrowTails=GA.nodeList[node_id_Dic[n[0]]][2]
        ##This stores the information regarding its connections to use the moveTo(e) method.
        moveArrowHeads={}
        for i in GA.nodeList:
            if node_id_Dic[n[0]] in GA.nodeList[i][2]:
                moveArrowHeads[i]=GA.nodeList[i][2][node_id_Dic[n[0]]]

        canvas.bind("<Button-1>",moveTo)
    else:
        canvas.bind("<Button-1>",moveTo)

##This listens for when the button regarding moving nodes is clicked and calls the relevant methods.
def Move(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",moveFrom)

##This method deletes nodes off the canvas.
def removeFromCanvas(e):
    ##This checks the area the user has clicked contains a single node only.
    if len(canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50))==2:
        ##This stores the nodeID found in that area.
        selectedNode=node_id_Dic[canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50)[0]]
        ##This calls the methods which delete the node out of any dictionaries which store its
        #information. The deleted node and its associated connecting arrows are taken out of the
        #arrays its present it and the nodeID is placed into the top of a priority queue.
        #This nodeID is then selected when a new node is drawn.
        GA.deleteNode(selectedNode)
        LK.delete_vertex(selectedNode)
        MN.remove(selectedNode)

        Delete

##This listesn out for when the user clicks for the Delete method.
def Delete(event):
    root.config(cursor="spider")
    canvas.bind("<Button-1>",removeFromCanvas)

##This allows us to call methods and variables from the algorithms class.
AL=Algorithms.algorithms(LK.vert_dict)
##The result variable has a  default setting of empty to allow the results canvas to be
#printed if a final path is not found.
result=[]

##This method allows the user to add custom heuristics.
def AddHeu(e):
    ##x and y are the coordinates of where the user has clicked to add a heuristic.
    x = e.x
    y = e.y
    ##This produces the dialog box asking for custom heuristics to be entered.
    heuAskBox= askstring('value', 'Please enter a heuristic')

    global heu
    ##This is the value entered by the user.
    heu = int(float(heuAskBox))

    ##This for loop goes through the coordinates of each node shown on the canvas.
    #The coordinate range for each node is compared against the x and y values stored above.
    #If x and y are within this range, then the heuristic entered by the user is associated to the nodeID of the node
    #associated to the coordinate range which x and y are found in.
    for i in GA.coordList:
        if GA.coordList[i]:
            if x > GA.coordList[i][1] - 20 and x < GA.coordList[i][1] + 20:
                if y < GA.coordList[i][2] + 10 and y > GA.coordList[i][2] - 10:
                    # print("colour test" + str(i))
                    heuset=[heu]
                    ##This method then adds the heuristic to the A* algorithm
                    LK.vert_dict[i].heuristic=heu
                    ##A label is produced on the interface to show the user which nodes have heuristic values.
                    heuLabel = canvas.create_text(GA.coordList[i][1] + 35,GA.coordList[i][2],text="+ " + str(heu),fill='dark orange')

def CreateHeu(event):
    root.config(cursor="")
    canvas.bind("<Button-1>", AddHeu)


def Run(event): ######error message if no algorithm selected
    root.config(cursor="")
    global finalPath,xTh,delaytime,iter
    ##This variable is used later for the delay method and has a default of 0 allowing the algorithm to run in realtime.
    xTh=0

    ##If an iterative search is selected, the iterative method is called from the algorithms class.
    if iter == True and algorithm in ('BFS', 'DFS', 'UCS', 'aStar'):
        ##If a value to define the maximum rows to search by iteratively is not entered, an error message appears.
        if not it.get():
            tkinter.messagebox.showinfo('error','Please enter a maximum number of rows to search down')
        ##Otherwise the iterative algorithm is called and the arguments are entered.
        else:
            finalPath = AL.iterative(int(startNode.get()),int(endNode.get()),algorithm,int(it.get())) #make a box to gain user input from )
    ##If a non iterative UCS or aStar search is selected, the relevant algorithm is called.
    elif iter==False and algorithm in ('UCS','aStar'):
        finalPath = AL.ucsAStar(int(startNode.get()),int(endNode.get()),algorithm)
    ##If a non iterative BFS or DFS search is selected, the relevant algorithm is called.
    elif iter==False and algorithm in ('BFS', 'DFS'):
        finalPath = AL.bdfs(int(startNode.get()),int(endNode.get()),algorithm)

    ##If the user does not enter a value for the time delay, an error message is displayed.
    if not delay.get():
        tkinter.messagebox.showinfo('error', 'Please enter a value for the time delay (for real time searches enter 0)')

    ##Else xTh is set to the value of the delay time entered and the display is upated accordingly.
    else:
        delaytime=int(delay.get())

        ##If no algorithm is selected then an error message is displayed to inform the user.
        if algorithm in ('none'):
         tkinter.messagebox.showinfo('error','Please select a search')

        if iter == True and not it.get():
            print("it.get not entered")
        # ##Otherwise apply the time delay to the display of the algorithm.
        else:
            for i in range(len(AL.getVisitedLog())):
                xTh=i
                display()
                root.update()
                root.after(delaytime*1000)

##This method is called by the run method and displays the results of the search algortihm.
def display():
    ##If the display method has been called for the first time, a result canvas is produced which
    #displays various results and labels
    if not result:#if result is empty then create the labels - ie not shown already
        resultcanvas = Frame(root)
        resultcanvas.pack(side=BOTTOM)

        ##If BFS is selected the queue of all the nodes left to be expanded are displayed.
        if iter==False and algorithm=='BFS':
            qsLabel=Label(resultcanvas,bg="yellow",text="Queue: ")
        elif iter==True and algorithm=='BFS':
            qsLabel=Label(resultcanvas,bg="yellow",text="Queue: ")

        ##If DFS is selected the stack of all the nodes left to be expanded are displayed.
        elif iter==False and algorithm=='DFS':
            qsLabel = Label(resultcanvas,bg="yellow", text="Stack: ")
        elif iter==True and algorithm=='DFS':
            qsLabel = Label(resultcanvas,bg="yellow", text="Stack: ")
        ##If UCS or A* are chosen the stack of all the nodes left to be expanded are displayed.
        elif iter==False and algorithm=='UCS':
            #priotity queue label
            qsLabel=Label(resultcanvas,bg="yellow",text="Priority Queue: ")
        elif iter==True and algorithm=='UCS':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")
        elif iter==False and algorithm=='aStar':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")
        elif iter==True and algorithm=='aSTar':
            qsLabel = Label(resultcanvas, bg="yellow", text="Priority Queue: ")
        ##This places the position of the chosen label.
        qsLabel.grid(column=0,row=2,sticky=W)

        ##This displays the final path of the search algorithm and positions it on the result canvas.
        finalPathLabel=Label(resultcanvas, bg="red", text="Final path: ")
        finalPathLabel.grid(column=0,row=0,sticky=W)

        finalPathValue = Label(resultcanvas, text=str(finalPath))
        finalPathValue.grid(column=1,row=0,sticky=W)

        ##This displays the current node being expanded positions it on the result canvas.
        expandLabel=Label(resultcanvas,bg="light pink",text="Now expanding: ")
        expandLabel.grid(column=0,row=1,sticky=W)

        expandValue = Label(resultcanvas, text=str(AL.getQsLog()[xTh][0]))
        expandValue.grid(column=1,row=1,sticky=W)

        ##This gets the value associated with the queue/stack/priority queue label.
        qsValue = Label(resultcanvas,text=str(AL.getQsLog()[xTh][-1]))
        qsValue.grid(column=1,row=2,sticky=W)

        ###This displays the list of visited nodes positions them on the result canvas.
        visitedLabel=Label(resultcanvas,bg="brown",text="Visited: ")
        visitedLabel.grid(column=0,row=3,sticky=W)

        visitedValue = Label(resultcanvas, text=str(AL.getVisitedLog()[xTh]))
        visitedValue.grid(column=1,row=3,sticky=W)

        ##This notifies the result variable that it is no longer empty
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

    ##If no final path is found then a message is printed
    if finalPath == None:
        print("No final path found")
    ##If a final path is found
    if not finalPath is None:
    ##The following colour changes are made to the nodes involved depending on their status.
        for n in GA.nodeList:
            ##Visited nodes are filled brown
            if n in AL.getVisitedLog()[xTh]:
                canvas.itemconfig(GA.nodeList[n][1],fill="brown")
                ##The node currently being expanded is turned light pink
                if n == AL.getQsLog()[xTh][0]:
                    canvas.itemconfig(GA.nodeList[n][1],fill="light pink")
            ##The nodes in the queue/stack left to be visited are turned yellow
            elif n in AL.getQsLog()[xTh][1]:
                canvas.itemconfig(GA.nodeList[n][1],fill="yellow")
            else:
                canvas.itemconfig(GA.nodeList[n][1],fill="")

            if finalPath == None:
                print("have not found final path yet")
            ##If a final path is found, the arrows change to red.
            elif AL.getQsLog()[xTh][0] == finalPath[-1]:
                    for a in range(len(finalPath) - 1):
                        print("hhhhhhh")
                        canvas.itemconfig(GA.nodeList[finalPath[a]][2][finalPath[a + 1]][0], fill="red")  # final path arrow

            else:
                ##If a final path is not found the arrows remain black
                    for a in GA.nodeList[n][2].values():
                       canvas.itemconfig(a[0],fill="black")

##This method allows the user to move forward step by step.
def NextStep(e):
    ##This adds 1 to the current time of the algorithm step, pushing to the next step forward.
    global xTh
    if xTh<len(AL.getQsLog())-1:
        xTh+=1
        display()
        root.update()

##This method allows the user to move forward step by step.
def PreStep(e):
    ##This minuses 1 to the current time of the algorithm step, pushing to the next step forward.
    global xTh
    ##As you cannot have negative values for an algorithm time, this checks that the value is always positive.
    if xTh>0:
        xTh-=1
        display()
        root.update()

##This binds all the buttons to their actions, so the correct methods are ran when a mouse button is clicked.
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
