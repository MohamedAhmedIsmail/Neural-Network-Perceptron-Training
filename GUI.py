from tkinter import *

root=Tk()

label_1=Label(root,text="Enter the Value of X1 Feature")
label_2=Label(root,text="Enter the Value of X2 Feature")
label_3=Label(root,text="Enter Learning rate")
label_4=Label(root,text="Enter Number of Epochs")

feature_1=Entry(root)
feature_2=Entry(root)
learn_rate=Entry(root)
epoch_rate=Entry(root)

label_1.grid(row=0)
label_2.grid(row=1)
label_3.grid(row=2)
label_4.grid(row=3)

feature_1.grid(row=0,column=1)
feature_2.grid(row=1,column=1)
learn_rate.grid(row=2,column=1)
epoch_rate.grid(row=3,column=1)

label_5=Label(root,text="Select Two Classes")
label_5.grid(row=4)
variable = StringVar(root)
variable.set("c1&c2")

w = OptionMenu(root, variable, "c1&c2", "c1&c3", "c2&c3")
w.grid(row=6)

c=Checkbutton(root, text="Add bias")
c.grid(columnspan=1)

button_1=Button(root,text="Button")
button_1.grid(row=8)
root.mainloop()
