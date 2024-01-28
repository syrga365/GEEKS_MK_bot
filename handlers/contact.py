from aiogram import types, Dispatcher
from config import bot
from const import CONTACT_TEXT


async def contact_button(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=CONTACT_TEXT
    )


def contact_register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(contact_button,
                               lambda call: call.data == "contact")
