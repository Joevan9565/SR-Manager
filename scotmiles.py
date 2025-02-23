import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

amount = any
current_balance = any

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents) 

# User Points Dictionary
user_points = {}

@bot.command()
async def points(ctx):
    user_id = ctx.author.id
    points = user_points.get(user_id, 0)
    await ctx.send(f'You have {points} ScotMiles!')

@bot.command()
async def add_points(ctx, user: discord.User, points: int):
    user_id = user.id
    user_points[user_id] = user_points.get(user_id, 0) + points
    await ctx.send(f'{points} ScotMiles added to {user.name}!')

@bot.command()
async def remove_points(ctx, user: discord.User, points: int):
    user_id = user.id
    user_points[user_id] = user_points.get(user_id, 0) - points
    await ctx.send(f'{points} ScotMiles removed from {user.name}!')

@bot.command()
async def reset_points(ctx, user: discord.User):
    user_id = user.id
    user_points[user_id] = 0
    await ctx.send(f'ScotMiles for {user.name} have been reset!')

@bot.command()
async def leaderboard(ctx):
    sorted_users = sorted(user_points, key=user_points.get, reverse=True)
    leaderboard = 'Leaderboard:\n'
    for index, user_id in enumerate(sorted_users, start=1):
        user = bot.get_user(user_id)
        leaderboard += f'{index}. {user.name} - {user_points[user_id]} ScotMiles\n'
    await ctx.send(leaderboard)

@bot.command()
async def redeeem(ctx, points: int):
    user_id = ctx.author.id
    if user_points.get(user_id, 0) >= points:
        user_points[user_id] -= points
        await ctx.send(f'{points} ScotMiles redeemed!')
    else:
        await ctx.send('Insufficient ScotMiles!')   

    if amount < 0:
        await ctx.send('Invalid Amount!')
        return
    
    if amount > current_balance:
        await ctx.send('Insufficient Balance!')
        return

    current_balance -= amount
    await ctx.send(f'{amount} ScotMiles redeemed!')

process = any
bot.run(DISCORD_TOKEN)