import math


def softmax(x):
    # オーバーフロー対策: 入力の最大値を引く
    max_x = max(x)
    exp_x = [math.exp(xi - max_x) for xi in x]
    sum_exp_x = sum(exp_x)
    return [xi / sum_exp_x for xi in exp_x]


# テストケース
test_input = [2.0, 1.0, 0.1, 3.0, -1.0, 4.1, 2.0, 0.0, 1.0, 3.2]

# softmax関数の実行
result = softmax(test_input)

# 結果の表示
print("入力:")
print(test_input)
print("\nSoftmax出力:")
print(result)
print("\n合計:")
print(sum(result))

# 各要素の確率を百分率で表示
print("\n確率分布（%）:")
for i, prob in enumerate(result):
    print(f"要素 {i}: {prob * 100:.2f}%")
