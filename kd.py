from telebot import types
import webbrowser
import pandas as pd

# Загрузка данных из CSV-файла
df = pd.read_csv('promocodes.csv',
                 usecols=['Торговая марка', 'Скидка по промокоду', 'Ссылка для активации промокода', 'Срок действия',
                          'Зона охвата', 'Условия для активации промокода', 'Промокод'])
company_names = df['Торговая марка'].unique()

# Словарь для хранения информации о кнопках и связанных с ними компаниях
dict_all_btns = {}


# Функции для создания клавиатур
# Каждая функция создает клавиатуру с кнопками для определенной категории компаний
def create_market_keyboard():
    global dict_all_btns
    market_company_names = company_names[:5]
    market_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(market_company_names):
        dict_all_btns[f"btn_market{index}"] = f'{item}'
        market_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_market{index}"))
    market_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return market_keyboard


def create_bank_keyboard():
    global dict_all_btns
    bank_company_names = company_names[5:15]
    bank_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(bank_company_names):
        dict_all_btns[f"btn_bank{index}"] = f'{item}'
        bank_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_bank{index}"))
    bank_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return bank_keyboard


def create_invest_keyboard():
    global dict_all_btns
    invest_company_names = company_names[15:16]
    invest_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(invest_company_names):
        dict_all_btns[f"btn_invest{index}"] = f'{item}'
        invest_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_invest{index}"))
    invest_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return invest_keyboard


def create_delivery_keyboard():
    global dict_all_btns
    delivery_company_names = company_names[16:30]
    delivery_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(delivery_company_names):
        dict_all_btns[f"btn_delivery{index}"] = f'{item}'
        delivery_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_delivery{index}"))
    delivery_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return delivery_keyboard


def create_health_keyboard():
    global dict_all_btns
    health_company_names = company_names[30:34]
    health_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(health_company_names):
        dict_all_btns[f"btn_health{index}"] = f'{item}'
        health_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_health{index}"))
    health_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return health_keyboard


def create_fastfood_keyboard():
    global dict_all_btns
    fastfood_company_names = company_names[34:40]
    fastfood_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(fastfood_company_names):
        dict_all_btns[f"btn_fastfood{index}"] = f'{item}'
        fastfood_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_fastfood{index}"))
    fastfood_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return fastfood_keyboard


def create_flower_keyboard():
    global dict_all_btns
    flower_company_names = company_names[40:41]
    flower_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(flower_company_names):
        dict_all_btns[f"btn_flower{index}"] = f'{item}'
        flower_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_flower{index}"))
    flower_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return flower_keyboard


def create_online_keyboard():
    global dict_all_btns
    online_company_names = company_names[41:48]
    online_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(online_company_names):
        dict_all_btns[f"btn_online{index}"] = f'{item}'
        online_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_online{index}"))
    online_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return online_keyboard


def create_clothes_keyboard():
    global dict_all_btns
    clothes_company_names = company_names[48:50]
    clothes_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(clothes_company_names):
        dict_all_btns[f"btn_clothes{index}"] = f'{item}'
        clothes_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_clothes{index}"))
    clothes_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return clothes_keyboard


def create_cosmetic_keyboard():
    global dict_all_btns
    cosmetic_company_names = company_names[50:52]
    cosmetic_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(cosmetic_company_names):
        dict_all_btns[f"btn_cosmetic{index}"] = f'{item}'
        cosmetic_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_cosmetic{index}"))
    cosmetic_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return cosmetic_keyboard


def create_taxi_keyboard():
    global dict_all_btns
    taxi_company_names = company_names[52:54]
    taxi_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(taxi_company_names):
        dict_all_btns[f"btn_taxi{index}"] = f'{item}'
        taxi_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_taxi{index}"))
    taxi_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return taxi_keyboard


def create_insurance_keyboard():
    global dict_all_btns
    insurance_company_names = company_names[54:58]
    insurance_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(insurance_company_names):
        dict_all_btns[f"btn_insurance{index}"] = f'{item}'
        insurance_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_insurance{index}"))
    insurance_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return insurance_keyboard


def create_ticket_keyboard():
    global dict_all_btns
    ticket_company_names = company_names[58:63]
    ticket_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(ticket_company_names):
        dict_all_btns[f"btn_ticket{index}"] = f'{item}'
        ticket_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_ticket{index}"))
    ticket_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return ticket_keyboard


def create_registration_keyboard():
    global dict_all_btns
    registration_company_names = company_names[63:]
    registration_keyboard = types.InlineKeyboardMarkup(row_width=1)
    for index, item in enumerate(registration_company_names):
        dict_all_btns[f"btn_registration{index}"] = f'{item}'
        registration_keyboard.add(
            types.InlineKeyboardButton(f'{item}', callback_data=f"btn_registration{index}"))
    registration_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"))
    return registration_keyboard


# Словарь с информацией о главном меню и связанными с ним клавиатурами
main_menu_info = {"Маркетплейс": {'market_menu': create_market_keyboard()},
                  "Бонусы от банка": {'bank_menu': create_bank_keyboard()},
                  'Инвестиции': {'invest_menu': create_invest_keyboard()},
                  'Доставка/продукты': {'delivery_menu': create_delivery_keyboard()},
                  'Аптеки/здоровье': {'health_menu': create_health_keyboard()},
                  'Фастфуд/Пицца/Ролы': {'fastfood_menu': create_fastfood_keyboard()},
                  'Цветы': {'flower_menu': create_flower_keyboard()},
                  'Онлайн сервис/подписка': {'online_menu': create_online_keyboard()},
                  'Обувь/одежда': {'clothes_menu': create_clothes_keyboard()},
                  'Косметика/парфюмерия': {'cosmetic_menu': create_cosmetic_keyboard()},
                  'Такси/каршеринг/АЗС': {'taxi_menu': create_taxi_keyboard()},
                  'Страхование': {'insurance_menu': create_insurance_keyboard()},
                  'Авиабилеты/гостиницы': {'ticket_menu': create_ticket_keyboard()},
                  'Регистрация/Счет для бизнеса': {'registration_menu': create_registration_keyboard()}
                  }

# Список с именами категорий для главной клавиатуры
names_of_callback_data = list(main_menu_info.keys())  #


# Функция для создания главной клавиатуры
def create_main_keyboard():
    main_keyboard = types.InlineKeyboardMarkup()
    for i in names_of_callback_data:
        main_keyboard.add(
            types.InlineKeyboardButton(i, callback_data=list(main_menu_info[i].keys())[0]),
            row_width=1
        )
    main_keyboard.add(
        types.InlineKeyboardButton('Таблица со всеми промокодами',
                                   url="https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M/edit#gid=0"),

    )
    return main_keyboard


# Функция для создания клавиатуры для последнего уровня
def create_last_keyboard(name):
    last_keyboard = types.InlineKeyboardMarkup()

    last_keyboard.add(
        types.InlineKeyboardButton('В меню', callback_data="main_menu"),
        types.InlineKeyboardButton(name, callback_data=list(main_menu_info[name].keys())[0]),
        row_width=1)

    return last_keyboard
