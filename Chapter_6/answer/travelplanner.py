from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# PromptTemplateの作成
travel_prompt = PromptTemplate(
    input_variables=["destination", "duration", "budget"],
    template="{destination}への{duration}日間の旅行プランを、予算{budget}で立ててください。毎日のスケジュールと提案を含めてください。",
)

# LLMの作成
llm = OpenAI(temperature=0.7)

# テンプレートを使用して具体的な旅行プランを生成
cities = ["東京", "パリ", "ニューヨーク"]
for city in cities:
    prompt = travel_prompt.format(destination=city, duration=5, budget="10万円")
    response = llm(prompt)
    print(f"{city}の旅行プラン：\n{response}\n")
