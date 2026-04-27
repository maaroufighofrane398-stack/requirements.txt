from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً 👋 البوت يعمل بنجاح!")

# أي رسالة
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token("8722503665:AAG-h3jZjeqMp7PRLzuJ6kFYfvPrMx5yfw0").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("help", start))

print("Bot is running...")

app.run_polling()
