# 第一章演習課題

## 課題一：n-gramモデルの概念と応用

n-gramモデルの主な特徴：
1. nは系列中の連続項目の数を表します。一般的なn-gramには以下があります：
   - ユニグラム (n=1): 単一の単語
   - バイグラム (n=2): 2つの連続する単語
   - トライグラム (n=3): 3つの連続する単語
2. n-gramモデルはマルコフ仮説に基づいており、ある単語の出現確率はその直前のn-1個の単語にのみ依存すると仮定します。
3. n-gramモデルは、コーパス内でn個の単語が共起する頻度を計算することで確率分布を推定します。
4. nの値が大きくなるにつれて、モデルはより長い文脈を捉えることができますが、データの疎性問題に直面します。

応用問題：以下のテキストコーパスが与えられています：

"The cat sat on the mat. The dog chased the cat. The mat was soft and warm. The cat and dog played on the soft mat."

以下の質問に答えてください：

a) このコーパスのトライグラム（3-gram）頻度表を作成してください。上位5つのトライグラムのみを示してください。

b) バイグラムモデルを使用して、文 "The cat sat on the soft" の確率を計算してください。（ヒント：ラプラススムージングを使用し、ボキャブラリーサイズを考慮してください）

c) "The cat and dog" の後に最も来る可能性が高い単語は、トライグラムモデルによるとどれですか？その理由も説明してください。

## 課題二：GPTモデルの進化に関する調査研究

### 背景：
GPT（Generative Pre-trained Transformer）モデルは、自然言語処理の分野で革命的な進歩をもたらしました。OpenAIによって開発されたこの一連のモデルは、テキスト生成、言語理解、そして多様なNLPタスクにおいて重要な進展を示しています。GPT-1から始まり、GPT-2、そしてGPT-3へと進化する中で、モデルの規模、能力、そして応用範囲が大きく拡大しました。

### 目的：
この課題の目的は、GPT-1、GPT-2、GPT-3の主要な特徴と進化を詳細に調査し、大規模言語モデルの発展における重要なマイルストーンを理解することです。また、これらのモデル間の違いを分析し、技術の進歩がどのようにモデルの性能と応用可能性を向上させたかを考察します。

### 指示：
以下に提供するGPT-1、GPT-2、GPT-3の論文を主要な情報源として使用してください。必要に応じて、追加の信頼できる資料（学術論文、技術ブログ、公式ドキュメントなど）も調査してください。
調査結果に基づいて、以下の表を埋めてください。
各項目について、可能な限り具体的な数値や説明を記入してください。

### GPTモデルの主要論文：
GPT-1: "Improving Language Understanding by Generative Pre-Training"
https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

GPT-2: "Language Models are Unsupervised Multitask Learners"
https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

GPT-3: "Language Models are Few-Shot Learners"
https://arxiv.org/abs/2005.14165

比較表：

| 特徴 | GPT-1 | GPT-2 | GPT-3 |
|------|-------|-------|-------|
| 発表年 |  |  |  |
| モデルサイズ（パラメータ数） |  |  |  |
| 学習データ量 |  |  |  |
| タスク適応性 |  |  |  |
| 主な改善点 |  |  |  |
| 典型的な応用例 |  |  |  |
| 言語カバレッジ |  |  |  |
| コンテキストウィンドウサイズ |  |  |  |
| トレーニング方法の特徴 |  |  |  |
| 主な技術的革新 |  |  |  |
