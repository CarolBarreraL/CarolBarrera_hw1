import numpy as np
import matplotlib.pyplot as plt

#Funcion con 10 variables aleatorias
def funcion():
	c=0
	variables=[]
	while c<10:
		x = np.random.rand()*2
		variables.append(x)
		c+=1
	return (sum(variables))**3

# Intervalo integral
a=0 
b=2
#N es el numero de puntos utilizado para calcular la integral
def Integral(N):
	valores=[]
	n=0
	while n<N:
		valores.append(funcion())
		n+=1
	area= (b-a)**10 #elevado por la dimension de la funcion
	return (sum(valores)/N)*area 

#resultado de la integral por el promedio de repetir el metodo anterior 20 veces
def ResultadoInt(N):
	s=0
	re=[]
	while s<20:
		re.append(Integral(N))
		s+=1
	return sum(re)/20

def num_integral():
	n=2
	val=[]
	N=[]
	pot=2
	while n<=8192:
		N.append(n)
		val.append(Integral(n))
		n=2**pot
		pot+=1

	return val, N

ValAnalitico = 1126400.0 # RESULTADO ANALITICO

error=[]
invRaizN=[]
rec=0
while rec< len(num_integral()[0]):
	invRaizN.append(1/(np.sqrt(num_integral()[1][rec])))
	error.append((abs(ValAnalitico-num_integral()[0][rec])/ValAnalitico)*100)
	rec+=1
	

plt.scatter(num_integral()[1],num_integral()[0])
plt.title('Valor de la integral vs N')
plt.xlabel('N(numero de puntos utilizado para calcular la integral)')
plt.ylabel('Valor calculado de la integral')
plt.savefig('num_integral.pdf')


plt.plot(invRaizN, error)
plt.title('Error vs 1/$\sqrt{N}$')
plt.xlabel('1/$\sqrt{N}$')
plt.ylabel('Error')
plt.savefig('err_integral.pdf')

