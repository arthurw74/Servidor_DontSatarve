import discord
from discord.ext import commands
import asyncio
import os
import subprocess

from discord import Webhook, RequestsWebhookAdapter # Importing discord.Webhook$

client = discord.Client()
# Insira o Token do bot

Dbd_BOT = "OTI5MDcyNDk5MDcxODA3NjA5.YdiAMQ.Wrj5CLAb_Q3svKqmzLPInBCJF2w"

berrybot = commands.Bot(command_prefix='!')
uRL= 'https://discord.com/api/webhooks/955225408289263657/JLZv-8T9AOs1rXfe1SxBS$
@berrybot.event
async def on_ready():
    g = open("dontstarvetogether_dedicated_server/version.txt",mode='r', encodi$
    f = open("/tmp/restartrunserver.log",mode='r', encoding='cp1252')
    webhook = Webhook.from_url(uRL, adapter=RequestsWebhookAdapter()) # Initial$
    webhook.send(content=str(f.readlines()[-1])) # Executing webhook.
    webhook.send(content=str('VERSAO '+str(g.read())))

berrybot.run(Dbd_BOT)


