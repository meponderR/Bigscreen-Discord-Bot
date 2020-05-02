@echo off
taskkill /im vlc.exe
for /f "eol=: delims=" %%F in ('dir /b /od *.mkv') do @set "newest=%%F"
vlc 0.mkv
del *.mkv