# 🔥 Firebase Setup Guide - TON MANDS

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click **"Add project"**
3. Enter project name: `ton-mands`
4. Disable Google Analytics (optional)
5. Click **"Create project"**

## Step 2: Enable Realtime Database

1. In Firebase Console, go to **Build** → **Realtime Database**
2. Click **"Create database"**
3. Choose **US-Central** or closest location
4. Select **Start in test mode** (for development)
5. Click **"Enable"**

## Step 3: Get Firebase Config

1. Go to **Project Settings** (gear icon)
2. Scroll down to **"Your apps"**
3. Click **Web** icon (`</>`)
4. Register app name: `TON MANDS Web`
5. Copy the `firebaseConfig` object

## Step 4: Update firebase-config.js

Open `firebase-config.js` and replace with your config:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "ton-mands-XXXXX.firebaseapp.com",
  databaseURL: "https://ton-mands-XXXXX-default-rtdb.firebaseio.com",
  projectId: "ton-mands-XXXXX",
  storageBucket: "ton-mands-XXXXX.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef123456"
};
```

## Step 5: Deploy to Vercel

```bash
cd telegram-mini-app
vercel --prod
```

## Step 6: Test Multiplayer

1. Open app in **2 different browsers** (or incognito)
2. Login with **different Telegram accounts**
3. Join the same battle
4. Both should see each other in real-time! ✅

## Database Structure

```
battles/
├── battle_1234567890_abc123/
│   ├── status: "waiting" | "spinning" | "finished"
│   ├── hostId: "user123"
│   ├── pool: 2.5
│   ├── timer: 30
│   ├── createdAt: 1234567890
│   ├── winnerIndex: 0
│   └── players/
│       ├── player_0/
│       │   ├── name: "Kinandra"
│       │   ├── userId: "123456"
│       │   ├── bet: 1.0
│       │   ├── emoji: "👤"
│       │   └── photo: "https://..."
│       └── player_1/
│           ├── name: "Dragon"
│           ├── userId: "789012"
│           ├── bet: 1.5
│           └── ...
└── battle_...
```

## Security Rules (Production)

After testing, update database rules:

```json
{
  "rules": {
    "battles": {
      "$battleId": {
        ".read": true,
        ".write": true,
        "players": {
          "$playerId": {
            ".validate": "newData.hasChildren(['name', 'bet', 'userId'])"
          }
        }
      }
    }
  }
}
```

## Troubleshooting

### Firebase not connecting?
- Check console for errors
- Verify config is correct
- Make sure database is in test mode

### Players not syncing?
- Check Firebase Realtime Database console
- Look for battle data updates
- Verify both users have same `currentBattleId`

### Deployment issues?
- Run `vercel --prod` again
- Check Vercel logs for errors
- Verify `firebase-config.js` is uploaded

---

**Need help?** Check [Firebase Docs](https://firebase.google.com/docs/database/web/start)
