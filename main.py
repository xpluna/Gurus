import discord
from os import getenv
from random import choice
from discord.ext import commands

prefix = 'k.'

intents = discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='k.', intents=intents)

bot.remove_command('help')

@bot.event
async def on_connect():
	print(f"Connected - {bot.user}")

# Help
@bot.command()
async def help(ctx, category=None):
	
	if category == None:
		embed = discord.Embed(title='Help', description=f'{prefix}help <category>', color=0x920505)
		embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)

		embed.add_field(name='Please choose a category', value='support\nmisc', inline=False)
		embed.set_footer(text='Written in Python with Sublime Text 3')
		await ctx.send(embed=embed)
	
	elif category == 'misc':
		embed = discord.Embed(title='Miscellaneous', color=0x920505)
		embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
		misG = {'echo <message>': 'Echo a message',	'rps <rock(r)/paper(p)/scissors(s)>': 'Play rock paper scissors with me!', 'toss <optional prediction Heads/Tails>': 'Flip a coin', 'rolldie <optional prediction 1-6>': 'Roll a die', 'si': 'Shows guild info', 'membercount': 'Shows guild\'s member count', 'donate': 'SkidLamer\'s Donation info.', 'invite': 'Invite the bot', "spoil <message>": "Returns a raw message with every character enclosed with ||"}
		for k, v in misG.items(): embed.add_field(name=f'{prefix}{k}', value=f'{v}', inline=False)
		embed.set_footer(text='Any user can run these commands')
		await ctx.send(embed=embed)
	
	elif category == 'support':
		embed = discord.Embed(title='Support', color=0x920505)
		embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
		supG = {'ts': 'Troubleshooting guide', 'ip': 'IP-Ban bypass guide', 'kr': 'KR-Farming guide', 'vpn': 'Lists renowned VPNs', 'info': 'Cheat-terms\' glossary'}
		for k, v in supG.items(): embed.add_field(name=f"{prefix}{k}", value=f'{v}', inline=False)
		embed.set_footer(text='Any user can run these commands')
		await ctx.send(embed=embed)

	else:
		await ctx.send(embed=discord.Embed(title='Error', color=0x920505, description='Unknown category'))

# Misc Commands
## echo, rolldie, toss, rps, members, si, donate, invite, spoil
@bot.command()
async def echo(ctx, message):
	if message:
		if ctx.author == bot.user:
			await ctx.send(f"||{'||||'.join('bruh')}||")

		else:
			await ctx.send(message)
		
		await ctx.message.delete()
	
	else:
		await ctx.send(embed=discord.Embed(title='Error', description=f'Usage - {prefix}echo <message>', color=0x920505))

@bot.command()
async def rolldie(ctx, pdt=None):
	if pdt:
		doc = choice([_ for _ in range(1,7)])
		if str(pdt).strip() == str(doc):
			await ctx.send(f':game_die: **{str(ctx.author)[:-5]}** predicted `{pdt}` :game_die:\nAnd rolled  a `{doc}`! :exploding_head:')
		else:
			await ctx.send(f':game_die: **{str(ctx.author)[:-5]}** predicted `{pdt}` :game_die:\nBut rolled  a `{doc}`! :disappointed:')
	else:
		oc = choice([_ for _ in range(1,7)])
		await ctx.send(f':game_die: **{str(ctx.author)[:-5]}** rolled a `{oc}` :game_die:')

@bot.command()
async def toss(ctx, pdt=None):
	if pdt:
		coc = choice(['Heads', 'Tails'])
		if coc == 'Heads':
			if str(pdt).lower().startswith('h'):
				await ctx.send(f':coin: **{str(ctx.author)[:-5]}** predicted `Heads` :coin:\nAnd got `Heads` :exploding_head:')
			else:
				await ctx.send(f':coin: **{str(ctx.author)[:-5]}** predicted `Tails` :coin:\nBut got `Heads`! :disappointed:')
		else:
			if str(pdt).lower().startswith('t'):
				await ctx.send(f':coin: **{str(ctx.author)[:-5]}** predicted `Tails` :coin:\nAnd got `Tails` :exploding_head:')
			else:
				await ctx.send(f':coin: **{str(ctx.author)[:-5]}** predicted `Heads` :coin:\nBut got `Tails`! :disappointed:')
	else:
		ncoc = choice(['Heads', 'Tails'])
		await ctx.send(f':coin: **{str(ctx.author)[:-5]}** tossed a coin and got `{ncoc}` :coin:')

