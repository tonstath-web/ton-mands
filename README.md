# 💎 TON MANDS - Telegram Mini App

Telegram Mini App untuk tracking harga crypto dengan interface modern!

## 📁 Struktur Project

```
telegram-mini-app/
├── public/
│   └── index.html          # Frontend (TON MANDS UI)
├── backend/
│   ├── app.py              # Flask backend
│   └── requirements.txt    # Python dependencies
├── bot.py                  # Telegram bot (TON MANDS)
├── .env                    # Environment variables
├── .env.example            # Example env
├── vercel.json             # Vercel deployment config
└── README.md               # This file
```

## 🛠️ Setup

### 1. Install Dependencies

**Backend:**
```bash
cd backend
pip install -r requirements.txt
```

### 2. Setup Environment Variables

Copy `.env.example` ke `.env`:
```bash
cp .env.example .env
```

Edit `.env`:
```env
BOT_TOKEN=your_bot_token_here
MINI_APP_URL=https://your-app.vercel.app
```

### 3. Deploy Frontend

Deploy folder `public` ke hosting (Vercel, Netlify, dll):

**Option 1: Vercel (Recommended)**
```bash
cd public
vercel --prod
```

**Option 2: Netlify**
```bash
netlify deploy --prod --dir=public
```

Catat URL yang didapat (contoh: `https://your-app.vercel.app`)

### 4. Setup Bot di Telegram

1. Buka @BotFather di Telegram
2. `/newapp` - buat Mini App baru
3. Pilih bot Anda
4. Masukkan URL Mini App (dari step 3)
5. BotFather akan berikan short name

Atau manual:
1. @BotFather → `/mybots`
2. Pilih bot → Bot Settings → Menu Button
3. Set Menu Button URL ke Mini App URL

### 5. Run Bot

**Local:**
```bash
# Terminal 1 - Backend
cd backend
python app.py

# Terminal 2 - Bot
python bot.py
```

**Production:**
```bash
# Backend di Vercel/server
# Bot di VPS/heroku
python bot.py
```

## 🎯 Features

### Frontend (TON MANDS App)
- ✅ Real-time crypto prices (BTC, ETH, BNB, SOL, DOGE)
- ✅ Portfolio tracking (simulated)
- ✅ 24h price change dengan color coding
- ✅ Telegram theme integration
- ✅ Haptic feedback
- ✅ Responsive design
- ✅ Auto-refresh setiap 30 detik
- ✅ TON MANDS branding

### Backend API
- ✅ `/api/prices` - Fetch dari MEXC API
- ✅ `/api/verify` - Verify Telegram WebApp
- ✅ `/api/user` - Save user data
- ✅ `/api/health` - Health check
- ✅ Fallback data jika API down

### Telegram Bot (TON MANDS)
- ✅ `/start` - Open TON MANDS button
- ✅ `/help` - Help commands
- ✅ `/prices` - Quick price check
- ✅ `/about` - Bot info
- ✅ WebApp data handler

## 📱 Cara Pakai

1. User buka bot TON MANDS di Telegram
2. Klik `/start` atau menu button
3. TON MANDS App terbuka di dalam Telegram
4. Lihat harga crypto real-time
5. Klik crypto untuk detail
6. Refresh prices kapan saja

## 🔧 Customization

### Ganti Crypto List
Edit `public/index.html`:
```javascript
const cryptos = [
    { symbol: 'BTC', name: 'Bitcoin' },
    { symbol: 'ETH', name: 'Ethereum' },
    // Add more...
];
```

### Ganti Warna Theme
Edit CSS di `public/index.html`:
```css
:root {
    --tg-theme-button-color: #3390ec;
    /* Change to your color */
}
```

### Tambah Fitur
Edit `backend/app.py` untuk tambah API endpoint baru.

## 🚀 Deploy to Production

### Backend (Vercel)
1. Buat `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    { "src": "backend/app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "backend/app.py" }
  ]
}
```

2. Deploy:
```bash
vercel --prod
```

### Bot (VPS/Heroku)
1. Upload semua file ke VPS
2. Install dependencies
3. Run dengan systemd/supervisor:
```ini
# /etc/systemd/system/crypto-bot.service
[Unit]
Description=Crypto Mini App Bot
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/telegram-mini-app
ExecStart=/path/to/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

4. Enable:
```bash
sudo systemctl enable crypto-bot
sudo systemctl start crypto-bot
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve Mini App frontend |
| `/api/prices` | GET | Get crypto prices |
| `/api/verify` | POST | Verify WebApp data |
| `/api/user` | POST | Save user data |
| `/api/health` | GET | Health check |

## 🔐 Security

- ✅ Telegram WebApp verification (implement di production)
- ✅ CORS enabled untuk frontend
- ✅ Environment variables untuk sensitive data
- ✅ Error handling untuk semua endpoint

## 📝 Notes

- Mini App URL **harus HTTPS**
- Bot token jangan commit ke git
- Test di Telegram Desktop dulu sebelum mobile
- Rate limit MEXC API: 10 requests/second

## 🤝 Support

Business Or Partnership DM: @jaxnije

---

**💎 TON MANDS - Your Crypto Tracker** 🚀
