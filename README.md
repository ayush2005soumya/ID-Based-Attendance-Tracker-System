
# 🧑‍💼 ID Card Attendance Tracker System

A smart, GUI-based attendance system using Python, OpenCV, and OCR to scan student ID cards, verify registered users, log attendance, send email alerts, and provide detailed dashboards for both students and admins.

---

## 📦 Features

- ✅ ID Card OCR using EasyOCR
- 🧾 Student/Admin Registration & Login System
- 📸 Auto Snapshot Capture on Attendance
- 📊 Daily & Total Attendance Logs (CSV)
- 📧 Email Notification for Attendance
- 🧑‍💻 GUI built with Tkinter
- 📂 Photo & Log Auto-Organization
- 🔐 Secure password validation

---
## 📦 Download
The Latest version is released in GitHub. Anyone can Download it and use it.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ayush2005soumya/ID-Based-Attendance-Tracker-System.git
cd attendance-tracker
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Dependencies include**:  
> `opencv-python`, `easyocr`, `pandas`, `tkinter`, `numpy`, `Pillow`, `smtplib`, `email-validator`

### 4. Download EasyOCR Language Model (First Use)

```python
import easyocr
reader = easyocr.Reader(['en'])  # This downloads model files
```

---

## 🚀 Run the App

```bash
python landing_page.py
```

---

## 📁 Project Structure

```
attendance-tracker/
├── landing_page.py         # Main entry GUI
├── main.py                 # Main app UI logic
├── scanner.py              # OCR, webcam & attendance logic
├── admin_login.py          # Admin GUI & dashboard
├── student_login.py        # Student GUI & dashboard
├── utils.py                # Helpers for logging, email, snapshots
├── dashboard_utils.py      # CSV table viewer GUI
├── notifier.py             # Email alert logic
├── student.csv             # Registered student data
├── attendance_status.csv   # Total attendance data
├── logs/                   # Daily CSV logs
├── photos/                 # Attendance snapshots
└── requirements.txt        # Python dependencies
```

---

## 🔒 Data Storage

- All user data is stored in local CSV files.
- Snapshots are auto-saved in `/photos`.
- Daily logs in `/logs/YYYY-MM-DD.csv`.

---

## ✉️ Email Setup

To enable email alerts:
1. Set your sender email and password in `notifier.py`
2. Use app password if 2FA is enabled on Gmail