@bot.command()
async def rps(ctx, ch=None):
	if not ch:
		await ctx.send(embed=discord.Embed(title='Error', description=f'Usage - {prefix}rps <rock[r]/paper[p]/scissors[s]>', color=0x920505))
	else:
		if choice(['rock', 'paper', 'scissors']) == 'rock':
			if str(ch).lower().startswith('r'):
				await ctx.send(f'(~~Gurus~~) :rock: vs :rock: (~~{str(ctx.author)[:-5]}~~)\nTie! Try again if you want to and probably you\'ll lose :D')
			elif str(ch).lower().startswith('s'):
				await ctx.send(f'(**Gurus**) :rock: vs :scissors: (~~{str(ctx.author)[:-5]}~~)\nHaha, I won! GG')
			elif str(ch).lower().startswith('p'):
				await ctx.send(f'(~~Gurus~~) :rock: vs :newspaper: (**{str(ctx.author)[:-5]}**)\nYou won! GG')
			else: return
		elif choice(['rock', 'paper', 'scissors']) == 'paper':
			if str(ch).lower().startswith('p'):
				await ctx.send(f'(~~Gurus~~) :newspaper: vs :newspaper: (~~{str(ctx.author)[:-5]}~~)\nTie! Try again if you want to and probably you\'ll lose :D')
			elif str(ch).lower().startswith('r'):
				await ctx.send(f'(**Gurus**) :newspaper: vs :rock: (~~{str(ctx.author)[:-5]}~~)\nHaha, I won! GG')
			elif str(ch).lower().startswith('s'):
				await ctx.send(f'(~~Gurus~~) :newspaper: vs :scissors: (**{str(ctx.author)[:-5]}**)\nYou won! GG')
			else: return
		elif choice(['rock', 'paper', 'scissors']) == 'scissors':
			if str(ch).lower().startswith('s'):
				await ctx.send(f'(~~Gurus~~) :scissors: vs :scissors: (~~{str(ctx.author)[:-5]}~~)\nTie! Try again if you want to and probably you\'ll lose :D')
			elif str(ch).lower().startswith('p'):
				await ctx.send(f'(**Gurus**) :scissors: vs :newspaper: (~~{str(ctx.author)[:-5]}~~)\nHaha, I won! GG')
			elif str(ch).lower().startswith('r'):
				await ctx.send(f'(~~Gurus~~) :scissors: vs :rock: (**{str(ctx.author)[:-5]}**)\nYou won! GG')
			else: return

@bot.command()
async def members(ctx):
	await ctx.send(embed=discord.Embed(title=ctx.guild, description=f'{ctx.guild.member_count} members!', color=0x920505))

@bot.command()
async def si(ctx):
	embed = discord.Embed(title='Server Info', color=0x920505)
	embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
	embed.set_footer(text=f"Guild ID: {ctx.guild.id}")
	embed.add_field(name='Owner', value=f'{ctx.guild.owner.mention}', inline=True)
	embed.add_field(name='Region', value=f'{ctx.guild.region}', inline=True)
	embed.add_field(name='Member Count', value=f'{ctx.guild.member_count}', inline=True)
	embed.add_field(name='Verification Level', value=f'{ctx.guild.verification_level}')
	await ctx.send(embed=embed)

@bot.command()
async def donate(ctx):
	await ctx.send(embed=discord.Embed(title="Donate to SkidLamer!",
						   description="Hey dont forget to donate to the once who works to provide these\nKrunker.io Cheats <a:rapswe_warning:763926124812042250>\n\n" +
										":money_with_wings: Here are ways you can donate :money_with_wings:\n\n" +
										"> Donate in Bitcoin\n" +
										"> -Address :  3CsDVq96KgmyPjktUe1YgVSurJVe7LT53G\n\n" +
										"> Donate in Ethereum\n" +
										"> -Address : 0x5dbF713F95F7777c84e6EFF5080e2f0e0724E8b1\n\n" +
										"> Donate in Ethereum Classic\n" +
										"> -Address : 0xF59BEbe25ECe2ac3373477B5067E07F2284C70f3\n\n" +
										"> Donate in Amazon eGift Card\n" +
										"> -Link : <https://amzn.to/346KrxT>. -Email : skidlamer@mail.com\n\n" +
										"Thank you all for the continuous support :revolving_hearts:",
						   color=0x009330))

