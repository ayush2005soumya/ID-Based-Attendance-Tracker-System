import cv2
import os
import pytesseract
import threading
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import Label, Text, END
from utils import (
    is_valid_id, log_attendance, load_registered_students,
    send_email_alert, save_snapshot
)
import face_recognition

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class Scanner:
    def __init__(self, root):
        self.root = root
        self.label = Label(self.root)
        self.label.pack()
        self.status_box = Text(self.root, height=10, width=60)
        self.status_box.pack()
        self.running = True
        self.cap = cv2.VideoCapture(0)
        self.students = load_registered_students()
        threading.Thread(target=self.capture_loop).start()

    def capture_loop(self):
        last_seen = {}
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)

            found_id = False
            for line in text.splitlines():
                line = line.strip()
                if is_valid_id(line):
                    student_id = line
                    found_id = True
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    if student_id not in last_seen:
                        log_attendance(student_id, now)
                        save_snapshot(student_id, frame)
                        send_email_alert(student_id)
                        last_seen[student_id] = now
                        self.status_box.insert(END, f"✅ Marked: {student_id} at {now}\n")
                        self.status_box.see(END)

            if not found_id:
                self.status_box.insert(END, "⚠️ No valid ID detected\n")
                self.status_box.see(END)

            # Show frame
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.cap.release()
