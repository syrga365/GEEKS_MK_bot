from aiogram import executor
from config import dp
from handlers import (
    start,
    registration,
    questionnaire,
    review,


)
from database import sql_commands

start.register_start_handlers(dp=dp)
registration.registration_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
review.review_handlers(dp=dp)


async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()


if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )