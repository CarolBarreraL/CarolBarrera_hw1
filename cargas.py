import numpy as np
import matplotlib.pyplot as plt

kantes= 8.987*10**9 #En N, m y C
nmCuadrado= 10**18 #nm
e= 1/(1.602176*10**(-19))#e

#Clase Carga
class Carga:
	k= kantes*nmCuadrado/(e**2)*(10**9) #Constante de Coulomb en N(en nm), e y nm
	x= np.linspace(-1,1,80)
	y= np.linspace(-1,1,80)
	xv, yv = np.meshgrid(x,y)
	def __init__(self, q0, x0, y0):
		self.q=q0	
		self.x=x0
		self.y=y0

	#Potencial de una carga
	def calcPot(self):
		V = self.q*Carga.k/np.sqrt((Carga.xv-self.x)**2 + (Carga.yv- self.y)**2)
		return V
	#Campo electrico de una carga
	def calcCampoE(self):
		hx=carga1.calcPot()[0][1]-carga1.calcPot()[0][0]
		hy=carga1.calcPot()[1][0]-carga1.calcPot()[0][0]
		xx=Carga.xv-self.x
		yy=Carga.yv-self.y
		dx = -(self.q*Carga.k/(np.sqrt((xx+hx*0.5)**2 + (yy)**2)) - self.q*Carga.k/(np.sqrt((xx-hx*0.5)**2 + (yy)**2)))/hx
		dy = -(self.q*Carga.k/(np.sqrt((xx)**2 + (yy+hy*0.5)**2)) - self.q*Carga.k/(np.sqrt((xx)**2 + (yy-hy*0.5)**2)))/hy
		return dx, dy


#Objetos de la clase Carga (las 4 cargas)
carga1=Carga(-1,-0.5, 0.5)
carga2=Carga(-1, 0.5,-0.5)
carga3=Carga(1, 0.5, 0.5)
carga4=Carga(1,-0.5,-0.5)

#Potencial debido a las 4 cargas
VTotal= carga1.calcPot() + carga2.calcPot() + carga3.calcPot() + carga4.calcPot()
#Campo electrico debido a todas las cargas (gradiente del potencial: derivada parcial en x y derivada parcial en y)
dxTotal = carga1.calcCampoE()[0]+carga2.calcCampoE()[0]+carga3.calcCampoE()[0]+carga4.calcCampoE()[0]
dyTotal = carga1.calcCampoE()[1]+carga2.calcCampoE()[1]+carga3.calcCampoE()[1]+carga4.calcCampoE()[1]

#Grafica del potencial y lineas de campo electrico
plt.imshow(VTotal, extent= [-1.0,1.0,-1.0,1.0], cmap='gist_heat', origin='lower')
plt.title('Potencial y lineas de Campo Electrico')
plt.colorbar()
plt.streamplot(Carga.xv,Carga.yv,dxTotal,dyTotal)
plt.savefig('cargas.pdf')







