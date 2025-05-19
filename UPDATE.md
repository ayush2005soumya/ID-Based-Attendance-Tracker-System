
# 🛠 UPDATE LOG – ID Card Attendance Tracker System

This document highlights all the major updates, feature additions, and improvements made to the project over time.

---

## 📅 May 2025

### ✅ Version 1.0 – Initial Features
- Implemented OCR-based attendance detection using **EasyOCR** and **Tesseract**.
- Attendance is logged with:
  - Timestamp
  - Snapshot of student ID
- Created **student.csv** for student record management.
- Attendance logs saved in:
  - `logs/YYYY-MM-DD.csv` (Daily logs)
  - `attendance_status.csv` (Cumulative count)

---

## ⚙️ Version 1.1 – Admin Panel
- Added `admin.py`:
  - Admin Panel GUI with entry fields for ID, Name, Phone, and Email.
  - Appends data to `student.csv`.
  - Handles creation if file is missing.

---

## 🎯 Version 1.2 – Email Notification System
- Integrated an email alert system without using third-party SMS APIs like Twilio.
- Sends attendance alert to the registered email using `smtplib`.

---

## 💡 Version 1.3 – GUI Enhancements
- Redesigned `main.py` layout:
  - Left side: Live camera tracking window.
  - Right side: Two panes showing:
    - 🔼 Upper half: Today's attendance log.
    - 🔽 Lower half: Total attendance summary.
- Added auto-refresh of CSV displays every 5 seconds.
- Integrated Admin Panel access directly from the main GUI via button.

---

## 🧠 Version 1.4 – Machine Learning Integration
- Integrated `easyocr` to enhance registration number recognition.
- Downloaded detection + recognition models locally to improve reliability and reduce repeated downloads.
- Increased accuracy of student ID detection over traditional OCR methods.

---

## 🔧 Fixes and Improvements
- Replaced deprecated Pandas `.append()` with `pd.concat()`.
- Fixed Unicode printing issues in Windows (`print(..., errors='ignore')`).
- Avoided threading-related `RuntimeError` by scheduling `tkinter` GUI updates on the main thread using `after()`.

---

## 📁 Directory Structure (Current)
```
Attendance Tracker System/
├── main.py
├── scanner.py
├── admin.py
├── utils.py
├── notifier.py
├── student.csv
├── logs/
│   └── 2025-05-XX.csv
├── attendance_status.csv
├── photos/
│   └── snapshot images
├── UPDATE.md
└── README.md
```

---
