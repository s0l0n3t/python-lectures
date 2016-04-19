#-*-coding:cp1254-*-
#s0l0n3t
import re
import urllib2 , urllib
import time



helping = ''' I have been pondering this question for some time now. What does it mean to disconnect? We all say we need to. We all believe connections healthy for us (any research out there?). What does it truly mean to disconnect.
                Are you consuming, using or creating with technology?
        You can test
                http://www.ip-adress.eu '''



while True:
        try:
                site = urllib2.urlopen("http://www.ip-adress.eu")
                for i in site:
            
                    ipv4 = re.search('''color: #000;">.+''',i)
                    dns = re.search('''"Reverse DNS">.+''',i)
                    proxy = re.search('''<div style="color: #a6cb11; font-weight: bold;">.+</div>''',i)
                    if ipv4:
                        ip = ipv4.group()[14:]
                        filter_ip = ip[:12]
                        print " ipv4 --> %s"%(filter_ip)
                    if dns:
                        dns = dns.group()[14:]
                        filter_dns = dns[:33]
                        print " dns adress --> %s"%(filter_dns)
                        
                    if proxy:
                        proxy = proxy.group()[48:]
                        filter_proxy = proxy[:17]
                        print " proxy adress --> %s"%(filter_proxy)
                        print
                        time.sleep(50)
        
        except KeyboardInterrupt:
                sys.exit()
                
        except :
                print "Disconnected"
                print
                print "Connection failed.Please test your connection"
                help = raw_input("more help (help or h) :")
                if help == "help" or "h":
                        print
                        print helping
                        time.sleep(1000)
                        break
                else:
                        break
        
#only there.but i will do it . İ haven't got any time
                
                
        
