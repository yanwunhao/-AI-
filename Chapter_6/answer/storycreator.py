from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# LLMの作成
llm = OpenAI(temperature=0.7)

# ステップ1：ストーリーのアウトライン生成
outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="'{topic}'というテーマで短いストーリーのアウトラインを作成してください。",
)
outline_chain = LLMChain(llm=llm, prompt=outline_prompt, output_key="outline")

# ステップ2：アウトラインに基づいて短編小説を作成
story_prompt = PromptTemplate(
    input_variables=["outline"],
    template="次のアウトラインに基づいて短編小説を書いてください：\n{outline}",
)
story_chain = LLMChain(llm=llm, prompt=story_prompt, output_key="story")

# ステップ3：物語の感情分析を行う
analysis_prompt = PromptTemplate(
    input_variables=["story"],
    template="次の短編小説の感情分析を行ってください：\n{story}",
)
analysis_chain = LLMChain(llm=llm, prompt=analysis_prompt, output_key="analysis")

# Sequential Chainの作成
overall_chain = SequentialChain(
    chains=[outline_chain, story_chain, analysis_chain],
    input_variables=["topic"],
    output_variables=["outline", "story", "analysis"],
    verbose=True,
)

# チェーンの実行
result = overall_chain({"topic": "宇宙開発"})

print("アウトライン:")
print(result["outline"])
print("\n短編小説:")
print(result["story"])
print("\n感情分析:")
print(result["analysis"])
