###----[ LIST INFOMASI ]----###
author  = 'Rochmat Basuki'
git_hub = 'github.com/RozhBasXYZ'
version = 'project closed'

###---[ IMPORT LIBRARY]----###
import time, sys, random, os, datetime
from datetime import datetime as DT
from time import sleep
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')

###---[ LOGO ]---###
def logo():
	return str(pyfiglet.figlet_format(' FREE  BLADE'))

###----[ BERSIH LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	
###---[ JAM ]---###
def waktu():
	a=time.localtime()     
	hr=a.tm_hour     
	mn=a.tm_min     
	sc=a.tm_sec     
	return ('{}:{}:{}'.format(hr,mn,sc))

###----[ WARNA ]----###
M = '\033[91m'
K = '\033[93m'
H = '\033[92m'
B = '\033[94m'
C = '\033[96m'
U = '\033[93m'
P = '\033[00m'

###----[ GATAU ]----###
class make:
	def __init__(self):
		self.rc = random.choice
		self.jam = waktu()
		self.ran = self.rc([M,K,H,B,C])
		self.wal = DT.now()
		self.logo = logo()
		self.blade = ['i     ','i love        ','i love you   ','i love you aww','                  ']
		self.main()
	def main(self):
		ahir = str(DT.now()-self.wal).split('.')[0]
		print(self.logo)
		name = input(f'\n [%s<%s] hai selamat datang, siapa nama kamu? \n nama : %s'%(H,P,K))
		clear_layar()
		print('%s'%(P)+self.logo)
		print(f' \n %shai %s%s%s, mohon maaf script ini telah di tutup permanen'%(P,K,name,P))
		print(f' %sdi karnakan script ini di perjual belikan kembali oleh\n beberapa oknum / pihak yang tidak bertanggung jawab'%(P))
		print(' mohon maaf bila hal ini tidak berkenan di anda')
		while True:
			for x in self.blade:
				sys.stdout.write('\r [%s!%s] sampai jumpa di next free blade, %s%s%s'%(H,P,self.ran,x,P));sys.stdout.flush();sleep(1)
		

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	clear_layar()
	make()
