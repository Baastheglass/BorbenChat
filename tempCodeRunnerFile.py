from configparser import ConfigParser 
from chatbot import chatBot
from chatbot import construct_message
import json

def main():
    config = ConfigParser()
    config.read('credentials.ini')
    api_key = config['gemini_app']['API_KEY']
    #chatbot = chatBot(api_key = api_key)
    chatbot = chatBot()
    chatbot.start_Conversation()
    print("Welcome to Baasil's chatbot!. Type quit to exit")
    while True:
        user_input = input("You: ")
        chatbot.conversation_history.append(construct_message(user_input))
        if(user_input.lower() == "quit"):
            print("Exiting :(")
            break
        try:
            response = chatbot.send_Prompt(user_input)
            print(type(response))
            res = json.loads(response)
            print(f"{chatbot.CHATBOT_NAME}: " + f"{res['text']}")
            for history in chatbot.conversation_history:
                print(history)
        except Exception as exp:
            print("Main exception caught")
            print(f"Error: {exp}")
main()