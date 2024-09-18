## 演習 1: PromptTemplate の作成と使用

タスク：旅行計画の提案を生成するための PromptTemplate を作成してください。
テンプレートには、目的地、旅行日数、予算を入力変数として含める必要があります。
その後、このテンプレートを使用して具体的な旅行計画(cities=["Tokyo", "Paris", "New York"])の提案を生成してください。
コードを記述してください。

## チャレンジ：複数モデルの連鎖

タスク：以下の多段階処理フローを作成してください：

1.  あるモデルを使用してストーリーのアウトラインを生成する
2.  別のモデルを使用して、そのアウトラインに基づいて短編小説を作成する
3.  3 番目のモデルを使用して、その物語の感情分析を行う

LangChain の Sequential チェーンを使用してこのフローを実装してください。

Sequential チェーンの使用方法：

1. 必要なモジュールをインポートします：

```
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
```

2. 各ステップのための LLMChain を作成します：

```
llm = OpenAI(temperature=0.7)
```

例：ステップ 1 のチェーン

```
outline_prompt = PromptTemplate(...)

outline_chain = LLMChain(llm=llm, prompt=outline_prompt, output_key="outline")
```

ステップ 2 と 3 も同様に作成します

3. Sequential チェーンを作成し、すべてのステップを結合します：

```

overall_chain = SequentialChain(

chains=[outline_chain, story_chain, analysis_chain],

input_variables=["topic"],

output_variables=["outline", "story", "analysis"],

verbose=True

)
```

4. チェーンを実行します：

```
result = overall_chain({"topic": "宇宙探査"})

print(result)
```

この方法により、各ステップの出力が次のステップの入力となり、

最終的に全体の結果が得られます。
