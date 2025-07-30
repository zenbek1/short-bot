from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8461610744:AAGhqcrnJBj9nPuCSHx2oE7ZuMezycJ9Uow"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю!")

async def reply_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text("Привет! Как дела?")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_hello))

    app.run_polling()
