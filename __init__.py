import os

import interactions

from config import DEV_GUILD

from src import logutil

logger = logutil.init_logger(os.path.basename(__file__))

class RockPaperScissors(interactions.Extension):
    @interactions.slash_command(
        "challenge", description="test command", scopes=[DEV_GUILD] if DEV_GUILD else None
    )
    async def test_cmd(self, ctx: interactions.SlashContext):
        """Register as an extension command"""
        await ctx.send("Challenge")