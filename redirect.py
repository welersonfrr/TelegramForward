import requests
from telethon import TelegramClient, events

# Obtenha seus valores em: my.telegram.org!
api_id = 123456789
api_hash = '1a2b3c4d5e6f7g8h9i0j'

# Criar bot via @BotFather
botToken = '123456789:1a2b3c4d5e6f7g8h9i0j'
url = 'https://api.telegram.org/bot' + botToken + '/sendMessage?'

xFrom = -123456789
xTo = -987654321

async def sendApi(msg):
    requests.post(url, json = msg)
    
client = TelegramClient('anonUser', api_id, api_hash)
@client.on(events.NewMessage(chats=[xFrom]))

async def main(event):
    me = await client.get_me()
    mensagem = event.message.message

    print('New message: ')
    print(event.message.message)
    print(' ')

    msg = {
        'chat_id':xTo,
        'parse_mode':'Markdown',
        'text': mensagem
    }
    await sendApi(msg)

with client:
    client.run_until_disconnected()

   