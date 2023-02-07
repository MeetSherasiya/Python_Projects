import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('meetsherasiya256@gmail.com','Meetu@0256')
subject =  "Testing Mail"
body = "I Love Python"
massage = "subject:{}\n\n{}".format(subject,body)
listadd = ['meetsherasiya635@gmail.com']
ob.sendmail('meetsherasiya256@gmail.com', listadd, massage)
print("Send Mail")
ob.quit()