# from aiogram.types import InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder

# from handlers import constants


# # создание callback кнопок
# def get_callback_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBuilder()

#     for text, data in btns.items():

#         keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

#     return keyboard.adjust(*sizes).as_markup()


# # создание URL кнопок
# def get_url_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBuilder()

#     for text, url in btns.items():

#         keyboard.add(InlineKeyboardButton(text=text, url=url))

#     return keyboard.adjust(*sizes).as_markup()


# # Создать микс из CallBack и URL кнопок
# def get_inlineMix_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBuilder()

#     for text, value in btns.items():
#         if '://' in value:
#             keyboard.add(InlineKeyboardButton(text=text, url=value))
#         else:
#             keyboard.add(InlineKeyboardButton(text=text, callback_data=value))

#     return keyboard.adjust(*sizes).as_markup()


# # клавиатура яндекс-доставки
# DELIVERY_KEYBOARD_ = {
#     'Яндекс доставка': constants.DELIVERY_YANDEX_URL
# }


# # # Клавиатура для отзывов на площадках:
# REVIEW_KEYBOARD_ = {
#     'Яндекс Карты': constants.REVIEW_YA,
#     '2ГИС': constants.REVIEW_2GIS,
#     'Tripadvisor': constants.REVIEW_TRIPADVISOR
# }


# # Клавиатура для контактов VK/INST:
# CONTACT_KEYBOARD_ = {
#     'VK': constants.VK_URL,
#     'Instagram': constants.INST_URL
# }
