import tkinter as tk
import pandas as pd
from tkinter import messagebox

CSV_PATH = r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\student.csv'

def AdminPanel():
    win = tk.Toplevel()
    win.title("Admin Panel")

    tk.Label(win, text="Student ID:").grid(row=0, column=0)
    tk.Label(win, text="Name:").grid(row=1, column=0)
    tk.Label(win, text="Phone:").grid(row=2, column=0)
    tk.Label(win,text="Email:").grid(row=3, column=0)

    id_entry = tk.Entry(win)
    name_entry = tk.Entry(win)
    phone_entry = tk.Entry(win)
    email_entry = tk.Entry(win)
    id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    phone_entry.grid(row=2, column=1)
    email_entry.grid(row=3, column=1)

    def add_student():
        new_data = pd.DataFrame([{
            'ID': id_entry.get(),
            'Name': name_entry.get(),
            'Phone': phone_entry.get(),
            'Email': email_entry.get()
        }])

        try:
            df = pd.read_csv(CSV_PATH)
            df = pd.concat([df, new_data], ignore_index=True)
        except FileNotFoundError:
            df = new_data

        df.to_csv(CSV_PATH, index=False)
        messagebox.showinfo("Success", "Student added.")


    tk.Button(win, text="Add", command=add_student).grid(row=4, column=0, columnspan=2)
