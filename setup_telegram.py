#!/usr/bin/env python3
"""
Telegram Bot Setup Script for TON MANDS
Attempts to setup Mini App via Telegram Bot API
"""

import os
import requests
import json

# Config
BOT_TOKEN = os.getenv('BOT_TOKEN', '8560595547:AAEv8OT5xNbiNQ6ula_g3uhy_KwH9CMIMVg')
MINI_APP_URL = os.getenv('MINI_APP_URL', 'https://ton-mands.vercel.app')
BOT_USERNAME = 'tonsaikhbot'

def get_bot_info():
    """Get bot information"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    response = requests.get(url)
    return response.json()

def send_message(chat_id, text):
    """Send message to chat"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=data)
    return response.json()

def set_menu_button(web_app_url, text="🚀 Open Mini App"):
    """
    Set bot menu button to open Web App
    
    NOTE: This requires the bot to be already configured with Mini App via @BotFather
    The Telegram Bot API does NOT support creating new Mini Apps programmatically.
    This only works if Mini App was already set up via @BotFather manually.
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/setChatMenuButton"
    data = {
        'menu_button': {
            'type': 'web_app',
            'text': text,
            'web_app': {
                'url': web_app_url
            }
        }
    }
    response = requests.post(url, json=data)
    return response.json()

def check_mini_app_status():
    """Check if Mini App is configured"""
    print("\n🔍 Checking Mini App status...")
    
    # Try to get bot info
    bot_info = get_bot_info()
    
    if bot_info.get('ok'):
        print(f"✅ Bot is active: @{bot_info['result']['username']}")
        print(f"   Name: {bot_info['result']['first_name']}")
        print(f"   ID: {bot_info['result']['id']}")
        return True
    else:
        print(f"❌ Bot not accessible: {bot_info}")
        return False

def main():
    """Main function"""
    
    print("🤖 TON MANDS - Telegram Bot Setup")
    print("=" * 50)
    
    # Check bot status
    if not check_mini_app_status():
        print("\n❌ Bot is not accessible. Check token!")
        return
    
    print("\n⚠️  IMPORTANT LIMITATION:")
    print("=" * 50)
    print("""
Telegram Bot API DOES NOT support creating Mini Apps programmatically.

Mini App setup MUST be done manually via @BotFather:

1. Open @BotFather in Telegram
2. Send: /newapp
3. Select bot: @tonsaikhbot
4. Enter title: TON MANDS
5. Enter URL: https://ton-mands.vercel.app
6. Enter short name: tonmands

This is a Telegram security requirement - NOT a code limitation!

Alternative: Users can access Mini App directly via:
https://ton-mands.vercel.app
    """)
    
    print("\n" + "=" * 50)
    print("💡 RECOMMENDATION:")
    print("=" * 50)
    print("""
Option A: Setup Mini App manually (3 minutes)
  - Open @BotFather
  - /newapp → Follow prompts
  - Done!

Option B: Use direct link (no bot needed)
  - Share: https://ton-mands.vercel.app
  - Users open in browser/Telegram

Option C: Set menu button (if Mini App already configured)
  - Run: python set_menu_button.py
  - Only works if Mini App was setup via @BotFather
    """)
    
    print("\n" + "=" * 50)
    print("📱 Bot Info:")
    print("=" * 50)
    print(f"Username: @{BOT_USERNAME}")
    print(f"Token: {BOT_TOKEN[:20]}...")
    print(f"Mini App URL: {MINI_APP_URL}")

if __name__ == '__main__':
    main()
