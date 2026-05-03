# 💎 QUICKSTART - TON MANDS Mini App

## Setup Cepat (5 Menit!)

### 1️⃣ Install Dependencies
```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app/backend
./venv/bin/pip install -r requirements.txt
```

### 2️⃣ Test Backend Local
```bash
cd backend
./venv/bin/python app.py
```

Backend akan jalan di: `http://localhost:5000`

Test API:
```bash
curl http://localhost:5000/api/prices
```

### 3️⃣ Deploy Frontend (Pilih Salah Satu)

#### Option A: Vercel (Recommended - Gratis!)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy folder public
cd ../public
vercel --prod
```

Catat URL yang didapat, contoh: `https://ton-mands.vercel.app`

#### Option B: Netlify (Gratis!)
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd ../public
netlify deploy --prod --dir=.
```

#### Option C: GitHub Pages (Gratis!)
1. Push folder `public` ke GitHub
2. Enable GitHub Pages di repository settings
3. URL: `https://username.github.io/repo-name`

### 4️⃣ Update .env
```bash
cd ..
nano .env
```

Ganti `MINI_APP_URL` dengan URL dari step 3:
```env
MINI_APP_URL=https://crypto-mini-app.vercel.app
```

### 5️⃣ Setup Bot di Telegram

#### Cara 1: Via @BotFather (Recommended)
1. Buka @BotFather di Telegram
2. `/newapp` - buat Mini App baru
3. Pilih bot Anda (`@your_bot_username`)
4. Masukkan title: "Crypto Mini App"
5. Masukkan description: "Track crypto prices"
6. Upload photo (optional)
7. Masukkan **Web App URL** (dari step 3)
8. Masukkan **Short name** (contoh: `cryptoapp`)

Done! Bot siap dipakai!

#### Cara 2: Manual Setting
1. @BotFather → `/mybots`
2. Pilih bot Anda
3. **Bot Settings** → **Menu Button**
4. **Configure Menu Button**
5. Send URL: `https://crypto-mini-app.vercel.app`
6. Set title: "🚀 Open App"

### 6️⃣ Run Bot

#### Local Testing:
```bash
python bot.py
```

#### Production (VPS/Server):
```bash
# Pakai nohup atau systemd
nohup python bot.py &

# Atau pakai systemd (lihat README.md)
```

---

## 📱 Test Mini App

1. Buka bot Anda di Telegram
2. Klik `/start`
3. Klik button **"🚀 Open Mini App"**
4. Mini App terbuka di dalam Telegram!
5. Lihat harga crypto real-time!

---

## 🎯 Fitur yang Sudah Ada

✅ **Frontend:**
- Real-time crypto prices (BTC, ETH, BNB, SOL, DOGE)
- Portfolio tracking
- 24h change dengan warna (hijau=naik, merah=turun)
- Telegram theme integration
- Haptic feedback
- Auto-refresh 30 detik
- Responsive design

✅ **Backend:**
- MEXC API integration (public, no auth!)
- Fallback data jika API down
- Health check endpoint
- CORS enabled

✅ **Telegram Bot:**
- `/start` - Open Mini App button
- `/help` - Help commands
- `/prices` - Quick price check
- `/about` - Bot info

---

## 🔧 Troubleshooting

### Mini App tidak muncul?
- Pastikan URL **HTTPS**
- Check di @BotFather sudah set correctly
- Restart bot

### Prices tidak muncul?
- Check backend logs
- Test API: `curl https://your-app.vercel.app/api/prices`
- MEXC API mungkin down (fallback data akan muncul)

### Bot tidak respond?
- Check BOT_TOKEN di .env
- Restart bot
- Check internet connection

---

## 📊 Next Steps (Optional)

### Tambah Fitur:
- [ ] User portfolio (save ke database)
- [ ] Price alerts (notification)
- [ ] Trading signals (connect ke trading bot)
- [ ] More cryptos (top 50)
- [ ] Price charts (graph)

### Improve:
- [ ] Database (PostgreSQL/MongoDB)
- [ ] User authentication
- [ ] WebSocket untuk real-time updates
- [ ] Push notifications
- [ ] Multi-language support

---

**Need Help?** DM: @jaxnije

**SIGNAL BY CRYPTO TRADE** 🚀
