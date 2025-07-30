from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yfinance as yf

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Используй /shortlist для получения списка акций.")

async def shortlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tickers = ["GME", "AMC", "BB", "PLTR"]
    messages = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get('regularMarketPrice')
        change = info.get('regularMarketChangePercent')
        messages.append(f"{ticker}: Цена ${price}, Изменение {change:.2f}%")
    text = "📉 Акции для шорта:\n" + "\n".join(messages)
    await update.message.reply_text(text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shortlist", shortlist))

    app.run_polling()
