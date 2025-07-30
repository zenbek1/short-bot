from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yfinance as yf

TOKEN = "ТВОЙ_ТОКЕН_ОТ_БОТА"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Используй /shortlist чтобы получить акции для шорта.")

async def shortlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tickers = ["GME", "AMC", "BB", "PLTR"]
    text = "📉 Акции для шорта:\n"

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        price = stock.info.get("regularMarketPrice", "N/A")
        change = stock.info.get("regularMarketChangePercent", 0)
        text += f"{ticker}: ${price} ({change:.2f}%)\n"

    await update.message.reply_text(text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shortlist", shortlist))
    app.run_polling()
