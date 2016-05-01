#! usr/bin/env python2
#-*-coding:cp1254-*-
#github.com/s0l0n3t/modules

import hashlib
import sys
import os
import urllib2
import urllib
import re


logo = ''' \t   ##################################################
           #         MD5 Encode // Decode tool 
           #        
           #             encode --> encoding to md5 hash
           #             decode --> decoding md5 to ascii
           #             help --> importing database
                         exit --> exiting script
'''

print logo

def urldata():
    md5 = raw_input(" :")
    site = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
    data =  urllib.urlencode({"md5":md5})
    request = urllib2.Request(site)
    response = urllib2.urlopen(request,data)
    payload = response.read()
    results = re.findall("<div class='white_bg_title'><span class='middle_title'>Hashed string</span>: (.*?)</div>", payload)
    if results:
        if md5.isalnum() and md5 != "\n" and len(md5) == 32:
            for result in results:
                print "############"
                print "##MD5 HASH##"
                print "############"
                print "\n%s"%(result)
    else :
        print "Veri tabanında bulunamadı"


def pythondata():
    data = raw_input(" :")
    print
    database = hashlib.md5(data)
    hash = database.hexdigest()
    print "%s ---> MD5 ---> %s"%(data,hash)
    print
    return


    
while True:
    if os.name == "posix":
        os.system("clear")

    else:
        if __name__ == "__main__":
            user= raw_input("encode or decode :")
            if user == "decode":
                urldata()
            
            elif user == "encode":
                pythondata()
            
            elif user == "help":
                print
                print ''' url database : http://md5.my-addr.com/ '''
            
            elif user == "exit":
                sys.exit()

            else:
                print
                print "No commands."
            
