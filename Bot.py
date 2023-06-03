from aiogram import executor, types, Dispatcher, Bot
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import ParseMode
from loguru import logger

#* Initializing the bot and dispatcher
bot = Bot('5890015741:AAEnTCXg_lg2T8d4Z0nbCwaPV8lPUldLwQY')
dp = Dispatcher(bot)

#*log
logger.debug("---Bot started working---")

#* Creating a handler that opens the ChatGPT
@dp.message_handler(commands = ['question'])
async def question(message: types.Message):
    
    #* Send message
    await bot.send_message(message.chat.id,'Hello, ask the bot a question link')

    #* Open and send photo
    file = open( 'E:\.vscode\PROJECTS\ChatGPT_bot\png\OpenAI.png', 'rb')

    #*log
    logger.debug("---Photo is open---")

    await bot.send_photo(message.chat.id, file)

    #* Creating a button when clicked, the transition to the web application takes place
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text ='Open ChatGPT', web_app = WebAppInfo(url = 'https://chat-gpt.org')))

    #*log
    logger.debug("---ChatGPT is open---")

    #* Send message
    await message.answer('Follow the link 🧐', reply_markup = markup)

    #TODO: if WebAppInfo == True:
        #TODO: await message.answer('did yoy manage to find the answer to your question?', reply_markup = types.ReplyKeyboardRemove())

#* Creating a handler that sends info to VK or GitHub when the button is clicked 
@dp.message_handler(commands = ['info'])
async def information(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    #* Creating buttons
    markup.add(types.InlineKeyboardButton('Vkontakte', callback_data ='https://vk.com/lazzyxxx'))
    markup.add(types.InlineKeyboardButton('GitHub', callback_data = 'https://github.com/14LaveN/ChatGPT_bot'))
    
    #* Send message
    await message.answer('---GitHub or VK---',reply_markup = markup, parse_mode=ParseMode.MARKDOWN)
    #*log
    logger.debug("---GitHub or VK---")

#* Creating a handler that throws a link to the VK when the button is clicked
@dp.message_handler(lambda message: message.text == 'Vkontakte')
async def handle_button_click(message: types.Message):
    #* Send message
    await bot.send_message(message.chat.id, 'https://vk.com/lazzyxxx')

    #*log
    logger.debug("---VK---")

    #* Send message
    await bot.send_message(message.chat.id, "You choosed VK")

    #* Open and send photo
    file = open('E:\.vscode\PROJECTS\ChatGPT_bot\png\Vk.png', 'rb')
    #*logp;-
    logger.debug('---Photo VK open---')

    await bot.send_photo(message.chat.id, file)

#* Creating a handler that throws a link to the GitHub when the button is clicked
@dp.message_handler(lambda message: message.text == 'GitHub')
async def handle_button_click(message: types.Message):
    #* Send message
    await bot.send_message(message.chat.id, 'https://github.com/14LaveN/ChatGPT_bot/tree/master/.vscode/PROJECTS/ChatGPT_bot')

    #*log
    logger.debug("---GitHub---")
    
    #* Send message
    await bot.send_message(message.chat.id, "You choosed GitHub👁‍🗨")

    #* Open and send photo
    file = open('E:\.vscode\PROJECTS\ChatGPT_bot\png\GitHub.png', 'rb')
    #*log
    logger.debug('---Photo GitHub open')

    await bot.send_photo(message.chat.id, file)

#* name verification
if __name__ == "__main__":
    #*Getting started with the bot
    executor.start_polling(dp)