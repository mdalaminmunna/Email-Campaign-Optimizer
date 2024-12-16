#Main application and API routes

from flask import Flask, render_template, request, jsonify
from database.db_setup import init_db
from services.ses_service import send_email_batch
from services.analytics_service import generate_metrics, visualize_metrics
from services.tracking_service import track_clicks, track_opens
import sqlite3

app = Flask(__name__)

#Initialize the database
init_db()

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    campaign_name = data.get('campaign_name')
    subject = data.get('subject')
    content = data.get('content')
    recipients = data.get('recipients') #List of emails

    if not all([campaign_name, subject, content, recipients]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    send_email_batch(campaign_name, subject, content, recipients)
    return jsonify({'message': 'Emails sent successfully'}), 200

@app.route('/analytics/<int:campaign_id>', methods=['GET'])
def analytics(campaign_id):
    metrics = generate_metrics(campaign_id)
    return jsonify(metrics), 200

@app.route('/visualize_metrics', methods=['GET'])
def visualize():
    visualize_metrics()
    return jsonify({'message': 'Metrics visualized and saved'}), 200

@app.route('/track/open/<int:campaign_id>', methods=['GET'])
def track_open(campaign_id):
    track_opens(campaign_id)
    return jsonify({'message': 'Opens tracked successfully'}), 200

@app.route('/track/click/<int:campaign_id>', methods=['GET'])
def track_click(campaign_id):
    track_clicks(campaign_id)
    return jsonify({'message': 'Clicks tracked successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)