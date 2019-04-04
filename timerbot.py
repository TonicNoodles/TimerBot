import discord
from datetime import datetime
from datetime import timedelta
import re
import time
import asyncio
import os

client = discord.Client()

paste = None # 2 hr
sap = None # 4 hr
paste279 = None # 2 hr
paste284 = None # 2 hr
paste299 = None # 2 hr
desert = None # 6 hr
ice = None # 6 hr
forest = None # 6 hr
crops = None # 4 hr

@client.event
async def on_ready():
	await client.change_presence(game = discord.Game(name = "the time.", type = 3))
	print("TimerBot is ready!")

@client.event
async def on_message(message):
	print(message.content)
	
	if message.author.bot: 
		return
		
	if not message.server:
		await client.send_message(message.channel, "Life can turn at any point and one may never realize it. From one event to the other our minds react to what we see in front of our eyes. We may not enjoy what we see but at times it is what we need to see. Life has a funny way of cracking those that think they know the way to go. Whether it be what you want or what you hate it won't go as planned. There always has to be one difficulty to make the achievable worth while. For the people that may never know the secrets they need to be told. Feel lucky. There are many words people might desire you ask to know but you never know to ask or how to say it because the truth hurts. Sometimes people do bad things to others to put themselves ahead and when it's time to come clean, they pity themselves and not the other. Greed is the weakness of every human. Not a single person can live on this earth without feeling the effects of greed. Want, want, want is all the brain desires. When the brain doesn't get what it desires it gets upset. Upset can range between crying to punching. The effects of the brain on how it chooses what to do in a given action is due to the build up. Many times the most passive person can want to punch, kick and scream but because of the upbringing will refrain from such action. They learned that punching, kicking and screaming has not given them anything they want in life through the childhood they had.")
		await client.send_message(message.channel, "Others however have decided that talking is never the way to go. Thinking just isn't an option. It's game on when the news breaks. This news can destroy the world. The problem is when does wanting something become evil. When does telling someone the truth of life give nothing in return. Like I previously stated, life has a way of doing the exact opposite of what is a expected. Telling the truth to those that need it might make certain things possible but how will it turn out in 5 years when you have what you want but the way you got it was evil and cruel and greedy. Also what happens when someone reveals your secret that you ratted out their secret for your own benefit? How will that affect them in the future. There is no answer. Life has a million ways to answer a single question, the greatest determiner of how things will go is time. Therefore we have TimerBot.")
		return
	
	global scar
	global paste
	global sap
	global paste279
	global paste284
	global paste299
	global desert
	global ice
	global forest
	global crops
	
	cmd = re.sub("[^A-Za-z]", "", message.content.lower())

	if cmd == "paste":
		if paste:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 7200) - (datetime.now() - paste)
			await client.send_message(message.channel, "A paste timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			paste = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(7200)
			await client.send_message(message.channel, "Server 188: Rag Paste is ready " + message.author)
			paste = None
		
	elif cmd == "279paste":
		if paste279:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 7200) - (datetime.now() - paste279)
			await client.send_message(message.channel, "An aberration paste timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			paste279 = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(7200)
			await client.send_message(message.channel, "Server 279: Aberration paste is ready " + message.author)
			paste279 = None

	elif cmd == "284paste":
                if paste284:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 7200) - (datetime.now() - paste284)
			await client.send_message(message.channel, "An aberration paste timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			paste284 = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(7200)
			await client.send_message(message.channel, "Server 284: Aberration paste is ready " + message.author)
			paste284 = None		

        elif cmd == "299paste":
               if paste299:
                	await client.add_reaction(message, "")
			remaining = timedelta(seconds = 7200) - (datetime.now() - paste299)
			await client.send_message(message.channel, "An aberration paste timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			paste299 = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(7200)
			await client.send_message(message.channel, "Server 299: Aberration paste is ready " + message.author)
			paste299 = None	
			
	elif cmd == "desert":
		if desert:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 21600) - (datetime.now() - desert)
			await client.send_message(message.channel, "The Desert Titan timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			desert = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(21600)
			await client.send_message(message.channel, "The Desert Titan is ready <@&550711821682606085>")
			desert = None		
	
	elif cmd == "ice":
		if ice:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 21600) - (datetime.now() - ice)
			await client.send_message(message.channel, "The Ice Titan timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			ice = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(21600)
			await client.send_message(message.channel, "The Ice Titan is ready <@&550711821682606085>")
			ice = None		
	
	elif cmd == "forest":
		if forest:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 21600) - (datetime.now() - forest)
			await client.send_message(message.channel, "The Forest Titan timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			forest = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(21600)
			await client.send_message(message.channel, "The Forest Titan is ready <@&550711821682606085>")
			forest = None
			
	elif cmd == "crops":
		if crops:
			await client.add_reaction(message, "")
			remaining = timedelta(seconds = 14400) - (datetime.now() - crops)
			await client.send_message(message.channel, "The crops timer is already running. Time remaining: " + str(remaining).split(".")[0])
		else:
			crops = datetime.now()
			await client.add_reaction(message, "")
			await asyncio.sleep(14400)
			await client.send_message(message.channel, "The crops are ready " + message.author)
			crops = None
				
print(os.getenv("BOT_TOKEN"))	
client.run(os.getenv("BOT_TOKEN")) 
