# Dev Govine 
# July - 9 - 2022
from tkinter import PhotoImage
from tkinter.ttk import *
from tkinter import *


gray_color = "#C0C0C0"
green_color = "#3DB39E"
white_color = "#FFFFFF"

# colors for number pad
light_gray = "#E9E9E9"
mid_dark_gray = "#5C5C5C"
custom_red = "#F60606"


root = Tk()
root.iconbitmap("assets\icons\cal-icon.ico")
root.title("Calculator")
root.geometry("300x540+1000+100")
root.config(background=white_color)


# # Getting all the images for each button icon
clock_img = PhotoImage(file=r'assets\\icons\\clock.png')
ruler_img = PhotoImage(file=r'assets\\icons\\ruler.png')
moreopts_img = PhotoImage(file=r'assets\\icons\\moreopts.png')
clear_img = PhotoImage(file=r'assets\\icons\\clear.png')

c_img = PhotoImage(file=r'assets\\icons\\letter-c.png')
# brackets_img = PhotoImage(file=r'assets\\icons\\parentheses-grouping-symbol.png')
percent_img = PhotoImage(file=r'assets\\icons\\percent-sign.png')
divide_img = PhotoImage(file=r'assets\\icons\\divide.png')


num7_img = PhotoImage(file=r'assets\\icons\\number-7.png')
num8_img = PhotoImage(file=r'assets\\icons\\number-8.png')
num9_img = PhotoImage(file=r'assets\\icons\\number-9.png')
multiply_img = PhotoImage(file=r'assets\\icons\\multiply.png')


num4_img = PhotoImage(file=r'assets\\icons\\number-4.png')
num5_img = PhotoImage(file=r'assets\\icons\\number-5.png')
num6_img = PhotoImage(file=r'assets\\icons\\number-6.png')
minus_img = PhotoImage(file=r'assets\\icons\\minus.png')


num1_img = PhotoImage(file=r'assets\\icons\\number-1.png')
num2_img = PhotoImage(file=r'assets\\icons\\number-2.png')
num3_img = PhotoImage(file=r'assets\\icons\\number-3.png')
plus_img = PhotoImage(file=r'assets\\icons\\plus.png')


# plus_less_img = PhotoImage(file=r'assets\\icons\\plusless.png')
num0_img = PhotoImage(file=r'assets\\icons\\number-0.png')
dot_img = PhotoImage(file=r'assets\\icons\\dot.png')
equal_img = PhotoImage(file=r'assets\\icons\\equal.png')


root.resizable(False, False)




# The display frame
displayframe = Frame(root, bg=green_color, width=570, height=150)



# CREATING THE OPTIONS FRAME
optionsframe = Frame(root, bg=white_color, width=570, height=150)
# Creating the options to pack onto the frame
clockbtn = Button(optionsframe, image=clock_img, width=24, height=24, border=0, background=white_color)
rulerbtn = Button(optionsframe, image=ruler_img, width=24, height=24, border=0, background=white_color)
moreoptsbtn = Button(optionsframe, image=moreopts_img, width=24, height=24, border=0, background=white_color)
clearbtn = Button(optionsframe, image=clear_img, width=24, height=24, border=0, background=white_color)


# CREATING THE SPACE BAR
spacerframe = Frame(root, bg=gray_color, width=285, height=1, border=0)


# CREATING THE NUMBER PAD
numberpadframe = Frame(root, bg=white_color)
# creating buttons to pack onto the number pad frame
# ROW ONE
cbtn = Button(numberpadframe, image=c_img,width=128, height=64, border=0, background=white_color)
# bracketsbtn = Button(numberpadframe, image=brackets_img,width=64, height=64, border=0, background=white_color)
percentbtn = Button(numberpadframe, image=percent_img,width=64, height=64, border=0, background=white_color)
dividebtn = Button(numberpadframe, image=divide_img,width=64, height=64, border=0, background=white_color)


# SECOND ROW
sevenbtn = Button(numberpadframe, image=num7_img,width=64, height=64, border=0, background=white_color)
eightbtn = Button(numberpadframe, image=num8_img,width=64, height=64, border=0, background=white_color)
ninebtn = Button(numberpadframe, image=num9_img,width=64, height=64, border=0, background=white_color)
multiplybtn = Button(numberpadframe, image=multiply_img,width=64, height=64, border=0, background=white_color)


# THIRD ROW
fourbtn = Button(numberpadframe, image=num4_img,width=64, height=64, border=0, background=white_color)
fivebtn = Button(numberpadframe, image=num5_img,width=64, height=64, border=0, background=white_color)
sixbtn = Button(numberpadframe, image=num6_img,width=64, height=64, border=0, background=white_color)
minusbtn = Button(numberpadframe, image=minus_img,width=64, height=64, border=0, background=white_color)


# FOURTH ROW
onebtn = Button(numberpadframe, image=num1_img,width=64, height=64, border=0, background=white_color)
twobtn = Button(numberpadframe, image=num2_img,width=64, height=64, border=0, background=white_color)
threebtn = Button(numberpadframe, image=num3_img,width=64, height=64, border=0, background=white_color)
plusbtn = Button(numberpadframe, image=plus_img,width=64, height=64, border=0, background=white_color)


# FIFTH ROW
# plusminusbtn = Button(numberpadframe, image=plus_less_img,width=64, height=64, border=0, background=white_color)
blankbtn = Button(numberpadframe, image=equal_img,width=64, height=64, border=0, background=white_color, state="disable")
zerobtn = Button(numberpadframe, image=num0_img,width=64, height=64, border=0, background=white_color)
dotbtn = Button(numberpadframe, image=dot_img,width=64, height=64, border=0, background=white_color)
equalbtn = Button(numberpadframe, image=equal_img,width=64, height=64, border=0, background=green_color)







# Showing the frame and buttons
displayframe.pack()

# bodyframe.pack()
optionsframe.pack()
clockbtn.pack(padx=(0,0), pady=(12, 12), side=LEFT)
rulerbtn.pack(padx=(24,24), pady=(12, 12), side=LEFT)
moreoptsbtn.pack(padx=(0,0), pady=(12, 12),  side=LEFT)
clearbtn.pack(padx=(100,0), pady=(12, 12), side=LEFT)

spacerframe.pack()


numberpadframe.pack()


# ROW ONE
cbtn.grid(column=0, columnspan=2, row=0)
# bracketsbtn.grid(column=1, row=0)
percentbtn.grid(column=2, row=0)
dividebtn.grid(column=3, row=0)


# SECOND ROW
sevenbtn.grid(column=0, row=1)
eightbtn.grid(column=1, row=1)
ninebtn.grid(column=2, row=1)
multiplybtn.grid(column=3, row=1)


# THIRD ROW
fourbtn.grid(column=0, row=2)
fivebtn.grid(column=1, row=2)
sixbtn.grid(column=2, row=2)
minusbtn.grid(column=3, row=2)


# FOURTH ROW
onebtn.grid(column=0, row=3)
twobtn.grid(column=1, row=3)
threebtn.grid(column=2, row=3)
plusbtn.grid(column=3, row=3)


# FIFTH ROW
# plusminusbtn.grid(column=0, row=4)

dotbtn.grid(column=0, row=4)
zerobtn.grid(column=1, row=4)
blankbtn.grid(column=2, row=4)
equalbtn.grid(column=3, row=4)

root.mainloop()
