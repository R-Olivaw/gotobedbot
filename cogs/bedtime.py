import os
import platform
import random
import aiosqlite
import asyncio
import aiohttp
import discord
from datetime import datetime
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks

class Bedtime(commands.Cog, name="bedtime"):
    def __init__(self, bot):
        self.bot = bot

    async def connect_db(self):
        db = await aiosqlite.connect(r'C:\Users\Alexa\GitHub\gotobedbot\database\database.db')
        cursor = await db.cursor()
        await cursor.execute('CREATE TABLE IF NOT EXISTS reminders (user_id TEXT, time TEXT)')
        await db.commit()
        return db

    @commands.hybrid_command(
        name="bedtime",
        description="Go to bed, bitch!.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    async def set_reminder_task(self, time, context: Context):
        await context.send(f'Reminder set for {time}!')

        current_time = datetime.now().strftime('%I:%M%p')
        delta_time = (datetime.strptime(time, '%I:%M%p') - datetime.strptime(current_time, '%I:%M%p')).total_seconds()

        await asyncio.sleep(delta_time)

        db = await 

async def setup(bot):
    await bot.add_cog(Bedtime(bot))            