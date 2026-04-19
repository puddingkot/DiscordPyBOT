import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

clientC = discord.Client(intents = intents)
client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('jestem online :)'))
    print('bot jest gotowy.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f"Użytkownik {member.name} został wyrzucony, pozdro")
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'zbanowano {member.name}')
    await member.ban(reason=reason)

# Unbans not working - need to be fixed / Unbany nie działają - potrzebna naprawa

@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discrimination):
            await ctx.guild.unban(user)
            await ctx.send(f'odbanowano {user.name}#{user.discrimination}')
            return



client.run('PlaceForAToken ;3')
