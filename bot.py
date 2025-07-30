from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8461610744:AAGhqcrnJBj9nPuCSHx2oE7ZuMezycJ9Uow"

async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text("Привет! Как дела?")
    elif "как дела" in text:
        await update.message.reply_text("Всё отлично! А у тебя?")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))
    app.run_polling()
