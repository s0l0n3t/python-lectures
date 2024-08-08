import smtplib
from requests import get
import time

user = 'exampleemail@gmail.com'
psd = 'examplepassword'
msg = 'Hey, your ip has changed! Use this one from now on: '
currip = '0.0.0.0' # It'll send an email the first time you execute this aswell
while True:
    newip = get('https://api.ipify.org').text
    if currip == newip:
        print("nonewip")
        #You can just comment the line above this one if you want to
    else:
        tmpmsg = "\n"+msg + newip +" The old one used to be: "+currip
        currip = newip
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect('smtp.gmail.com')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user,psd)
        #You can change the second parameter, use ('from','to','message')
        server.sendmail(user, user, tmpmsg)

        server.quit()
        with open('/home/pi/DEV/iphistory.txt', 'a') as f:
            f.write('newip: '+currip+'\n')
            f.close()
        print('New IP Found: '+tmpmsg)
    time.sleep(7200)