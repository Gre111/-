import openai

def query_gpt4(question):
    openai.api_key = "sk-qcQuCMd8xyjGyXHoC22930A7F0934f0f8b7d41578c33DaC2"
    #openai.base_url = url
    openai.base_url = 'https://api.gpts.vin/v1/chat/completions'


    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # 确认使用 GPT-4 模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        print(response)
        return response['choices'][0].message['content']
    except Exception as e:
        return str(e)

# 问题
question = "你能干什么？"

# 获取并打印回答
answer = query_gpt4(question)
print(answer)