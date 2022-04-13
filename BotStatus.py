import discord
from discord.ext import commands
import asyncio
import os
import subprocess

from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook$

client = discord.Client()
# Insira o Token do bot

Dbd_BOT = <seu TOKEN>

berrybot = commands.Bot(command_prefix='!')
uRL= "Sua Url Webhook
@berrybot.event
async def on_ready():
    g = open("dontstarvetogether_dedicated_server/version.txt",mode='r', encodi$
    f = open("/tmp/restartrunserver.log",mode='r', encoding='cp1252')
    webhook = Webhook.from_url(uRL, adapter=RequestsWebhookAdapter()) # Initial$
    webhook.send(content=str(f.readlines()[-1])) # Executing webhook.
    webhook.send(content=str('VERSAO '+str(g.read())))

berrybot.run(Dbd_BOT)


