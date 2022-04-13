import discord
from discord.ext import commands
import asyncio
import os
import subprocess

from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook and discord.RequestsWebhookAdapter

client = discord.Client()
# Insira o Token do bot

Dbd_BOT = "You tokem"

berrybot = commands.Bot(command_prefix='!')
uRL= "sua URL"
@berrybot.event
async def on_ready():
    g = open("dontstarvetogether_dedicated_server/version.txt",mode='r', encoding='cp1252') 
    f = open("/tmp/restartrunserver.log",mode='r', encoding='cp1252')
    webhook = Webhook.from_url(uRL, adapter=RequestsWebhookAdapter()) # Initializing webhook
    webhook.send(content=str(f.readlines()[-1])) # Executing webhook.
    webhook.send(content=str('VERSAO '+str(g.read())))

berrybot.run(Dbd_BOT)


