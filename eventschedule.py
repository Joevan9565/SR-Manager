import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# Load the environment variables
load_dotenv()

# Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Bot Prefix
bot = commands.Bot(command_prefix='!')

# Events Dictionary
scheduled_events = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='schedule', help='Schedule an event')
async def schedule_event(ctx, time: int, *, event: str):
    scheduled_events[event] = time
    await ctx.send(f'{event} has been scheduled in {time} seconds')
    return

    await ctx.send (f'Scheduling {event_name} in {time} seconds')

# Create a task for the scheduled event
scheduled_events[event_name] = asyncio.create_task(event_task(ctx, time , event_name))

@bot.command()
async def cancel(ctx, event_name: str):
    if event_name in scheduled_events:
        scheduled_events[event_name].cancel()
        await ctx.send(f'{event_name} has been cancelled')
        return
    else:
        await ctx.send(f'{event_name} is not scheduled')
        return

@bot.command()
async def list(ctx):
    if len(scheduled_events) == 0:
        await ctx.send('No events are scheduled')
        return
    else:
        for event in scheduled_events:
            await ctx.send(f'{event} is scheduled in {scheduled_events[event]} seconds')
        return

async def event_task(ctx, time: int, event: str):
    await asyncio.sleep(time)
    await ctx.send(f'{event} has started')

bot.run(DISCORD_TOKEN)


