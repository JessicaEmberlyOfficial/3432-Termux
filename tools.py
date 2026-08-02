import os
import socket
import random
os.system("clear")
question = input("""
\33[93m//////////////////////////////////////////////////////
// /$$$$$$$$ /$$$$$$   /$$$$$$  /$$        /$$$$$$  //
//|__  $$__//$$__  $$ /$$__  $$| $$       /$$__  $$ //
//   | $$  | $$  \ $$| $$  \ $$| $$      | $$  \__/ //
//   | $$  | $$  | $$| $$  | $$| $$      |  $$$$$$  //
//   | $$  | $$  | $$| $$  | $$| $$       \____  $$ //
//   | $$  | $$  | $$| $$  | $$| $$       /$$  \ $$ //
//   | $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/ //
//   |__/   \______/  \______/ |________/ \______/  //
//////////////////////////////////////////////////////
\33[91mAttack Tools:
(a1). darksploit-framework - Tool to run and create exploits.
(a2). Ransomware - A tool to create Ransomware.
(a3). powerdos - Denial-Of-Service tool.
(a4). GoldenEye - Denial-Of-Service tool.
(a5). EliteToolKit - Denial-Of-Service tool.

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
(d2). GoblinWordGnerator - Password profiling tool similar to elpscrk.
(d3). THC-Hydra - Parallelized login cracker supporting many protocols.
(d4). Instagram Bruter - Instagram bruteforcing tool.
(d5). SMTP Tester - A tool to brute force an SMTP server account.

Social Engineering:
(e1). BeeF - Browser Exploitation Framework.
(e2). phishmailer - Professional Phishing Email Generation Tool.
(e3). sms-stealer - Silent SMS interceptor via Telegram bot.
(e4). setoolkit - Social Engineeeing toolkit.
(e5). the-theif - Hijack cookies and transmit them to Telegram.

\33[94mWeb Security and Tunneling:
(f1). afrog - Fast Vulnerability Scanner with PoC Support.
(f2). ngrok - Secure tunneling to localhost.

\33[93mCase Development:
(g1). cng - Case number generator.

\33[91m(e). exit - This exits this script.

\33[97mPlease make a choice: """)
if question == "a1":
  os.system("clear")
  os.system("darksploit-framework")
if question == "a2":
  os.system("cd " + os.getcwd() + "/Ransomware/ && python3 Ransomware")
if question == "a3":
  os.system("clear")
  os.system("powerdos")
if question == "a4":
  os.system("clear")
  useragents = input("Do you want to use the default user agents? (y, or n): ")
  if useragents == "y":
    os.system("clear")
    target = input("Please specify a domain for a target (e.g. https://www.website.com): ")
    os.system("clear")
    workers = input("How many workers? (default: 10): ")
    os.system("clear")
    sockets = input("How many sockets? (default: 500): ")
    os.system("clear")
    method = input("Which method? (get, post, or random): ")
    os.system("clear")
    verify = input("Do you want to verify SSL certificate? (True, or False): ")
    os.system("clear")
    debug = input("Do you want debug enabled? (True, or False): ")
    os.system("clear")
    os.system("python " + os.getcwd() + "/GoldenEye/goldeneye.py " + target + " -w " + workers + " -s " + sockets + " -m " + method + " -n " + verify + " -d " + debug)
  if useragents == "n":
    os.system("clear")
    target = input("Please specify a domain for a target (e.g. https://www.website.com): ")
    os.system("clear")
    uafile = input("Please specify a file for user agents: ")
    os.system("clear")
    workers = input("How many workers? (default: 10): ")
    os.system("clear")
    sockets = input("How many sockets? (default: 500): ")
    os.system("clear")
    method = input("Which method? (get, post, or random): ")
    os.system("clear")
    verify = input("Do you want to verify SSL certificate? (True, or False): ")
    os.system("clear")
    debug = input("Do you want debug enabled? (True, or False): ")
    os.system("clear")
    os.system("python " + os.getcwd() + "/GoldenEye/goldeneye.py " + target + " -u " + os.getcwd() + "/" + uafile + " -w " + workers + " -s " + sockets + " -m " + method + " -n " + verify + " -d " + debug)
if question == "a5":
  os.system("clear && python " + os.getcwd() + "/EliteToolKit/elitekitv1.py")

if question == "b1":
  os.system("clear")
  os.system("bitb-framework")
if question == "b2":
  os.system("clear")
  os.system("cctvip")
if question == "b3":
  os.system("clear")
  os.system("local2onion")
