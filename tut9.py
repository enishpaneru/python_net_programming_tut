# • A module for implementing the client side of an HTTP connection
import http.client as httplib
c = httplib.HTTPConnection("www.python.org",80)
c.putrequest("HEAD","/tut/tut.html")
c.putheader("Someheader","Somevalue")
c.endheaders()
r = c.getresponse()
data = r.read()
print(data)
c.close()
# • Low-level control over HTTP headers, methods, data transmission, etc.

# • A module for sending email messages
import smtplib
serv = smtplib.SMTP(host="smtp.gmail.com",port=25)
print('first')

serv.connect("smtp.gmail.com",587)
serv.ehlo()
serv.starttls()
serv.ehlo()

print('before')
serv.login('enishpaneru2017@gmail.com','newpw2017')
print('here')
msg = """\
From: dave@dabeaz.com
To: enishpaneru.ep@gmail.com
Subject: Get off my lawn!
Blah blah blah"""
serv.sendmail("enishpaneru2017@gmail.com",['paneruenish.ep@gmail.com'],msg)
# • Useful if you want to have a program send you a
# notification, send email to customers, etc.