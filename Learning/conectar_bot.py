"""
Crear una app desde discord dev portal
luego de eso podemos proseguir con lo siguiente que es la connection y la importation de la libreria de discord
"""
import discord
# desde discord.ext importamos para los comandos del bot
from discord.ext import commands

# en este caso por temas de seguridad se usara variables de entorno
import os
from dotenv import load_dotenv
load_dotenv()

# necesitamos el token de Discord Dev Portal
TOKEN = os.getenv("TOKEN_DISCORD")
intents = discord.Intents.default()
intents.message_content = True  # Para poder recibir el contenido de los mensajes

# ajustamos algunos parameters del bot

bot = commands.Bot(command_prefix="^", intents=intents, status="online")


# command_prefix es el signo clave con el que podremos llamar las funciones que queramos del bot

# seguido podemos crear un comando para poder utilizarlo con el bot

# usando los decoradores se podra modificar funciones y parameters

# crear un evento

@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


# ejemplo
# una function que responda cuando se le llama

@bot.command()
async def message(ctx):
    await ctx.send("HOla")
    # el argumento ctx es el contexto en el cual se ejecuta el comando, este proporciona methods y atributos
    # en este caso estamos usando el method send para enviar un mensaje


# convertidores
# los convertidores en resumen reciben un o varios argumentos y retorna un tipo de valor distinto

@bot.command()
async def add(ctx, a: int, b: int):
    # Se requiere usar anotaciones para el uso del los convertidores
    await ctx.send(a + b)

# una function de esto es cuando queramos usar una function como parameter


def to_upper(argument: str) -> str.upper:
    return argument.upper()


@bot.command()
async def upper_(ctx, *, content: to_upper):
    await ctx.send(content)


bot.run(TOKEN)