@bot.command()
async def invite(ctx):
	await ctx.send('**Invite the bot** - https://discord.com/api/oauth2/authorize?client_id=866586315733860382&permissions=419840&scope=bot')

@bot.command()
async def spoil(ctx, *, message):
	embed = discord.Embed(title="Spoiled Message", color=0x920505)
	embed.set_footer(text=ctx.author)
	embed.add_field(name="Result", value="||"+"||||".join(message)+"||", inline=False)
	embed.add_field(name="Raw", value="```||"+"||||".join(message)+"||```")
	await ctx.send(embed=embed)

# Support Commands
## ip, kr, ts, info, vpn
@bot.command()
async def ip(ctx):
	embed = discord.Embed(title=":hammer: IP-Ban Bypass Methods :open_mouth:", description="Guide to Bypass IP Ban `Connection Banned 0x1`\nChange VPN in case of `Connection Banned 0x2`", color = 0x920505)
	embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
	embed.add_field(name="`1` Unplug your router for some (5-10) minutes", value="Works **only** with *Dynamic* IPs.", inline=False)
	embed.add_field(name="`2` Use a VPN", value=f"There are free VPNs out in the residence, which may be\n slower, have time limits on connection and other cons.\nYou can get them from the web store. Use `{prefix}vpn` for a list of VPNs", inline=False)
	embed.add_field(name="`3` Krunker's Proxy Server", value="https://browserfps.com", inline=False)
	embed.set_footer(text="Join us! https://skidlamer.github.io/wp")
	
	await ctx.send(embed=embed)

@bot.command()
async def kr(ctx):
	embed = discord.Embed(title=":money_with_wings: KR-Farming Methods :money_with_wings:", color=0x920505)
	embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
	embed.add_field(name="`1` Enabling Challenge Mode ||Level 30+||", value="Increase the KR you earn by **1.5 times**!\nBut, your HP will fall by **50%** *oeuf*", inline=False)
	embed.add_field(name="`2` Free Spins", value="You get a sweet chance to try your luck by\nusing the **Free** Spin for watching an *AD*\n***every hour*** after completing a match.", inline=False)
	embed.add_field(name="`3` Playing games. No shit.", value=":nerd:", inline=False)
	embed.set_footer(text="You cannot hack KR. No shit.")
	
	await ctx.send(embed=embed)

@bot.command()
async def ts(ctx):
	embed = discord.Embed(title="Troubleshooting",
						  description="Troubleshooting Guide",
						  color = 0x920505)
	embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
	embed.add_field(name="`1` Showing Discord invite / Update Prompt",
					value="Update the script. Either wait for update or ask\nothers to check if it doesn't work.",
					inline=False)
	embed.add_field(name="`2` High Ping",
					value="Change VPN location nearest to your country, or\nPlay in servers nearest to your location.\nConsider upgrading your internet connection\n(if nothing helps)",
					inline=False)
	embed.add_field(name="`3` Game not Loading",
					value="Re-install script from the update links, or\nUse another hack or wait for an update, or\nClear browser *cache* `Ctrl + Shift + Delete`",
					inline=False)
	embed.add_field(name="`4` Failed to Fetch / Socket Error",
					value="Re-install script, and\nClear cache, or\nSwitch hack",
					inline=False)
	embed.set_footer(text="Join us! https://skidlamer.github.io/wp")
	await ctx.send(embed=embed)
	
