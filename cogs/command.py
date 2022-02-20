from mi.ext import Context, commands
from mi.framework import Note

from ceilingfox import ceiling_fox_number, ceiling_fox_yes_no, ceiling_fox_story


class MentionCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.mention_command(text='!yesno')
    async def yesno(self, ctx: Context):
        await ctx.message.reply(f'{ctx.author.action.get_mention()}\n{ceiling_fox_yes_no()}')

    @commands.mention_command(text='!story')
    async def story(self, ctx: Context):
        await ctx.message.reply(f'{ctx.author.action.get_mention()}\n{ceiling_fox_story()}')

    @commands.mention_command(text='!number')
    async def number(self, ctx: Context):
        await ctx.message.reply(f'{ctx.author.action.get_mention()}\n{ceiling_fox_number()}')


def setup(bot: commands.Bot):
    bot.add_cog(MentionCommandCog(bot))
