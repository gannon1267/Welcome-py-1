import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or('F^ ', 'F^'), intents=intents)
welcome_text = "welcome to the server yata yata yata"

@bot.check
async def check(ctx):
    member = ctx.author
    print(member)
    if str(member) == "equinox#7480" or str(member) == "LittleFenne#0001":
        print("true")
        return(True)
    else:
        print("false")
        return(False)
@bot.command()
async def gen_send(ctx, words, userid):
        general = bot.get_channel(923084022249320490) or await bot.fetch_channel(923084022249320490)
        allwordg=f"<@!{userid}> {words}"

        if userid == "none":
            await general.send(words)
        else:
            await general.send(allwordg)
      

@bot.command()
async def ent_send(ctx, words, userid):
    entrance = bot.get_channel(955071525256568892) or await bot.fetch_channel(955071525256568892)
    if userid == "none":
        await entrance.send(words)
    else:
        allworde=f"<@!{userid}> {words}"
        await entrance.send(allworde)
    

@bot.event
async def on_raw_reaction_add(payload):
  user = bot.get_user(payload.user_id) 
  channel = bot.get_channel(payload.channel_id)
  msg = await channel.fetch_message(payload.message_id)
  auth = mesg.author.id
  emoji = str(payload.emoji)
  auth_role = payload.member.guild.get_role(955566126518136854)
  if auth_role in payload.member.roles:
      rolev = payload.member.guild.get_role(955569859956191314)
      roleu = payload.member.guild.get_role(955969005234040842)
      if emoji == "✅":
          await payload.member.add_roles(rolev)
          await payload.member.remove_roles(roleu)
          await msg.delete()
          await gen_send(user, welcome_text, auth)


bot.run("OTU1NDQwMjc5NDUwNzEwMDc2.YjhtGQ.kozZwra_R36aBqlq6PabGzgATVk")
