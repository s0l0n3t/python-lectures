#-*-coding:cp1254-*-

import socket
import os

class info:
    host = raw_input("Host :")
    port = 172

info = info()
def right():
   for i in xrange(15):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((info.host,info.port))
    dosya = open("recv.txt","a")
    s.listen(15)
    print "Emir bekleniyor..."
    for i in xrange(1):
        server,addr = s.accept()
        os.system("Cls")
        listening = server.recv(1024)
        dosya.write(listening) and dosya.write("\n")
        dosya.close()
        os.startfile("recv.txt","print")
        port += 1
#server'a client yardımıyla bağlanılacak ve printerdan yazı çıkartılacak.
        server.close()
    exit()

right()

