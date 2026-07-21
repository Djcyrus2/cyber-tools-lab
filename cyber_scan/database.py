import sqlite3
from datetime import datetime


DATABASE = "cyber_scan/scans.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        port INTEGER,
        status TEXT,
        scan_time TEXT
    )
    """)

    conn.commit()
    conn.close()



def save_scan(target, port, status):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scans
    (target, port, status, scan_time)

    VALUES (?, ?, ?, ?)
    """,
    (
        target,
        port,
        status,
        str(datetime.now())
    ))

    conn.commit()
    conn.close()



def show_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM scans"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()