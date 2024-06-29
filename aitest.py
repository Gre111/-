from zhipuai import ZhipuAI

client = ZhipuAI(api_key="1a25d07bc3aff6067940fa7f760c8c89.TpFJTXGSpGKutIUx")
def generate_response(prompt):
    response = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "user", "content": prompt},
            # {"role": "assistant", "content": "我是人工智能助手"},
            # {"role": "user", "content": "你叫什么名字"},
            # {"role": "assistant", "content": "我叫chatGLM"},
            # {"role": "user", "content": "你都可以做些什么事"},
        ],
    )
    return response

while True:
    prompt = input("请输入：")
    if prompt == "exit":
        break
    if prompt != "":
        response = generate_response(prompt)
        print(response.choices[0].message.content)
# print(response.choices[0].message.content)