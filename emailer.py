import smtplib
from email.mime.text import MIMEText

def send_email(device_info):
    sender_email = "youremail@example.com"
    receiver_email = "recipient@example.com"
    subject = "New Device Detected"
    body = f"New device detected: {device_info}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email using your SMTP server
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'yourpassword')
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Example device info to send
device_info = "SSID: MyWiFi, BSSID: 00:14:22:01:23:45"
send_email(device_info)
