# from aiogram import types, Dispatcher
# from config import bot
#
#
# async def backend_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в понедельник в 15:00!"
#     )
#
#
# async def frontend_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас во вторник в 15:00!"
#     )
#
#
# async def ios_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в среду в 15:00!"
#     )
#
#
# async def android_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в четверг в 15:00!"
#     )
#
#
# async def designer_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в пятницу в 15:00!"
#     )
#
#
# async def programmer_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в субботу в 15:00!"
#     )
#
#
# async def manager_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в понедельник в 15:00!"
#     )
#
#
# async def qa_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас во вторник в 15:00!"
#     )
#
#
# async def iop_call(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text="Отлично! Мы ждем вас в среду  в 15:00!"
#     )
#
#
# def register_questionnaire_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(backend_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(frontend_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(ios_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(android_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(designer_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(programmer_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(manager_call,
#                                        lambda call: call.startwith == "direction_")
#     dp.register_callback_query_handler(qa_call,
#                                        lambda call: call.starwith == "direction_")
#     dp.register_callback_query_handler(ios_call,
#                                        lambda call: call.startswith == "direction_")