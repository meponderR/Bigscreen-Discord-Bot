import discord
from discord.ext import commands
import youtube_dl as ytdl
import subprocess

TOKEN = "TokenSetup"

client = commands.Bot(command_prefix ='PrefixSetup')

ydl_opts = {
    'default_search': 'auto',
    'format': 'bestvideo[filesize<=SizeSetupM][height <=? QualitySetup]+bestaudio',
    'cachedir': False,
    'outtmpl': '0'
}

@client.event
async def on_ready():
	print("Bot Connected")

@client.command(name='play', brief="Plays the requested video.")
async def play(ctx, *, url):
    if ctx.channel.id == CidSetup:
        print("Play command issued from channel #" + ctx.channel.id)
        await ctx.channel.purge(limit=1)
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        subprocess.call(['playlat.bat'])

@client.command(name='stop', brief="Stops the video.")
async def stop(ctx):
    if ctx.channel.id == CidSetup:
        print("Stop command issued from channel #" + ctx.channel.id)
        await ctx.channel.purge(limit=1)
        subprocess.call(['stopvlc.bat'])

client.run(TOKEN)
