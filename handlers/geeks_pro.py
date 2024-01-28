from aiogram import types, Dispatcher
from config import bot


async def geeks_pro_button(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="КТО МОЖЕТ СТАЖИРОВАТЬСЯ В GEEKS PRO?\n"
              "Geeks Pro предоставляет возможность стажировки как для выпускников Geeks, так и других образовательных центров, курсов и ВУЗов.\n\n"
              "КАК ПОПАСТЬ К НАМ?\n"
              "Для поступления на стажировочную программу вам нужно пройти отборочное тестирование. Пожалуйста, свяжитесь с нами\n\n"
              "ЧТО ТАКОЕ ЦЕНТР КАРЬЕРЫ GEEKS PRO?\n"
              "Центр карьеры Geeks Pro предоставляет выпускникам Geeks и других учебных заведений возможность пройти стажировочную программу"
             " по повышению квалификации. В программе командная работа над коммерческими проектами, мастер-классы по soft и hard навыкам, помощь в трудоустройстве и многое другое."
    )


def register_geeks_pro_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
       geeks_pro_button,
        lambda call: call.data == "geeks_pro"
    )