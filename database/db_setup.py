#Database initialization and setup

import sqlite3

def init_db():
    conn = sqlite3.connect('email_campaign.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL,
            recipients TEXT NOT NULL,
            sent_at TEXT,
            open_rate INTEGER DEFAULT 0,
            click_rate INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()