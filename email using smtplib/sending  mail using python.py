import smtplib
sender = 'sarveushcandy@gmail.com'
password = 'clez ndqe hmhq vbne'
receiver = 'msarveush@gmail.com'
message = "welcome!"
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.starttls()
smtp_obj.login(sender,password)
smtp_obj.sendmail(sender,receiver,message)
print("successfully send mail!")
