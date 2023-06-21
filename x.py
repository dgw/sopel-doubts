"""
Authors: xnaas <me@xnaas.info> (2022)
License: The Unlicense (public domain)
Require: python>=3.8
"""
from sopel import plugin


@plugin.rule(r'^[XⓍ]$')
def x_to_doubt(bot, trigger):
	bot.action('doubts')
