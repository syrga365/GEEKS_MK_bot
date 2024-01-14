from aiogram import types, Dispatcher
from config import bot


async def backend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в понедельник в 15:00.Мы ждем вас!"
    )


async def frontend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет во вторник в 15:00.Мы ждем вас!"
    )


async def ios_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в среду в 15:00.Мы ждем вас!"
    )


async def android_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в понедельник в 15:00.Мы ждем вас!"
    )


async def designer_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в пятницу в 15:00.Мы ждем вас!"
    )


async def programmer_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
              f"Пробный урок пройдет в субботу в 15:00.Мы ждем вас!"
     )


async def manager_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в пятницу в 15:00.Мы ждем вас!"
    )


async def qa_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в пятницу в 15:00.Мы ждем вас!"
    )


async def iop_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f" {call.data.replace('direction_', '')}, отличный выбор!!! \n"
             f"Пробный урок пройдет в пятницу в 15:00.Мы ждем вас!"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(backend_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(frontend_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(ios_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(android_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(designer_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(programmer_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(manager_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(qa_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(iop_call,
                                       lambda call: call.data.startswith("direction_"))
