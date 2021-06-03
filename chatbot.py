from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Instanciando o bot, primeiro parâmetro é o nome (obrigatório)
# Segundo e terceiros parametros são para armazenar as conversas localmente
# E ficar mais "inteligente" com isso
bot = ChatBot(
    'ChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

#Instanciando ListTrainer passando como parâmetro o bot
trainer = ListTrainer(bot)

# Setando qual será o método de treino do bot
# Neste caso será uma pequena lista
trainer.train([
    'Oi',
    'Oi, tudo bem?',
    'Tudo bem, e você?',
    'Eu vou bem',
    'Qual seu nome?',
    'Meu nome é ' + bot.name + '!',
])

print('Digite algo...')

while True:
    try:
        user_input = input()

        # metódo get_response(pergunta) retorna uma resposta mais aproximada
        bot_response = bot.get_response(user_input)

        print(bot_response)

    # crtl + c para sair
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
