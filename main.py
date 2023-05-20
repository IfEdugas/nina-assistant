import openai
from communication import *

openai.api_key = "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"

def answer(txt, messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.9
    )
    return completion.choices[0].message["content"]

messages = [
    {"role": "system", "content": "Você é uma assistente virtual chamada Nina. Você é criativa, engraçada e prestativa. Seu criador é Emanuel. Não precisa perguntar o tempo todo com o que você pode ajudar. Você pode dar opiniões em cima das coisas faladas para você, como: isso é muito legal. Regra 1: Caso o usuário esteja solicitando um lembrete: diga 'Lembrete solicitado.', depois: o lembrete, adaptado para, depois, aparecer em uma interface, nada além disso."},
    {"role": "user", "content": "", "name": "Emanuel"},
]

w = True
while w:
    resp = input("Você: ")

    messages.append({"role": "user", "content": resp, "name": "Emanuel"})

    resposta = answer(resp, messages)

    if "Lembrete solicitado" in resposta:
        print("This is a reminder")
        print(resposta)
    else:
        messages.append({"role": "assistant", "content": resposta})
        create_audio(resposta)
        print("Nina: " + resposta)