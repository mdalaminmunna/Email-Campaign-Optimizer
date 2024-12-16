#Amazon SES integration and email sending

import boto3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database.queries import log_email_campaign

ses_client = boto3.client('ses', region_name='us-east-1')

def send_email_batch(campaign_name, subject, content, recipients):
    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = 'example@example.com'
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'html'))

        #Send email via SES
        ses_client.send_raw_email(
            Source='example@example.com',
            Destinations=[recipient],
            RawMessage={'Data': msg.as_string()}
        )
    
    #Log the campaign in the database
    log_email_campaign(campaign_name, subject, content, recipients)