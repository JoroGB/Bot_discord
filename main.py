from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
load_dotenv()


TOKEN: str = os.getenv("TOKEN_DISCORD")

intents = discord.Intents.default()
intents.message_content = True # Habilita el intent para recibir el contenido de los mensajes
bot = commands.Bot(command_prefix="^", intents=intents, status="online")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command(name="msg")
async def message(ctx, *, arg):
    await ctx.send(arg)


@bot.command()
async def add(ctx, a:int, b:int):
    await ctx.send(a + b)



def upper_(argument: str):
    return argument.upper()
@bot.command()
async def up(ctx, *, content:upper_):
    await ctx.send(content)

@bot.command()
async def send_image(ctx):
    with open("src/img.png") as image:
        await ctx.send(image)


bot.run(TOKEN)

    k