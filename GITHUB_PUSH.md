# 🚀 PANDUAN PUSH KE GITHUB - TON MANDS

---

## ✅ **Git Sudah Ready!**

Project TON MANDS sudah di-commit:
- ✅ 13 files
- ✅ Branch: `main`
- ✅ Commit: "💎 TON MANDS - Initial commit"

---

## 📋 **Step-by-Step Push ke GitHub:**

### **Step 1: Buat Repo di GitHub**

1. Buka **https://github.com/new**
2. Login dengan akun GitHub Anda
3. **Repository name**: `ton-mands`
4. **Description**: "💎 TON MANDS - Telegram Mini App for Crypto Tracking"
5. **Public** (atau Private jika mau)
6. **JANGAN centang** "Add a README file"
7. Klik **Create repository**

---

### **Step 2: Copy URL Repo**

Setelah repo dibuat, GitHub akan tampilkan URL seperti:
```
https://github.com/YOUR_USERNAME/ton-mands.git
```

**Copy URL ini!**

---

### **Step 3: Push dari Terminal**

Kembali ke terminal, jalankan:

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app

# Ganti YOUR_USERNAME dengan username GitHub Anda
git remote add origin https://github.com/YOUR_USERNAME/ton-mands.git

# Push ke GitHub
git push -u origin main
```

**Jika diminta auth:**
- Masukkan **GitHub username**
- Masukkan **GitHub Personal Access Token** (bukan password!)

**Cara buat token:**
1. Buka https://github.com/settings/tokens
2. **Generate new token (classic)**
3. Centang: `repo` (Full control of private repositories)
4. **Generate token**
5. **Copy token** (simpan baik-baik, hanya muncul sekali!)

---

### **Step 4: Verify Push**

Buka repo GitHub Anda:
```
https://github.com/YOUR_USERNAME/ton-mands
```

Harus muncul semua files TON MANDS!

---

## 🎯 **Step 5: Deploy di Vercel**

### **1. Buka Vercel**
```
https://vercel.com/new
```

### **2. Login dengan GitHub**
- Klik **Continue with GitHub**
- Authorize Vercel

### **3. Import Repo**
- Cari repo `ton-mands`
- Klik **Import**

### **4. Configure Project**
- **Framework Preset**: `Other`
- **Root Directory**: `./` (kosongkan)
- **Build Command**: kosongkan
- **Output Directory**: `public`

### **5. Deploy!**
- Klik **Deploy**
- Tunggu 1-2 menit

### **6. Done!**
Dapat URL:
```
https://ton-mands-xxxx.vercel.app
```

---

## 📱 **Step 6: Setup di Telegram**

### **1. Buka @BotFather**
```
/newapp
```

### **2. Ikuti Instruksi:**
```
→ Pilih bot TON MANDS (token: 8772804057:AAHPjPWVBR5GCV_eZhMt_wEa9kxSCFFefEc)
→ Title: "💎 TON MANDS"
→ Description: "Track crypto prices real-time"
→ Upload photo (optional, 640x360)
→ Web App URL: https://ton-mands-xxxx.vercel.app
→ Short name: tonmands
```

### **3. Test!**
1. Buka bot TON MANDS di Telegram
2. `/start`
3. Klik **"💎 Open TON MANDS"**
4. App terbuka!

---

## 🎨 **Next: Desain UI!**

Setelah deploy, kita bisa mulai desain:

- **Warna**: TON blue (#0088cc) atau custom
- **Logo**: Upload logo TON MANDS
- **Layout**: Modern, minimalist, atau fancy
- **Fitur**: Charts, alerts, portfolio, dll
- **Animasi**: Smooth transitions

---

## 💡 **Troubleshooting:**

### **Git Push Failed:**
```bash
# Jika ada error "remote already exists"
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/ton-mands.git
git push -u origin main
```

### **Vercel Deploy Failed:**
- Check logs di Vercel Dashboard
- Pastikan `vercel.json` ada
- Test local dulu: `cd backend && ./venv/bin/python app.py`

### **Mini App Tidak Muncul:**
- Pastikan URL **HTTPS** (Vercel otomatis)
- Check di @BotFather URL sudah benar
- Clear cache Telegram

---

## 📞 **Butuh Bantuan?**

DM: @jaxnije

---

**💎 TON MANDS - Ready to Deploy!** 🚀
