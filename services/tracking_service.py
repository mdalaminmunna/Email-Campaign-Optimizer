#Open and click tracking logic

import sqlite3

def track_opens(campaign_id):
    conn = sqlite3.connect('email_campaign.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE campaigns SET open_rate = open_rate + 1 WHERE campaign_id =?
        ''', (campaign_id,))
    conn.commit()
    conn.close()

def track_clicks(campaign_id):
    conn = sqlite3.connect('email_campaign.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE campaigns SET click_rate = click_rate + 1 WHERE campaign_id =?
        ''', (campaign_id,))
    conn.commit()
    conn.close()