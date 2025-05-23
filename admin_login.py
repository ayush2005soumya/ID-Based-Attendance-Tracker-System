import tkinter as tk
from tkinter import messagebox
import csv
import os
import pandas as pd
from datetime import datetime
from tkinter import filedialog
from dashboard_utils import open_csv_editor

ADMIN_FILE = r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\admin_data.csv"

def register_window():
    reg_win = tk.Toplevel()
    reg_win.title("Register New Admin")
    reg_win.geometry("500x500")
    reg_win.resizable(False, False)

    # Center the frame for inputs
    frame = tk.Frame(reg_win)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame, text="Name").grid(row=0, column=0, pady=5, sticky='e')
    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Admin ID").grid(row=1, column=0, pady=5, sticky='e')
    admin_id_entry = tk.Entry(frame, width=30)
    admin_id_entry.grid(row=1, column=1, pady=5)

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
        admin_id = admin_id_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if os.path.exists(ADMIN_FILE):
            with open(ADMIN_FILE, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if admin_id == row[1] or email == row[2] or phone == row[3]:
                        messagebox.showerror("Error", "Admin already registered.")
                        return

        with open(ADMIN_FILE, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, admin_id, email, phone, password])
            messagebox.showinfo("Success", "Registration successful.")
            reg_win.destroy()

    tk.Button(frame, text="Register", width=20, command=register).grid(row=6, column=0, columnspan=2, pady=15)

def show():
    win = tk.Toplevel()
    win.title("Admin Login")
    win.geometry("700x700")
    win.resizable(False, False)

    # Center frame for inputs
    frame = tk.Frame(win)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame, text="Name").grid(row=0, column=0, pady=5, sticky='e')
    name_entry = tk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Phone").grid(row=1, column=0, pady=5, sticky='e')
    phone_entry = tk.Entry(frame, width=30)
    phone_entry.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Email").grid(row=2, column=0, pady=5, sticky='e')
    email_entry = tk.Entry(frame, width=30)
    email_entry.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Password").grid(row=3, column=0, pady=5, sticky='e')
    password_entry = tk.Entry(frame, show="*", width=30)
    password_entry.grid(row=3, column=1, pady=5)

    def login():
        phone = phone_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if not os.path.exists(ADMIN_FILE):
            messagebox.showerror("Error", "No admins registered yet.")
            # Just return, don't close the window
            return

        with open(ADMIN_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == email and row[3] == phone and row[4] == password:
                    messagebox.showinfo("Login Success", f"Welcome, {row[0]}!")
                    win.destroy()
                    open_admin_dashboard(row[0])  # Pass admin name
                    return


        # If no matching credentials found:
        messagebox.showerror("Login Failed", "Incorrect credentials or not registered.")
        password_entry.delete(0, tk.END)  # Clear password field for retry
        # Do NOT close the window here — so just return

    def open_admin_dashboard(admin_name):
        dash = tk.Toplevel()
        dash.title(f"Admin Dashboard - {admin_name}")
        dash.geometry("600x400")
        dash.resizable(False, False)

        tk.Label(dash, text=f"Welcome {admin_name}!", font=("Arial", 16)).pack(pady=20)

        card_frame = tk.Frame(dash)
        card_frame.pack(pady=30)

        # Define button style
        btn_style = {"font": ("Arial", 12), "width": 22, "height": 2, "bg": "#f0f0f0"}

        def view_total_attendance():
            open_csv_editor(r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\attendance_status.csv", title="Total Attendance")

        def view_todays_attendance():
            today = datetime.now().strftime('%Y-%m-%d')
            today_file = os.path.join(r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\logs", f"{today}.csv")
            if os.path.exists(today_file):
                open_csv_editor(today_file, title="Today's Attendance")
            else:
                messagebox.showinfo("Info", "No attendance recorded for today yet.")

        def edit_attendance():
            file_path = filedialog.askopenfilename(
                title="Select Attendance File to Edit",
                filetypes=[("CSV Files", "*.csv")],
                initialdir=r"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\logs"
            )
            if file_path:
                open_csv_editor(file_path, title="Edit Selected Attendance")


        tk.Button(card_frame, text="📋 See Total Attendance", command=view_total_attendance, **btn_style).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(card_frame, text="✏️ Edit Attendance", command=edit_attendance, **btn_style).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(card_frame, text="📅 See Today's Attendance", command=view_todays_attendance, **btn_style).grid(row=1, column=0, columnspan=2, pady=10)


    tk.Button(frame, text="Login", width=20, command=login).grid(row=4, column=0, columnspan=2, pady=15)
    tk.Label(frame, text="Are you registered?").grid(row=5, column=0, pady=5)
    tk.Button(frame, text="Register", width=15, command=register_window).grid(row=5, column=1, pady=5)
