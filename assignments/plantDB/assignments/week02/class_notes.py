"""
class notes

##WTF with ssh
ssh-add -l to see if key is there...

git: 
-can i push from any subfolder?
-why does push sometimes not work?
-can id_rsa hold private keys for more than one ssh account? or only one?
(id_rsa.work, id_rsa.home, id_rsa.work.pub, id_rsa.home.pub)

protocol notes
smtp, pop3, imap, http
imap can count sequence: doesn't have to wait for reply (from server? from client? both? not sure) before proceeding
"""

import smtplib

username = 'pantagrel'
password = 'th3tr335bl00m'
from_addr = 'bananarama <bananas@monkeytown.com>'
to_addrs = 'pantagrel@hotmail.com'
subject = 'this is the THE MESSAGE!!!! A MESSAGE! IN THE INBOX!!!!!'
message = 'salad for breakfast'
template = "from: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
headers = template % (from_addr, to_addrs, subject)
email_body = headers + message

server = smtplib.SMTP('smtp.hotmail.com', 587)
#  server = smtplib.SMTP('smtp.hotmail.com', 587) find the port for hotmail

server.set_debuglevel(True) #to see interaction
server.ehlo()
server.starttls()
server.ehlo() #re-identify after TLS begins
server.login(username, password)
server.sendmail(from_addr, [to_addrs, ], email_body)

server.close()
del server #clean up var server after closing it