"""
Telegram Bot untuk TON MANDS Mini App
"""
import os
import logging
from telegram import (
    Update, 
    WebAppInfo, 
    KeyboardButton, 
    ReplyKeyboardMarkup
)
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config
BOT_TOKEN = os.getenv('BOT_TOKEN', '8772804057:AAHPjPWVBR5GCV_eZhMt_wEa9kxSCFFefEc')
MINI_APP_URL = os.getenv('MINI_APP_URL', 'https://ton-mands.vercel.app')
CHANNEL_USERNAME = 'tonmands'  # Update dengan channel Anda

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    username = f"@{user.username}" if user.username else ""
    
    # Simulate balance (nanti bisa connect ke database)
    balance = 0.084  # TON
    
    # Generate referral link
    user_id = user.id
    referral_link = f"https://t.me/{context.bot.username}?start=ref{user_id}"
    
    # Create inline keyboard dengan 2 buttons
    # Gunakan WebAppInfo untuk Mini App yang proper
    keyboard = [
        [KeyboardButton("📢 Join TON Mands Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [KeyboardButton("🚀 Open Mini App", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # Welcome message
    message = f"""Hello {user.first_name} {username} 👋

Welcome to TON Mands Mini App.
Your balance: {balance} TON

Your referral link:
{referral_link}
"""
    
    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        """📚 **TON MANDS - Help**

**Commands:**
/start - Open Mini App
/balance - Check your balance
/invite - Get referral link
/help - Show this help
/about - About TON MANDS

**Features:**
💎 Real-time crypto prices
📊 Portfolio tracking
📈 Market analytics
🎁 Referral rewards

**Mini App:**
Click "🚀 Open Mini App" button to launch!

Powered by Telegram Mini Apps 🚀
        """,
        parse_mode='Markdown'
    )

async def balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /balance command"""
    user_id = update.effective_user.id
    
    # Simulate balance (nanti connect database)
    balance = 0.084
    
    await update.message.reply_text(
        f"""💎 **Your Balance**

💰 Amount: {balance} TON

≈ ${(balance * 3.5):.2f} USD

_This is a demo balance. Connect to real wallet for actual balance._
        """,
        parse_mode='Markdown'
    )

async def invite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /invite command - Get referral link"""
    user_id = update.effective_user.id
    referral_link = f"https://t.me/{context.bot.username}?start=ref{user_id}"
    
    await update.message.reply_text(
        f"""🎁 **Invite Friends & Earn!**

Your referral link:
{referral_link}

**Rewards:**
💎 0.01 TON per friend
🎯 Bonus for top referrers

Share your link and start earning!
        """,
        parse_mode='Markdown'
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /about command"""
    await update.message.reply_text(
        """💎 **About TON MANDS**

**Version:** 1.0.0
**Platform:** Telegram Mini App

**Features:**
• Real-time crypto prices
• Portfolio tracking
• Market analytics
• Referral system
• TON ecosystem integration

**Supported Tokens:**
₿ BTC, Ξ ETH, ₿ BNB, ◎ SOL, Ð DOGE, 💎 TON

**Technology:**
• Frontend: HTML, CSS, JavaScript
• Backend: Python Flask
• API: MEXC Public API
• Platform: Telegram + Vercel

**Business Or Partnership DM:** @jaxnije

*TON MANDS - Build • Hold • Grow*
        """,
        parse_mode='Markdown'
    )

async def prices_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /prices command - Quick price check"""
    try:
        import requests
        
        # Fetch from MEXC API
        url = 'https://api.mexc.com/api/v3/ticker/24hr'
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Top cryptos
        symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'DOGEUSDT', 'TONUSDT']
        
        msg = "📊 **Crypto Prices**\n\n"
        
        for ticker in data:
            if ticker['symbol'] in symbols:
                symbol = ticker['symbol'].replace('USDT', '')
                price = float(ticker['lastPrice'])
                change = float(ticker['priceChangePercent'])
                
                emoji = '🟢' if change >= 0 else '🔴'
                sign = '+' if change >= 0 else ''
                
                # Format price based on value
                if price < 1:
                    price_str = f"${price:.6f}"
                else:
                    price_str = f"${price:,.2f}"
                
                msg += f"{emoji} **{symbol}**: {price_str} ({sign}{change:.2f}%)\n"
        
        msg += "\n🚀 Open Mini App for more features!"
        
        await update.message.reply_text(msg, parse_mode='Markdown')
        
    except Exception as e:
        logger.error(f"Error fetching prices: {e}")
        await update.message.reply_text("⚠️ Failed to fetch prices. Please try again later.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Update {update} caused error: {context.error}")

def main():
    """Main function"""
    logger.info("Starting TON MANDS Bot...")
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("balance", balance_command))
    application.add_handler(CommandHandler("invite", invite_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("prices", prices_command))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot started! Listening for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
