from settings import settings
import discord
from bot_logic import *
from comandos import comandos

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if not message.content.startswith('$') and not message.content.startswith('oi'):
        return
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        senha = gen_pass(12)
        await message.channel.send(f"Sua senha é: `{senha}`")
    elif message.content.startswith("$comandos"):
        await message.channel.send("Esses são os comandos existentes:" + str(comandos))
    elif message.content.startswith("oi"):
        await message.channel.send("Olá, Como posso ajudar? Caso queira saber os comandos digite: $comandos")
    else:
        await message.channel.send("Não entendo esse comando!")

client.run(settings["TOKEN"])