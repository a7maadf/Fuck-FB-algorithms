import Constants as keys
from telegram.ext import MessageHandler, Updater, CommandHandler, Filters
import Responses as R

from webserver import keep_alive
import os


#pip install python-telegram-bot==13.15.0
print("Bot Started")

def start_command(update, context):
    update.message.reply_text('Type a message that you dont want it to be detected by Facebook or Instagram servers :D')
    update.message.reply_text('This bot was fully programmed and made by Ahmad Fawzy \nWebsite: https://ahmad-fawzy.com/')
    update.message.reply_text('type / for options')
def supp_langs(update, context):
  update.message.reply_text('English')
  update.message.reply_text('French')
  update.message.reply_text('German')
  update.message.reply_text('Swedish')
  update.message.reply_text('Spanish')
  update.message.reply_text('Italian')
  update.message.reply_text('Portuguese')
  update.message.reply_text('and moooore')
  update.message.reply_text('Supporting Arabic soon')




def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused an error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
keep_alive()
main()

