import discord
from datetime import datetime
from datetime import timedelta
import re
import time
import asyncio
import os

client = discord.Client()

scar = None # 45 min
paste = None # 2 hr
sap = None # 4 hr

@client.event
async def on_ready():
	await client.change_presence(game = discord.Game(name = "the time.", type = 3))
	print("TimerBot is ready!")

@client.event
async def on_message(message):
	print(message.content)
	
	if message.author.bot: return
    if message.server is None: return 
		await client.send_message(message.channel, "Test")
		await client.send_message(message.channel, "Test")
    await client.process_commands(message)
	
	global scar
	global paste
	global sap
	
	cmd = re.sub("[^A-Za-z]", "", message.content.lower())

	if cmd == "scar":
		if scar:
			await client.add_reaction(message, "🚫")
			remaining = timedelta(seconds = 2700) - (datetime.now() - scar)
			await client.send_message(message.channel, "A scar timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			scar = datetime.now()
			await client.add_reaction(message, "✅")
			await asyncio.sleep(2700)
			await client.send_message(message.channel, "Scar is ready @here")
			scar = None
	
	elif cmd == "paste":
		if paste:
			await client.add_reaction(message, "🚫")
			remaining = timedelta(seconds = 7200) - (datetime.now() - paste)
			await client.send_message(message.channel, "A paste timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			paste = datetime.now()
			await client.add_reaction(message, "✅")
			await asyncio.sleep(7200)
			await client.send_message(message.channel, "Paste is ready @here")
			paste = None
	
	elif cmd == "sap":
		if sap:
			await client.add_reaction(message, "🚫")
			remaining = timedelta(seconds = 14400) - (datetime.now() - sap)
			await client.send_message(message.channel, "A sap timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			sap = datetime.now()
			await client.add_reaction(message, "✅")
			await asyncio.sleep(14400)
			await client.send_message(message.channel, "Sap is ready @here")
			sap = None
	
print(os.getenv("BOT_TOKEN"))	
client.run(os.getenv("BOT_TOKEN"))
