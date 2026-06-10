from tkinter import *
from tkinter import messagebox

# ---------------- WINDOW ---------------- #
root = Tk()
root.title("Contact Management System")
root.geometry("900x550")
root.configure(bg="#F8FAFC")
root.resizable(False, False)

# ---------------- DATA ---------------- #
contactlist = [
    ["Siddharth", "369854712"],
    ["Gaurav", "521155222"],
    ["Abhishek", "78945614"],
    ["Sakshi", "58745246"],
    ["Mohit", "5846975"],
    ["Karan", "5647892"],
    ["Shreya", "89685320"],
    ["Palak", "98564785"],
    ["Ganesh", "85967412"]
]

Name = StringVar()
Number = StringVar()

# ---------------- FUNCTIONS ---------------- #

def update_count():
    count_label.config(text=f"Total Contacts: {len(contactlist)}")


def Selected():
    if len(contact_list.curselection()) == 0:
        messagebox.showerror("Error", "Please select a contact")
        return None
    return contact_list.curselection()[0]


def reset_fields():
    Name.set("")
    Number.set("")


def refresh_contacts():
    contactlist.sort()
    contact_list.delete(0, END)

    for name, phone in contactlist:
        contact_list.insert(END, name)

    update_count()


def add_contact():
    name = Name.get().strip()
    phone = Number.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Please fill all fields")
        return

    if not phone.isdigit():
        messagebox.showerror("Error", "Phone number must contain digits only")
        return

    contactlist.append([name, phone])
    refresh_contacts()
    reset_fields()

    messagebox.showinfo("Success", "Contact Added Successfully")


def view_contact():
    index = Selected()

    if index is None:
        return

    name, phone = contactlist[index]

    Name.set(name)
    Number.set(phone)


def edit_contact():
    index = Selected()

    if index is None:
        return

    name = Name.get().strip()
    phone = Number.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Please fill all fields")
        return

    contactlist[index] = [name, phone]

    refresh_contacts()
    reset_fields()

    messagebox.showinfo("Success", "Contact Updated Successfully")


def delete_contact():
    index = Selected()

    if index is None:
        return

    confirm = messagebox.askyesno(
        "Delete Contact",
        "Are you sure you want to delete this contact?"
    )

    if confirm:
        del contactlist[index]
        refresh_contacts()
        reset_fields()


def exit_app():
    root.destroy()


# ---------------- HEADER ---------------- #

header = Label(
    root,
    text="My Contact Book",
    bg="#1E293B",
    fg="white",
    font=("Segoe UI", 22, "bold"),
    pady=15
)

header.pack(fill=X)

# ---------------- LEFT CARD ---------------- #

left_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
left_frame.place(x=30, y=90, width=340, height=380)

Label(
    left_frame,
    text="Name",
    bg="white",
    font=("Segoe UI", 12, "bold")
).place(x=20, y=30)

Entry(
    left_frame,
    textvariable=Name,
    font=("Segoe UI", 12),
    width=25
).place(x=20, y=60)

Label(
    left_frame,
    text="Phone Number",
    bg="white",
    font=("Segoe UI", 12, "bold")
).place(x=20, y=110)

Entry(
    left_frame,
    textvariable=Number,
    font=("Segoe UI", 12),
    width=25
).place(x=20, y=140)

# ---------------- BUTTONS ---------------- #

Button(
    left_frame,
    text="➕ Add",
    bg="#2563EB",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=add_contact
).place(x=20, y=220)

Button(
    left_frame,
    text="✏ Edit",
    bg="#F59E0B",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=edit_contact
).place(x=170, y=220)

Button(
    left_frame,
    text="👁 View",
    bg="#10B981",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=view_contact
).place(x=20, y=280)

Button(
    left_frame,
    text="🗑 Delete",
    bg="#EF4444",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=delete_contact
).place(x=170, y=280)

Button(
    left_frame,
    text="🔄 Reset",
    bg="#6B7280",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=reset_fields
).place(x=20, y=330)

Button(
    left_frame,
    text="🚪 Exit",
    bg="#111827",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=12,
    command=exit_app
).place(x=170, y=330)

# ---------------- RIGHT CONTACT LIST ---------------- #

right_frame = Frame(root, bg="white", bd=2, relief=RIDGE)
right_frame.place(x=420, y=90, width=430, height=380)

Label(
    right_frame,
    text="Contacts",
    bg="white",
    font=("Segoe UI", 16, "bold")
).pack(pady=10)

scrollbar = Scrollbar(right_frame)

contact_list = Listbox(
    right_frame,
    font=("Segoe UI", 12),
    width=35,
    height=14,
    selectbackground="#2563EB",
    selectforeground="white",
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=contact_list.yview)

scrollbar.pack(side=RIGHT, fill=Y)
contact_list.pack(pady=10)

# ---------------- FOOTER ---------------- #

count_label = Label(
    root,
    text="Total Contacts: 0",
    bg="#F8FAFC",
    fg="#1E293B",
    font=("Segoe UI", 11, "bold")
)

count_label.place(x=30, y=500)

refresh_contacts()

root.mainloop()