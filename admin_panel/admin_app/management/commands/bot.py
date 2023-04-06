from django.core.management.base import BaseCommand
from admin_panel.settings import TOKEN
from telegram.ext import CallbackContext, Updater, Filters, MessageHandler
from telegram import Bot, Update
from telegram.utils.request import Request


def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    text = update.message.text

    reply_text = f'Yours id {chat_id}\n{text}'

    update.message.reply_text(
        text=reply_text
    )


class Command(BaseCommand):
    help = 'telegram bot'

    def handle(self, *args, **options):
        request = Request(
            con_pool_size=8,
            connect_timeout=0.5,
            read_timeout=1.0
        )

        bot = Bot(
            request=request,
            token=TOKEN,
        )

        updater = Updater(
            bot=bot,
            use_context=True
        )

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()

