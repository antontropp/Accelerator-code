import numpy as np
import math
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

def drift(L):
   L = L
   dx = np.array([[1,L],[0,1]])
   dy = np.array([[1,L],[0,1]])
   return dx,dy,L
   
def fquad(L,K):
    L = L
    K = math.sqrt(K)
    xfoc = np.array([[math.cos(K*L), math.sin(K*L)/K],[-K*math.sin(K*L), math.cos(K*L)]])
    yfoc = np.array([[math.cosh(K*L), math.sinh(K*L)/K],[K*math.sinh(K*L), math.cosh(K*L)]])
    return xfoc,yfoc,L
    
def dquad(L,K):
    L = L
    K = math.sqrt(K)
    xdefoc = np.array([[math.cosh(K*L), math.sinh(K*L)/K],[K*math.sinh(K*L), math.cosh(K*L)]])
    ydefoc= np.array([[math.cos(K*L), math.sin(K*L)/K],[-K*math.sin(K*L), math.cos(K*L)]])
    return xdefoc,ydefoc,L
    
def straight():
    xp = np.arange(0,1)        
    x = np.arange(-0.005,0.01,0.005) #x and xp for when xp is 0
    yp = np.arange(0,1)        
    y = np.arange(-0.05,0.1,0.05)
    return x,xp,y,yp

def scanned():
    xp = np.arange(-0.00001,0.00001,0.00001)
    x = np.arange(-0.01,0.01,0.001)     # x and xp for when xp is scanned
    yp = np.arange(0,1)        
    y = np.arange(-0.05,0.1,0.05)
    return x,xp,y,yp
    
def randomed():
    x = []
    for a in range (0, 10):
        x.append(random.uniform(-0.05, 0.05))
    
    xp = []
    for a in range (0, 10):
        xp.append(random.uniform(-0.00001, 0.00001)) #x and xp dfor random values
        
    y = []
    for a in range (0, 10):
        y.append(random.uniform(-0.05, 0.05))
        
    yp = []
    for a in range (0, 10):
        yp.append(random.uniform(-0.05, 0.05))
    return x,xp,y,yp
    
def gaussian():
    x = []
    for a in range (0, 5):
        x.append(random.gauss(0, 0.01))
    
    xp = []
    for a in range (0, 5):
        xp.append(random.gauss(0, 0.00001))
        
    y = []
    for a in range (0, 5):
        y.append(random.uniform(-0.05, 0.05))
        
    yp = []
    for a in range (0, 5):
        yp.append(random.uniform(-0.05, 0.05))
    return x,xp,y,yp
    
#Works to first take section[0]and then section[0] again to get the one value     
    
def initplot(x,xp,y,yp,matrixx,matrixy):      
    xprint = []
    xpprint = []
    yprint = []
    ypprint = []
    for i in range (0,len(x)):
        for a in range(0,len(xp)):
            for t in range(0,len(y)):
                for b in range(0,len(yp)):
                    calc = np.array([x[i],xp[a]])
                    calc1 = np.dot(matrixx,calc)
                    xprint = np.append(xprint,calc1[0])
                    xpprint = np.append(xpprint,calc1[1])
    for i in range (0,len(x)):
        for a in range(0,len(xp)):
            for t in range(0,len(y)):
                for b in range(0,len(yp)):
                    calc = np.array([y[t],yp[b]])
                    calc1 = np.dot(matrixy,calc)
                    yprint = np.append(yprint,calc1[0])
                    ypprint = np.append(ypprint,calc1[1])
    return xprint,xpprint,yprint,ypprint
    
def plot(x,xp,y,yp,matrixx,matrixy):
    xprint = []
    xpprint = []
    yprint = []
    ypprint = []
    for a in range (0,len(x)):
        calc = np.array([x[a],xp[a]])
        calc1 = np.dot(matrixx,calc)
        xprint = np.append(xprint,calc1[0])
        xpprint = np.append(xpprint,calc1[1])    
    for a in range (0,len(y)):
        calc = np.array([y[a],yp[a]])
        calc1 = np.dot(matrixy,calc)
        yprint = np.append(yprint,calc1[0])
        ypprint = np.append(ypprint,calc1[1])
    return xprint,xpprint,yprint,ypprint
    
#Function to make the length plot for each set length usually like np.arange(0,500,10)
def plotfocal(section,start):
    h = start()
    x = h[0]
    xp = h[1]
    y = h[2]
    yp = h[3]
    matrixx = np.array([[1,0],[0,1]])
    matrixy = np.array([[1,0],[0,1]])
    lprint = []
    printvalues = initplot(x,xp,y,yp,matrixx,matrixy)
    x = printvalues[0]
    xp = printvalues[1]
    y = printvalues[2]
    yp = printvalues[3]
    for t in range (0,len(x)):
        lprint = np.append(lprint,0)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x,y,lprint,c=u'b')
    for t in range (0,len(section)):
        s = section[t]
        matrixx = s[0]
        matrixy = s[1]
        length = s[2]
        lprint = lprint+length
        printvalues = plot(x,xp,y,yp,matrixx,matrixy)
        x = printvalues[0]
        xp = printvalues[1]
        y = printvalues[2]
        yp = printvalues[3]
        ax.scatter(x,y,lprint,c=u'r')
    return
