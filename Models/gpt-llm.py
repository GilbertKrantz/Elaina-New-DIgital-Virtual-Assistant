import openai

openai.api_key = "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"

messageHistory = []

def chat(input:str, role = "user"):
    messageHistory.append({"role": role, "content": input})
    completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = messageHistory)
    reply = completion.choices[0].message.content
    messageHistory.append({"role": "assistant", "content": reply})

    return reply
