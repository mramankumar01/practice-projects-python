from openai import OpenAI

key = "sk-proj-AezsSxmA3iiQ6hz2DyfazNotRTlEyLnmg4kj4uZZaVmdL432grt4JsHsnIb1Ozls4xy4Ear9vvH3BlbkFJ80NGrk84euFQoGahQA_7U0BKp9uBcWmGwdOop19Uz9A0lDgVLm6TS0TEH54G0GKyitz8gBrqkA"

messages = [] # Context Manager

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(messages=messages, model="gpt-4o")

    # print(chat_completion)

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message) # keeps the context
    print(f"Jarvis: {message["content"]}")

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis, How may I help you?")
    # print("User: ", end="")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)




