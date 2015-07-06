import numpy as np
import math
import matplotlib.pyplot as plt
import random

def drift(L):
   d = np.array([[1, L],[0, 1]])
   return d
   
def fquad(L,K):
    K = math.sqrt(K)
    foc = np.array([[math.cos(K*L), math.sin(K*L)/K],[-K*math.sin(K*L), math.cos(K*L)]])
    return foc
    
def dquad(L,K):
    K = math.sqrt(K)
    defoc = np.array([[math.cosh(K*L), math.sinh(K*L)/K],[K*math.sinh(K*L), math.cosh(K*L)]])
    return defoc
def initial(x,xp):
    x = np.array([[x],[xp]])
    return x
    
   
    
def sections(a,initial):
    l = len(a)
    if l == 1:   
        calc = a[l-1]
        l = l-1
    else:
        calc1 = a[l-1]
        calc2 = a[l-2]
        calc = np.dot(calc1,calc2)
        l = l-2
    while l > 0:
        calc1 = a[l-1]
        calc = np.dot(calc,calc1)
        l = l-1
    calc = np.dot(calc,initial)
    return calc
    
    
    
#def plotfocal(section,xp,x,):

def straight():
    xp = np.arange(0,1)        
    x = np.arange(-0.05,0.06,0.01) #x and xp for when xp is 0
    return x,xp

def scanned():
    xp = np.arange(-0.0001,0.0001,0.00001)
    x = np.arange(-0.05,0.06,0.01)     # x and xp for when xp is scanned
    return x,xp
    
def randomed():
    x = []
    for a in range (0, 10):
        x.append(random.uniform(-0.05, 0.05))
    
    xp = []
    for a in range (0, 10):
        xp.append(random.uniform(-0.00001, 0.00001)) #x and xp dfor random values
    return x,xp
    
def gaussian():
    x = []
    for a in range (0, 10):
        x.append(random.gauss(0, 0.01))
    
    xp = []
    for a in range (0, 10):
        xp.append(random.gauss(0, 0.00001))
    return x,xp
    
def plot(L,x,xp):
    #section = drift(2)
    section = fquad(2.5,0.001)
       
    x = x
    xp = xp
    
    lengthx = len(x)
    lengthxp = len(xp)
    xprint = []
    yprint = []
    #Setting up initial conditions for the array
    
    #Making loops to calculate the x and xp values after going through a section
    for a in range (0,lengthxp):
        for i in range (0,lengthx):
            initial = np.array([[x[i]],[xp[a]]])
            h = np.dot(section,initial)
            xprint = np.append(xprint,h[0])
            yprint = np.append(yprint,h[1])
    #Double for loops to make a different numbers of x and xp work
            
    zprint = []
    #Loops to now do a drift from the set length value L that is taken as an argument
    for a in range (0,lengthxp):    
        for i in range (0,lengthx):
            b = xprint[i+(a*(lengthx-1))]+yprint[i+(a*(lengthx-1))]*L
            zprint = np.append(zprint,b)
    return zprint
    
#Function to make the length plot for each set length usually like np.arange(0,500,10)
def plotfocal(length,start):
    h = start()
    x = h[0]
    xp = h[1]
    l = len(length)
    for i in range (0,l):
        L = length[i]
        zprint = plot(L,x,xp)
        zl = len(zprint)
        lprint = []
        for t in range (0,zl):
            lprint = np.append(lprint,L)
        plt.plot(lprint,zprint,'ro')
    return
# np.arange(-0.05,0.005,0.0001)
#np.arange(-0.5,0.5,0.1)



    
