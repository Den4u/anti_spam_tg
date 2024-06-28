from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# import handlers.constants as constants


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


# # основная клавиатура для гостей:
# BASE_GUEST_KB = get_keyboard(
#     constants.RESERVE_BUTTON_GUEST,
#     constants.MENU_BUTTON,
#     constants.DELIVERY_BUTTON,
#     constants.CONTACT_BUTTON,
#     constants.ROUTE_BUTTON,
#     constants.REVIEW_BUTTON,
#     placeholder="Выберите действие",
#     sizes=(2, 2, 2),
# )

# del_keyboards_admin = ReplyKeyboardRemove()

# Позволяет добавлять кнопки к существующей клавиатуре.
# _GUEST_KEYBOARD = ReplyKeyboardBuilder()
# _GUEST_KEYBOARD.attach(START_GUEST_KEYBOARD)
# _GUEST_KEYBOARD.row(KeyboardButton(text='Доп кнопка!'),)
