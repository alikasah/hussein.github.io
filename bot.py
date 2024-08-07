import telebot

TOKEN = '7371705533:AAHwWPklQRb054fTJGTpIrFPCpnQNPbVSqg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message ="*Hello*\nI'm a simple robot that sends anything copyable with one line \nEx: `\n1111` `\n2222`\n*Just send me a message example:* `\n1111\n2222`\n*Dev by: @nothing_4k*"
    bot.reply_to(message, welcome_message, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def send_code_blocks(message):
    if message.text != "/start":
        codes = message.text.split('\n')

        code_blocks = ''
        for code in codes:
            code_blocks += f"`{code}\n`"

        bot.send_message(chat_id=message.chat.id, text=code_blocks, parse_mode='Markdown')


print('running...')
bot.polling()
