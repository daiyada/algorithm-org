# Binary Min-Heap Implementation in Python

標準ライブラリ heapq の挙動を再現した、Python による Min-Heap (最小ヒープ) のスクラッチ実装です。完全二分木 (Complete Binary Tree) 構造を配列上で管理し、優先度付きキューとしての操作を効率的に行います。

## 📋 Overviewヒープは以下の特性を持つ木構造です。

1. 構造的特性: 完全二分木である（最下層を除いて全てのレベルが埋まっており、最下層は左詰めされている）。
2. 順序特性 (Heap Property): 親ノードの値は、常に子ノードの値以下である（Min-Heap の場合）。

- parent.val <= children.val

- 従って、根 (Root) には常に最小値が存在する。

## 🧠 Data Structure

ヒープは論理的には「木」ですが、物理的には 配列 (List) として実装されます。インデックス $i$ のノードに対して、親子関係は以下の数式でマッピングされます。

- Parent: $\lfloor \frac{i - 1}{2} \rfloor$

- Left Child: $2i + 1$

- Right Child: $2i + 2$


## 🚀 Time Complexity Summary

要素数を $N$ としたときの計算量は以下の通りです。

| Method | Operation | Time Complexity | Note |
| --- | --- | --- | --- |
| push | 追加 | $O(\log N)$ | 末尾に追加して sift_up |
| pop | 削除 | $O(\log N)$ | ルートを削除して、末尾を持ってきて sift_down |
| peek | 最小値参照 | $O(1)$ | 配列の先頭 heap[0] を見るだけ |
| pushpop | 追加 & 削除 | $O(\log N)$ | push + pop ($2\log N$) よりも定数倍高速 |
| replace | 削除 & 追加 | $O(\log N)$ | pop + push ($2\log N$) よりも定数倍高速 |
| heapify | 構築 | $O(N)$ | 線形時間で構築 |


## 🛠 Internal Algorithms

効率的なヒープ操作を支える2つの核となる内部操作があります。

1. Sift Up (Bubble Up)

- 使用箇所: push
- 動作: 新しい要素をヒープの最下層（配列末尾）に追加した後、ヒープ条件を満たすまで親と交換しながら「浮上」させます。
- 計算量: 木の高さ $H \approx \log_2 N$ に比例するため $O(\log N)$。

2. Sift Down (Sink Down)

- 使用箇所: pop, heapify, pushpop, replace
- 動作: ルートにある要素がヒープ条件（親 $\le$ 子）を満たしていない場合、左右の子のうち小さい方と交換しながら適切な位置まで「沈下」させます。
- 計算量: 木の高さ $H \approx \log_2 N$ に比例するため $O(\log N)$。

## 📉 Why is heapify O(N)?

heapify は配列全体をヒープ構造に変換しますが、これは $O(N \log N)$ ではなく $O(N)$ で完了します。


### アルゴリズム

最後の親ノード（インデックス $N/2 - 1$）から逆順にルート（$0$）に向かって sift_down を適用します。

### 計算量の証明

各ノードで発生する計算コストは、「そのノードの高さ（沈む距離）」に比例します。

- 葉 (Leaves): ノード数の約50%を占めるが、高さ0なのでコスト 0。
- その上の層: ノード数の約25%を占めるが、高さ1なのでコスト 1。
- ルート: ノード数は1つだが、高さ $\log N$。

全体の計算量は以下の級数の和になります。

$$\sum_{h=0}^{\log N} \frac{N}{2^{h+1}} \cdot h \approx O(N)$$

直感的には、「大多数のノード（葉に近い層）は移動距離が短く、移動距離が長いノード（ルート付近）は数が少ない」ため、トータルでは $N$ に収束します。

## ⚡ Optimization: pushpop & replace

これらは2つの操作をアトミックに行うことで、定数倍の高速化を実現しています。

### Naive Implementation vs Optimized

もし replace (最小値を捨てて新しい値を入れる) を単純な pop + push で実装すると：

1. pop: ルート削除 $\to$ 末尾移動 $\to$ sift_down (コスト $\log N$)
2. push: 末尾追加 $\to$ sift_up (コスト $\log N$)
- 合計: $2 \log N$ のコストと、配列サイズの変更処理が発生。

最適化された replace では：

1. ルートを新しい値で上書き $\to$ sift_down (コスト $\log N$)
- 合計: $1 \log N$ で済み、配列サイズの変更も発生しません。

## 📝 Usage Python from heap import Heap

```
# O(N) で初期化
h = Heap([5, 3, 8, 1, 2, 9]) 

# 追加 O(log N)
h.push(4)

# 最小値取得 O(log N)
min_val = h.pop() # -> 1

# 追加して最小値取得 (効率的)
val = h.pushpop(6) 
```