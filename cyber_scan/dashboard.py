from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = "cyber_scan/scans.db"


def get_scans():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT target, port, status, scan_time
        FROM scans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


@app.route("/")
def home():

    scans = get_scans()

    return render_template(
        "index.html",
        scans=scans
    )


if __name__ == "__main__":
    app.run(debug=True)