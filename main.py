import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Настройка доступа к Google Таблицам
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Название таблицы").sheet1

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для записи на тренировки. Используйте команду /register для записи.')

# Функция для обработки команды /register
def register(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    sheet.append_row([user.first_name, user.last_name, user.username])
    update.message.reply_text('Вы успешно записаны на тренировку!')

def main() -> None:
    # Создание экземпляра Updater и передача ему токена API
    updater = Updater("7456296843:AAE6JBsi6C7wWKNPJOMdUjqbVB6c3DukiL4")

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчиков команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
