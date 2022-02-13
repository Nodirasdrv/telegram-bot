import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config("TOKEN_BOT")
)


@bot.message_handler(commands=["get"])
def answer_start(message):
    print(message.from_user.id)
    text = f"{message.from_user.first_name}" \
           f" {message.from_user.last_name}," \
           f" would you like to pick up your beverage or delivery?"
    keyboard_in = types.InlineKeyboardMarkup()
    btn_6 = types.InlineKeyboardButton(text="Pick up", callback_data="pick up")
    btn_7 = types.InlineKeyboardButton(text="Delivery", callback_data="delivery")

    keyboard_in.add(btn_6, btn_7)

    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.message_handler(commands=["start"])
def answer_start(message):
    print(message.from_user.id)
    text = f"Hi, {message.from_user.first_name}" \
           f" {message.from_user.last_name}! " \
           f"Do you want to order some coffee?" \
           f" What kind of coffee do you want to order?"
    keyboard_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text="Capuccino", callback_data="capuccino")
    btn_2 = types.InlineKeyboardButton(text="Latte", callback_data="latte")
    btn_3 = types.InlineKeyboardButton(text="Espresso", callback_data="espresso")
    btn_4 = types.InlineKeyboardButton(text="Macchiato", callback_data="macchiato")
    btn_5 = types.InlineKeyboardButton(text="Frappe", callback_data="frappe")
    keyboard_in.add(btn_1, btn_2, btn_3, btn_4, btn_5)

    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call: True)
def send_course(call):
    if call.data == "capuccino":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Capuccino Grande - 0.7ml")
        btn_2 = types.KeyboardButton("Capuccino Tall - 0.4ml")
        btn_3 = types.KeyboardButton("Capuccino Short - 0.2ml")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "latte":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Latte Grande - 0.7ml")
        btn_2 = types.KeyboardButton("Latte Tall - 0.4ml")
        btn_3 = types.KeyboardButton("Latte Short - 0.2ml")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "espresso":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Espresso Grande - 0.5ml")
        btn_2 = types.KeyboardButton("Espresso Tall - 0.3ml")
        btn_3 = types.KeyboardButton("Espresso Short - 0.2ml")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "macchiato":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Macchiato Grande - 0.9ml")
        btn_2 = types.KeyboardButton("Macchiato Tall - 0.7ml")
        btn_3 = types.KeyboardButton("Macchiato Short - 0.5ml")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "frappe":
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton("Frappe Grande - 0.7ml")
        btn_2 = types.KeyboardButton("Frappe Tall - 0.6ml")
        btn_3 = types.KeyboardButton("Frappe Short - 0.5ml")
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f"You chose {call.data}!"
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply)
    elif call.data == "pick up":
        text = f"You chose {call.data}!" \
               f" Pick up your drink at Garden Street 34 - Coffee Shop 'Sip-sip' "
        bot.send_message(call.message.chat.id, text)
    elif call.data == "delivery":
        text = f"You chose {call.data}!" \
               f"Please leave your address!"
        bot.send_message(call.message.chat.id, text)


@bot.message_handler(content_types=["text"])
def send_good_message(message):
    if message.text == "Capuccino Grande - 0.7ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 6.99$")
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Capuccino Tall - 0.4ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 4.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Capuccino Short - 0.2ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 3.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Latte Grande - 0.7ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 7.99$")
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Latte Tall - 0.4ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 6.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Latte Short - 0.2ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 5.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Espresso Grande - 0.5ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 3.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Espresso Tall - 0.3ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 2.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Espresso Short - 0.2ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 1.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Macchiato Grande - 0.9ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 8.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Macchiato Tall - 0.7ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 7.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Macchiato Short - 0.5ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 6.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Frappe Grande - 0.7ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 6.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Frappe Tall - 0.6ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 5.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")
    elif message.text == "Frappe Short - 0.5ml":
        bot.send_message(
            message.chat.id,
            "It will cost you 4.99$"
        )
        bot.send_message(
            message.chat.id,
            "Want to get your coffee? Write /get")


bot.polling()
