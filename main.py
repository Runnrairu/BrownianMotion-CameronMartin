# -*- coding: utf-8 -*-

import numpy as np
import time
rng = np.random.default_rng()
pi=3.14159265358979323

def basis_CameronMartin(k,x,T):
    if False: #k==0
        return x/np.sqrt(T)
    else:
        return np.sqrt(2*T)*np.sin((k+0.5)*pi*x/T)/(pi*(k+0.5))
    
    


n=100000 #時間ステップの数 t=0を１つめとする
m=1000 #用いるCameron martin空間の基底
T=10.0
path=10000 #生成したいブラウン運動の数
delta_t=T/n


        


brownian_normal=[[0 for j in range(n)] for i in range(path)]
brownian_Cameron=[[0 for j in range(n)] for i in range(path)]




start = time.time() 
noise_normal=rng.standard_normal((path, n-1))
scale=np.sqrt(T/n)
for i in range(path):
    for j in range(n-1):
        brownian_normal[i][j+1]=brownian_normal[i][j]+scale*noise_normal[i][j]

end = time.time() 
time_diff = end - start 
print(time_diff) 

start=time.time() 
CM=[[0]* n  for j in range(m)]
for k in range(m):
    for j in range(n):
        CM[k][j]=basis_CameronMartin(k, delta_t*j,T)

noise_cameron=rng.standard_normal((path, m))
brownian_Cameron=np.dot(noise_cameron,CM)

end = time.time() 
time_diff = end - start 
print(time_diff) 

mean=np.mean(brownian_Cameron,axis=0)
variance = np.var(brownian_Cameron, axis=0)

print(mean,variance)

mean=np.mean(brownian_normal,axis=0)
variance = np.var(brownian_normal, axis=0)

print(mean,variance)