if question == "b4":
  os.system("clear")
  os.system("maskme")
if question == "b5":
  os.system("clear")
  os.system("shorturl")
  
if question == "c1":
  os.system("clear")
  os.system("darkcrawler")
if question == "c4":
  os.system("clear")
  os.system("holehe")
if question == "c5":
  os.system("clear")
  os.system("hound")
if question == "c6":
  os.system("clear")
  os.system("instsghost")
if question == "c7":
  os.system("clear")
  os.system("python " + os.getcwd() + "/ipinfo/ipinfo.py")
if question == "c8":
  os.system("clear")
  os.system("locateme")
if question == "c9":
  os.system("clear")
  os.system("maigret")
if question == "c10":
  os.system("clear")
  os.system("numunfo")
if question == "c11":
  os.system("clear")
  os.system("onionsearch")
if question == "c12":
  os.system("clear")
  os.system("phoneinfo")
if question == "c13":
  os.system("clear")
  username = input("What username do you want to search?: ")
  os.system("clear && cd sherlock && ./sherlock " + username)
if question == "c14":
  os.system("clear")
  os.system("tookie-osint")
if question == "c15":
  os.system("clear")
  os.system("webinfo")
if question == "c16":
  os.system("clear")
  os.system("clear")
  which = input("(d)omain, (e)mail, (k)eyword, (p)hone, (u)sername?: ")
  if which == "d":
    os.system("clear")
    domain = input("What domain?: ")
    os.system("clear")
    os.system("cd ~ && cd ~/go/bin && ./leaker domain " + domain)
  if which == "e":
    os.system("clear")
    email = input("What email?: ")
    os.system("clear")
    os.system("cd ~ && cd ~/go/bin && ./leaker email " + email)
  if which == "k":
    os.system("clear")
    keyword = input("What keyword?: ")
    os.system("clear")
    os.system("cd ~ && cd ~/go/bin && ./leaker keyword " + keyword)
  if which == "p":
    os.system("clear")
    phonenumber = input("What phone number?: ")
    os.system("clear")
    os.system("cd ~ && cd ~/go/bin && ./leaker phone " + phonenumber)
  if which == "u":
    os.system("clear")
    username = input("What username?: ")
    os.system("clear")
    os.system("cd ~ && cd ~/go/bin && ./leaker username " + username)
if question == "c17":
  os.system("clear")
  website = input("Please enter a website: ")
  os.system("clear")
  ip = socket.gethostbyname(website)
  print("The website IP is: " + ip)

if question == "d1":
  os.system("clear")
  os.system("elpscrk -x " + os.getcwd() + "/passwords.txt")
if question == "d2":
  os.system("clear && cd " + os.getcwd() + "/GoblinWordGenerator && python3 goblin.py")
if question == "d3":
  os.system("clear")
  os.system("hydra")
if question == "d4":
  os.system("clear")
  username = input("What is the username?: ")
  os.system("clear")
  passlist = input("Where is your passlist? (e.g. ~/mypasslist.txt): ")
  os.system("clear && cd " + os.getcwd() + "/instabruteforce && python -u " + username + "-p " + passlist)
if question == "d5":
  os.system("clear && cd SMTP_Tester && python smtp_tester.py")
  
if question == "e1":
  os.system("clear")
  os.system("beef")
if question == "e2":
  os.system("clear")
  os.system("phishmailer")
if question == "e3":
  os.system("clear")
  os.system("sms-stealer")
if question == "e4":
  os.system("clear")
  os.system("setoolkit")
if question == "e5":
  os.system("clear")
  os.system("the-theif")

if question == "f1":
  os.system("clear")
  os.system("afrog")
if question == "f2":
  os.system("clear")
  os.system("ngrok")

if question == "g1":
  os.system("clear")
  number = random.randint(1, 9)
  initial = input("Please input the first, middle, and last initial of the POI (e.g. pcp): ")
  os.system("clear")
  state = input("Please input the state of the POI (e.g. KS): ")
  file = os.getcwd() + "/casenumber.txt"
  if os.path.isfile(file):
    with open(file, "r") as f:
      current_number = f.read()
      new_number = int(current_number)
      new_number += 1
      os.system("clear")
      print("Your case number is: " + initial + "-" + state + "-" + str(new_number))
      f.close()
    with open(file, "w") as f:
      f.write("" + str(new_number))
  else:
    with open(file, "w") as f:
      number = f.write("1")
      os.system("clear")
      print("Your case number is: " + initial + "-" + state + "-1")

if question == "e":
  os.system("clear")
  os.system("exit")