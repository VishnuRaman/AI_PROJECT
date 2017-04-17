# @version 15-04-2017
# @author Rasveer Bansi
from tkinter import *
import tkinter.messagebox

root = Tk()

#creates the frame to place the buttons
topFrame = Frame(root)
topFrame.pack()


#creates the canvas to draw everything onto
canvas = Canvas(root, width=1200, height=1000)
canvas.pack()

# rectangle canvas and space for notes
box = canvas.create_rectangle(120, 30, 750, 600)

noteBox = canvas.create_rectangle(120, 30, 1200, 600)

# noteBox = canvas.create_text(1100, 38, text="Notes")
noteLabel = Label(topFrame, text="\n \n Notes")
noteLabel.pack(side=RIGHT)

spacing = Label(topFrame, text="\n \n                                               ")
spacing.pack(side=RIGHT)
#new node button
def newNode(event):

    # rectangle canvas and space for notes
    box = canvas.create_rectangle(120, 30, 750, 600)

    noteBox = canvas.create_rectangle(120, 30, 1200, 600)

    #creates the oval
    canvas.create_oval(400, 100, 480, 160)
    #labels the node
    canvas.create_text(440, 130, text="1")

    #the left arrow stemming from the node
    canvas.create_line(420, 155, 375, 210)
    #the right arrow stemming from the node
    canvas.create_line(460, 156, 510, 210)

    #set of text notes linked to that row of nodes
    canvas.create_text(900, 140, text="first set of notes \n"
                                         +"related to the first node")

#the button to create a the first new node
newNodeButton = Button(topFrame, text="New Node")
newNodeButton.bind("<Button-1>", newNode)
newNodeButton.pack(side=LEFT)

#next button and shows next two nodes and arrows
def next(event):
    #node 2
    # creates the oval
    canvas.create_oval(330, 210, 415, 270)
    # labels the node
    canvas.create_text(372, 240, text="2")
    # the left arrow stemming from the node
    canvas.create_line(350, 267, 310, 325)
    #the right arrow stemming from the node
    canvas.create_line(385, 270,423, 325)

    #node 3
    # creates the oval
    canvas.create_oval(480, 210, 565, 270)
    # labels the node
    canvas.create_text(523, 240, text="3")
    # the left arrow stemming from the node
    canvas.create_line(505, 268, 480, 325)
    #the right arrow stemming from the node
    canvas.create_line(540, 268, 580, 325)

    # the button to create a the first new node
    canvas.create_text(900, 250, text="next set of notes \n"
                                       + "related to the second row \n" + "of nodes")
#creates the next button to produce the next row of nodes
nextButton = Button(topFrame, text="Next")
nextButton.bind("<Button-1>", next)
nextButton.pack(side=LEFT)

# #this undos the node created by the next button
# def undo(event):
#     canvas.delete(event)
#
# #this is the undo button
# undoButton = Button(topFrame, text="Undo")
# undoButton.bind("<Button-1>", undo)
#undoButton.pack(side=LEFT)

#this resets the graph to a blank one
def reset(event):
    canvas.delete(ALL)

#this is the reset button
resetButton = Button(topFrame, text="Reset")
resetButton.bind("<Button-1>", reset)
resetButton.pack(side=LEFT)


root.mainloop()
