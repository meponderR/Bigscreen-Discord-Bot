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
        await ctx.channel.purge(limit=1)
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        cmdCommand = "playlat.bat"
        process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

@client.command(name='Stop', brief="Stops the video.")
async def stop(ctx):
    if ctx.channel.id == CidSetup:
        await ctx.channel.purge(limit=1)
        cmdCommand = "stopvlc.bat"
        process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

client.run(TOKEN)
