from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import direction_course_info_keyboard


async def course_button(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Выберите направление который вас интересует",
        reply_markup=await direction_course_info_keyboard()
    )


def register_course_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        course_button,
        lambda call: call.data == "course"
    )