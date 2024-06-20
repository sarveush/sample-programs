import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender = "sarveushcandy@gmail.com"
receiver = "msarveush@gmail.com"
app_password = "clez ndqe hmhq vbne"  
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.starttls()
smtp_obj.login(sender, app_password)
message = MIMEMultipart("alternative")
message['Subject'] = "image attachment test"
message['From'] = sender
message['To'] = receiver
# html = f"""
#         <html>
#         <head>       
#         </head>
#         <body style="background-image: url("Screenshot 2024-06-18 104553.png"); background-size: cover; background-repeat: no-repeat;">
#             <p>This is your email content.</p>
#             # <a href="https://www.w3schools.com/">Click this here</a>
#         </body>
#         </html>
#         """
# htmlPart = MIMEText(html, 'html')
# message.attach(htmlPart)
image_path = "Screenshot 2024-06-18 104553.png"
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    imagePart = MIMEImage(image_data, 'jpg')
    imagePart.add_header('Content-ID', '<image_cid>')
    message.attach(imagePart)

smtp_obj.sendmail(sender, receiver, message.as_string())
smtp_obj.quit()
print('Email sent successfully!')








