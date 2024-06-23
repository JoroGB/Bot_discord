import discord
from discord.ext import commands
import os

from discord.ext.commands import Context
from discord.ext.commands._types import BotT
from discord.ext.commands.converter import T_co
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN_DISCORD")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="^", intents=intents, status="online")


class Retorna(commands.Converter):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # Los convertidores deben de tener el nombre de convert si no tira un Attribute error
    @classmethod
    async def convert(cls, ctx, name):
        return cls(nombre=name, edad=12)


@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


@bot.command()
async def nombrar(ctx, *, re: Retorna):
    await ctx.send(f"Te nombro como {re.nombre} y tu edad es de {re.edad}")


bot.run(TOKEN)
