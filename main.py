import tkinter as tk
from scanner import Scanner
from admin import AdminPanel
import pandas as pd
import os
from datetime import datetime

BASE_PATH = r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System'
LOG_DIR = os.path.join(BASE_PATH, 'logs')
TOTAL_ATTENDANCE_PATH = os.path.join(BASE_PATH, 'attendance_status.csv')

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ID Card Attendance Tracker")

        # Main layout frames
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Scanner widget in left frame
        self.scanner = Scanner(self.left_frame)

        # Admin Panel Button
        self.admin_btn = tk.Button(self.left_frame, text="Admin Panel", command=AdminPanel)
        self.admin_btn.pack(pady=10)

        # Right frame split into top and bottom halves
        self.top_right = tk.LabelFrame(self.right_frame, text="Today's Logs", padx=5, pady=5)
        self.top_right.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        self.bottom_right = tk.LabelFrame(self.right_frame, text="Total Attendance", padx=5, pady=5)
        self.bottom_right.pack(fill=tk.BOTH, expand=True)

        # Text boxes
        self.log_text = tk.Text(self.top_right, height=15, width=60)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        self.total_text = tk.Text(self.bottom_right, height=15, width=60)
        self.total_text.pack(fill=tk.BOTH, expand=True)

        # Refresh logs every few seconds
        self.update_csv_views()
        self.root.after(5000, self.periodic_update)

    def update_csv_views(self):
        today = datetime.now().strftime('%Y-%m-%d')
        log_path = os.path.join(LOG_DIR, f'{today}.csv')

        # Update today's log
        try:
            with open(log_path, 'r') as f:
                self.log_text.delete('1.0', tk.END)
                self.log_text.insert(tk.END, f.read())
        except FileNotFoundError:
            self.log_text.delete('1.0', tk.END)
            self.log_text.insert(tk.END, "No log found for today.")

        # Update total attendance
        try:
            df = pd.read_csv(TOTAL_ATTENDANCE_PATH)
            self.total_text.delete('1.0', tk.END)
            self.total_text.insert(tk.END, df.to_string(index=False))
        except FileNotFoundError:
            self.total_text.delete('1.0', tk.END)
            self.total_text.insert(tk.END, "No total attendance file found.")

    def periodic_update(self):
        self.update_csv_views()
        self.root.after(5000, self.periodic_update)


if __name__ == '__main__':
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