@bot.command()
async def info(ctx, page=1):
	embed = discord.Embed(title="Info", color = 0x920505)
	embed.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)
	if page == 1:
		cheG = {"Aim range": "[0, 1000, 10] Set above 0 to make the aimbot pick enemies only at the selected range.", "Aim offset": "[-4, 1, 0.1] The lower it is, the lower the aimbot will shoot (0=head, -4=body).", "Aim noise": "[0, 2, 0.005] The higher it is, the lower is the aimbot accuracy.", "Supersilent aim": "Only works with quickscope and silent aim, makes it almost invisible that you're looking at somebody when you're shooting at him.", "Aim at AIs": "Makes the aimbot shoot at NPCs.", "FOV check": "Makes you only shoot at enemies that are in your field of view. Prevents 180 flicks."}
		for k, v in cheG.items(): embed.add_field(name=k, value=v, inline=True)
		embed.set_footer(text=f"Restart is required after changing any of these settings.")
		await ctx.send(embed=embed)
	elif page == 2: 
		cheG = {"FOV box": "Creates a box in which enemies can be targetted, enable with FOV check.", "Wallbangs"	: "Makes the aimbot shoot enemies behind walls.", "Aimbot range check": "Checks if the enemy is in range of your weapon before shooting it, disable for rocket launcher.", "Auto reload": "Automatically reloads your weapon when it's out of ammo.", "Prevent melee throwing": "Prevents you from throwing your knife.", "Mark aimbot target": "Shows who is the aimbot targetting at the time, useful for aim assist/aim correction."}
		for k, v in cheG.items(): embed.add_field(name=k, value=v, inline=True)
		embed.set_footer(text=f"Restart is required after changing any of these settings.")
		await ctx.send(embed=embed)
	elif page == 3: 
		cheG = {"Draw FOV box": "Draws the FOV box from aimbot settings.", "Friendly chams": "Show Chams for friendly players.", "RGB interval": "[50, 1000, 50] How fast will the RGB chams change colour.", "Skin hack": "Makes you able to use any skin in game, only shows on your side.", "Billboard shaders": "Disable if you get fps drops.", "Always aim": "Makes you slower and jump lower, but the aimbot can start shooting at enemies  faster. Only use if ur good at bhopping."}
		for k, v in cheG.items(): embed.add_field(name=k, value=v, inline=True)
		embed.set_footer(text=f"Restart is required after changing any of these settings.")
		await ctx.send(embed=embed)
	elif page == 4: 
		cheG =	{"Show GUI button": "Disable if you don't want the dog under settings to be visible.", "GUI on middle mouse button": "Makes it possible to open this menu by clicking the mouse wheel.", "Keybinds": "Turn keybinds on/off, Aimbot-Y, ESP-H.", "No inactivity kick": "Disables the 'Kicked for inactivity' message (client side, but works).", "Auto nuke": "Automatically nukes when you are able to.", "Force nametags on": "Use in custom games with disabled nametags."}
		for k, v in cheG.items(): embed.add_field(name=k, value=v, inline=True)
		embed.set_footer(text=f"Restart is required after changing any of these settings.")
		await ctx.send(embed=embed)
	elif page == 5: 
		cheG = {"Use Kpal CSS": "Use the kpal CSS when no custom CSS is Applied.", "Uncap FPS": "Disables V-Sync.", "Adblock": "Disables ads.", "s m o o t h n e s s": 'Decreases the speed on locking the player thus making it smooth\n(**makes hax less sussy**)'}
		for k, v in cheG.items(): embed.add_field(name=k, value=v, inline=True)
		embed.set_footer(text=f"Restart is required after changing any of these settings.")
		await ctx.send(embed=embed)
	elif page > 5: await ctx.send('There are only 5 pages, ye stupid.')

@bot.command()
async def vpn(ctx):
	embed = discord.Embed(title="List of VPNs", description="Renowned VPNs", color = 0x920505)
	vpns = {"WindScribe"	 : "https://windscribe.com/",
			"Proton"		 : "https://protonvpn.com/",
			"HideMe"		 : "https://hide.me/",
			"Setup"		         : "https://setupvpn.com/",
			"VeePN"			 : "https://veepn.com/",
			"Earth"			 : "https://earthvpn.com/",
			"OneClick"		 : "https://vpnoneclick.com/",
			"ZenMate"		 : "https://zenmate.com/",
			"HotSpot Shield"         : "https://www.hotspotshield.com/",
			"TunnelBear"	         : "https://www.tunnelbear.com/",
			"SurfShark"		 : "https://surfshark.com/"}
	for k, v in vpns.items(): embed.add_field(name=k, value=v, inline=True)
	embed.set_footer(text="Join us! https://skidlamer.github.io/wp")
	await ctx.send(embed=embed)

bot.run(getenv('token'))
