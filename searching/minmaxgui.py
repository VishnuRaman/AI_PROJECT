# make a button like create node to create squares
# then do the enter values method
# then store the values into an array
# then next button = min method and max methods and collects stored numbers for algorithms


import GuiArray,ManageNode,Algorithms

from tkinter import *

from tkinter.simpledialog import askstring

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#pop up box - leads to canvas


#canvas
canvas = Canvas(root, width=1020,height=500,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

GA=GuiArray.guiArray(canvas)
MN=ManageNode.manageNode()

#create buttons

############
###########
#MAKE A BUTTON FOR CREATING THE BOXES AND ENTER VALUES AND STORE AS A LIST
############
############

button1=Button(bottomFrame,text="Run")

button2=Button(topFrame2,text="Create a group of values")

button3=Button(topFrame2,text="Previous Step")
button4=Button(topFrame2,text="Next Step")

button1.pack(side=BOTTOM)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

#change these to entry boxes

# #set 1
# box1=canvas.create_rectangle(15,490,65,440)
# box2=canvas.create_rectangle(95,490,145,440)
# box3=canvas.create_rectangle(175,490,225,440)
#
# #set 2
# box4=canvas.create_rectangle(275,490,325,440)
# box5=canvas.create_rectangle(355,490,405,440)
# box6=canvas.create_rectangle(435,490,485,440)
#
# #set 3
# box7=canvas.create_rectangle(535,490,585,440)
# box8=canvas.create_rectangle(615,490,665,440)
# box9=canvas.create_rectangle(695,490,745,440)
#
# #set 4
# box10=canvas.create_rectangle(795,490,845,440)
# box11=canvas.create_rectangle(875,490,925,440)
# box12=canvas.create_rectangle(955,490,1005,440)

def popupValue(e):

    # provides pop up box

    # if not canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105):
    #     oval=canvas.create_oval(e.x-50,e.y-50,e.x+50,e.y+40)
    #
    #     value = askstring('value', 'Please enter a title')
    #
    # box12 = canvas.create_rectangle(955, 490, 1005, 440)
    if not canvas.find_enclosed(e.x-50,e.y-50,e.x+50,e.y+50):
        box=canvas.create_rectangle(e.x-25,e.y-25,e.x+25,e.y+25)

        value = askstring('value', 'Please enter a value')

        if value == None:
            valueEntry = canvas.create_text(e.x, e.y, text="")
        else:
            value = int(value)

            valueEntry = canvas.create_text(e.x,e.y, text=str(value))



    #need to store all the values entered not just one at a time

    #maybe do a loop so if button click, add to a list

    valueList = [value] #need to add every new click too
    print(valueList)

    #make a list that stores all the entered values

    print("jjjjj")

    #now need to store entries to use them
    #

def ValueEntry(event):
    print("fffff")
    #select square and click then it opens a pop up value and that value is then placed
    #as a label into the bottom square
    #which is then fetched by the algorithm

    root.config(cursor="cross")
    canvas.bind("<Button-1>", popupValue)

def Run(event):
    root.config(cursor="")

    # lines leading up to min triangle
    # set 1
    line1 = canvas.create_line(40, 440, 120, 290)
    line2 = canvas.create_line(120, 440, 120, 290)
    line3 = canvas.create_line(200, 440, 120, 290)
    # min triangle
    min1 = canvas.create_polygon(85, 240, 120, 290, 155, 240, fill="dark green")
    minLine1 = canvas.create_line(120, 240, 510, 90)

    # set 2
    line4 = canvas.create_line(300, 440, 380, 290)
    line5 = canvas.create_line(380, 440, 380, 290)
    line6 = canvas.create_line(460, 440, 380, 290)
    # min triangle
    min2 = canvas.create_polygon(345, 240, 380, 290, 415, 240, fill="dark green")
    minLine2 = canvas.create_line(380, 240, 510, 90)

    # set 3
    line7 = canvas.create_line(560, 440, 640, 290)
    line8 = canvas.create_line(640, 440, 640, 290)
    line9 = canvas.create_line(720, 440, 640, 290)
    # min triangle
    min3 = canvas.create_polygon(605, 240, 640, 290, 675, 240, fill="dark green")
    minLine3 = canvas.create_line(640, 240, 510, 90)

    # set 4
    line10 = canvas.create_line(820, 440, 900, 290)
    line11 = canvas.create_line(900, 440, 900, 290)
    line12 = canvas.create_line(980, 440, 900, 290)
    # min triangle
    min4 = canvas.create_polygon(865, 240, 900, 290, 935, 240, fill="dark green")
    minLine4 = canvas.create_line(900, 240, 510, 90)

    # max triangle
    max = canvas.create_polygon(475, 90, 510, 40, 545, 90, fill="dark red")



    #run the algorithms for min and max and enter the data into the correct spaces on the gui


button1.bind("<Button-1>",Run)
button2.bind("<Button-1>",ValueEntry)

root.mainloop()