from tkinter import *
import TaskManagerBE as backend

window = Tk()


def clear_entry():
    for entry in (e1, e2, e3, e4):
        entry.delete(0, END)


def view_command():
    clear_entry()
    task.delete(0, END)
    for row in backend.view():
        task.insert(END, row)


def search_command():
    task.delete(0, END)
    for row in backend.search(entry1.get(), entry2.get(), entry3.get(), entry4.get()):
        task.insert(END, row)
    clear_entry()


def add_command():
    task.delete(0, END)
    backend.insert((entry1.get()).lower(), (entry2.get()).lower(), (entry3.get()).lower(), (entry4.get()).lower())
    for row in backend.view():
        task.insert(END, row)
    clear_entry()


def selected_item(event):
    try:
        global index
        select_item = task.get(task.curselection())
        index = select_item[0]
        clear_entry()
        e1.insert(END, select_item[1])
        e2.insert(END, select_item[2])
        e3.insert(END, select_item[3])
        e4.insert(END, select_item[4])

    except IndexError:
        pass


def delete_command():
    backend.delete(index)
    view_command()


def update_command():
    backend.update(entry1.get(), entry2.get(), entry3.get(), entry4.get(), index)
    view_command()


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Date")
l2.grid(row=0, column=2)
l3 = Label(window, text="Description")
l3.grid(row=1, column=0)
l4 = Label(window, text="Location")
l4.grid(row=1, column=2)
entry1 = StringVar()
e1 = Entry(window,textvariable=entry1)
e1.grid(row=0, column=1)
entry2 = StringVar()
e2 = Entry(window,textvariable=entry2)
e2.grid(row=0, column=3)
entry3 = StringVar()
e3 = Entry(window,textvariable=entry3)
e3.grid(row=1, column=1)
entry4 = StringVar()
e4 = Entry(window, textvariable=entry4)
e4.grid(row=1, column=3)
task = Listbox(window, height=5, width=30)
task.grid(row=2, column=0, columnspan=2, rowspan=6)

sb = Scrollbar(window)
sb.grid(row=3, column=2, rowspan=3)
task.config(yscrollcommand=sb.set)
sb.config(command=task.yview)

task.bind('<<ListboxSelect>>', selected_item)

b1 = Button(window, text="View all", width=15, command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window, text="Search", width=15, command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window, text="Add task", width=15, command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window, text="Update task", width=15, command= update_command)
b4.grid(row=5,column=3)

b5 = Button(window, text="Terminate task", width=15, command=delete_command)
b5.grid(row=6,column=3)

window.mainloop()