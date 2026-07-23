import os
import socket
os.system("clear")
question = input("""\33[91mAttack Tools:
(a1). darksploit-framework - Tool to run and create exploits.
(a2). powerdos - Denial-Of-Service tool.

\33[94mDefensive Tools:
(b1). bitb-framework - Browser in the browser attack framework.
(b2). cctvip - CCTVPIP camera database.
(b3). local2onion - Expose localhost on the darkweb using Tor.
(b4). maskme - URL masking tool.
(b5). shorturl - URL shortening tool.

\33[93mInformation Gathering:
(c1). darkcrawler - Crawl .onion sites through Tor and generate threat reports.
(c2). holehe - Email OSINT tool.
(c3). hound - Lightweight info gathering and GPS coordinate capture.
(c4). instaghost - Professional Instagram OSINT tool.
(c5). ipinfo - IP information gathering.
(c6). locateme - Live location tracker using Google Maps.
(c7). maigret - Check username availability.
(c8). numinfo - Phone number intelligence and lookup tool.
(c11). onionsearch - Scrape .onion URLs from various Tor search engines.
(c12). phoneinfo - Phone number information gathering tool.
(c13). sherlock - Username discovery tool.
(c14). tookie-osint - OSINT username search tool – scan 400+ social platforms.
(c15). webinfo - Website information gathering tool.
(c16). leaker - Passive leak enumeration tool.
(c17). web2ip - Website to IP tool.

\33[91mPassword Tools:
(d1). elpscrk - Password profiling tool inspired by the Mr. Robot series.
(d2). THC-Hydra - Parallelized login cracker supporting many protocols.

Social Engineering:
(e1). BeeF - Browser Exploitation Framework.
(e2). phishmailer - Professional Phishing Email Generation Tool.
(e3). sms-stealer - Silent SMS interceptor via Telegram bot.
(e4). setoolkit - Social Engineeeing toolkit.
(e5). the-theif - Hijack cookies and transmit them to Telegram.

\33[94mWeb Security and Tunneling:
(f1). afrog - Fast Vulnerability Scanner with PoC Support.
(f2). ngrok - Secure tunneling to localhost.

\33[91m(e). exit - This exits this script.

\33[97mPlease make a choice: """)
if question == "a1":
  os.system("darksploit-framework")
if question == "a2":
  os.system("powerdos")
  
if question == "b1":
  os.system("bitb-framework")
if question == "b2":
  os.system("cctvip")
if question == "b3":
  os.system("local2onion")
if question == "b4":
  os.system("maskme")
if question == "b5":
  os.system("shorturl")
  
if question == "c1":
  os.system("darkcrawler")
if question == "c4":
  os.system("holehe")
if question == "c5":
  os.system("hound")
if question == "c6":
  os.system("instsghost")
if question == "c7":
  os.system("python ~/ipinfo/ipinfo.py")
if question == "c8":
  os.system("locateme")
if question == "c9":
  os.system("maigret")
if question == "c10":
  os.system("numunfo")
if question == "c11":
  os.system("onionsearch")
if question == "c12":
  os.system("phoneinfo")
if question == "c13":
  os.system("sherlock")
if question == "c14":
  os.system("tookie-osint")
if question == "c15":
  os.system("webinfo")
if question == "c16":
  os.system("clear")
  which = input("(d)omain, (e)mail, (k)eyword, (p)hone, (u)sername?: ")
  if which == "d":
    os.system("clear")
    domain = input("What domain?: ")
    os.system("clear")
    os.system("cd ~ && cd go/bin && ./leaker domain " + domain)
  if which == "e":
    os.system("clear")
    email = input("What email?: ")
    os.system("clear")
    os.system("cd ~ && cd go/bin && ./leaker email " + email)
  if which == "k":
    os.system("clear")
    keyword = input("What keyword?: ")
    os.system("clear")
    os.system("cd ~ && cd go/bin && ./leaker keyword " + keyword)
  if which == "p":
    os.system("clear")
    phonenumber = input("What phone number?: ")
    os.system("clear")
    os.system("cd ~ && cd go/bin && ./leaker phone " + phonenumber)
  if which == "u":
    os.system("clear")
    username = input("What username?: ")
    os.system("clear")
    os.system("cd ~ && cd go/bin && ./leaker username " + username)
if question == "c17":
  os.system("clear")
  website = input("Please enter a website: ")
  os.system("clear")
  ip = socket.gethostbyname(website)
  print("The website IP is: " + ip)

if question == "d1":
  os.system("elpscrk")
if question == "d2":
  os.system("hydra")

if question == "e1":
  os.system("beef")
if question == "e2":
  os.system("phishmailer")
if question == "e3":
  os.system("sms-stealer")
if question == "e4":
  os.system("setoolkit")
if question == "e5":
  os.system("the-theif")

if question == "f1":
  os.system("afrog")
if question == "f2":
  os.system("ngrok")

if question == "e":
  os.system("clear")
  os.system("exit")