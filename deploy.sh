#!/bin/bash
# TON MANDS Bot - Auto Deploy Script
# Usage: bash deploy.sh

echo "🚀 TON MANDS - Auto Deploy to VPS"
echo "=================================="

# Update system
echo "📦 Updating system..."
sudo apt update -y

# Install Python & Git
echo "🐍 Installing Python & Git..."
sudo apt install python3 python3-pip git screen -y

# Clone repository
echo "📥 Cloning repository..."
cd ~
git clone https://github.com/tonstath-web/ton-mands.git
cd ton-mands/telegram-mini-app

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Create .env file
echo "⚙️  Creating .env file..."
cat > .env << EOF
BOT_TOKEN=8560595547:AAEv8OT5xNbiNQ6ula_g3uhy_KwH9CMIMVg
MINI_APP_URL=https://ton-mands.vercel.app
EOF

# Create systemd service
echo "🔧 Creating systemd service..."
sudo bash -c 'cat > /etc/systemd/system/tonmands-bot.service << EOF
[Unit]
Description=TON MANDS Telegram Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/ton-mands/telegram-mini-app
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF'

# Enable and start service
echo "🚀 Starting bot service..."
sudo systemctl daemon-reload
sudo systemctl enable tonmands-bot
sudo systemctl start tonmands-bot

# Check status
echo ""
echo "=================================="
echo "✅ Deployment Complete!"
echo "=================================="
echo ""
sudo systemctl status tonmands-bot --no-pager

echo ""
echo "📱 Test your bot:"
echo "   Open Telegram: t.me/tonsaikhbot"
echo "   Send: /start"
echo ""
echo "🔧 Useful commands:"
echo "   Check status: sudo systemctl status tonmands-bot"
echo "   View logs: sudo journalctl -u tonmands-bot -f"
echo "   Restart: sudo systemctl restart tonmands-bot"
echo "   Stop: sudo systemctl stop tonmands-bot"
echo ""
