import os,requests,json
def info():
	os.system('clear')
	print("NOOB IS BACK")
	ip = input(" INPUT IP ADDRESS : ")
	ipinfo = requests.post('http://ip-api.com/json/'+ip)
	z = json.loads(ipinfo.text)
	st = z['status']
	ccode = z['countryCode']
	reg = z['region']
	cty = z['city']
	tzone = z['timezone']
	isp = z['isp']
	ips = z['query']
	ass = z['as']
	org = z['org']
	ips = z['query']
	country = z['country']
	regi = z['regionName']
	if st == 'success':
		print('STATUS : '+st+'\nCOUNTRY CODE :  '+ccode+'\nREGION :   '+reg+'\nCITY :   '+cty+'\nTIME ZONE :   '+tzone+'\nINTERNET SUPPLYER :   '+isp+'\nIP ADDRESS :   '+ips+'\nINTERNET :   '+ass+'\nORG  '+org+'\nCOUNTRY :   '+country+'\nREGION NAME :   '+regi)
	else:
		print("NOT FOUND ")
info()
