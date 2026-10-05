import anthropic

client = anthropic.Anthropic()


def summarize(text: str) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=512,
        messages=[{"role": "user", "content": text}],
    )
    return message.content[0].text
