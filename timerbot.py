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
	
	if message.author.bot or not message.server:
		await client.send_message(message.channel, "Life can turn at any point and one may never realize it. From one event to the other our minds react to what we see in front of our eyes. We may not enjoy what we see but at times it is what we need to see. Life has a funny way of cracking those that think they know the way to go. Whether it be what you want or what you hate it won't go as planned. There always has to be one difficulty to make the achievable worth while. For the people that may never know the secrets they need to be told. Feel lucky. There are many words people might desire you ask to know but you never know to ask or how to say it because the truth hurts. Sometimes people do bad things to others to put themselves ahead and when it's time to come clean, they pity themselves and not the other. Greed is the weakness of every human. Not a single person can live on this earth without feeling the effects of greed. Want, want, want is all the brain desires. When the brain doesn't get what it desires it gets upset. Upset can range between crying to punching. The effects of the brain on how it chooses what to do in a given action is due to the build up. Many times the most passive person can want to punch, kick and scream but because of the upbringing will refrain from such action. They learned that punching, kicking and screaming has not given them anything they want in life through the childhood they had.")
		await client.send_message(message.channel, "Others however have decided that talking is never the way to go. Thinking just isn't an option. It's game on when the news breaks. This news can destroy the world. The problem is when does wanting something become evil. When does telling someone the truth of life give nothing in return. Like I previously stated, life has a way of doing the exact opposite of what is a expected. Telling the truth to those that need it might make certain things possible but how will it turn out in 5 years when you have what you want but the way you got it was evil and cruel and greedy. Also what happens when someone reveals your secret that you ratted out their secret for your own benefit? How will that affect them in the future. There is no answer. Life has a million ways to answer a single question, the greatest determiner of how things will go is time. Therefore we have TimerBot.")
		return
	
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
