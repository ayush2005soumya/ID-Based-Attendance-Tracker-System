import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
from dashboard_utils import open_csv_editor  # Reuse the GUI table editor
from tkinter import filedialog

STUDENT_FILE = r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\student.csv"

def register_student():
    reg_win = tk.Toplevel()
    reg_win.title("Register New Student")
    reg_win.geometry("500x500")
    reg_win.resizable(False, False)

    frame = tk.Frame(reg_win)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame, text="Name").grid(row=0, column=0, pady=5, sticky='e')
    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Student ID").grid(row=1, column=0, pady=5, sticky='e')
    student_id_entry = tk.Entry(frame, width=30)
    student_id_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Email").grid(row=2, column=0, pady=5, sticky='e')
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Phone").grid(row=3, column=0, pady=5, sticky='e')
    phone_entry = tk.Entry(frame, width=30)
    phone_entry.grid(row=3, column=1, pady=5)

    tk.Label(frame, text="Password").grid(row=4, column=0, pady=5, sticky='e')
    password_entry = tk.Entry(frame, show='*', width=30)
    password_entry.grid(row=4, column=1, pady=5)

    tk.Label(frame, text="Confirm Password").grid(row=5, column=0, pady=5, sticky='e')
    confirm_entry = tk.Entry(frame, show='*', width=30)
    confirm_entry.grid(row=5, column=1, pady=5)

    def register():
        name = name_entry.get()
        student_id = student_id_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if os.path.exists(STUDENT_FILE):
            with open(STUDENT_FILE, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if student_id == row[0] or email == row[2] or phone == row[3]:
                        messagebox.showerror("Error", "Student already registered.")
                        return

        with open(STUDENT_FILE, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, email, phone, password])
            messagebox.showinfo("Success", "Student registered successfully.")
            reg_win.destroy()

    tk.Button(frame, text="Register", width=20, command=register).grid(row=6, column=0, columnspan=2, pady=15)


def show_student_login():
    win = tk.Toplevel()
    win.title("Student Login")
    win.geometry("700x700")
    win.resizable(False, False)

    frame = tk.Frame(win)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame, text="Email").grid(row=0, column=0, pady=5, sticky='e')
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Phone").grid(row=1, column=0, pady=5, sticky='e')
    phone_entry = tk.Entry(frame, width=30)
    phone_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Password").grid(row=2, column=0, pady=5, sticky='e')
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.grid(row=2, column=1, pady=5)

    def login():
        email = email_entry.get()
        phone = phone_entry.get()
        password = password_entry.get()

        if not os.path.exists(STUDENT_FILE):
            messagebox.showerror("Error", "No students registered yet.")
            return

        with open(STUDENT_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == email and row[3] == phone and row[4] == password:
                    messagebox.showinfo("Login Success", f"Welcome, {row[1]}!")
                    open_student_dashboard(row[0])  # Pass student ID to dashboard
                    win.destroy()
                    return

        messagebox.showerror("Login Failed", "Incorrect credentials or not registered.")
        password_entry.delete(0, tk.END)

    tk.Button(frame, text="Login", width=20, command=login).grid(row=3, column=0, columnspan=2, pady=15)
    tk.Label(frame, text="Not registered?").grid(row=4, column=0, pady=5)
    tk.Button(frame, text="Register", width=15, command=register_student).grid(row=4, column=1, pady=5)


def open_student_dashboard(student_id):
    dash = tk.Toplevel()
    dash.title("Student Dashboard")
    dash.geometry("600x400")
    dash.configure(bg="#f9f9f9")

    tk.Label(dash, text=f"📚 Welcome, {student_id}", font=("Arial", 16, "bold"), bg="#f9f9f9").pack(pady=20)

    def view_total():
        open_csv_editor(r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\attendance_status.csv", title="Total Attendance")

    def view_today():
        today = datetime.now().strftime('%Y-%m-%d')
        today_file = os.path.join(r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\logs", f"{today}.csv")
        if os.path.exists(today_file):
            open_csv_editor(today_file, title="Today's Attendance")
        else:
            messagebox.showinfo("No Data", "No attendance recorded today.")

    tk.Button(dash, text="📊 View Total Attendance", width=30, font=("Arial", 12), command=view_total).pack(pady=10)
    tk.Button(dash, text="📅 View Today's Attendance", width=30, font=("Arial", 12), command=view_today).pack(pady=10)
