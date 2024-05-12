import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("jakeydunning98@gmail.com", "DutchBitches!")
 
# message to be sent
message = "test email"
 
# sending the mail
s.sendmail("jakeydunning98@gmail.com", 
           "jacob_dunning@outlook.com", 
           message)
 
# terminating the session
s.quit()