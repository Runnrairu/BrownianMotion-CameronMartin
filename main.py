# -*- coding: utf-8 -*-

import numpy as np
import time
rng = np.random.default_rng()
pi=3.14159265358979323

def basis_CameronMartin(k,x,T):#今回は三角関数基底を使用。違う基底を用いるときはここを変更
    return np.sqrt(2*T)*np.sin((k+0.5)*pi*x/T)/(pi*(k+0.5))
    
    


n=10000 #時間ステップの数 t=0を１つめとする
m=20 #用いるCameron martin空間の基底
T=10.0
path=10000 #生成したいブラウン運動の数
delta_t=T/n

matrix = np.triu(np.ones((n, n)), k=0) #オイラー法で作るとき用の上三角行列

start_1 = time.time() #通常手法の計算時間計算
noise_normal=rng.standard_normal((path, n)) #ガウシアンノイズの生成
scale=np.sqrt(T/n) #時間スケールでかける定数

brownian_normal=scale*np.dot(noise_normal,matrix) #通常手法での計算

end_1 = time.time() #通常手法の計算時間計測終了
time_diff_1 = end_1 - start_1 
print(time_diff_1) 


CM=[[0]* n  for j in range(m)] #Cameron martinの基底を先に計算しておく
for k in range(m):
    for j in range(n):
        CM[k][j]=basis_CameronMartin(k, delta_t*j,T)
start_2=time.time() #現状基底は先に計算しておいて表から読み込めるため、ここから提案手法の計測スタート
noise_cameron=rng.standard_normal((path, m)) #ガウシアンノイズの生成
brownian_Cameron=np.dot(noise_cameron,CM) #ブラウン運動の計算

end_2 = time.time() 
time_diff_2 = end_2 - start_2 
print(time_diff_2) 



mean1=np.mean(brownian_normal,axis=0) #通常手法の期待値を計算（理論値は0）
variance1 =path*np.var(brownian_normal, axis=0)/(path-1) #通常手法の不偏分散を計算（理論値は10、Tと同じ）

print(mean1,variance1)

mean2=np.mean(brownian_Cameron,axis=0) #提案手法の期待値を計算（理論値は0）
variance2 =path*np.var(brownian_Cameron, axis=0)/(path-1) #提案手法の不偏分散を計算（期待値は10、Tと同じ）

print(mean2,variance2)
print(time_diff_1) 
print(time_diff_2) 
print(variance1[-1],variance2[-1])
