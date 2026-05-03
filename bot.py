"""
Telegram Bot untuk Mini App
"""
import os
import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config
BOT_TOKEN = os.getenv('BOT_TOKEN', '8772804057:AAHPjPWVBR5GCV_eZhMt_wEa9kxSCFFefEc')
MINI_APP_URL = os.getenv('MINI_APP_URL', 'https://your-app.vercel.app')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    
    # Create keyboard with Mini App button
    keyboard = [
        [KeyboardButton("💎 Open TON MANDS", web_app=WebAppInfo(url=MINI_APP_URL))],
        [KeyboardButton("📊 Prices"), KeyboardButton("ℹ️ Help")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    
    await update.message.reply_text(
        f"""👋 Hi {user.first_name}!

💎 **Welcome to TON MANDS!** 💎

Your real-time crypto price tracker!

**Click the button below to open the Mini App:**

💎 **Open TON MANDS** - View live prices, portfolio & analytics

Or use commands:
📊 /prices - Quick price check
ℹ️ /help - Help menu
📱 /about - About TON MANDS
        """,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        """📚 **TON MANDS - Help**

**Commands:**
/start - Open Mini App
/prices - Quick price check
/help - Show this help
/about - About TON MANDS

**Features:**
💎 Real-time crypto prices
📊 Portfolio tracking
📈 Market analytics
🔄 Auto-refresh every 30s

**Supported Cryptos:**
₿ BTC, Ξ ETH, ₿ BNB, ◎ SOL, Ð DOGE

**Mini App:**
Click "💎 Open TON MANDS" button to launch!

Powered by Telegram Mini Apps 🚀
        """,
        parse_mode='Markdown'
    )

async def prices_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /prices command"""
    try:
        import requests
        
        # Fetch from MEXC API
        url = 'https://api.mexc.com/api/v3/ticker/24hr'
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Top 5 cryptos
        symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'DOGEUSDT']
        
        msg = "📊 **Crypto Prices**\n\n"
        
        for ticker in data:
            if ticker['symbol'] in symbols:
                symbol = ticker['symbol'].replace('USDT', '')
                price = float(ticker['lastPrice'])
                change = float(ticker['priceChangePercent'])
                
                emoji = '🟢' if change >= 0 else '🔴'
                sign = '+' if change >= 0 else ''
                
                msg += f"{emoji} **{symbol}**: ${price:,.2f} ({sign}{change:.2f}%)\n"
        
        msg += "\n🚀 Open Mini App for more features!"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error fetching prices: {e}")
        await update.message.reply_text("⚠️ Failed to fetch prices. Please try again later.")

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /about command"""
    await update.message.reply_text(
        """💎 **About TON MANDS**

Version: 1.0.0
Developer: @jaxnije

**Features:**
• Real-time crypto prices from MEXC
• Portfolio tracking
• Price charts
• Market analytics
• Web-based Mini App interface

**Technology:**
• Frontend: HTML, CSS, JavaScript
• Backend: Python Flask
• API: MEXC Public API
• Platform: Telegram Mini Apps

Business Or Partnership DM: @jaxnije

*TON MANDS - Your Crypto Tracker*
        """,
        parse_mode='Markdown'
    )

async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle data sent from Mini App"""
    try:
        data = update.message.web_app_data.data
        logger.info(f"WebApp data received: {data}")
        
        # Process the data (e.g., save to database)
        await update.message.reply_text(
            "✅ Data received from Mini App!\n\n"
            f"Data: {data[:100]}..." if len(data) > 100 else f"Data: {data}"
        )
    except Exception as e:
        logger.error(f"Error processing webapp data: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error: {context.error}")

def main():
    """Main function"""
    logger.info("Starting Crypto Mini App Bot...")
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("prices", prices_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot started! Listening for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
