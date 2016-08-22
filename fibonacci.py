def fib_1(max):
	a,b = 0,1

	while(a<max):
		print(a)
		a ,b = b, a+b  

fib_1(10) 

def fib_3(max): 
	a,b  = 0,1 

	while (a<max):
		yield a
		a,b =b,a+b

for n in fib_3(10):
	print(n)

