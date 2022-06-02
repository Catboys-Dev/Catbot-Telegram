from server import keep_alive
import logging
from telegram import *
from telegram.ext import *
import requests
import re
import json
import random
import sys
import os
import time
from humanfriendly import format_timespan
import asyncio

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Global
start_time = time.time()

# Bot stuff
BOT_TOKEN = ""
BOT_VERSION = "1.2.5"

def get_image():
  response = requests.get("https://api.catboys.com/img")
  json_data = json.loads(response.text)
  imageurl = json_data['url']
  return(imageurl)

def get_catboy_image():
  response = requests.get("https://api.catboys.com/img")
  json_data = json.loads(response.text)
  imageurl = json_data['url']
  return(imageurl)

def get_catboy():
  response = requests.get("https://api.catboys.com/catboy")
  json_data = json.loads(response.text)
  catboy = json_data['response']
  return(catboy)

def get_eightball():
  response = requests.get("https://api.catboys.com/8ball")
  json_data = json.loads(response.text)
  eightball = json_data['response']
  image = json_data['url']
  return(eightball, image)

def get_ping():
  response = requests.get("https://api.catboys.com/ping")
  json_data = json.loads(response.text)
  ping = json_data['catboy_says']
  if ping == "rawr":
    ping = "rawr (200 OK)"
  else:
    ping = "server is down"
  return(ping)

def get_inspquote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  inspquote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(inspquote)

def get_cat():
  response = requests.get("https://api.thecatapi.com/v1/images/search?limit=1")
  json_data = json.loads(response.text)
  cat = json_data[0]['url']
  return(cat)


