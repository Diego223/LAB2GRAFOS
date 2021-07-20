#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio 2
#Diego Crespo 19541
from Base import Dibujador, V3, color
from numpy import sin, cos



width = 960
height = 1500

caja = Dibujador(height,width)
#k=0
caja.glColor(0,0,1)
#TRIANGULO
caja.glLine(V3(100,100),V3(140,140))
caja.glLine(V3(140,140),V3(180,100))
caja.glLine(V3(180,100),V3(100,100))

#CUADRADO
caja.glLine(V3(500,600),V3(600,600))
caja.glLine(V3(500,500),V3(500,600))
caja.glLine(V3(600,500),V3(600,600))
caja.glLine(V3(500,500),V3(600,500))
#PENTAGONO

caja.glLine(V3(200,300),V3(300,400))
caja.glLine(V3(300,400),V3(400,300))
caja.glLine(V3(400,300),V3(350,200))
caja.glLine(V3(200,300),V3(250,200))
caja.glLine(V3(250,200),V3(350,200))

#HEXAGONO
caja.glLine(V3(800,400),V3(900,500))
caja.glLine(V3(900,500),V3(1000,400))
caja.glLine(V3(1000,400),V3(1000,300))
caja.glLine(V3(1000,300),V3(900,200))
caja.glLine(V3(900,200),V3(800,300))
caja.glLine(V3(800,300),V3(800,400))

#HEPTAGONO
caja.glLine(V3(100,500),V3(125,575))
caja.glLine(V3(125,575),V3(200,600))
caja.glLine(V3(200,600),V3(275,575))
caja.glLine(V3(275,575),V3(300,500))
caja.glLine(V3(300,500),V3(275,425))
caja.glLine(V3(275,425),V3(125,425))
caja.glLine(V3(125,425),V3(100,500))
#caja.glLine(V3(125,475),V3(100,500))







caja.glFinish("salida.bmp")





