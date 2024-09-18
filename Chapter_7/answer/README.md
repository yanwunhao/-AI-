## 参考コード

```
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from typing import List
import json

# a) Pydanticモデルの定義
class ProductInfo(BaseModel):
    name: str = Field(description="商品名")
    price: float = Field(description="価格")
    stock: int = Field(description="在庫数")

# a) PydanticOutputParserの作成
output_parser = PydanticOutputParser(pydantic_object=ProductInfo)

# b) テストデータの生成
test_data = [
    {"name": "スマートフォン", "price": 79999.99, "stock": 100},
    {"name": "ノートパソコン", "price": 129999.99, "stock": 50},
    {"name": "ワイヤレスイヤホン", "price": 19999.99, "stock": 200}
]

# c) 言語モデルの応答をシミュレートする関数
def mock_llm_response(data: dict) -> str:
    return json.dumps(data)

# d) パーサーをテストする関数
def test_parser():
    for data in test_data:
        # モックLLM応答の生成
        llm_response = mock_llm_response(data)

        try:
            # パーサーを使用して応答を解析
            parsed_output = output_parser.parse(llm_response)

            # 解析結果の検証
            assert isinstance(parsed_output, ProductInfo)
            assert parsed_output.name == data["name"]
            assert parsed_output.price == data["price"]
            assert parsed_output.stock == data["stock"]

            print(f"テスト成功: {parsed_output}")
        except Exception as e:
            print(f"テスト失敗: {e}")

# e) メインブロック
if __name__ == "__main__":
    print("PydanticOutputParserのテストを開始します...")
    test_parser()
    print("テスト完了")
```
