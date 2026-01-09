import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте 👋\n\n"
        "Если хотите сделать в Roblox войс чат 🎧\n"
        "напишите гмайлы.\n\n"
        "Там уже привязан войс чат.\n"
        "С новым аккаунтом не работает ❌"
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN не найден")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
# redeploy
