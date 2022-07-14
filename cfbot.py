import asyncio
import random
from datetime import datetime

from mipa.ext import commands, tasks
from mipa.router import Router
from mipac.models import Note
from mipac.util import check_multi_arg
from mipac import File
from mipac.manager import MiFile

import ceilingfox

# Load Misskey configuration
config = ceilingfox.configparser.ConfigParser()
config.read(ceilingfox.os.path.join(ceilingfox.os.path.dirname(__file__), 'bot.cfg'))
url = "https://" + config.get("misskey", "instance")
token = config.get("misskey", "token")

INITIAL_COGS = ['cogs.command']

if not check_multi_arg(url, token):
    raise Exception("Misskey instance and token are required.")


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__()

        for cog in INITIAL_COGS:
            self.load_extension(cog)

    @tasks.loop(3600)
    async def loop1h(self):
        await bot.client.note.action.send(content=ceilingfox.ceiling_fox_post(), visibility="public")

    @tasks.loop(43200)
    async def loop12h(self):
        #  ceilingfox.load_emojis()
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Emojis loaded!")

    async def on_ready(self, ws):
        await Router(ws).connect_channel(["global", "main"])  # Connect to global and main channels
        await self.client.note.action.send(content=datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " $[rotate.deg=180 :blobfox:] Bot started!", visibility="specified")
        self.loop12h.start()  # Launching renew emojis every 12 hours
        self.loop1h.start()  # Launching posting every hour

    async def on_mention(self, note: Note):
        if not note.author.is_bot:
            if not note.content:  # Because it may be only an image
                return
            inhalt = note.content
            if not inhalt.find("!story") != -1 and not inhalt.find("!number") != -1 and not inhalt.find("!yesno") != -1:
                text = note.author.action.get_mention()
                text += ceilingfox.ceiling_fox_post()
                if not inhalt.find("!fox") != -1:
                    await note.reply(content=text)  # Reply to a note
                else:
                    folders = await self.client.drive.action.get_folders()
                    all_file: list[File] = []
                    for folder in folders:
                        all_file.extend(await folder.action.file.action.get_files(limit=100))

                    await note.reply(content=text, files=[MiFile(file_id=random.choice(all_file).id)])

        await self.progress_command(note)


if __name__ == "__main__":
    bot = MyBot()
    asyncio.run(bot.start(url, token))
