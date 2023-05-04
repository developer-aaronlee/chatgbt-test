import requests

url = "https://api.openai.com/v1/images/generations"
api_key = "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"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

prompt = input("Describe An Image: ")

data = {
    "model": "image-alpha-001",
    "prompt": prompt,
    "num_images": 1,
    "size": "512x512",
    "response_format": "url",
}


def generate_response():
    response = requests.post(url, headers=headers, json=data)
    image_url = response.json()["data"][0]["url"]
    print(f"Image Output: {image_url}")


while True:
    generate_response()
    rerun_prompt = input("Regenerate Response? Y/N: ").upper()
    if rerun_prompt == "Y":
        continue
    else:
        break

