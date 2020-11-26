import discord
from discord.ext import commands
import json

token = "NDc3MTY4Mzc3NTA5NzA3Nzc2.W2x7rg.QSoD3Z7XaLoUnoiESlfO0kHyIwI"


def get_prefix(client, message):  # get the prefix of a server and use it only in the server!
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event
async def on_ready():
    # login of client
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='!help'))
    print('{0.user} just unleashed!'.format(client))


@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, prefix="-1"):
    if (prefix == "-1"):
        await ctx.send("You need to specify your prefix!")
        prefix = "."
        return

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f"Prefix changed to {prefix}")


client.run(token)
