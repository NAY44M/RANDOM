import random
ugen=[]
for txxxtt in range (10):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14','15'])
	c='vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,90)
	e='0'
	f=random.randrange(3000,5000)
	g=random.randrange(20,70)
	h='Mobile Safari/537.36'
	ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ffg)
print(ugen)