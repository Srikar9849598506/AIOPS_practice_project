import ollama


def summarize(text):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": f"""
                Summarize the following news in exactly one bullet point.

                Text:
                {text}
                """
            }
        ]
    )

    return response["message"]["content"]
