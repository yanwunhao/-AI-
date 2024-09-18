import os
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.callbacks import get_openai_callback

# OpenAI APIキーを設定してください
# os.environ["OPENAI_API_KEY"] = "あなたのAPIキー"


class PersonalityBot:
    def __init__(self, name, personality_desc, memory_capacity=5):
        self.name = name
        self.personality_desc = personality_desc
        self.memory = ConversationBufferMemory(k=memory_capacity)
        self.llm = OpenAI(temperature=0.7)

        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=f"{personality_desc}\n{{history}}\n人間: {{input}}\nAI: ",
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True,
            memory=self.memory,
        )

    def respond(self, user_input):
        return self.chain.predict(input=user_input)


class MultiPersonalityBot:
    def __init__(self):
        self.personalities = {
            "哲学者": PersonalityBot(
                "哲学者",
                "あなたは深い洞察力を持つ哲学者です。人生の意味や倫理的なジレンマについて、複雑で思慮深い回答をします。",
            ),
            "コメディアン": PersonalityBot(
                "コメディアン",
                "あなたはウィットに富んだコメディアンです。ユーモアを交えた返答や、状況をおもしろおかしく描写することを好みます。",
            ),
            "科学者": PersonalityBot(
                "科学者",
                "あなたは論理的で分析的な科学者です。科学的事実や統計を用いて説明し、常に証拠に基づいた回答をします。",
            ),
            "詩人": PersonalityBot(
                "詩人",
                "あなたは感性豊かな詩人です。美しい言葉や比喩を用いて、感情的で印象的な表現をします。",
            ),
        }
        self.current_personality = None

    def switch_personality(self, personality):
        if personality in self.personalities:
            self.current_personality = self.personalities[personality]
            return f"{personality}の人格に切り替わりました。"
        else:
            return "指定された人格は存在しません。"

    def respond(self, user_input):
        if self.current_personality:
            return self.current_personality.respond(user_input)
        else:
            return "人格が選択されていません。'switch_personality'を使用して人格を選択してください。"

    def get_memory(self, personality):
        if personality in self.personalities:
            return self.personalities[personality].memory.chat_memory.messages
        else:
            return "指定された人格は存在しません。"

    def modify_memory(self, personality, index, new_content):
        if personality in self.personalities:
            try:
                self.personalities[personality].memory.chat_memory.messages[
                    index
                ].content = new_content
                return f"{personality}の記憶を修正しました。"
            except IndexError:
                return "指定されたインデックスが範囲外です。"
        else:
            return "指定された人格は存在しません。"


def run_chat_session(bot):
    print("多人格チャットボットへようこそ！")
    print("利用可能な人格: 哲学者、コメディアン、科学者、詩人")
    print(
        "コマンド: 'switch:<人格名>' で人格を切り替え、'quit' で終了、'memory:<人格名>' で記憶を表示"
    )
    print("'modify:<人格名>:<インデックス>:<新しい内容>' で記憶を修正")

    while True:
        user_input = input("あなた: ")

        if user_input.lower() == "quit":
            break
        elif user_input.startswith("switch:"):
            personality = user_input.split(":")[1]
            print(bot.switch_personality(personality))
        elif user_input.startswith("memory:"):
            personality = user_input.split(":")[1]
            print(bot.get_memory(personality))
        elif user_input.startswith("modify:"):
            _, personality, index, new_content = user_input.split(":", 3)
            print(bot.modify_memory(personality, int(index), new_content))
        else:
            with get_openai_callback() as cb:
                response = bot.respond(user_input)
                print(f"AI: {response}")
                print(
                    f"トークン使用量: {cb.total_tokens} (プロンプト: {cb.prompt_tokens}, 生成: {cb.completion_tokens})"
                )


if __name__ == "__main__":
    multi_bot = MultiPersonalityBot()
    run_chat_session(multi_bot)
