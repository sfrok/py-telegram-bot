from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import data


def linked_button(function):
    def wrapper(bot, update):
        message_text = 'Press any button:'
        markup = [
            [InlineKeyboardButton(text='Go to google.com', url='https://www.google.com/')],
            [InlineKeyboardButton(text='Go to our telegram channel', url='https://t.me/ithumor')],
            [InlineKeyboardButton(text='Go to our telegram king', url='https://t.me/thecete')],
            [InlineKeyboardButton(text='Back', callback_data=data.cbMain)]
        ]
        reply = InlineKeyboardMarkup(markup)
        result = function(bot, update, reply, message_text)
        return result
    return wrapper


@linked_button
def url_reply(bot, update, reply, message_text):
    bot.editMessageText(text=message_text,
                        chat_id=update.callback_query.message.chat_id,
                        reply_markup=reply,
                        message_id=update.callback_query.message.message_id)