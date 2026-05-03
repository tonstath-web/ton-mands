# 🚀 Deploy ke Vercel - Step by Step

## 📋 Persiapan

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login ke Vercel
```bash
vercel login
```

Pilih login dengan:
- GitHub (recommended)
- GitLab
- Bitbucket
- Email

---

## 🎯 Deploy (2 Cara)

### **Cara 1: Deploy dengan CLI (Cepat!)**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app

# Deploy production
vercel --prod
```

**Pertanyaan yang akan muncul:**
```
Set up and deploy? [Y/n] → Y
Which scope? → Pilih account Anda
Link to existing project? [y/N] → N
What's your project's name? → crypto-mini-app
In which directory is your code located? → ./
Want to override the settings? [y/N] → N
```

**Output:**
```
🔍  Inspecting: https://crypto-mini-app-xyz.vercel.app
✅  Production: https://crypto-mini-app-xyz.vercel.app
```

**Catat URL production!** Contoh: `https://crypto-mini-app-xyz.vercel.app`

---

### **Cara 2: Deploy dengan Git (Recommended untuk Production)**

#### Step 1: Push ke GitHub
```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app

# Init git (jika belum)
git init
git add .
git commit -m "Initial commit - Crypto Mini App"

# Buat repo di GitHub, lalu:
git remote add origin https://github.com/yourusername/crypto-mini-app.git
git push -u origin main
```

#### Step 2: Connect ke Vercel
1. Buka https://vercel.com/new
2. **Import Git Repository**
3. Pilih repo `crypto-mini-app`
4. **Root Directory**: `.` (root)
5. **Framework Preset**: `Other`
6. Klik **Deploy**

#### Step 3: Auto Deploy
Setiap kali push ke GitHub:
```bash
git add .
git commit -m "Update feature"
git push
```

Vercel akan **auto deploy** dalam hitungan detik!

---

## ⚙️ Setup Environment Variables di Vercel

### Via CLI:
```bash
vercel env add BOT_TOKEN 8620014091:AAFKWWiGZEYpD20HvFuxNPyP_VZm7UhhyBI
vercel env add MINI_APP_URL https://crypto-mini-app-xyz.vercel.app
```

### Via Dashboard:
1. Buka project di Vercel Dashboard
2. **Settings** → **Environment Variables**
3. Add variables:
   - `BOT_TOKEN` = `8620014091:AAFKWWiGZEYpD20HvFuxNPyP_VZm7UhhyBI`
   - `MINI_APP_URL` = `https://crypto-mini-app-xyz.vercel.app`
4. **Save**

---

## 🔗 Setup Mini App di Telegram

### Step 1: Buka @BotFather
```
/newapp
```

### Step 2: Ikuti Instruksi
1. Pilih bot Anda
2. Enter title: `Crypto Mini App`
3. Enter description: `Track crypto prices real-time`
4. Upload photo (optional, 640x360)
5. **Enter Web App URL**: `https://crypto-mini-app-xyz.vercel.app`
6. Enter short name: `cryptoapp`

### Step 3: Test
1. Buka bot Anda di Telegram
2. Klik `/start`
3. Klik button **"🚀 Open Mini App"**
4. Mini App terbuka!

---

## 🎨 Custom Domain (Optional)

Punya domain? Setup custom domain:

1. Vercel Dashboard → Project → **Settings** → **Domains**
2. Add domain: `crypto.yourdomain.com`
3. Setup DNS records di domain provider:
   ```
   Type: CNAME
   Name: crypto
   Value: cname.vercel-dns.com
   ```
4. Wait 5-10 menit
5. Done!

---

## 📊 Monitoring

### Check Deployment Status
```bash
vercel ls
```

### View Logs
```bash
vercel logs
```

### Open Dashboard
```bash
vercel open
```

---

## 🔧 Troubleshooting

### Build Failed
```bash
# Check local first
vercel dev

# Fix errors, then deploy again
vercel --prod
```

### API Not Working
- Check environment variables di Vercel
- View logs: `vercel logs`
- Test API: `curl https://your-app.vercel.app/api/health`

### Mini App Tidak Muncul
- Pastikan URL **HTTPS** (Vercel otomatis HTTPS)
- Check di @BotFather URL sudah benar
- Clear cache Telegram (Settings → Data and Storage)

---

## 💡 Tips Vercel

### 1. Preview Deployments
Setiap push ke branch (bukan main) dapat **preview URL**:
```bash
git checkout -b feature/new-ui
git push
# Vercel deploy ke: https://crypto-mini-app-abc.vercel.app
```

### 2. Rollback
Deploy gagal? Rollback ke versi sebelumnya:
- Dashboard → Deployments → Klik deployment sebelumnya → **Rollback**

### 3. Analytics
Enable Vercel Analytics (gratis):
- Dashboard → Project → **Analytics** → **Enable**

### 4. Speed Insights
Enable Speed Insights:
- Dashboard → Project → **Speed Insights** → **Enable**

---

## 📈 Vercel Hobby Plan (Gratis)

✅ **Unlimited deployments**
✅ **100GB bandwidth/bulan** (cukup untuk 10k+ users)
✅ **Auto HTTPS**
✅ **Custom domains**
✅ **Edge network** (cepat di Indonesia)
✅ **Auto scaling**

**Upgrade ke Pro ($20/month)** jika butuh:
- More bandwidth (1TB)
- Priority support
- Team collaboration

---

## 🎯 Next Steps Setelah Deploy

1. ✅ **Test Mini App** di Telegram
2. ✅ **Share ke users** (t.me/your_bot)
3. ✅ **Monitor logs** di Vercel Dashboard
4. ✅ **Update berkala** (git push = auto deploy)

---

**Deploy sekarang?** Tinggal jalankan:
```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app
vercel --prod
```

Done! 🚀
