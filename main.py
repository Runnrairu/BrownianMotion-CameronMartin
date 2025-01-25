# -*- coding: utf-8 -*-

import numpy as np
import time
rng = np.random.default_rng()
pi=3.14159265358979323

def basis_CameronMartin(k,x,T):
    if False: 
        return x/np.sqrt(T)
    else:
        return np.sqrt(2*T)*np.sin((k+0.5)*pi*x/T)/(pi*(k+0.5))
    
    


n=10000 #時間ステップの数 t=0を１つめとする
m=20 #用いるCameron martin空間の基底
T=10.0
path=10000 #生成したいブラウン運動の数
delta_t=T/n


        


brownian_normal=[[0 for j in range(n)] for i in range(path)]
brownian_Cameron=[[0 for j in range(n)] for i in range(path)]


matrix = np.triu(np.ones((n, n)), k=0) 

start_1 = time.time() 
noise_normal=rng.standard_normal((path, n))
scale=np.sqrt(T/n)

brownian_normal=scale*np.dot(noise_normal,matrix)

end_1 = time.time() 
time_diff_1 = end_1 - start_1 
print(time_diff_1) 


CM=[[0]* n  for j in range(m)]
for k in range(m):
    for j in range(n):
        CM[k][j]=basis_CameronMartin(k, delta_t*j,T)
start_2=time.time() 
noise_cameron=rng.standard_normal((path, m))
brownian_Cameron=np.dot(noise_cameron,CM)

end_2 = time.time() 
time_diff_2 = end_2 - start_2 
print(time_diff_2) 

mean=np.mean(brownian_Cameron,axis=0)
variance1 =(path+1)*np.var(brownian_Cameron, axis=0)/path

print(mean,variance1)

mean=np.mean(brownian_normal,axis=0)
variance2 =(path+1)*np.var(brownian_normal, axis=0)/path

print(mean,variance2)
print(time_diff_1) 
print(time_diff_2) 
print(variance1[-1],variance2[-1])
