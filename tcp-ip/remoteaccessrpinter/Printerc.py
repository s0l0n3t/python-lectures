#-*-coding:cp1254-*-
import socket
def yazdirma():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host="192.168.1.8"
    page = raw_input("Dosya :")
    port = 166
    ip=socket.gethostbyname(host)
    s.connect((ip,port))
    with open(page,"r") as leaf:
        setr = leaf.read(1024)
    s.sendto(setr,(ip,port))
    s.close()
    print "Yazdırma işlemi sunucuya başarıyla gö
yazdirma()
