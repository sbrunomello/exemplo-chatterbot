from chatterbot import ChatBot
bot = ChatBot('Bot')

print('Digite algo...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break