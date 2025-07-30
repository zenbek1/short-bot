import yfinance as yf
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Получаем токен из переменной окружения

# Список популярных акций
TICKERS = ['AAPL', 'TSLA', 'AMZN', 'NVDA', 'META', 'NFLX', 'MSFT', 'GOOGL', 'AMD', 'INTC']

async def shortlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "📉 Акции, которые сейчас падают:\n\n"
    count = 0

    for ticker in TICKERS:
        data = yf.Ticker(ticker).history(period="2d")
        if len(data) < 2:
            continue

        yesterday_close = data['Close'][-2]
        today_close = data['Close'][-1]
        change_percent = (today_close - yesterday_close) / yesterday_close * 100

        if change_percent < -1.0:  # Падение больше 1%
            text += f"{ticker}: {today_close:.2f} USD ({change_percent:.2f}%)\n"
            count += 1

        if count >= 5:
            break

    if count == 0:
        text = "🚫 Сегодня нет акций, которые падают больше чем на 1%."

    await update.message.reply_text(text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("shortlist", shortlist))
    print("✅ Бот запущен")
    app.run_polling()
