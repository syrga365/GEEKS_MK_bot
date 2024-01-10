from aiogram import types, Dispatcher
from config import bot
from const import REVIEW_TEXT
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.sql_commands import Database


class ReviewStates(StatesGroup):
    review = State()


async def review_from_users(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Просим оставить отзыв на нас!"
    )
    await ReviewStates.review.set()


async def load_review(message: types.Message,
                           state: FSMContext):
    db = Database()
    async with state.proxy() as data:
        data['review'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text=REVIEW_TEXT.format(
            user=message.from_user.first_name
        )
    )
    async with state.proxy() as data:
        db.sql_insert_review_from_users(
            tg_id=message.from_user.id,
            review=data['review']
        )
    await state.finish()


def review_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        review_from_users,
        lambda call: call.data == "review"
    )
    dp.register_message_handler(
        load_review,
        state=ReviewStates.review,
        content_types=['text']
    )