from datetime import datetime
import os
import asyncio
from random import *
import mi
import configparser
from mi import Note
from mi.ext import commands, tasks
from mi.note import Note
from mi.router import Router
from ceilingfox import *

#Load Misskey configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'bot.cfg'))
uri="wss://"+config.get("misskey","instance")+"/streaming"
token=config.get("misskey","token")


class MyBot(commands.Bot):
    def __init__(self, cmd_prefix: str):
        super().__init__(cmd_prefix)
    
    
    @tasks.loop(3600)
    async def loop1h(self):
        await bot.post_note(content=CeilingfoxPost())
    
    @tasks.loop(43200)
    async def loop12h(self):
        LoadEmojis()
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" Emojis loaded!")

    async def on_ready(self, ws):
        await Router(ws).connect_channel(["global", "main"])  #Connect to global and main channels
        await self.post_note(content=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" $[rotate.deg=180 :blobfox:] Bot started!", visibility="specified")
        self.loop12h.start()  #Launching renew emojis every 12 hours
        self.loop1h.start()  #Launching posting every hour
        
        
    async def on_mention(self, note: Note):
        text=""
        if (not note.author.bot):
            inhalt=note.content
            if (note.author.host is None):
                text="@"+note.author.username+" " #Building the reply on same instance
            else:
                text="@"+note.author.username+"@"+note.author.host+" " #Building the reply on foreign instance
                
            if (inhalt.find("!yesno")!= -1):
                text+="\n"+CeilingfoxYesNo()
            elif (inhalt.find("!story")!= -1):
                text+=CeilingfoxStory()
            elif (inhalt.find("!number")!= -1):
                text+=CeilingfoxNumber()
            else:
                text+=CeilingfoxPost()            
            
            await note.reply(content=text) #Reply to a note


if __name__ == "__main__":
    bot = MyBot("")
    asyncio.run(bot.start(uri, token))
   