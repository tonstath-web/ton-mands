// Vercel Serverless API Route for Telegram Backend
const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '8790293521:AAHgFk1ACJbdMAaJEdOHMa23u4OA_VFyYEw';
const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}`;

// In-memory storage (Vercel serverless)
const battles = new Map();

// Helper: Telegram API call
async function telegramAPI(method, data) {
  try {
    const response = await fetch(`${TELEGRAM_API}/${method}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return await response.json();
  } catch (error) {
    console.error('Telegram API error:', error);
    return null;
  }
}

// Generate battle ID
function generateBattleId() {
  return 'b_' + Math.random().toString(36).substr(2, 9);
}

export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }
  
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  const { action, battleId, data } = req.body;
  
  try {
    switch (action) {
      case 'create': {
        const id = generateBattleId();
        const battle = {
          id,
          hostId: data.userId,
          pool: data.bet || 0,
          timer: 30,
          status: 'waiting',
          players: {},
          createdAt: Date.now()
        };
        
        // Add host as first player
        battle.players['host'] = {
          name: data.name,
          userId: data.userId,
          bet: data.bet,
          emoji: data.emoji,
          photo: data.photo,
          isHost: true
        };
        
        battles.set(id, battle);
        
        // Send to Telegram (optional logging)
        await telegramAPI('sendMessage', {
          chat_id: data.userId,
          text: `🎮 Battle Created!\nID: \`${id}\`\nPool: ${battle.pool} TON\nWaiting for players...`,
          parse_mode: 'Markdown'
        }).catch(() => {});
        
        return res.json({ success: true, battle });
      }
      
      case 'get': {
        const battle = battles.get(battleId);
        if (!battle) {
          return res.json({ success: false, error: 'Battle not found' });
        }
        return res.json({ success: true, battle });
      }
      
      case 'join': {
        const battle = battles.get(battleId);
        if (!battle) {
          return res.json({ success: false, error: 'Battle not found' });
        }
        
        if (battle.status !== 'waiting') {
          return res.json({ success: false, error: 'Battle already started' });
        }
        
        // Check if player already exists
        const existingPlayer = Object.entries(battle.players).find(
          ([, p]) => p.userId === data.userId
        );
        
        if (existingPlayer) {
          // Add to existing bet
          existingPlayer[1].bet += data.bet;
          battle.pool += data.bet;
          battles.set(battleId, battle);
          
          return res.json({ 
            success: true, 
            battle,
            playerId: existingPlayer[0],
            message: 'Bet added'
          });
        }
        
        // New player
        const playerId = 'p_' + Math.random().toString(36).substr(2, 6);
        battle.players[playerId] = {
          name: data.name,
          userId: data.userId,
          bet: data.bet,
          emoji: data.emoji,
          photo: data.photo,
          joinedAt: Date.now()
        };
        battle.pool += data.bet;
        
        battles.set(battleId, battle);
        
        // Notify via Telegram
        await telegramAPI('sendMessage', {
          chat_id: data.userId,
          text: `✅ Joined Battle!\nPool: ${battle.pool} TON\nPlayers: ${Object.keys(battle.players).length}`,
          parse_mode: 'Markdown'
        }).catch(() => {});
        
        return res.json({ success: true, battle, playerId });
      }
      
      case 'update': {
        const battle = battles.get(battleId);
        if (!battle) {
          return res.json({ success: false, error: 'Battle not found' });
        }
        
        Object.assign(battle, data);
        battles.set(battleId, battle);
        
        return res.json({ success: true, battle });
      }
      
      case 'start': {
        const battle = battles.get(battleId);
        if (!battle) {
          return res.json({ success: false, error: 'Battle not found' });
        }
        
        battle.status = 'spinning';
        battle.winnerIndex = data.winnerIndex;
        battles.set(battleId, battle);
        
        // Notify all players
        const playerList = Object.values(battle.players);
        for (const player of playerList) {
          await telegramAPI('sendMessage', {
            chat_id: player.userId,
            text: `🎰 Battle Started!\nGood luck! 🍀`,
            parse_mode: 'Markdown'
          }).catch(() => {});
        }
        
        return res.json({ success: true, battle });
      }
      
      case 'delete': {
        battles.delete(battleId);
        return res.json({ success: true });
      }
      
      default:
        return res.status(400).json({ success: false, error: 'Invalid action' });
    }
  } catch (error) {
    console.error('Battle API error:', error);
    return res.status(500).json({ success: false, error: error.message });
  }
}
