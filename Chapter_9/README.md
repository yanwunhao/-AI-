## 課題一： Embedding キャッシュの実装

キャッシュ機能を持つ Embedding 生成器を実装してください。

この問題は RAG システムにおける Embedding 生成とキャッシュ戦略を評価します。RAG アプリケーションでは、embeddings を効率的に生成および管理することが、システムのパフォーマンス向上と API 呼び出しの削減に極めて重要です。

要件：

LangChain の CacheBackedEmbeddings と InMemoryStore を使用します。

テキストのリストを受け取り、対応する Embeddings を返す関数を実装します。

テキストの Embedding がすでにキャッシュにある場合、再計算せずにキャッシュから直接返します。

キャッシュにない場合は、Embedding を計算してキャッシュに保存します。

使用例：

```
embedder = create_cached_embedder()
texts = ["こんにちは", "世界"]
embeddings = embedder.embed_documents(texts)
print(embeddings)
# 2回目の呼び出しはキャッシュから取得されるはずです
embeddings_cached = embedder.embed_documents(texts)
print(embeddings_cached)
# 期待される出力: 両方の呼び出しで同じembeddingsが返されるべきです
```

## 課題二： シンプルなベクトル類似度検索

基本的なベクトル類似度検索関数を実装してください。

この問題は RAG システムの核心的な検索機能を評価します。RAG では、クエリベクトルに最も類似した文書ベクトルを見つけることが、関連性の高い正確な回答を生成するための重要なステップです。

要件：

関数はクエリベクトルとベクトルのリストを入力として受け取ります。

クエリベクトルとリスト内の各ベクトルとのコサイン類似度を計算します。

類似度が最も高い上位 N 個のベクトルのインデックスと類似度スコアを返します。

入力例と出力例：

```
query_vector = [1, 2, 3]
vector_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
N = 2
result = vector_similarity_search(query_vector, vector_list, N)
print(result)
# 期待される出力: [(2, 0.9999), (3, 0.9647)]  # (インデックス, 類似度スコア)
```
