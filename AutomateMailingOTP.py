""" this program will send OTP to the given email id 
    otp will be random and generated through the function """

# to test this program, firstly enter your original credentials like mailId and password

import smtplib
import random
def otpGenerator():
    numList=list(('0123456789'))
    otpList=list()
    for i in range(4):
        ran=random.choice(numList)
        otpList.append(ran)
    otp=''
    for i in otpList:
        otp=otp+i
    return otp


myMail='your_email@gmail.com'   #your emailId 
password='your_email_account_password'  #password coressponding to the entered mail id

toMail=input("\n Enter the email id : ")
# enter email id of that person, whom you want to send email

msg1='OTP for your initiated transaction is '
otp=otpGenerator()
msg2='.\nPlease, Do not enclose this OTP to anyone.'
msg=msg1+otp+msg2
""" 'msg1' and 'msg2' are the normal containers to store messages as
 strings. 'otp' variable will hold the returned otp as output of 
 the otpGenerator function """


server=smtplib.SMTP('smtp.gmail.com',587)
""" smtp.gmail.com  is the host and 587 is the port number"""

server.starttls()
""" this 'server.starttls()'  will start the 'transport layer
    security' which will encrypt the data while transferring"""


server.login(myMail, password)
""" here your entered credentials(email and password) are 
    in login function """

print("\n Login Success !")
""" When the email account get logged in via given password
    then the above message will print"""

server.sendmail(myMail,toMail , msg)
""" 'sendmail' is a function, which require your email_id and
    receiver's email and the message to send the mail """

print('\n Mail Sent !')