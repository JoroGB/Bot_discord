from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

TOKEN: str = os.getenv("TOKEN_DISCORD")

intents = discord.Intents.default()
intents.message_content = True  # Habilita el intent para recibir el contenido de los mensajes
bot = commands.Bot(command_prefix="^", intents=intents, status="online")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


class GetAcciones:
    def __init__(self, id_c, valor):
        self.id = id_c
        self.valor = valor

    @classmethod
    async def convert(cls, ctx, name):
        from pycoingecko import CoinGeckoAPI
        cg = CoinGeckoAPI()
        price = cg.get_price(ids=name, vs_currencies='usd')
        return cls(id_c=name, valor=price[name]['usd'])


@bot.command()
async def pyg(ctx, *, cripto: GetAcciones):
    await ctx.send(f"Value of {cripto.id} is equal to {cripto.valor} usd")


bot.run(TOKEN)
