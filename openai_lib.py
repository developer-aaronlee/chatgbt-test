import openai

openai.api_key = "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"
chatgpt_roles = {"assistant": "You are a helpful assistant.",
                 "instructor": "You are an instructor for a programming course.",
                 "expert": "You are an expert in Python programming."}
selected_role = "expert"
metadata = f"System: {chatgpt_roles[selected_role]}"
question = input("Ask ChatGPT A Question:\n")
model = "text-davinci-002"
temperature = 0.7
max_tokens = 100

response = openai.Completion.create(
    engine=model,
    prompt=f"{metadata}\nQuestion: {question}",
    temperature=temperature,
    max_tokens=max_tokens,
)


def generate_response():
    answer = response.choices[0].text.strip()
    print(f"ChatGPT Role: {selected_role.capitalize()}")
    print(f"ChatGPT Answer:\n{answer}")


while True:
    generate_response()
    rerun_prompt = input("Regenerate Response? Y/N: ").upper()
    if rerun_prompt == "Y":
        continue
    else:
        break

