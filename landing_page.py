import tkinter as tk
from tkinter import messagebox
import admin_login
import student_login
import main
def open_admin_login():
    admin_login.show()

def open_student_login():
    student_login.show_student_login()

def open_main_app():
    root1 = tk.Toplevel()
    root1.title("Main Application")
    app = main.AttendanceApp(root1)


def show():
    root = tk.Tk()
    root.title("Attendance Tracker App")
    root.geometry("700x700")

    tk.Label(root, text="Welcome to Attendance Tracker App", font=("Courier New", 20)).pack(pady=20)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    admin_card = tk.Frame(frame, bd=2, relief="groove", padx=20, pady=20)
    admin_card.grid(row=0, column=0, padx=20)
    tk.Label(admin_card, text="👨🏻‍💼\nAdmin Login", font=("Garamond", 14)).pack()
    tk.Button(admin_card, text="Login", command=open_admin_login,bg="lightblue",fg="black").pack(pady=10)

    student_card = tk.Frame(frame, bd=2, relief="groove", padx=20, pady=20)
    student_card.grid(row=0, column=1, padx=20)
    tk.Label(student_card, text="👩🏻‍🎓\nStudent Login", font=("Garamond", 14)).pack()
    tk.Button(student_card, text="Login", command=open_student_login,bg="lightblue",fg="black").pack(pady=10)

    main_card = tk.Frame(frame, bd=2, relief="groove", padx=20, pady=20)
    main_card.grid(row=0, column=2, columnspan=2, pady=20)
    tk.Label(main_card, text="📚\nTake Attendance", font=("Garamond", 14)).pack()
    tk.Button(main_card, text="Open", command=open_main_app,bg="lightblue",fg="black").pack(pady=10)


    tk.Button(root, text="Exit", command=root.quit,bg="lightblue",fg="black").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    show()