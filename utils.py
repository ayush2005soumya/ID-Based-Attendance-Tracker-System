import os
import cv2
import pandas as pd
from datetime import datetime
from notifier import send_email_notification

BASE_DIR = os.getcwd()
LOG_DIR = os.path.join(BASE_DIR, "logs")
PHOTO_DIR = os.path.join(BASE_DIR, "photos")
CSV_PATH = os.path.join(BASE_DIR, "student.csv")
ATTENDANCE_PATH = os.path.join(BASE_DIR, "attendance_status.csv")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(PHOTO_DIR, exist_ok=True)

def is_valid_id(text):
    return text.startswith('23U10') and len(text) == 8 and text[5:].isdigit()

def load_registered_students():
    try:
        return pd.read_csv(CSV_PATH).set_index('ID').to_dict(orient='index')
    except FileNotFoundError:
        return {}

def log_attendance(student_id, timestamp):
    today = datetime.now().strftime('%Y-%m-%d')
    log_file = os.path.join(LOG_DIR, f"{today}.csv")

    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write("ID,Timestamp\n")
    with open(log_file, 'a') as f:
        f.write(f"{student_id},{timestamp}\n")

    if os.path.exists(ATTENDANCE_PATH):
        df = pd.read_csv(ATTENDANCE_PATH)
    else:
        df = pd.DataFrame(columns=['ID', 'Count'])

    if student_id in df['ID'].values:
        df.loc[df['ID'] == student_id, 'Count'] += 1
    else:
        df = pd.concat([df, pd.DataFrame([{'ID': student_id, 'Count': 1}])], ignore_index=True)

    df.to_csv(ATTENDANCE_PATH, index=False)

def send_email_alert(student_id):
    students = load_registered_students()
    if student_id in students and 'Email' in students[student_id]:
        email = students[student_id]['Email']
        msg = f"Attendance marked for {student_id} at {datetime.now().strftime('%H:%M:%S')}"
        send_email_notification(email, "Attendance Alert", msg)

def save_snapshot(student_id, frame):
    filename = os.path.join(PHOTO_DIR, f"{student_id}_{datetime.now().strftime('%H%M%S')}.jpg")
    cv2.imwrite(filename, frame)
