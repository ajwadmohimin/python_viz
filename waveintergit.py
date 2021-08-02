#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 06:05:50 2021

@author: ajwadmohimin
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig,ax=plt.subplots(1,1);
ax.axis("on");

plt.rc("mathtext",fontset='stix')
x=np.linspace(0,2*np.pi,500)
y=np.zeros(x.size)
ax.set_xlim([0,x.max()])
imyl=ax.set_ylim([-15,15])
ax.set_xlabel(r"x")
ax.set_ylabel(r"$y=f\ (x,t)$")
ln, =ax.plot(np.ma.array(x,mask=False),y,"-",color='C0',
             label=r"$y1=Asin\frac{2\pi}{\lambda}(x+vt)$")
ln2, =ax.plot(np.ma.array(x,mask=False),y,"-",color='C1',
              label=r"$y2=Asin\frac{2\pi}{\lambda}(x-vt)$")
ln3, =ax.plot(np.ma.array(x,mask=False),y,"-",color='C2',
              label=r"$y3=y1+y2$")
ax.legend(loc='upper right')
ax.set_title(r"$Superposition\ of\ two\ sine\ wave\ aproaching\ from\ opposite\ side$")
tx=ax.text(2.5,-14,'')
fig.tight_layout()
def wav(A,lm,x,v,t):
    return A*np.sin((2*np.pi/lm)*(x-(v*t)))
def wavinv(A,lm,x,v,t):
    return A*np.sin((2*np.pi/lm)*(x+(v*t)))
A,lm,v=5,5,1
dt=[0.3] #animation interval in ms.
fc=50 #frameCount
dtl=0.17 #delT for function
i_l=0
def graph(i,dt):
    x=ln.get_xdata()
    t =i + dtl
    tx.set_text("$time={0:0.3f}$".format(t))
    y=wav(A,lm,x,v,t)
    im=ln.set_ydata(y)
    y2=wavinv(A,lm,x,v,t)
    im2=ln2.set_ydata(y2)
    y3=y+y2
    im3=ln3.set_ydata(y3)
    if(np.abs(y3.max())>1.7*A or np.abs(y3.max()) < 0.3*A):
        ima_=ln.set_alpha(0.25) #alpha for opacity
        ima2_=ln2.set_alpha(0.25)
        ima3_=ln3.set_alpha(1)
        return im,im2,im3,ima_,ima2_,ima3_
    else:
        ima=ln.set_alpha(1)
        ima2=ln2.set_alpha(1)
        ima3=ln3.set_alpha(1)
        return im,im2,im3,ima,ima2,ima3

def aniu(i):
    return graph(i,dt)
ani=anim.FuncAnimation(fig,func=aniu,frames=range(fc),interval=1000*dt[0],repeat=False)
print("frameRate=",1/dt[0],"totalAniRunTime={0:0.2f} minute".format((fc/(1/dt[0]))/60))
ani.save("waves.mp4",writer="ffmpeg")