import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, html_file_path):
    # Create a multipart message
    message = MIMEMultipart()

    # Setup the parameters of the message
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Read the HTML file
    with open(html_file_path, 'r') as html_file:
        html_content = html_file.read()

    # Attach HTML content
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    # Create SMTP session
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the SMTP server
        server.login(sender_email, sender_password)
        
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

    finally:
        # Quit the SMTP server
        server.quit()

# Example usage
sender_email = 'sarveushcandy@gmail.com'
sender_password = 'clez ndqe hmhq vbne'  # App password if using Gmail
receiver_email = 'msarveush@gmail.com'
subject = 'HTML File Test'

html_file_path = 'index.html'  # Adjust your file path here
html_file_path = html_file_path.replace("\\", "/")

# Function Call
send_email(sender_email, sender_password, receiver_email, subject, html_file_path)