// Telegram Bot Backend for TON MANDS
// Serverless function for Vercel

const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '8790293521:AAHgFk1ACJbdMAaJEdOHMa23u4OA_VFyYEw';
const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}`;

// Store battles in memory (for Vercel serverless)
// In production, use Redis or database
const battles = new Map();

// Helper: Make Telegram API call
async function telegramAPI(method, data) {
  const response = await fetch(`${TELEGRAM_API}/${method}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return response.json();
}

// Generate unique battle ID
function generateBattleId() {
  return 'battle_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6);
}

// Create new battle
async function createBattle(battleData) {
  const battleId = generateBattleId();
  const battle = {
    id: battleId,
    ...battleData,
    createdAt: Date.now(),
    status: 'waiting',
    players: {}
  };
  
  battles.set(battleId, battle);
  
  // Send notification to bot admin (optional)
  // await telegramAPI('sendMessage', {
  //   chat_id: ADMIN_CHAT_ID,
  //   text: `🎮 New battle created: ${battleId}`
  // });
  
  return battle;
}

// Get battle by ID
function getBattle(battleId) {
  return battles.get(battleId);
}

// Update battle
function updateBattle(battleId, updates) {
  const battle = battles.get(battleId);
  if (battle) {
    Object.assign(battle, updates);
    battles.set(battleId, battle);
  }
  return battle;
}

// Join battle
function joinBattle(battleId, playerData) {
  const battle = battles.get(battleId);
  if (!battle) return null;
  
  const playerId = 'player_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4);
  battle.players[playerId] = {
    ...playerData,
    joinedAt: Date.now()
  };
  
  battles.set(battleId, battle);
  return { playerId, battle };
}

// Leave battle
function leaveBattle(battleId, playerId) {
  const battle = battles.get(battleId);
  if (battle && battle.players[playerId]) {
    delete battle.players[playerId];
    battles.set(battleId, battle);
  }
}

// Delete battle (cleanup)
function deleteBattle(battleId) {
  battles.delete(battleId);
}

// Cleanup old battles (older than 1 hour)
function cleanupOldBattles() {
  const now = Date.now();
  const oneHour = 60 * 60 * 1000;
  
  for (const [id, battle] of battles.entries()) {
    if (now - battle.createdAt > oneHour) {
      battles.delete(id);
    }
  }
}

// Run cleanup every 10 minutes
setInterval(cleanupOldBattles, 10 * 60 * 1000);

// Export for Vercel serverless function
export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }
  
  try {
    const { action, battleId, playerData, updates } = req.body;
    
    switch (action) {
      case 'create':
        const newBattle = await createBattle(playerData);
        return res.json({ success: true, battle: newBattle });
      
      case 'get':
        const battle = getBattle(battleId);
        return res.json({ success: true, battle });
      
      case 'update':
        const updated = updateBattle(battleId, updates);
        return res.json({ success: true, battle: updated });
      
      case 'join':
        const result = joinBattle(battleId, playerData);
        return res.json({ success: true, ...result });
      
      case 'leave':
        leaveBattle(battleId, playerData.playerId);
        return res.json({ success: true });
      
      case 'delete':
        deleteBattle(battleId);
        return res.json({ success: true });
      
      default:
        return res.status(400).json({ success: false, error: 'Invalid action' });
    }
  } catch (error) {
    console.error('Telegram backend error:', error);
    return res.status(500).json({ success: false, error: error.message });
  }
}
