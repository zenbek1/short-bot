from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8461610744:AAGhqcrnJBj9nPuCSHx2oE7ZuMezycJ9Uow"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот и работаю успешно 🚀")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Добавим хендлер команды /start
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    main()
