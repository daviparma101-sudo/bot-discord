from settings import settings
import discord
from bot_logic import *
from discord.ext import commands
from comandos import *

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')
@bot.command()
async def ola(ctx):
    await ctx.reply("Olá!")

@bot.command()
async def moeda(ctx):
    resultado = flip_coin()
    await ctx.reply(resultado)

@bot.command()
async def senha(ctx, tamanho):
    senha_gerada = gen_pass(int(tamanho))
    await ctx.reply(senha_gerada) 

@bot.command()
async def comandos(ctx):
    comandos = ["/senha (numero), /moeda, /ola, /comandos"]
    await ctx.reply(f"os comandos são {comandos}")


bot.run(settings["TOKEN"]) 
