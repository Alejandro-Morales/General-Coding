#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:14:10 2021

@author: alejandromorales
"""
import matplotlib.pyplot as plt
import random
import math



A = [0]
x = [0]
autocorr = []

#Generar grafica
for i in range(1,2000):
    x.append(i)
    A.append(A[i-1]+((i+1)*.0001)+(500*random.uniform(-1,1)))
    #Para que veas que cuando no se van sumando la autocorrelacion en 0 para puros random
    #A.append((500*random.uniform(-1,1)))
    
plt.plot(x,A)

#calcular mean
sum = 0
for j in range(len(A)):
    sum = sum + A[j]

mean = sum/len(A)

#calcular var y SD
var = 0
for k in range(len(A)):
    var = var + ((A[k]-mean)*(A[k]-mean))

var = var/len(A)
SD = math.sqrt(var)

x1 = []
#queremos correlation de 40 lags
for m in range(1000):   
    x1.append(m)
    lag = 0
    for l in range(m,len(A)):
        lag = lag + ((A[l-m]-mean)*(A[l]-mean))
    autocov = lag/len(A)
    autocorr.append(autocov/var)

#plt.bar(x1,autocorr) no se porque si la pongo aqui no se grafica, siempre la pongo en command window
