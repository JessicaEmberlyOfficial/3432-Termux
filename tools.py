import os
os.system("clear")
question = input("""
Attack Tools:
(a1). darksploit-framework - Tool to run and create exploits.
(a2). powerdos - Denial-Of-Service tool.

Defensive Tools:
(b1). bitb-framework - Browser in the browser attack framework.
(b2). cctvip - CCTVPIP camera database.
(b3). local2onion - Expose localhost on the darkweb using Tor.
(b4). maskme - URL masking tool.
(b5). shorturl - URL shortening tool.

Information Gathering:
(c1). darkcrawler - Crawl .onion sites through Tor and generate threat reports.
(c2). dorks-eye - Google dorking tool.
(c3). holehe - Email OSINT tool.
(c4). hound - Lightweight info gathering and GPS coordinate capture.
(c5). instaghost - Professional Instagram OSINT tool.
(c6). ipinfo - IP information gathering.
(c7). locateme - Live location tracker using Google Maps.
(c8). maigret - Check username availability.
(c9). numinfo - Phone number intelligence and lookup tool.
(c10). onionsearch - Scrape .onion URLs from various Tor search engines.
(c11). phoneinfo - Phone number information gathering tool.
(c12). sherlock - Username discovery tool.
(c13). tookie-osint - OSINT username search tool – scan 400+ social platforms.
(c14). webinfo - Website information gathering tool.

Password Tools:
(d1). elpscrk - Password profiling tool inspired by the Mr. Robot series.

Social Engineering:
(e1). BeeF - Browser Exploitation Framework.
(e2). phishmailer - Professional Phishing Email Generation Tool.
(e3). sms-stealer - Silent SMS interceptor via Telegram bot.
(e4). setoolkit - Social Engineeeing toolkit.
(e5). the-theif - Hijack cookies and transmit them to Telegram.

Web Security and Tunneling:
(f1). afrog - Fast Vulnerability Scanner with PoC Support.
(f2). ngrok - Secure tunneling to localhost.

Please make a choice: """)
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
if question == "c2":
  os.system("dorks-eye")
if question == "c3":
  os.system("holehe")
if question == "c4":
  os.system("hound")
if question == "c5":
  os.system("instsghost")
if question == "c6":
  os.system("python ~/ipinfo/ipinfo.py")
if question == "c7":
  os.system("locateme")
if question == "c8":
  os.system("maigret")
if question == "c9":
  os.system("numunfo")
if question == "c10":
  os.system("onionsearch")
if question == "c11":
  os.system("phoneinfo")
if question == "c12":
  os.system("sherlock")
if question == "c13":
  os.system("tookie-osint")
if question == "c14":
  os.system("webinfo")

if question == "d1":
  os.system("elpscrk")

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