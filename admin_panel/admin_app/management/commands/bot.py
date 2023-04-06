from django.core.management.base import BaseCommand
from admin_panel.settings import TOKEN
from telegram.ext import CallbackContext, Updater, Filters, MessageHandler, CommandHandler
from telegram import Bot, Update
from telegram.utils.request import Request
from admin_app.models import Theme
from django.db.models.aggregates import Count
from random import randint
from django.db.models.aggregates import Aggregate


def send_text(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    count = Theme.objects.all().count()
    count2 = Theme.objects.all()
    random_index = randint(0, count - 1)
    text = count2[random_index]
    print(text)
    update.message.reply_text(
        text=count2[random_index]
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

        message_handler2 = CommandHandler('send', send_text)
        updater.dispatcher.add_handler(message_handler2)

        updater.start_polling()

