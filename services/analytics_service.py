#Analytics calculations and reports

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def generate_metrics(campaign_id):
    conn = sqlite3.connect('email_campaign.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campaigns WHERE campaign_id =?", (campaign_id,))
    campaign = cursor.fetchone()
    conn.close()

    metrics = {
        'campaign_name': campaign[1],
        'open_rate': campaign[6],
        'click_rate': campaign[7],
    }
    return metrics

def visualize_metrics():
    conn = sqlite3.connect('email_campaign.db')
    campaign = pd.read_sql_query("SELECT * FROM campaigns", conn)
    conn.close()

    plt.bar(campaign['name'], campaign['open_rate'], label='Open Rate', color='blue')
    plt.bar(campaign['name'], campaign['click_rate'], label='Click Rate', color='green', alpha=0.7)
    plt.xlabel('Campaign Name')
    plt.ylabel('Rate (%)')
    plt.title('Campaign Performance Metrics')
    plt.legend()
    plt.savefig('static/metrics.png')