from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TARGET_USERNAME = "Cal887"

def mock_text(text):
    result = ""
    upper = False
    for char in text:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char
    return result

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    if user.username != TARGET_USERNAME:
        return
    if not update.message.text:
        return
    mocked = mock_text(update.message.text)
    await update.message.reply_text(mocked)

if __name__ == "__main__":
    import os
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
