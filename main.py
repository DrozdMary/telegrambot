import telebot
from kd import *
from text import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_main_keyboard()  # Создание главной клавиатуры
    bot.send_message(message.chat.id,
                     main_menu_text,
                     reply_markup=keyboard)


pressed_btn = ''


# обработка main_keyboard и переход во вложенное меню
@bot.callback_query_handler(func=lambda callback: callback.data.endswith('_menu'))
def first_level_callback_handler(callback):
    global pressed_btn
    pressed_btn = callback.data
    for main_menu_data in main_menu_info.values():
        if callback.data in main_menu_data.keys():
            bot.edit_message_text(edited_text,
                                  callback.message.chat.id,
                                  callback.message.message_id,
                                  reply_markup=main_menu_data[callback.data])
        elif callback.data == 'main_menu':
            bot.edit_message_text(main_menu_text,
                                  callback.message.chat.id,
                                  callback.message.message_id,
                                  reply_markup=create_main_keyboard())


# Обработка кнопок главного меню
@bot.callback_query_handler(func=lambda callback: callback.data.startswith('btn_'))
def second_level_callback_handler(callback):
    if callback.data in list(dict_all_btns.keys()):
        edited_df = df.where(df['Торговая марка'] == dict_all_btns[callback.data]).dropna()
        bot.send_message(callback.message.chat.id, message_1, )
        for index, row in edited_df.iterrows():
            promocode = f"{row['Промокод']}"
            bot.send_message(callback.message.chat.id,
                             promocode_text.format(row['Торговая марка'], row['Скидка по промокоду'],
                                                   row['Ссылка для активации промокода'], row['Срок действия'],
                                                   row['Зона охвата'], row['Условия для активации промокода']))
            bot.send_message(callback.message.chat.id,
                             promocode)
            pressed_btn_name = ''
        for external_key, internal_dict in main_menu_info.items():
            # Проверяем, есть ли вложенный словарь с ключом, который нужно найти
            if pressed_btn in internal_dict:
                pressed_btn_name = external_key

        bot.send_message(callback.message.chat.id,
                         last_message,
                         reply_markup=create_last_keyboard(pressed_btn_name))


if __name__ == "__main__":
    bot.polling(none_stop=True)
    # Запуск бота в режиме постоянного ожидания сообщений
