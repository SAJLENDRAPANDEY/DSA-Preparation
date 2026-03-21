import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('any emeail id','password')
subject='any write subject '
body='body of the message '
message="subject:{}\n\n{}".format(subject,body)
listadd=['list of multiple mail jisko mail krna h ']
ob.sendmail('login mail',listadd,message)
print("send mail")