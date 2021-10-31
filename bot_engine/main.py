#!/usr/bin/env python3

import telebot
from optparse import OptionParser

path = {
    'api': 'bot_engine/access/api.txt',
    'chat_id': 'bot_engine/access/chat_id.txt',
    'info_folder': 'bot_engine/info/'
}


def message():
    if options.website == '':
        msg = f'<b>Внимание, новая заявка!</b>\n\n' \
              f'<b>Имя:</b> <i>{options.name}</i>\n' \
              f'<b>Номер телефона:</b> <i>{options.phone}</i>\n' \
              f'<b>E-Mail:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт:</b> <i>У пользователя отсутствует сайт</i>'
    else:
        msg = f'<b>Внимание, новая заявка!</b>\n\n' \
              f'<b>Имя:</b> <i>{options.name}</i>\n' \
              f'<b>Номер телефона:</b> <i>{options.phone}</i>\n' \
              f'<b>E-Mail:</b> <i>{options.email}</i>\n' \
              f'<b>Cайт пользователя:</b> <i>{options.website}</i>'
    return msg


parser = OptionParser()
parser.add_option('-n', '--name', dest='name',
                  help='Name of user', metavar='NAME')
parser.add_option('-p', '--phone', dest='phone',
                  help='Phone Number', metavar='PHONE')
parser.add_option('-e', '--email', dest='email',
                  help='User E-Mail', metavar='EMAIL')
parser.add_option('-w', '--website', dest='website',
                  help='Web-Site', metavar='WEBSITE')

(options, args) = parser.parse_args()

with open(path['api'], 'r') as apifile:
    bot = telebot.TeleBot(apifile.read())

with open(path['chat_id'], 'r') as chat_id:
    bot.send_message(chat_id=chat_id.read(), text=message(), parse_mode='html')
