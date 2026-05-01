import os
import customtkinter as ctk
from tkinter import messagebox
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4
from PIL import Image
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def run_backend():
    os.system("back_end.exe")
def set_icon(app):
    app.iconbitmap("logo.ico")
def pdfb():
    try:
        with open("output.txt", "r") as f:
            lines = f.readlines()
        data = [line.strip().split("\t") for line in lines]
        pdf = SimpleDocTemplate("Resource_Report.pdf", pagesize=A4)
        table = Table(data)
        pdf.build([table])
        messagebox.showinfo("Success", "pdf saved successfully")
    except Exception:
        messagebox.showerror("Error", "fahhhhhhh!!!! pdf failed")
def reshjo():
    with open("input.txt", "w") as f:
        f.write("2")
    run_backend()
    available = []
    with open("output.txt", "r") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if "Available" in line:
                parts = line.split()
                if parts:
                    available.append(parts[0])
    return available
app = ctk.CTk()
app.geometry("920x540")
app.title("Campus Resource Allocation System")
set_icon(app)
sidebar = ctk.CTkFrame(app, width=220)
sidebar.pack(side="left", fill="y")
content = ctk.CTkFrame(app)
content.pack(side="right", expand=True, fill="both")
app.bind_all("<Tab>", lambda e: e.widget.tk_focusNext().focus())
def screen():
    for widget in content.winfo_children():
        widget.destroy()
def addwin():
    screen()
    ctk.CTkLabel(content, text="add resource", font=("Arial", 24)).pack(pady=20)
    ide = ctk.CTkEntry(content, placeholder_text="resource id")
    ide.pack(pady=10)
    nam = ctk.CTkEntry(content, placeholder_text="resource name")
    nam.pack(pady=10)
    def submit(event=None):
        rid = ide.get().strip()
        name = nam.get().strip()
        if rid == "" or name == "":
            messagebox.showerror("Error", "Fill all fields")
            return
        with open("input.txt", "w") as f:
            f.write(f"1\n{rid} {name}")
        run_backend()
        messagebox.showinfo("Success", "resource added successfully")
        ide.delete(0, "end")
        nam.delete(0, "end")

    ctk.CTkButton(content, text="Submit", command=submit).pack(pady=20)
    content.bind("<Return>", submit)
def dekh():
    screen()
    ctk.CTkLabel(content, text="View Resource", font=("Arial", 24)).pack(pady=20)
    box = ctk.CTkTextbox(content, width=650, height=260)
    box.pack(pady=10)
    with open("input.txt", "w") as f:
        f.write("2")
    run_backend()
    with open("output.txt", "r") as f:
        box.insert("0.0", f.read())
    ctk.CTkButton(content, text="Download PDF", command=pdfb).pack(pady=10)
def inuse():
    screen()
    ctk.CTkLabel(content, text="Allocate Resource", font=("Arial", 24)).pack(pady=20)
    available_ids = reshjo()
    res_var = ctk.StringVar(value="Select Resource")
    res_dropdown = ctk.CTkOptionMenu(content, values=available_ids if available_ids else ["No Available"], variable=res_var)
    res_dropdown.pack(pady=10)
    usere = ctk.CTkEntry(content, placeholder_text="User Name")
    usere.pack(pady=10)
    userole = ctk.StringVar(value="Student")
    type_dropdown = ctk.CTkOptionMenu(content, values=["Student", "Faculty"], variable=userole)
    type_dropdown.pack(pady=10)
    def submit(event=None):
        rid = res_var.get()
        uname = usere.get().strip()
        utype = userole.get()
        if rid in ["Select Resource", "No Available"] or uname == "":
            messagebox.showerror("Error", "Fill all fields")
            return
        with open("input.txt", "w") as f:
            f.write(f"3\n{rid} {uname} {utype}")
        run_backend()
        with open("output.txt", "r") as f:
            result = f.read()
        messagebox.showinfo("Result", result)
        usere.delete(0, "end")
    ctk.CTkButton(content, text="Submit", command=submit).pack(pady=20)
    content.bind("<Return>", submit)
def relre():
    screen()
    ctk.CTkLabel(content, text="Release Resource", font=("Arial", 24)).pack(pady=20)
    id_entry = ctk.CTkEntry(content, placeholder_text="Resource ID")
    id_entry.pack(pady=10)
    def submit(event=None):
        rid = id_entry.get().strip()
        if rid == "":
            messagebox.showerror("Error", "Enter ID")
            return
        with open("input.txt", "w") as f:
            f.write(f"4\n{rid}")
        run_backend()
        with open("output.txt", "r") as f:
            messagebox.showinfo("Result", f.read())
        id_entry.delete(0, "end")
    ctk.CTkButton(content, text="Submit", command=submit).pack(pady=20)
    content.bind("<Return>", submit)
def delre():
    screen()
    ctk.CTkLabel(content, text="Delete Resource", font=("Arial", 24)).pack(pady=20)
    idey = ctk.CTkEntry(content, placeholder_text="Resource ID")
    idey.pack(pady=10)
    def submit(event=None):
        rid = idey.get().strip()
        if rid == "":
            messagebox.showerror("Error", "Enter ID")
            return
        with open("input.txt", "w") as f:
            f.write(f"5\n{rid}")
        run_backend()
        with open("output.txt", "r") as f:
            messagebox.showinfo("Result", f.read())
        idey.delete(0, "end")
    ctk.CTkButton(content, text="Delete", command=submit).pack(pady=20)
    content.bind("<Return>", submit)
ctk.CTkLabel(sidebar, text="Menu", font=("Arial", 22)).pack(pady=20)
ctk.CTkButton(sidebar, text="Add Resource", command=addwin).pack(pady=12)
ctk.CTkButton(sidebar, text="View Resources", command=dekh).pack(pady=12)
ctk.CTkButton(sidebar, text="Allocate Resource", command=inuse).pack(pady=12)
ctk.CTkButton(sidebar, text="Release Resource", command=relre).pack(pady=12)
ctk.CTkButton(sidebar, text="Delete Resource", command=delre).pack(pady=12)
app.mainloop()
#forntend by SARTHAK SINGH AND KRISHNA UNIYAL.