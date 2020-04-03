import smtplib


sender_email="manishsinghbhadouria34@gmail.com"
password="manish1234"
reciever_email="manishsinghbhadouria4@gmail.com"
message="Hello"


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.sendmail(sender_email,reciever_email,message)

    



