import openai

openai.api_key = "PasteYourAPIKeyHere"

chat_prompt = ""

while(True):

    chat_prompt = input("Enter message for Chat GPT: ")

    if chat_prompt.lower() == "#exit":
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": chat_prompt},
            ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(result)