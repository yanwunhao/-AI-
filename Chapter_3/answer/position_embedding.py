import numpy as np
import matplotlib.pyplot as plt


def positional_encoding(max_seq_len, d_model):
    """
    Transformer論文で説明されている位置エンコーディングを実装します。

    アルゴリズムのステップ：
    1. 各位置に対して、異なる周波数の波の系列を生成する
    2. 偶数インデックスには正弦を、奇数インデックスには余弦を使用する
    3. 指数関数的に減衰する周波数を使用して、各位置の一意性を確保する

    引数：
    max_seq_len (int): 最大シーケンス長
    d_model (int): モデルの次元

    戻り値：
    np.array: 形状が(max_seq_len, d_model)の位置エンコーディング
    """
    position = np.arange(max_seq_len)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))

    pos_encoding = np.zeros((max_seq_len, d_model))
    pos_encoding[:, 0::2] = np.sin(position * div_term)
    pos_encoding[:, 1::2] = np.cos(position * div_term)

    return pos_encoding


# 関数をテスト
max_seq_len, d_model = 100, 64
pe = positional_encoding(max_seq_len, d_model)

# 位置エンコーディングを可視化
plt.figure(figsize=(10, 10))
plt.imshow(pe, cmap="viridis", aspect="auto")
plt.title("position encoding")
plt.xlabel("encoding dimension")
plt.ylabel("seq position")
plt.colorbar()
plt.show()

print("位置エンコーディングの形状:", pe.shape)
print("\n最初の位置の最初の数値:")
print(pe[0, :10])
