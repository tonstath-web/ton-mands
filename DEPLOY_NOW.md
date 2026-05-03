# 🚀 DEPLOY VERCEL - TON MANDS

**Dipandu Langkah-demi-Langkah!**

---

## ✅ **GitHub Sudah Ready!**

Repo: **https://github.com/tonstath-web/ton-mands**

---

## 🎯 **DEPLOY SEKARANG (5 Menit)**

### **Step 1: Buka Vercel**
```
https://vercel.com/new
```

### **Step 2: Login**
- Klik **"Continue with GitHub"**
- Login dengan akun GitHub Anda (`tonstath-web`)
- Authorize Vercel

### **Step 3: Import Repository**
- Di bagian **"Import Git Repository"**
- Cari repo: **`ton-mands`**
- Atau scroll cari: **tonstath-web/ton-mands**
- Klik **"Import"**

### **Step 4: Configure Project**

Di halaman "Configure [repo-name]":

```
FRAMEWORK PRESET: Other
ROOT DIRECTORY: ./  (kosongkan)
BUILD COMMAND: (kosongkan)
OUTPUT DIRECTORY: public
INSTALL COMMAND: (kosongkan)
```

**Environment Variables:**
Klik **"Environment Variables"** → **"Add New"**:

| Name | Value |
|------|-------|
| `BOT_TOKEN` | `8772804057:AAHPjPWVBR5GCV_eZhMt_wEa9kxSCFFefEc` |
| `MINI_APP_URL` | *(nanti diisi setelah deploy)* |

Klik **"Save"**

### **Step 5: Deploy!**
- Klik **"Deploy"** (tombol biru di bawah)
- **TUNGGU 1-2 MENIT** ⏳

### **Step 6: Done!**
- Akan muncul animasi build
- Setelah selesai: **"Your deployment is ready!"**
- **COPY URL** yang muncul, contoh:
  ```
  https://ton-mands-xyz123.vercel.app
  ```

---

## 📱 **SETUP TELEGRAM BOTFATHER**

### **1. Buka @BotFather**
```
/newapp
```

### **2. Ikuti Instruksi:**

```
Choose a bot for your Mini App:
→ Pilih bot TON MANDS Anda

Enter a title for your Mini App:
→ "💎 TON MANDS"

Enter a description:
→ "Track crypto prices real-time"

Send us a photo for your Mini App (640x360):
→ SKIP (ketik /skip) atau upload gambar

Enter the Web App URL:
→ Paste URL dari Vercel: https://ton-mands-xyz123.vercel.app

Enter a short name for your Mini App:
→ tonmands
```

### **3. Done!**
BotFather akan konfirmasi:
```
Great! Your Mini App has been configured.
```

---

## 🎉 **TEST MINI APP**

### **1. Buka Bot TON MANDS**
- Cari bot Anda di Telegram
- Atau klik link: `t.me/YOUR_BOT_USERNAME`

### **2. Start Bot**
```
/start
```

### **3. Klik Menu Button**
- Klik **"💎 Open TON MANDS"** di menu bawah
- ATAU klik button **"🚀 Open Mini App"**

### **4. Mini App Terbuka!**
- Lihat harga crypto real-time
- Portfolio tracking
- Auto-refresh setiap 30 detik

---

## 🔧 **TROUBLESHOOTING**

### **Vercel Deploy Gagal?**
1. Buka **"Deployment"** tab di Vercel
2. Klik deployment yang failed
3. Lihat **"Logs"** - ada error detail
4. Fix error, lalu **"Redeploy"**

### **Mini App Tidak Muncul?**
1. Check URL di BotFather sudah benar (harus HTTPS)
2. Restart Telegram (close & reopen)
3. Clear cache: Settings → Data and Storage → Clear Cache

### **Prices Tidak Muncul?**
1. Check backend logs di Vercel: **Functions** → **backend/app.py**
2. Test API: `https://ton-mands-xyz.vercel.app/api/health`
3. MEXC API mungkin down (ada fallback data)

---

## 🎨 **NEXT: DESAIN UI**

Setelah deploy berhasil, **kita mulai desain UI**!

Bisa request:
- Ganti warna (TON blue, gradient, dll)
- Tambah logo
- Animasi baru
- Layout modern
- Fitur tambahan (charts, alerts, portfolio)

---

## 📞 **BUTUH BANTUAN?**

Screenshot error + kirim ke saya, saya bantu fix!

---

**🚀 DEPLOY SEKARANG: https://vercel.com/new**

**💎 TON MANDS - Almost Live!** 🎯
