"""Press X to doubt.

Original version released under The Unlicense by xnaas at
https://git.actionsack.com/xnaas/sopel-doubts
"""
from sopel import plugin


# yes, both cases of the double struck X need to be included; they are caseless,
# so a case-insensitive regex can't match both with just one.
X_CLASS = '[XⓍ𝕏𝕩]'


@plugin.rule(rf"^{X_CLASS}$")
def x(bot, trigger):
	bot.action("doubts")


@plugin.rule(rf"^presse[ds] {X_CLASS}$")
@plugin.ctcp('ACTION')
def press_x(bot, trigger):
	bot.action("doubts")
