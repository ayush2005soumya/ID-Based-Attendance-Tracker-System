# 🎓 ID Card Attendance Tracker System (Python + OpenCV + OCR + GUI)
A computer vision-based attendance system that uses OCR (Optical Character Recognition) to detect student ID cards through a webcam, mark attendance, log it daily, take snapshots, and optionally send notifications via email.

## ✅ Features

- 🔍 **Real-Time ID Card Scanning** via webcam using OpenCV and Tesseract OCR.
- 🧠 **OCR-Based ID Detection** with validation against registered students.
- 🗃️ **Student Database Management** via a simple admin panel.
- 📷 **Snapshot Logging** — saves a photo on each successful attendance.
- 📅 **Daily Log Files** and `attendance_status.csv` for total counts.
- 📤 **Email Alerts** when a student is marked present (optional).
- 📊 **GUI Interface** using Tkinter.
- 📁 Organized data storage (`logs/`, `photos/`, `students.csv`).

## 🧰 Requirements

- Python 3.8+
- Tesseract OCR installed (Windows users: [Download here](https://github.com/tesseract-ocr/tesseract))
- pip packages:
  pip install opencv-python pytesseract pandas pillow face_recognition
## 🏗️ Project Structure
📂 Attendane Tracker System

├── main.py                  # Launches the GUI

├── scanner.py               # Core webcam + OCR logic

├── admin.py                 # Admin panel for adding students

├── utils.py                 # Attendance logging & helper functions

├── notifier.py              # Email alert system

├── students.csv             # Registered student database

├── photos/                  # Saved snapshots of marked students

├── logs/                    # Daily attendance logs

├── attendance_status.csv    # Total attendance counts per student

# 🛠️ Setup Instructions
## Install Tesseract
Download and install Tesseract from https://github.com/tesseract-ocr/tesseract
## Update the path in scanner.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
## Install Python Packages
pip install opencv-python pytesseract pandas pillow face_recognition
## Run the App
python main.py
## 🧑‍💼 Admin Panel (Registering Students)
Click on Admin Panel in the GUI and enter:
ID
Name
Phone
Email (if using email alerts)
This will update students.csv.

## 📤 Email Alerts (Optional)
If you don’t want to use Twilio for SMS, use email alerts:
Update your Gmail/SMTP credentials in notifier.py.
Enable Less Secure App Access or App Passwords in your Google account.
The system will send attendance notifications to registered student emails.

## 📌 Notes
The system assumes student IDs start with 23U10 and are 8 characters long.
You can change this logic in utils.py → is_valid_id().
Logs are stored in logs/YYYY-MM-DD.csv.
Snapshots saved to photos/.

## 📸 Screenshots (Optional)
(Add screenshots here of the GUI and attendance detection)

## 📜 License
This project is for educational purposes. Customize or enhance it freely for your institution.
