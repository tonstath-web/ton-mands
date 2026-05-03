# ☁️ TON MANDS - Cloudflare Pages Deployment

**100% GRATIS - Unlimited Bandwidth**

---

## 🚀 **2 CARA DEPLOY:**

### **Option A: Manual via Dashboard (TERMUDAH!)** ⭐ RECOMMENDED

**5 Menit, tinggal klik-klik!**

### **Option B: Python Script (Otomatis)**

**Butuh Cloudflare API Token**

---

## 📋 **OPTION A: MANUAL DEPLOY (MUDAH!)**

### **Step 1: Buka Cloudflare Pages**
```
https://pages.cloudflare.com
```

### **Step 2: Sign Up / Login**
- Buat akun Cloudflare (GRATIS!)
- Tidak perlu kartu kredit

### **Step 3: Create Project**
```
Create a project → Direct Upload
```

### **Step 4: Upload Folder**

**Cara Upload:**

1. Buka folder project:
   ```
   /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app/public
   ```

2. **Pilih SEMUA file** di folder `public`

3. **Drag & Drop** ke Cloudflare Pages

   ATAU

4. **Zip dulu** folder `public`, lalu upload file zip

### **Step 5: Project Name**
```
ton-mands
```

### **Step 6: Deploy!**
- Klik **"Deploy"**
- Tunggu 30 detik - 1 menit

### **Step 7: Done!**

Dapat URL gratis:
```
https://ton-mands.pages.dev
```

---

## 🐍 **OPTION B: PYTHON SCRIPT**

### **Step 1: Setup Cloudflare API**

**1. Buat API Token:**
```
https://dash.cloudflare.com/profile/api-tokens
```

**2. Create Token:**
- Template: `Edit Cloudflare Pages`
- Permissions: `Cloudflare Pages: Edit`
- Klik **Continue to summary**
- **Create Token**

**3. Copy Token!**
```
CLOUDFLARE_API_TOKEN=xxxxxxxxxxxxxxxxxxxx
```

**4. Get Account ID:**
```
https://dash.cloudflare.com
```
- Account ID ada di sidebar kanan
- Copy Account ID

### **Step 2: Set Environment Variables**

```bash
export CLOUDFLARE_API_TOKEN='your_token_here'
export CLOUDFLARE_ACCOUNT_ID='your_account_id_here'
```

### **Step 3: Run Deploy Script**

```bash
cd /mnt/data/openclaw/workspace/.openclaw/workspace/telegram-mini-app
python deploy_cloudflare.py
```

### **Step 4: Done!**

Script akan:
- ✅ Zip folder `public`
- ✅ Upload ke Cloudflare Pages
- ✅ Update `.env` dengan URL baru
- ✅ Kasih tau URL Mini App

---

## 📱 **SETUP DI BOTFATHER:**

Setelah deploy (Option A atau B):

### **1. Buka @BotFather**
```
t.me/BotFather
```

### **2. Setup Mini App**
```
/newapp
→ Pilih @tonsaikhbot
→ Title: 💎 TON MANDS
→ Description: Track crypto prices real-time
→ Photo: /skip
→ Web App URL: https://ton-mands.pages.dev
→ Short name: tonmands
```

### **3. Test!**

Buka @tonsaikhbot:
```
/start
→ Klik "🚀 Open Mini App"
→ Mini App terbuka!
```

---

## 💰 **CLOUDFLARE PAGES FREE:**

| Feature | Limit |
|---------|-------|
| **Sites** | Unlimited |
| **Bandwidth** | 100GB/hari |
| **Requests** | Unlimited |
| **Build minutes** | 500/bulan |
| **Storage** | 5GB |
| **Custom domain** | ✅ Gratis |
| **HTTPS** | ✅ Otomatis |
| **CDN** | ✅ Global |

**100% GRATIS!** Tidak perlu kartu kredit!

---

## 🎯 **REKOMENDASI:**

**Option A (Manual)** lebih mudah kalau:
- ✅ Pertama kali deploy
- ✅ Tidak mau ribet API token
- ✅ Cuma deploy 1-2 kali

**Option B (Script)** lebih baik kalau:
- ✅ Mau auto-deploy
- ✅ Sering update
- ✅ Mau integrate dengan CI/CD

---

## 💬 **NEXT:**

**Pilih Option A atau B?**

**A)** Manual via Dashboard (saya pandu step-by-step)

**B)** Python Script (butuh API token)

**Kabar-kabarin pilihannya!** 🚀☁️
