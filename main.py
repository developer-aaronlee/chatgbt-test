import requests

url = "https://api.openai.com/v1/chat/completions"
api_key = "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"
chatgpt_roles = {"assistant": "You are a helpful assistant.",
                 "instructor": "You are an instructor for a programming course.",
                 "expert": "You are an expert in Python programming."}
selected_role = chatgpt_roles["assistant"]
question = input("Ask ChatGPT A Question:\n")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": f"{selected_role}"},
        {"role": "user", "content": f"{question}"}
    ]
}


def generate_response():
    response = requests.post(url, headers=headers, json=data)
    answer = response.json()["choices"][0]["message"]["content"]
    print(f"ChatGPT Answer:\n{answer}")


while True:
    generate_response()
    rerun_prompt = input("Regenerate Response? Y/N: ").upper()
    if rerun_prompt == "Y":
        continue
    else:
        break

