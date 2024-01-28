from aiogram import executor
from config import dp
from handlers import (
    start,
    registrationformk,
    questionnaire,
    review,
    sign_up,
    contact,
    course,
    course_info_questionnaire,
    geeks_pro,


)
from database import sql_commands

start.register_start_handlers(dp=dp)
registrationformk.registration_handlers(dp=dp)
review.review_handlers(dp=dp)
sign_up.signup_to_course_handlers(dp=dp)
contact.contact_register_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
course.register_course_handlers(dp=dp)
course_info_questionnaire.register_course_questionnaire_handlers(dp=dp)
geeks_pro.register_geeks_pro_handlers(dp=dp)


async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()


if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )