import asyncio
from datetime import datetime

from mi.ext import commands, tasks
from mi.note import Note
from mi.router import Router

from ceilingfox import *

#Load Misskey configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'bot.cfg'))
uri="wss://"+config.get("misskey","instance")+"/streaming"
token=config.get("misskey","token")



INITIAL_COGS = ['cogs.command']
class MyBot(commands.Bot):
    def __init__(self, cmd_prefix: str):
        super().__init__(cmd_prefix)
        
        for cog in INITIAL_COGS:
            self.load_extension(cog)
    
    
    @tasks.loop(3600)
    async def loop1h(self):
        await bot.post_note(content=ceiling_fox_post(), visibility="public")
    
    @tasks.loop(43200)
    async def loop12h(self):
        load_emojis()
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" Emojis loaded!")

    async def on_ready(self, ws):
        await Router(ws).connect_channel(["global", "main"])  #Connect to global and main channels
        await self.post_note(content=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" $[rotate.deg=180 :blobfox:] Bot started!", visibility="specified")
        self.loop12h.start()  #Launching renew emojis every 12 hours
        self.loop1h.start()  #Launching posting every hour
        
        
    async def on_mention(self, note: Note):
        text=""
        if (not note.author.bot):
            if not note.content:  # Because it may be only an image
                return
            inhalt=note.content
            #if not inhalt.find("!story")!= -1 and not inhalt.find("!number")!= -1 and not inhalt.find("!yesno")!= -1:
            if (note.author.host is None):
                text="@"+note.author.username+" " #Building the reply on same instance
            else:
                text="@"+note.author.username+"@"+note.author.host+" " #Building the reply on foreign instance
            text+= ceiling_fox_post()                
            await note.reply(content=text) #Reply to a note
        #await self.progress_command(note)


if __name__ == "__main__":
    bot = MyBot("")
    asyncio.run(bot.start(uri, token))
