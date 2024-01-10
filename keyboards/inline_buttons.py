from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboards():
    markup = InlineKeyboardMarkup()
    start_menu_button = InlineKeyboardButton(
        "РЕГИСТРАЦИЯ",
        callback_data="registration"
    )
    sign_up_button = InlineKeyboardButton(
        "ЗАПИСАТЬСЯ НА КУРСЫ",
        callback_data="sign_up"
    )
    review_button = InlineKeyboardButton(
        "ОТЗЫВ",
        callback_data="review"
    )
    markup.add(start_menu_button)
    markup.add(sign_up_button)
    markup.add(review_button)
    return markup


async def direction_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = InlineKeyboardButton(
        "Backend",
        callback_data="direction_backend"
    )
    frontend_button = InlineKeyboardButton(
        "Frontend",
        callback_data="direction_frontend"
    )
    ios_button = InlineKeyboardButton(
        "IOS",
        callback_data="direction_ios"
    )
    android_button = InlineKeyboardButton(
        "Android",
        callback_data="direction_android"
    )
    designer_button = InlineKeyboardButton(
        "UI/UX дизайнер",
        callback_data="direction_ui/ux"
    )
    programmer_button = InlineKeyboardButton(
        "Основы программирование",
        callback_data="direction_programmer"
    )
    manager_button = InlineKeyboardButton(
        "Менеджер проектов",
        callback_data="direction_manager"
    )
    qa_button = InlineKeyboardButton(
        "Тестирование ПО ",
        callback_data="direction_qa"
    )
    iop_button = InlineKeyboardButton(
        "Искусственный интелект",
        callback_data="direction_iop"
    )
    markup.add(backend_button)
    markup.add(frontend_button)
    markup.add(ios_button)
    markup.add(android_button)
    markup.add(designer_button)
    markup.add(programmer_button)
    markup.add(manager_button)
    markup.add(qa_button)
    markup.add(iop_button)
    return markup
