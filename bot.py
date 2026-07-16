 from telegram.ext import Application,CommandHandler, ContextTypes

TOKEN = 8993269375:AAHdCqxkVzPh1gBaMYlS27rY7Mh62y95wbE

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to TickerSage AI!\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/btc - Show BTC analysis (coming soon)"
    )

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 BTC analysis module is under development."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))

print("TickerSage AI is running...")
app.run_polling()