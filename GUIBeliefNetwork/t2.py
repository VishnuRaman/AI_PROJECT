from tkinter import *

def overlaps(x1, y1, x2, y2):
    '''returns overlapping object ids in ovals dict'''
    oval_list = [] # make a list to hold overlap objects
    c_object = table.find_overlapping(x1, y1, x2, y2)
    for k,v in ovals.items():  # iterate over ovals dict
        if v in c_object:      # if the value of a key is in the overlap tuple
            oval_list.append(k)# add the key to the list
    return oval_list

a = Tk()
# make a dictionary to hold object ids
ovals = {}

table = Canvas(a, width=500, height=300, bg='white')
table.pack()

# create oval_a and assign a name for it as a key and
# a reference to it as a value in the ovals dict.
# the key can be whatever you want to call it
# create the other ovals as well, adding each to the dict
# after it's made
oval_a = table.create_oval(40, 40, 80, 80)
table.create_text(60,60,text="a")
ovals['oval_a'] = oval_a

oval_b = table.create_oval(60, 60, 120, 120)
table.create_text(90,90,text="b")
ovals['oval_b'] = oval_b

oval_c = table.create_oval(120, 120, 140, 140)
table.create_text(130,130,text="c")
ovals['oval_c'] = oval_c

# draw a rectangle
rectangle = table.create_rectangle(30, 30, 70, 70)
table.create_text(50,50,text="r")
# print the return value of the overlaps function
# using the coords of the rectangle as a bounding box

print(overlaps(table.coords(rectangle)[0],table.coords(rectangle)[1],table.coords(rectangle)[2],table.coords(rectangle)[3]))

a.mainloop()