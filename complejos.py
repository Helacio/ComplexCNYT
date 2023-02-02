import math
def suma(c1,c2):
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    resultado = (real, imag)
    return resultado

#Propuesto en clase
def prettyPcplx(c):
    print(str(c[0])+ "+" + str(c[1]) + "i")

def mult(c1, c2):
    d1 = c1[0] * c2[0] - c1[1] * c2[1]
    d2 = c1[0] * c2[1] + c1[1] * c2[0]
    d = (d1, d2)
    return d

def resta(c1,c2):
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    resultado = (real, imag)
    return resultado

def div(c1, c2):
    d1 = (c1[0] * c1[1] + c2[0] * c2[1] / c1[1] ** 2 + c2[1] ** 2)
    d2 = (c1[1] * c2[0] - c2[0] * c2[1] / c1[1] ** 2 + c2[1] ** 2)
    d = (d1, d2)
    #prettyPcplx(d)
    return d

def modulo(c1):
    d = ((c1[0] ** 2) + (c1[1] ** 2))** 0.5
    return d
    
def conjugado(c1):
    d1 = c1[0]
    d2 = -1 * c1[1]
    d = (d1, d2)
    return d

def reprePolarCart(c1):
    d1 = c1[0] * math.cos(c1[1])
    d2 = c1[0] * math.sin(c1[1])
    d = (d1, d2)
    return d
    
def fase(c1):
    if c1[0] != 0:
        return math.atan(c1[1] / c1[0])
    
