#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
negin awesome bot
you shoud put your token in token.txt
'''
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from finglish import f2p

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('سلام به بات فینگلیش به فارسی من خوش آمدید این بات قابلیت ان را دارد که متن فینگلیش شما را دریافت کرده و فارسی شده ی آن را به شما بر می گرداند برای ادامه help/ را بزنید')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('لطفا متن فینگلیش خود را وارد نمایید تا متن فارسی شده ی آن را دریافت کنید به همین راحتی:)')


def fin2per(bot, update):
    """convert user message from fingilish to persian."""
    recived = update.message.text
    update.message.reply_text(f2p(recived))


def read_token():
    with open('token.txt', 'r') as file:
        return file.readline().strip()


def main():
    updater = Updater(read_token())
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, fin2per))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()