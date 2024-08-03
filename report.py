import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
EMAIL_ADDRESS = 'charinandan20@gmail.com'
EMAIL_PASSWORD = 'jcpa jbyd atui xicv'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Function to send email
def send_email(subject, body, to_address,file_path,custom_filename):
    for to_addresses in to_address:
        msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ','.join(to_addresses)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))
    
    if file_path:
        filename = file_path.split('/')[-1]  # Get the file name
        attachment = open(file_path, 'rb')  # Open the file as binary

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= "{custom_filename}"')

        msg.attach(part)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_address, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Function to generate report
def generate_report():
    html = """
<html>
  <body>
    <p>Hello,<br>
       This is a Daily Report on work.<br>
       <br>
           <span style="color:blue;">Thanks with Regards,</span><br>
           <b style="color:blue; font-size: 16px;">Karamala Revanandachari</b><br>
           <b style="color:blue; font-size: 16px;">Ph: +919642192992</b>
    </p>
  </body>
</html>
"""
    return html

# Job to send daily report
def job():
    subject = "Report on Automatic Email"
    body =generate_report()
    to_address = ['dhananjaya310@gmail.com','revanandh905@gmail.com']
    file_path= r'C:\Users\REVANANDA CHARI\Desktop\sales_data.csv'
    custom_filename='DailyReport.csv'
    send_email(subject, body, to_address,file_path,custom_filename)

# Schedule the job every day at 8:00 AM
schedule.every().day.at("16:46").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
