#!/usr/bin/env python
import math
import random

def arrh(t,temp,temp0=100,dh=1800):
    r=8.314
    at=math.exp(-dh/r*(1/temp-1/temp0))
    t0=t*at
    return t0    
    
def kv(t,k,s0,nu):    
    e=[]
    for i in t:
        etemp=s0/k*(1-math.exp(-(k*i)/nu))
        e.append(etemp)  

    return e

def expp(t,a):    
    e=[]
    for i in t:
        etemp=a*(i**(0.1))
        e.append(etemp)
    return e

def relax(e0,t,b,temp):    
    t0=arrh(t,temp)
    e=e0*math.exp(-t0/b)
    return e

def noise(v0,delta):
    v1=v0+random.random()*delta
    return v1

def boot_sawy(h,d,g,k,nu):
    pc0=((2*k)/(1-nu**2))*(h/d)**3
    pc=pc0*(25+700*(h/d)+315*(g/(d/2)))/(0.15+130*(h/d)+1400*(h/d)**2+145*(g/(d/2)))
    return pc
      
def experimento(h,d,temp,g):
    e=relax(1500,1,4,temp)
    p=boot_sawy(h,d,g,e,0.35)
    p=noise(p,0.2)
    return p
