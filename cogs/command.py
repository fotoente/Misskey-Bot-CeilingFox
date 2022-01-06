from mi.ext import commands
from mi import Note

from ceilingfox import ceiling_fox_number, ceiling_fox_yes_no, ceiling_fox_story
from utils import get_mention


class MentionCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.mention_command(regex=r'!yesno')
    async def yesno(self, ctx: Note):
        await ctx.reply(f'{get_mention(ctx)}\n{ceiling_fox_yes_no()}')

    @commands.mention_command(regex=r'!story')
    async def story(self, ctx: Note):
        await ctx.reply(f'{get_mention(ctx)}\n{ceiling_fox_story()}')
    
    @commands.mention_command(regex=r'!number')
    async def number(self, ctx: Note):
        await ctx.reply(f'{get_mention(ctx)}\n{ceiling_fox_number()}')


def setup(bot: commands.Bot):
    bot.add_cog(MentionCommandCog(bot))
