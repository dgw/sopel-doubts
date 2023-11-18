"""
Authors: xnaas <me@xnaas.info> (2022-2023)
License: The Unlicense (public domain)
"""
from sopel import plugin


@plugin.rule(r"^[XⓍ𝕏]$")
def x_to_doubt(bot, trigger):
	bot.action("doubts")
