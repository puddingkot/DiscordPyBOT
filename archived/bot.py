import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('jestem online :)'))
    print('bot jest gotowy.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='PokeTrener')
    await client.add_roles(member, role)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'zbanowano {member.name}#{member.discrimation}')

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

client.run('TokenHere')
