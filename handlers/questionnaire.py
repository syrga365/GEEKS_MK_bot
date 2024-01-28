from aiogram import types, Dispatcher
from config import bot


async def backend_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'Backend' пройдет в четрверг в 15:00. Мы ждем вас!\n\n"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def frontend_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'Frontend' пройдет в четверг в 15:00.Мы ждем вас!\n\n"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def ios_and_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'Мобильной разработки IOS/ANDROID' пройдет в субботу в 16:00. Мы ждем вас!\n\n"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def designer_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'UX/UI дизайна' пройдет в пятницу в 15:00.Мы ждем вас!\n\n"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def qa_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'Тестирование по' пройдет в среду в 18:00.Мы ждем вас!\n\n"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def iop_mk_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Пробный урок по направлению 'Искусственный интеллект' пройдет в четверг в 19:00.Мы ждем вас!"
             "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
    )


async def backend_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Backend - отличный выбор"
    )


async def frontend_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Frontend - отличный выбор"
    )


async def ios_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="IOS разработка- отличный выбор"
    )


async def android_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Android разработка - отличный выбор"
    )


async def designer_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="UX/UI дизайнер - отличный выбор"
    )


async def programmer_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Основы программирования - отличный выбор"
    )


async def manager_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Менеджер проектов - отличный выбор"
    )


async def qa_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Тестирование ПО - отличный выбор"
    )


async def iop_course_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Искусственный интеллект - отличный выбор"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(backend_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(frontend_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(ios_and_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(designer_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(qa_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(iop_mk_call,
                                       lambda call: call.data.startswith("direction_"))
    dp.register_callback_query_handler(backend_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(frontend_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(ios_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(designer_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(android_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(qa_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(iop_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(programmer_course_call,
                                       lambda call: call.data.startswith("course_"))
    dp.register_callback_query_handler(manager_course_call,
                                       lambda call: call.data.startswith("course_"))
