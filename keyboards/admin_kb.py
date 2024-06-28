from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# создание клавиатуры
def get_keyboard(
    *btns: str,
    placeholder: str = None,
    request_contact: int = None,
    request_location: int = None,
    sizes: tuple[int] = (2,),
):
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):

        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:

            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
            resize_keyboard=True, input_field_placeholder=placeholder)


# главная админ клавиатура:
BASE_ADMIN_KB = get_keyboard(
    "Списки:",
    placeholder="Выберите действие",
    )

# # клавиатура для управления резервом: (Сделать Inline!)
# ADMIN_RESERVE_KB = get_keyboard(
#     "Новый резерв",
#     "Изменить бронь",
#     "Удалить бронь",
#     placeholder="Выберите действие",
#     sizes=(1, 1, 1),
# )

# KEYBOARD_NUMBER = [
#     [KeyboardButton(text='Поделиться номером.', request_contact=True)],
#     [KeyboardButton(text='Определить локацию.', request_location=True)],
# ]

# KEYBOARD_NUMBER_ = get_keyboard(
#     "Поделиться номером.",
#     request_contact=True)


# KEYBOARD_NUMBER = [
#     [KeyboardButton(text='Поделиться номером.', request_contact=True)],
#     [KeyboardButton(text='Определить локацию.', request_location=True)],
# ]

# del_keyboards_admin = ReplyKeyboardRemove()


# # клавиатура для карточек резервов
# RESERVE_CARD_KEYBOARD = [
#             InlineKeyboardButton(
#                 'Удалить бронь', callback_data='delete_reservation'
#             ),
#             InlineKeyboardButton(
#                 'Изменить бронь', callback_data='edit_reservation'
#             ),]
