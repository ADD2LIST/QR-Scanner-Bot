# -*- coding: utf-8 -*-

from telegram.ext import Updater, MessageHandler, Filters

from pyzbar.pyzbar import decode

from PIL import Image

TOKEN = "6003057608:AAGHWgY8TQkQzjdQnJP3MWbEfn8uMWU8WpM"

def decode_qr(update, context):

    chat_id = update.message.chat_id

    if update.message.photo:

        photo = update.message.photo[-1]

        file_id = photo.file_id

        new_file = context.bot.get_file(file_id)

        image = Image.open(new_file.download_as_bytearray())

        try:

            qr_codes = decode(image)

            if qr_codes:

                result = qr_codes[0].data.decode("utf-8")

                context.bot.send_message(chat_id=chat_id, text=result)

            else:

                context.bot.send_message(chat_id=chat_id, text="No QR code found in the image.")

        except Exception as e:

            context.bot.send_message(chat_id=chat_id, text=str(e))

    else:

        context.bot.send_message(chat_id=chat_id, text="Please send a photo with a QR code.")

def main():

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.photo, decode_qr))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()

