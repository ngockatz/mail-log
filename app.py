from tkinter import *
import backend

def view_record():
    log.delete(0,END) #first empty list
    for row in backend.view(): #loop through every record
        log.insert(END,row)

def search_command():
    log.delete(0,END)
    for row in backend.search(tdate.get(),tname.get(),tnop.get(),temail.get()
                              ,tchecked.get(),tdatech.get()):
        log.insert(END,row)

def add_command():
    backend.insert(tdate.get(),tname.get(),tnop.get(),temail.get()
                              ,tchecked.get(),tdatech.get())
    log.delete(0,END)
    log.insert(END,(tdate.get(),tname.get(),tnop.get(),temail.get()
                              ,tchecked.get(),tdatech.get()))
    view_record()

def get_select(event):
    global selected
    try:
        #log.curselection:
        index=log.curselection()[0]
        selected=log.get(index) #returns a tuple

    #update text box based on current selection
        e1.delete(0,END)
        e1.insert(END,selected[1])
        e2.delete(0,END)
        e2.insert(END,selected[2])
        e3.delete(0,END)
        e3.insert(END,selected[3])
        e4.delete(0,END)
        e4.insert(END,selected[4])
        e5.delete(0,END)
        e5.insert(END,selected[5])
        e6.delete(0,END)
        e6.insert(END,selected[6])

    except IndexError:
        pass
        
def delete_command():
    backend.delete(selected[0])
    log.delete(0,END)
    view_record()

def update_command():
    backend.update(selected[0],tdate.get(),tname.get(),tnop.get(),temail.get()
                              ,tchecked.get(),tdatech.get())
    log.delete(0,END)
    view_record()

window=Tk()

window.wm_title("Mail Log")
#label
ldate=Label(window,text="Date Received")
ldate.grid(row=0,column=0)

lname=Label(window,text="Name")
lname.grid(row=1,column=0)

lnop=Label(window,text="No of")
lnop.grid(row=0,column=2)

lemail=Label(window,text="Email sent?")
lemail.grid(row=1,column=2)

lchecked=Label(window,text="Checked out")
lchecked.grid(row=0,column=4)

ldatechk=Label(window,text="Date checked")
ldatechk.grid(row=1,column=4)

#text field
tdate=StringVar()
e1=Entry(window,textvariable=tdate)
e1.grid(row=0,column=1)

tname=StringVar()
e2=Entry(window,textvariable=tname)
e2.grid(row=1,column=1)

tnop=StringVar()
e3=Entry(window,textvariable=tnop)
e3.grid(row=0,column=3)

temail=StringVar()
e4=Entry(window,textvariable=temail)
e4.grid(row=1,column=3)

tchecked=StringVar()
e5=Entry(window,textvariable=tchecked)
e5.grid(row=0,column=5)

tdatech=StringVar()
e6=Entry(window,textvariable=tdatech)
e6.grid(row=1,column=5)

#List all records
log = Listbox(window, height=10, width = 60)
log.grid(row=2,column=0,rowspan=6,columnspan=4)

#Scroll bar
sb=Scrollbar(window)
sb.grid(row=2,column=4,rowspan=6)

#Configure scroll bar with list
log.configure(yscrollcommand=sb.set)
sb.configure(command=log.yview)

#Return an id when user selects from listbox
log.bind('<<ListboxSelect>>',get_select)

#Buttons
b1=Button(window,text='View all',width=12,command=view_record)
b1.grid(row=2,column=5)

b2=Button(window,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=5)

b3=Button(window,text='Add entry',width=12,command=add_command)
b3.grid(row=4,column=5)

b4=Button(window,text='Update',width=12,command=update_command)
b4.grid(row=5,column=5)

b5=Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=6,column=5)

b6=Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=5)

window.mainloop()