def start(update, context):
    username = update.message.chat.username
    keyboard = [
        [
            InlineKeyboardButton("Add Catbot to my group", callback_data='1', url="https://t.me/catbot_robot?startgroup=hbase"),
            InlineKeyboardButton("Official group", callback_data='2', url="https://t.me/catboylounge"),
        ],
        [
            InlineKeyboardButton("Catboys.com", callback_data='3', url="https://catboys.com"),
            InlineKeyboardButton("Catbot.dev", callback_data='4', url="https://catbot.dev"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"\U0001F44B Hello {username}!\n\nCatbot is a simple and fun bot to fill all your neko needs and provide practical uses for your Telegram group. We have a few games and moderation commands with more things being developed and added all the time (check /changelog for our changelog)!\n\n<b>A few useful commands to begin:</b>\n/help - view commands and general information on the bot\n/info - view more useful information on the bot\n/support - see how you can get support for the bot\n/changelog - checkout what has changed\n\nPowered by <a href='https://catboys.com'>catboys.com</a>", parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=reply_markup)

def help(update, context):
    chat_id = update.message.chat_id
    keyboard = [
        [
            InlineKeyboardButton("Add Catbot to my group", callback_data='1', url="https://t.me/catbot_robot?startgroup=hbase"),
            InlineKeyboardButton("Official group", callback_data='2', url="https://t.me/catboylounge"),
        ],
        [
            InlineKeyboardButton("Catboys.com", callback_data='3', url="https://catboys.com"),
            InlineKeyboardButton("Catbot.dev", callback_data='4', url="https://catbot.dev"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text="\U0001F44B <b>Commands & Support</b>\n\n/help - Shows the available commands and more\n/info - Shows information about the bot\n/img - Gets a random catboy/yaoi image\n/catboy - Gets a random catboy image\n\n/yaoi - Gets a random yaoi image/cat - Gets a random cat photo\n/meme - Gets a random meme\n/quote - Gets a random inspirational quote\n/uwu - Have a virtual catboy\n/8ball - The classic magic 8 ball\n/flip - Heads or tails\n/ping - Ping the server\n/support - Get support for the bot\n/changelog - See what changed\n\n<b>Website: </b><a href='https://catboys.com'>catboys.com</a>\n<b>Bot Website: </b><a href='https://catbot.dev'>catbot.dev</a>\n<b>Support group: </b><a href='https://t.me/catboylounge'>CatboyLounge</a>\n<b>Support us: </b><a href='https://patreon.com/CatboyLounge'>Patreon</a>\n<b>Follow us: </b><a href='https://twitter.com/CatboyLounge'>Twitter</a>\n\nBrought to you by <a href='https://catboys.com'>catboys.com</a>", parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=reply_markup)

def img(update, context):
    url = get_image()
    catemoji = ['\U0001F63A', '\U0001F638', '\U0001F63B']
    chat_id = update.message.chat_id
    caption = "Brought to you by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text=random.choice(catemoji) + " Catboys")
    context.bot.send_photo(chat_id=chat_id, photo=url, caption=caption, parse_mode=ParseMode.HTML)

def catboy(update, context):
    url = get_catboy_image()
    catemoji = ['\U0001F63A', '\U0001F638', '\U0001F63B']
    chat_id = update.message.chat_id
    caption = "Brought to you by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text=random.choice(catemoji) + " Catboys")
    context.bot.send_photo(chat_id=chat_id, photo=url, caption=caption, parse_mode=ParseMode.HTML)

def cat(update, context):
    url = get_cat()
    catemoji = ['\U0001F63A', '\U0001F638', '\U0001F63B']
    chat_id = update.message.chat_id
    caption = "Image from <a href='https://thecatapi.com'>thecatapi.com</a>, bot by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text=random.choice(catemoji) + " Here, have a cat")
    context.bot.send_photo(chat_id=chat_id, photo=url, caption=caption, parse_mode=ParseMode.HTML)

def quote(update, context):
    quote = get_inspquote()
    chat_id = update.message.chat_id
    caption = "\n\nQuote by <a href='https://zenquotes.io'>zenquotes.io</a>, bot powered by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text="\U0001F4AC <b>An inspirational quote</b>\n\n" + quote + caption, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def uwu(update, context):
    response = get_catboy()
    catemoji = ['\U0001F63A', '\U0001F638', '\U0001F63B']
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=random.choice(catemoji) + " <b>Catboy says</b>\n\n" + response + "\n\nPowered by <a href='https://catboys.com'>catboys.com</a>", parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def eightball(update, context):
    eightball,image = get_eightball()
    chat_id = update.message.chat_id
    caption = "\U0001F340 The 8ball says...\n\n" + eightball + "\n\nPowered by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_photo(chat_id=chat_id, photo=image, caption=caption, parse_mode=ParseMode.HTML)

def flip(update, context):
    options = ['Heads', 'Tails']
    image = "https://catboys.com/assets/coin_flip.png"
    response = random.choice(options)
    chat_id = update.message.chat_id
    caption = "<b>" + response + "</b>\n\nPowered by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_photo(chat_id=chat_id, photo=image, caption=caption, parse_mode=ParseMode.HTML)

def ping(update, context):
    response = get_ping()
    chat_id = update.message.chat_id
    caption = "\n\nPowered by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text="\U0001F3D3 <b>Server response</b>\n\n" + response + caption, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def changelog(update, context):
    chat_id = update.message.chat_id
    caption = caption = "\n\nThe Telegram Catbot by <a href='https://catboys.com'>catboys.com</a>"
    context.bot.send_message(chat_id=chat_id, text="\U0001F5A5 <b>Catbot Changelog</b>\n\n<b>v1.2.5 (current)</b>\n- Added memes (/meme) and changelog (/changelog)\n\n<b>v1.2.4</b>\n- Updated command formatting\n\n<b>v1.2.3</b>\n- Added moderation commands (discord only)\n\n<b>v1.2.2</b>\n- Added the cbavatar command (discord only)\n\n<b>v1.2.1</b>\n- Updated help command formatting\n\n<b>v1.2</b>\n- Added many commands including /cat, /quote, and more\n\n<b>v1.1</b>\n- Reworked the code for performance\n\n<b>v1.0</b>\n- Initial release" + caption, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def support(update, context):
    chat_id = update.message.chat_id
    keyboard = [
        [
            InlineKeyboardButton("Join our Discord server", callback_data='2', url="https://catbot.dev/discord"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=chat_id, text="\U0001F91D <b>Catbot Support</b>\nBelow are a few ways to contact us\n\nDiscord: <a href='https://catbot.dev/discord'>Our Discord server</a>\n\nPowered by <a href='https://catboys.com'>catboys.com</a>", parse_mode=ParseMode.HTML, disable_web_page_preview=True, reply_markup=reply_markup)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("img", img))
    dp.add_handler(CommandHandler("catboy", catboy))
    dp.add_handler(CommandHandler("cat", cat))
    dp.add_handler(CommandHandler("quote", quote))
    dp.add_handler(CommandHandler("uwu", uwu))
    dp.add_handler(CommandHandler("8ball", eightball))
    dp.add_handler(CommandHandler("flip", flip))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("support", support))
    dp.add_handler(CommandHandler("changelog", changelog))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

async def update_task():
  while True:
    update_uptime()
    update_memoryusage()
    update_cpuusage()
    await asyncio.sleep(60)
    update_uptime()
    update_memoryusage()
    update_cpuusage()
    await asyncio.sleep(60)

if __name__ == '__main__':
    keep_alive()
    main()
