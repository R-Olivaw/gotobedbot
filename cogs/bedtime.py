import platform
import random
import aiosqlite
import asyncio
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class Bedtime(commands.Cog, name="bedtime"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="bedtime", description="Go to bed, bitch."
    )
    @checks.not_blacklisted()
    async def set_reminder(self, context: Context):
        await context.send("What time do you want to go to bed?")

        def check(msg):
            return msg.author == context.author and msg.channel == context.channel

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=80)
            time = msg.content

            db = self.bot.init_db()
            cursor = await db.cursor()
            await cursor.execute('INSERT INTO reminders (user_id, time) VALUES (?, ?)', (context.author.id, time))
            await db.commit()

            await context.send(f'Reminder set for {time}!')

        except:
            await context.send('Something went wrong!')

async def setup(bot):
    await bot.add_cog(Bedtime(bot))            