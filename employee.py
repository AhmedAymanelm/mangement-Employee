from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox
from PIL import Image, ImageTk

db = Database('Employee.db')

root = Tk()
root.title("Employee Management System")
root.geometry('1300x800+100+10')
root.resizable(False, False)
root.configure(background='#101A58')

# =============================== Frame =============
entry_frame = Frame(root, bg='#101A58')
entry_frame.place(x=1, y=1, width=350, height=800)
title = Label(entry_frame, text='Employee Company', font=('calibri', 14, 'bold'), fg='white', background='#101A58')
title.place(x=2, y=3)

name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
phone = StringVar()
address = StringVar()

image = Image.open('log.jpeg')  # تأكد من استخدام المسار الصحيح للصورة
logo = ImageTk.PhotoImage(image)
lbl_logo = Label(root, image=logo)
lbl_logo.place(x=80, y=560)

# ====================== Label And Entry =============
lbl_name = Label(entry_frame, text='Name', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_name.place(x=1, y=47)
entry_name = Entry(entry_frame, width=20, textvariable=name, justify='left', font=(11))
entry_name.place(x=80, y=47, height=33)

lbl_job = Label(entry_frame, text='Job', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_job.place(x=1, y=100)
entry_job = Entry(entry_frame, width=20, textvariable=job, justify='left', font=(11))
entry_job.place(x=80, y=100, height=33)

lbl_gender = Label(entry_frame, text='Gender', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_gender.place(x=1, y=150)
combo_gender = ttk.Combobox(entry_frame, state='readonly', width=18, justify='left', font=(11))
combo_gender['values'] = ('male', 'female')
combo_gender.place(x=80, y=150, height=30)

lbl_age = Label(entry_frame, text='Age', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_age.place(x=3, y=200)
entry_age = Entry(entry_frame, width=20, textvariable=age, justify='left', font=(11))
entry_age.place(x=80, y=200, height=33)

lbl_email = Label(entry_frame, text='Email', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_email.place(x=1, y=255)
entry_email = Entry(entry_frame, width=20, textvariable=email, justify='left', font=(11))
entry_email.place(x=80, y=250, height=33)

lbl_phone = Label(entry_frame, text='Phone', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_phone.place(x=1, y=300)
entry_phone = Entry(entry_frame, width=20, textvariable=phone, justify='left', font=(11))
entry_phone.place(x=80, y=300, height=33)

lbl_address = Label(entry_frame, text='Address:', bg='#101A58', fg='white', font=('monospace', 14, 'bold'))
lbl_address.place(x=1, y=340)
entry_address = Entry(entry_frame, width=20, textvariable=address, justify='left', font=(11))
entry_address.place(x=79, y=380, height=50)

# ================================ BUTTON =================================
btn_frame = Frame(entry_frame, background='#101A58', bd=1, relief=SOLID)
btn_frame.place(x=10, y=450, width=335, height=100)

btnadd = Button(btn_frame,
                text='Add',
                width=13,
                height=1,
                font=('monospace', 14, 'bold'),
                fg='black',
                bg='Green',
                bd=0,
                command=lambda: add_employee())
btnadd.place(x=4, y=5)

btndel = Button(btn_frame,
                text='Delete',
                width=13,
                height=1,
                font=('monospace', 14, 'bold'),
                fg='black',
                bg='blue',
                bd=0,
                command=lambda: delete_employee())
btndel.place(x=170, y=5)

btnupdate = Button(btn_frame,
                   text='Update',
                   width=13,
                   height=1,
                   font=('monospace', 14, 'bold'),
                   fg='black',
                   bg='#FF0000',
                   bd=0,
                   command=lambda: update_employee())
btnupdate.place(x=4, y=50)

btnclear = Button(btn_frame,
                  text='Clear',
                  width=13,
                  height=1,
                  font=('monospace', 14, 'bold'),
                  fg='black',
                  bg='#FFFF00',
                  bd=0,
                  command=lambda: clear_entries())
btnclear.place(x=170, y=50)

# ================================== table frame ======================
tree_frame = Frame(root, background='white')
tree_frame.place(x=365, y=1, width=950, height=800)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('calibri', 13), rowheight=100)
style.configure("mystyle.Treeview.Heading", font=('calibri', 13))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style='mystyle.Treeview')
tv.heading("1", text="ID")
tv.column("1", width=40)

tv.heading("2", text="Name")
tv.column("2", width=140)

tv.heading("3", text="Age")
tv.column("3", width=50)

tv.heading("4", text="Job")
tv.column("4", width=120)

tv.heading("5", text="Gender")
tv.column("5", width=140)

tv.heading("6", text="Address")
tv.column("6", width=140)

tv.heading("7", text="Phone")
tv.column("7", width=150)

tv.heading("8", text="Email")
tv.column("8", width=190)
tv['show'] = 'headings'
tv.pack()

def hide():
    root.geometry('357x545')

def show():
    root.geometry('1300x800+100+10')

btnhide = Button(entry_frame, background='white', text="Hide", cursor='hand2', fg='#000000', command=hide)
btnhide.place(x=270, y=10)
btnshow = Button(entry_frame, background='white', text="Show", cursor='hand2', fg='#000000', command=show)
btnshow.place(x=310, y=10)

# ========================== Functions ==========================
def getdata(event):
    select_row = tv.focus()
    data = tv.item(select_row)
    global row
    row = data['values']
    name.set(row[1])
    job.set(row[3])
    gender.set(row[4])
    age.set(row[2])
    email.set(row[7])
    phone.set(row[6])
    address.set(row[5])

def display_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_employee():
    if entry_name.get() == "" or entry_address.get() == "" or entry_job.get() == "" or entry_email.get() == "" or entry_age.get() == "" or entry_phone.get() == "" or combo_gender.get() == "":
        messagebox.showerror("Error", "Please do not leave any spaces.")
        return
    db.insert(
        entry_name.get(),
        entry_age.get(),
        entry_job.get(),
        combo_gender.get(),
        entry_phone.get(),
        entry_address.get(),
        entry_email.get()
    )
    messagebox.showinfo("Success", "Added new employee")
    clear_entries()
    display_all()

def delete_employee():
    if not tv.selection():
        messagebox.showerror("Error", "Please select a record to delete")
        return
    selected_item = tv.selection()[0]
    db.remove(tv.item(selected_item)['values'][0])
    tv.delete(selected_item)
    messagebox.showinfo("Success", "deleted  successfully")
    clear_entries()
    display_all()

def update_employee():
    if entry_name.get() == "" or entry_address.get() == "" or entry_job.get() == "" or entry_email.get() == "" or entry_age.get() == "" or entry_phone.get() == "" or combo_gender.get() == "":
        messagebox.showerror("Error", "Please do not leave any spaces.")
        return
    db.update(
        row[0],
        entry_name.get(),
        entry_age.get(),
        entry_job.get(),
        combo_gender.get(),
        entry_phone.get(),
        entry_address.get(),
        entry_email.get()
    )
    messagebox.showinfo("Success", "updated  successfully")
    clear_entries()
    display_all()

def clear_entries():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    phone.set("")
    address.set("")
    entry_name.focus_set()

tv.bind("<ButtonRelease-1>", getdata)
display_all()

root.mainloop()
