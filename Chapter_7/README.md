## 課題一：PydanticOutputParser の実装

以下の Pydantic モデルが与えられています：

```
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    name: str = Field(description="商品名")
    price: float = Field(description="価格")
    stock: int = Field(description="在庫数")
```

このモデルを使用して、以下のタスクを実行してください：
a) PydanticOutputParser を作成する Python コードを書いてください。
b) テストデータとして 3 つの製品情報を含むリストをインポートしてください。

```
test_data = [
    {"name": "スマートフォン", "price": 79999.99, "stock": 100},
    {"name": "ノートパソコン", "price": 129999.99, "stock": 50},
    {"name": "ワイヤレスイヤホン", "price": 19999.99, "stock": 200}
]
```

c) 言語モデルの応答をシミュレートする関数を作成してください。この関数は、製品情報を受け取り JSON 文字列を返すものとします。
d) パーサーをテストする関数を作成してください。この関数は、各テストデータに対して以下を行うものとします：

モック LLM 応答の生成
パーサーを使用した応答の解析
解析結果の検証

e) 作成したテスト関数を実行するメインブロックを書いてください。
完全な実行可能な Python スクリプトとして、上記の全ての要素を含むコードを提供してください。
