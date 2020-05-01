@echo off
pip install discord.py youtube-dl
wget https://phoenixnap.dl.sourceforge.net/project/fart-it/fart-it/1.99b/fart.exe
cls

set /p Token=Enter your Discord bot token:
set /p Prefix=Enter the prefix you want to for the bot(e.g., !, ?, $):
set /p Quality=Enter the max resolution for videos in pixels(e.g., 1080, 720, 2160):
set /p Size=Enter the max size for videos in megabytes(e.g., 500, 250, 1000):
set /p Cid=Enter the channel id of your bot chanel:

fart "%CD%\Code\main.py" TokenSetup %Token%
fart "%CD%\Code\main.py" PrefixSetup %Prefix%
fart "%CD%\Code\main.py" QualitySetup %Quality%
fart "%CD%\Code\main.py" SizeSetup %Size%
fart "%CD%\Code\main.py" CidSetup %Cid%
del fart.exe
