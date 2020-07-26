from tkinter import *
import backend1

window = Tk()

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend1.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend1.search(text_title.get(),text_author.get(),text_year.get(),text_ISBN.get()):
        list1.insert(END,row)

def add_command():
    backend1.insert(text_title.get(),text_author.get(),text_year.get(),text_ISBN.get())
    list1.delete(0,END)
    list1.insert(END,(text_title.get(),text_author.get(),text_year.get(),text_ISBN.get()))

def delete_command():
    backend1.delete(selected_tuple[0])
    view_command()

def update_command():
    backend1.update(selected_tuple[0],text_title.get(),text_author.get(),text_year.get(),text_ISBN.get())
    view_command()

window.wm_title("Bookstore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)
l2 = Label(window,text="Author")
l2.grid(row=0,column=2)
l3 = Label(window,text="Year")
l3.grid(row=1,column=0)
l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

text_title = StringVar()
e1 = Entry(window,textvariable=text_title)
e1.grid(row=0,column=1)
text_author = StringVar()
e2 = Entry(window,textvariable=text_author)
e2.grid(row=0,column=3)
text_year = StringVar()
e3 = Entry(window,textvariable=text_year)
e3.grid(row=1,column=1)
text_ISBN = StringVar()
e4 = Entry(window,textvariable=text_ISBN)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
list1.bind("<<ListboxSelect>>",get_selected_row)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
