import tkinter as tk
from scanner import Scanner
from admin import AdminPanel

def launch_gui():
    root = tk.Tk()
    root.title("ID Card Attendance Tracker")

    scanner = Scanner(root)
    admin_btn = tk.Button(root, text="Admin Panel", command=AdminPanel)
    admin_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
