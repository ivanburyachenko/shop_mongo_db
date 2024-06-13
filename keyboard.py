import telebot

back_button = telebot.types.KeyboardButton("🔙 Повернутися назад")

#-----------------------------------------------------------------------------------
menu_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

menu_button1 = telebot.types.KeyboardButton("🛒 Кошик")
menu_button2 = telebot.types.KeyboardButton("🪪 Мій профіль")
menu_button3 = telebot.types.KeyboardButton("🔍 Про магазин")
menu_button4 = telebot.types.KeyboardButton("📙 Каталог товарів")

menu_keyboard.add(menu_button1,menu_button2,menu_button3,menu_button4)
#-----------------------------------------------------------------------------------
profile_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

profile_button1 = telebot.types.KeyboardButton("✏️ Змінити інформацію профілю")

profile_keyboard.add(profile_button1, back_button)
#-----------------------------------------------------------------------------------
change_profile_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

change_profile_button1 = telebot.types.KeyboardButton("✏️ Змінити ім'я")
change_profile_button2 = telebot.types.KeyboardButton("✏️ Змінити прізвище")
change_profile_button3 = telebot.types.KeyboardButton("✏️ Змінити поштову скриньку")
change_profile_button4 = telebot.types.KeyboardButton("✏️ Змінити номер телефону")
change_profile_button5 = telebot.types.KeyboardButton("✏️ Змінити адресу")

change_profile_keyboard.add(change_profile_button1, change_profile_button2, change_profile_button3, change_profile_button4, change_profile_button5, back_button)
#-----------------------------------------------------------------------------------
basket_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

basket_button_clear = telebot.types.KeyboardButton("🗑 Очистити кошик")

basket_keyboard.add(basket_button_clear, back_button)

#------------------------------------------------------------------------------------
def create_catalog(text_list, back_catalog_button, next_catalog_button):
    catalog_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    if back_catalog_button == True:        
        back_page_button = telebot.types.KeyboardButton("⬅️ Попередня сторінка") 
        catalog_keyboard.add(back_page_button)

    text_list.sort()

    for text in text_list:
        button = telebot.types.KeyboardButton(text)
        catalog_keyboard.add(button)

    if next_catalog_button == True:   
        forward_page_button = telebot.types.KeyboardButton("➡️ Наступна сторінка")
        catalog_keyboard.add(forward_page_button)
    catalog_keyboard.add(back_button)
    
    return catalog_keyboard