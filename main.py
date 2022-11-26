import os
import types

import cv2
import dp as dp
from telegram import bot
import requests
import Responses as R
import Constraints as keys
from telegram.ext import *
import telepot

print('Bot Started....')


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def start_command(update, context):
    update.message.reply_text('QR code to link')
    update.message.reply_text('Link to QR code')


def help_command(update, context):
    update.message.reply_text('if you need help try asking google !')


# def handle_message(update, context):




    # text = str(update.message.text).lower()
    # print(text)
    # qr_img = qrcode.make(text)
    # # qr_img.save("qr-img.jpg")
    # chat_id = update.message.chat_id
    # bot.send_photo(chat_id, photo=open('qr-img.jpg', 'rb'))


def error(update, context):
    update.message.reply_text("sorry i don't know its meaning, try a different word")
    print(f"Update{update} caused error {context.error}")


def image_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    new_file = context.bot.get_file(obj.file_id)
    new_file.download('qrcode.png')

    image = cv2.imread('qrcode.png')
    detector = cv2.QRCodeDetector()
    val, b, c = detector.detectAndDecode(image)
    os.remove("qrcode.png")
    update.message.reply_text(val)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    # dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
