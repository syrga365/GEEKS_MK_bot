from aiogram import types, Dispatcher
from config import bot
from const import REGISTRATION_TEXT
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.sql_commands import Database
from keyboards.inline_buttons import direction_keyboard


class RegistrationStates(StatesGroup):
    first_name = State()
    age = State()
    direction = State()
    call_number = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Как вас зовут?🙃"
    )
    await RegistrationStates.first_name.set()


async def load_first_name(message: types.Message,
                          state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько вам лет?(Напишите в виде чисел😎)"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Какое направление вас интересует?🤩",
        reply_markup=await direction_keyboard()

    )
    await RegistrationStates.next()


async def load_direction(call: types.CallbackQuery,
                         state: FSMContext):
    async with state.proxy() as data:
        call.data.replace("direction_", "")
        print(data)

    await bot.send_message(
        chat_id=call.from_user.id,
        text="Оставьте свой номер чтобы мы с вами связались😇",

    )
    await RegistrationStates.next()


async def load_call_number(message: types.Message,
                           state: FSMContext):
    db = Database()
    async with state.proxy() as data:
        data['call_number'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text=REGISTRATION_TEXT.format(
            user=message.from_user.first_name
        )
    )
    async with state.proxy() as data:
        db.sql_insert_registration_users(
            tg_id=message.from_user.id,
            first_name=data['first_name'],
            age=data['age'],
            direction=data['direction'],
            call_number=data['call_number']
        )
    await state.finish()


def registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_first_name,
        state=RegistrationStates.first_name,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_direction,
        state=RegistrationStates.direction,
    )
    dp.register_message_handler(
        load_call_number,
        state=RegistrationStates.call_number,
        content_types=['text']
    )
