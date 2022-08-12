from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} 

I am Telegram Most Powerful Subtitle Muxer Bot

I can Mux Any srt or ass File in File or Video

Use Help Command to Know How to Use me

"""
    HELP_TEXT = """
Recommended
➠ Use Hardmux If You Have More Time

Recommended
➠ Use Softmux To add Subtitle Fastly in It

Softmux
➠ Send /softmux to add Subtitle Softly in it

HardMux
➠ Send /hardmux to add Subtitle hardly in it 

"""
    ABOUT_TEXT = """
 **👲 Developer :** [Steve](https://t.me/EnthadaNokunne)\n
 **❄️ Credits :** Everyone in this journey\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Owner', url='https://t.me/EnthadaNokunne'),
        InlineKeyboardButton('💬 Admin', url='https://t.me/chemistry2021e')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
