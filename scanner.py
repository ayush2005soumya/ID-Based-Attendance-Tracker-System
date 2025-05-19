import cv2
import os
import easyocr
import threading
import pytesseract
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import Label, Text, END
from utils import (
    is_valid_id, log_attendance, load_registered_students,
    send_email_alert, save_snapshot
)
import face_recognition
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Ensure the Tesseract OCR path is set correctly if using pytesseract
# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=False)  # Ensure GPU=False unless using CUDA

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
        threading.Thread(target=self.capture_loop, daemon=True).start()

    def update_status(self, message):
        """Safely update the GUI from any thread."""
        self.status_box.insert(END, message)
        self.status_box.see(END)

    def capture_loop(self):
        last_seen = {}
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            results = reader.readtext(gray)

            found_id = False
            for bbox, text, conf in results:
                cleaned_text = text.strip().upper().replace(" ", "").replace("\n", "")
                if is_valid_id(cleaned_text):
                    student_id = cleaned_text
                    found_id = True
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    if student_id not in last_seen:
                        log_attendance(student_id, now)
                        save_snapshot(student_id, frame)
                        send_email_alert(student_id)
                        last_seen[student_id] = now
                        self.root.after(0, lambda sid=student_id, n=now: self.update_status(f"✅ Marked: {sid} at {n}\n"))

            if not found_id:
                self.root.after(0, lambda: self.update_status("⚠️ No valid ID detected\n"))

            # Show frame
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.cap.release()

    def stop(self):
        self.running = False
        self.cap.release()
