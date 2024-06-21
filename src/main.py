import discord
import os

TOKEN = os.environ
print(TOKEN["TOKEN_DISCORD"])
input()

intents = discord.Intents.default()
intents.messages_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send('Hello!')


client.run(TOKEN)
