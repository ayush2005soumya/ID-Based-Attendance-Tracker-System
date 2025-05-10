import os
import cv2
import pandas as pd
from datetime import datetime
from notifier import send_email_notification

def is_valid_id(text):
    return text.startswith('23U10') and len(text) == 8

def load_registered_students():
    try:
        return pd.read_csv(r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\student.csv').set_index('ID').to_dict(orient='index')
    except FileNotFoundError:
        return {}

def log_attendance(student_id, timestamp):
    # Create logs directory
    os.makedirs(r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\logs', exist_ok=True)
    folder_path = r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System'
    os.path.join(folder_path, "attendance_status.csv")
    # 1. Daily log
    today = datetime.now().strftime('%Y-%m-%d')
    log_path = rf'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\logs/{today}.csv'
    
    if not os.path.exists(log_path):
        with open(log_path, 'w') as f:
            f.write("ID,Timestamp\n")
    
    with open(log_path, 'a') as f:
        f.write(f"{student_id},{timestamp}\n")

    # 2. Total attendance
    status_path = r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\attendance_status.csv'
    if os.path.exists(status_path):
        df = pd.read_csv(status_path)
    else:
        df = pd.DataFrame(columns=['ID', 'Count'])

    if student_id in df['ID'].values:
        df.loc[df['ID'] == student_id, 'Count'] += 1
    else:
        new_row = pd.DataFrame([{'ID': student_id, 'Count': 1}])
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(status_path, index=False)
    
def send_email_alert(student_id):
    students = load_registered_students()
    if student_id in students:
        email = students[student_id]['Email']
        msg = f"Attendance marked for {student_id} at {datetime.now().strftime('%H:%M:%S')}"
        send_email_notification(email, "Attendance Alert", msg)


def save_snapshot(student_id, frame):
    os.makedirs(r'G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\photos', exist_ok=True)
    filename = rf"G:\MY PROJECTS\OPENCV PROJECTS\Attendane Tracker System\photos/{student_id}_{datetime.now().strftime('%H%M%S')}.jpg"
    cv2.imwrite(filename, frame)
