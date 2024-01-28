from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


async def start_menu_keyboards():
    markup = InlineKeyboardMarkup()
    start_menu_button = InlineKeyboardButton(
        "РЕГИСТРИРОВАТЬСЯ НА ПРОБНЫЙ УРОК",
        callback_data="registration"
    )
    sign_up_button = InlineKeyboardButton(
        "ЗАПИСАТЬСЯ НА КУРСЫ",
        callback_data="sign_up"
    )
    course_button = InlineKeyboardButton(
        "УЗНАТЬ О НАШИХ КУРСАХ",
        callback_data="course"
    )
    geeks_pro_button = InlineKeyboardButton(
        "УЗНАТЬ О СТАЖИРОВКЕ В GEEKS PRO",
        callback_data="geeks_pro"
    )
    review_button = InlineKeyboardButton(
        "ОСТАВИТЬ ОТЗЫВ",
        callback_data="review"
    )
    contact_button = InlineKeyboardButton(
        "СВЯЗАТЬСЯ С НАМИ",
        callback_data="contact"
    )
    markup.add(start_menu_button)
    markup.add(sign_up_button)
    markup.add(course_button)
    markup.add(geeks_pro_button)
    markup.add(review_button, contact_button)
    return markup


async def direction_mk_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = KeyboardButton(
        "Backend",
        callback_data="direction_backend"
    )
    frontend_button = KeyboardButton(
        "Frontend",
        callback_data="direction_frontend"
    )
    ios_and_button = KeyboardButton(
        "IOS/ANDROID разработка",
        callback_data="direction_ios"
    )
    designer_button = KeyboardButton(
        "UI/UX дизайнер",
        callback_data="direction_ui/ux"
    )
    qa_button = KeyboardButton(
        "Тестирование ПО ",
        callback_data="direction_qa"
    )
    iop_button = KeyboardButton(
        "Искусственный интелект",
        callback_data="direction_iop"
    )
    kids_button = KeyboardButton(
        "Детское программирование",
        callback_data="direction_сhild_programming"
    )
    markup.add(backend_button)
    markup.add(frontend_button)
    markup.add(ios_and_button)
    markup.add(designer_button)
    markup.add(qa_button)
    markup.add(iop_button)
    markup.add(kids_button)
    return markup


async def direction_course_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = InlineKeyboardButton(
        "Backend",
        callback_data="course_backend"
    )
    frontend_button = InlineKeyboardButton(
        "Frontend",
        callback_data="course_frontend"
    )
    ios_button = InlineKeyboardButton(
        "IOS разработка",
        callback_data="course_ios"
    )
    android_button = InlineKeyboardButton(
        "ANDROID разработка",
        callback_data="course_android"
    )
    designer_button = InlineKeyboardButton(
        "UI/UX дизайнер",
        callback_data="course_ui/ux"
    )
    qa_button = InlineKeyboardButton(
        "Тестирование ПО ",
        callback_data="course_qa"
    )
    iop_button = InlineKeyboardButton(
        "Искусственный интелект",
        callback_data="course_iop"
    )
    programming_button = InlineKeyboardButton(
        "Основы программирования",
        callback_data="course_programming"

    )
    kids_button = InlineKeyboardButton(
        "Детское программирования",
        callback_data="course_kids"
    )
    manager_button = InlineKeyboardButton(
        "Проектный менеджер",
        callback_data="course_manager"
    )
    markup.add(backend_button)
    markup.add(frontend_button)
    markup.add(ios_button)
    markup.add(android_button)
    markup.add(designer_button)
    markup.add(qa_button)
    markup.add(iop_button)
    markup.add(programming_button)
    markup.add(manager_button)
    markup.add(kids_button)
    return markup


async def direction_course_info_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = InlineKeyboardButton(
        "Backend",
        callback_data="backend"
    )
    frontend_button = InlineKeyboardButton(
        "Frontend",
        callback_data="frontend"
    )
    ios_button = InlineKeyboardButton(
        "IOS разработка",
        callback_data="ios"
    )
    android_button = InlineKeyboardButton(
        "ANDROID разработка",
        callback_data="android"
    )
    designer_button = InlineKeyboardButton(
        "UI/UX дизайнер",
        callback_data="ui/ux"
    )
    qa_button = InlineKeyboardButton(
        "Тестирование ПО ",
        callback_data="qa"
    )
    iop_button = InlineKeyboardButton(
        "Искусственный интелект",
        callback_data="iop"
    )
    programming_button = InlineKeyboardButton(
        "Основы программирования",
        callback_data="programming"

    )
    kids_button = InlineKeyboardButton(
        "Детское программирования",
        callback_data="kids"
    )
    manager_button = InlineKeyboardButton(
        "Проектный менеджер",
        callback_data="manager"
    )
    markup.add(backend_button)
    markup.add(frontend_button)
    markup.add(ios_button)
    markup.add(android_button)
    markup.add(designer_button)
    markup.add(qa_button)
    markup.add(iop_button)
    markup.add(programming_button)
    markup.add(manager_button)
    markup.add(kids_button)
    return markup
