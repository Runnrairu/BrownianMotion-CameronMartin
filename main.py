# -*- coding: utf-8 -*-

import numpy as np
import time

pi=3.14159265358979323

def basis_CameronMartin(k,x,T):
    if k==0:
        return x/np.sqrt(T)
    else:
        return np.sqrt(2*T)*np.sin((k+0.5)*pi*x/T)/(pi*(k+0.5))
    
    


n=100001 #時間ステップの数 t=0を１つめとする
m=10 #用いるCameron martin空間の基底
T=10.0
path=10000 #生成したいブラウン運動の数
delta_t=T/n

CM=[[0]* n  for j in range(m)]
for i in range(m):
    for j in range(n):
        CM[i][j]=basis_CameronMartin(i, delta_t*j,T)



start = time.time() 





end = time.time() 
time_diff = end - start 
print(time_diff) 




