from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import yfinance as yf

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # <-- вставь сюда свой токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, который показывает акции для шорта. Используй команду /shortlist")

async def shortlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Пример: получаем данные для нескольких акций и отправляем краткий список
    tickers = ["GME", "AMC", "BB", "PLTR"]  # примеры популярных шортовых акций
    messages = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get('regularMarketPrice')
        change = info.get('regularMarketChangePercent')
        messages.append(f"{ticker}: Цена: ${price}, Изменение: {change:.2f}%")

    text = "📉 Акции для шорта:\n" + "\n".join(messages)
    await update.message.reply_text(text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shortlist", shortlist))

    app.run_polling()
