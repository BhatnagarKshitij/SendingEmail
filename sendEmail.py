import smtplib 
  
# list of email_id to send the mail 
listOfEmail = ["listofEmailId@yourmail.com"] 
  
for i in range(len(listOfEmail)): 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("YourEmailAddress", "Password") 
    message = "Message"
    s.sendmail("sender_email_id", li[i], message) 
    s.quit() 