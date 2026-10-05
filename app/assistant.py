from openai import OpenAI

client = OpenAI()


def answer(question: str) -> str:
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content or ""


def draw(prompt: str) -> str:
    image = client.images.generate(model="dall-e-3", prompt=prompt)
    return image.data[0].url or ""
