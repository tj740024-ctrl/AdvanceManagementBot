# main.py
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# Import your utils package (ensure utils/__init__.py exists)
from utils import moderation, fun, backup

from config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I am Management Bot. Use /help to see available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available Commands:\n"
        "/start - Check if bot is alive\n"
        "/help - Show this help\n"
        "/backup - Auto-backup group rules/settings\n"
        "/joke - Get a random joke\n"
        "Moderation: Auto-delete spam/bad words"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Make sure these functions exist in your utils modules and are async:
    # async def auto_backup(update, context): ...
    # async def tell_joke(update, context): ...
    app.add_handler(CommandHandler("backup", backup.auto_backup))
    app.add_handler(CommandHandler("joke", fun.tell_joke))

    # Message Moderation
    # moderation.scan_message should be async def scan_message(update, context)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, moderation.scan_message))

    logger.info("✅ Management Bot started!")
    app.run_polling()


if __name__ == "__main__":
    main()
