import json
import openai


with open("ChatGPT/secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_key"]


openai.api_key = api_key


def get_response(message: list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=1.0
    )
    return response.choices[0].message


if __name__ == "__main__":
    nome = "EMILY"
    messages = [
        {"role": "system", "content": f"Sei un assistente virtuale chiamata {nome} e parli italiano."}
    ]
    try:
        while (True):
            user_input = input("\nTu: ")
            messages.append({"role": "user", "content": user_input})
            new_message = get_response(message=messages)
            print(f"\n{nome}: {new_message['content']}")
            messages.append(new_message)
    except KeyboardInterrupt:
        print("A presto!")
