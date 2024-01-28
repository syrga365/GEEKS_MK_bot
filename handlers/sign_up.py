from aiogram import types, Dispatcher
from config import bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.sql_commands import Database
from keyboards.inline_buttons import direction_mk_keyboard
from const import SIGN_UP_TEXT


class SignUpStates(StatesGroup):
    last_name = State()
    first_name = State()
    age = State()
    direction = State()
    call_number = State()


async def sign_up_registration(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=SIGN_UP_TEXT.format(
            user=call.from_user.first_name
        )
    )
    await SignUpStates.last_name.set()


async def load_last_name(message: types.Message,
                            state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Напишите свое имя"
    )
    await SignUpStates.next()


async def load_first_name(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Cколько вам лет?",

    )
    await SignUpStates.next()


async def load_age(message: types.Message,
                    state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Выберите направление которое хотите записаться",
        reply_markup=await direction_mk_keyboard()

    )
    await SignUpStates.next()


async def load_direction(call: types.CallbackQuery,
                         state: FSMContext):
    async with state.proxy() as data:
        call.data.replace("direction_", "")
        data['direction'] = call.data.replace("direction_", "")
        print(data)
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Просим оставить свой номер:",

    )
    await SignUpStates.next()


async def load_call_number(message: types.Message,
                           state: FSMContext):
    db = Database()
    async with state.proxy() as data:
        data['call_number'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Вы успешно записались на наши курсы!!!\n"
              "Наш адрес: г.Бишкек, Ибраимова 103, БЦ Victory, правое крыло 4этаж!"
        )
    async with state.proxy() as data:
        db.sql_insert_signup_to_course(
            tg_id=message.from_user.id,
            last_name=data['last_name'],
            first_name=data['first_name'],
            age=data['age'],
            direction=data['direction'],
            call_number=data['call_number']
        )
    await state.finish()


def signup_to_course_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        sign_up_registration,
        lambda call: call.data == "sign_up"

    )
    dp.register_message_handler(
        load_last_name,
        state=SignUpStates.last_name,
        content_types=['text']
    )
    dp.register_message_handler(
        load_first_name,
        state=SignUpStates.first_name,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=SignUpStates.age,
        content_types=['text']
    )
    dp.register_callback_query_handler(
        load_direction,
        lambda call: call.data.startswith == 'direction_'

    )
    dp.register_message_handler(
        load_call_number,
        state=SignUpStates.call_number,
        content_types=['text']
    )

