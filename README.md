
# BrownianMotion-CameronMartin

## 目的
本レポジトリの目的は、Ito-Nishioの定理を活用してブラウン運動を効率的に数値的に実装すること。

通常、ブラウン運動は次のように行われる。$`\epsilon_t`$をガウシアンノイズとして

$$
B_{t+\Delta t}=B_t+\sqrt{\Delta t} \epsilon_t
$$

これよりも計算時間が短く、それでいて期待値や分散の収束がいい方法はないだろうか。


## Ito-Nishioの定理  
Ito-Nishioの定理は、ブラウン運動の確率測度の変換を通じて、新しい確率過程を生成する手法を提供する。この定理を利用することで、ブラウン運動の効率的なサンプリングが可能となる。

### statement
各$`h_i`$ はCameron-Martin空間の正規直交基底、各$`\epsilon_i`$は独立な標準ガウスノイズ。このとき

$$
\sum^m_{i=1} \epsilon_i h_i(t)
$$

はブラウン運動に弱収束する。（厳密には誘導される測度がWiener測度に収束）

## 選んだ基底関数
実装において、以下の基底関数をCameron-Martin空間の正規直交基底として選択した：

$$
h_k(t) = \frac{1}{\pi(k+0.5)}\sqrt{\frac{2}{T}} \sin\left(\frac{(k+0.5 )\pi t}{T}\right) \quad (k=1,2,\ldots)
$$

ここで$`T`$ はシミュレーション区間の長さ（今回は$`[0,10]`$ ）

これを用いて、伊藤-西尾の定理を使ったブラウン運動の実装を行う。

## 結果
以下に通常手法とCameron-Martin空間を利用した手法の比較結果を示す。nは時間ステップ数、mは用いる基底の数、pathは生成するサンプルパスの数。

$`n=1000, m=10, path=1000`$ 

| メソッド       | 処理時間 (秒) | 時刻Tでの分散誤差 (%) |
|----------------|---------------|--------------|
| 通常手法       | 0.73         | 3.1           |
| Cameron-Martin | 0.02           | 1.2       |


$`n=100000, m=300, path=10000`$ 

| メソッド       | 処理時間 (秒) | 時刻Tでの分散誤差 (%) |
|----------------|---------------|--------------|
| 通常手法       | 742           | 0.5          |
| Cameron-Martin | 302           | 0.07         |

これらはCameron側は基底計算込みである。この計算は先にやっておいて読み込めるので、この計算時間を除外した場合はさらに圧倒的な差となる。

n=10000, m=20, path=10000

| メソッド       | 処理時間 (秒) | 時刻Tでの分散誤差 (%) |
|----------------|---------------|--------------|
| 通常手法       | 15.10           | 2.1          |
| Cameron-Martin | 0.93           | 1.1         |

ちなみにあまり着目してこなかったが、期待値誤差もこの場合通常は0.02、cameronは0.001と非常に強い。



### 考察
Cameron-Martin空間を利用した手法では、通常手法と比較して計算速度が約2.5倍向上し、分散誤差も大幅に低下した。この結果は、Cameron-Martin空間内での基底選択がブラウン運動の数値的性質を効果的に捉えていることを示唆している。

この計算時間短縮の結果はある意味当然で、生成するガウシアンノイズ数は通常手法が$`path\times n`$個、提案手法が$`path\times m`$個であり、計算する行列サイズは通常手法が$`(path,n)\times(n,n)`$で、提案手法が$`(path,m)\times (m,n)`$と、非常に規模が小さくなっているからである。これだけ規模を下げてもブラウン運動の本質的な部分を捉えているので、誤差が普通のやり方より小さい。

## 発展
今後の発展として以下の方向性を考えている：
1. **基底の変更による精度の変化**  
   異なる基底（例：Chebyshev基底やFourier基底）を試すことで、さらなる精度向上や計算効率の向上を検証する。

2. **SDE離散化的アルゴリズムの改善向上**  
   Stochastic Depthなど、SDEの離散化に関連する機械学習アルゴリズムへの応用を検討する。特にCameron-Martin空間の特性を活かすことで、より高精度なモデルを構築する可能性がある。

---

Cameron-Martin空間の利用は、ブラウン運動の効率的な数値実装や関連分野への応用において非常に有望な手法であることが示された。
