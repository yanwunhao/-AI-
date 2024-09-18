import numpy as np


def layer_norm(x, eps=1e-5):
    """
    レイヤー正規化を実装します。

    アルゴリズムのステップ：
    1. 特徴次元に沿って入力テンソルの平均を計算する
    2. 特徴次元に沿って入力テンソルの分散を計算する
    3. 計算された平均と分散を使用して入力を正規化する

    引数：
    x (np.array): 形状が(バッチサイズ, 特徴数)の入力配列
    eps (float): 数値の安定性のために分散に加える小さな値

    戻り値：
    np.array: 入力と同じ形状の正規化された配列
    """
    # ステップ1：平均を計算
    mean = np.mean(x, axis=-1, keepdims=True)

    # ステップ2：分散を計算
    variance = np.var(x, axis=-1, keepdims=True)

    # ステップ3：正規化
    return (x - mean) / np.sqrt(variance + eps)


# 関数をテスト
x = np.array([1, 2, 3, 4, 5])  # 2x5行列を作成
print("元の配列：")
print(x)
print("\n正規化された配列：")
print(layer_norm(x))
