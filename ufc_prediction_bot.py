import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Telegram API Token
TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Backend API URL
apiUrl = 'https://your-backend-url.onrender.com'  # Replace with your actual backend URL

# Command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Send me the names of two UFC fighters, and I will predict the winner. Use the format: "fighter1 vs fighter2".')

# Command to handle the prediction request
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if "vs" not in text:
        await update.message.reply_text('Please use the correct format: "fighter1 vs fighter2"')
        return

    try:
        fighter1, fighter2 = text.split("vs")
        fighter1 = fighter1.strip()
        fighter2 = fighter2.strip()

        if fighter1.lower() == fighter2.lower():
            await update.message.reply_text("Please provide two different fighters.")
            return

        # Make a POST request to the backend API
        response = requests.post(f"{apiUrl}/predict", json={"fighter_1": fighter1, "fighter_2": fighter2})
        data = response.json()

        if "prediction" in data:
            await update.message.reply_text(f"Prediction: {data['prediction']}")
        else:
            await update.message.reply_text("Sorry, I couldn't make a prediction. Please make sure the fighter names are correct.")

    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text("An error occurred while processing your request.")

async def main() -> None:
    # Create Application instance using the Telegram API Token
    application = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, predict))

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

