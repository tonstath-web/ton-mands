# 🚀 TON MANDS - Manual Deploy Guide

Karena Vercel CLI butuh login, kita deploy manual!

---

## 🎯 **Option 1: Deploy via Vercel Dashboard (TERMUDAH!)**

### **Step 1: Push ke GitHub**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app

# Init git
git init
git add .
git commit -m "TON MANDS - Initial commit"

# Buat repo di GitHub.com (gratis)
# Lalu push:
git remote add origin https://github.com/YOUR_USERNAME/ton-mands.git
git branch -M main
git push -u origin main
```

### **Step 2: Deploy di Vercel.com**

1. Buka **https://vercel.com/new**
2. Login dengan GitHub
3. **Import Git Repository**
4. Pilih repo `ton-mands`
5. **Root Directory**: `.` (kosongkan)
6. **Framework Preset**: `Other`
7. Klik **Deploy**

**DONE!** Dalam 1-2 menit dapat URL:
```
https://ton-mands-xxxx.vercel.app
```

---

## 🎯 **Option 2: Deploy via Vercel CLI (Butuh Login)**

### **Step 1: Install & Login**

```bash
# Install
npm install -g vercel

# Login (akan buka browser)
vercel login
```

Pilih login dengan **GitHub** (termudah).

### **Step 2: Deploy**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app
vercel --prod
```

Jawab pertanyaan:
```
Set up and deploy? [Y/n] → Y
Which scope? → Pilih account
Link to existing project? [y/N] → N
Project name? → ton-mands
Directory? → ./
Override settings? [y/N] → N
```

**DONE!** Dapat URL production.

---

## 🎯 **Option 3: Deploy via Netlify (Alternatif)**

### **Step 1: Install Netlify CLI**

```bash
npm install -g netlify-cli
```

### **Step 2: Deploy**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app/public
netlify deploy --prod --dir=.
```

Pertanyaan:
```
Choose team → Personal
Site name? → ton-mands
```

**DONE!** Dapat URL: `https://ton-mands.netlify.app`

---

## 🎯 **Option 4: GitHub Pages (Gratis Total)**

### **Step 1: Push ke GitHub**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app

git init
git add .
git commit -m "TON MANDS"

# Buat repo di GitHub
git remote add origin https://github.com/YOUR_USERNAME/ton-mands.git
git branch -M main
git push -u origin main
```

### **Step 2: Enable GitHub Pages**

1. Buka repo di GitHub
2. **Settings** → **Pages**
3. **Source**: Deploy from branch
4. **Branch**: `main` → folder `/public`
5. **Save**

Dalam 5 menit dapat URL:
```
https://YOUR_USERNAME.github.io/ton-mands/
```

---

## 📱 **Setelah Deploy - Setup di Telegram:**

### **1. Setup Mini App di BotFather**

```
/newapp
→ Pilih bot TON MANDS
→ Title: "💎 TON MANDS"
→ Description: "Track crypto prices real-time"
→ Upload photo (optional)
→ Web App URL: https://ton-mands.vercel.app (URL dari deploy)
→ Short name: tonmands
```

### **2. Test di Telegram**

1. Buka bot TON MANDS
2. `/start`
3. Klik **"💎 Open TON MANDS"**
4. App terbuka!

---

## 🎨 **Next: Desain UI**

Setelah deploy, kita bisa mulai desain ulang:

- Ganti warna (sesuai brand TON)
- Tambah logo
- Animasi baru
- Layout yang lebih modern
- Fitur tambahan (charts, alerts, dll)

---

## 💡 **Rekomendasi Saya:**

**Gunakan Option 1 (Vercel Dashboard)** karena:
- ✅ Paling mudah (klik-klik doang)
- ✅ Otomatis HTTPS
- ✅ Auto deploy tiap git push
- ✅ Gratis unlimited
- ✅ Cepat di Indonesia

**Mau saya bantu push ke GitHub dulu?** Baru deploy via dashboard! 🚀

---

**💎 TON MANDS - Ready to Deploy!** 🎯
