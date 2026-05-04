// Firebase Configuration
// Replace with your Firebase project config
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Get Realtime Database
const db = firebase.database();

// Generate unique battle ID
function generateBattleId() {
  return 'battle_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

// Create new battle in Firebase
function createBattleInFirebase(battleData) {
  const battleId = generateBattleId();
  const battleRef = db.ref('battles/' + battleId);
  
  battleRef.set({
    ...battleData,
    createdAt: firebase.database.ServerValue.TIMESTAMP,
    status: 'waiting'
  });
  
  return battleId;
}

// Update battle in Firebase
function updateBattleInFirebase(battleId, updates) {
  const battleRef = db.ref('battles/' + battleId);
  battleRef.update(updates);
}

// Listen to battle changes
function listenToBattle(battleId, callback) {
  const battleRef = db.ref('battles/' + battleId);
  battleRef.on('value', (snapshot) => {
    const data = snapshot.val();
    if (data) {
      callback(data);
    }
  });
  return battleRef;
}

// Join battle
function joinBattle(battleId, playerData) {
  const battleRef = db.ref('battles/' + battleId + '/players');
  const playerRef = battleRef.push();
  playerRef.set({
    ...playerData,
    joinedAt: firebase.database.ServerValue.TIMESTAMP
  });
  return playerRef.key;
}

// Remove battle (cleanup)
function removeBattle(battleId) {
  db.ref('battles/' + battleId).remove();
}

// Get active battles
function getActiveBattles(callback) {
  const battlesRef = db.ref('battles');
  battlesRef.orderByChild('status').equalTo('waiting').on('value', (snapshot) => {
    const battles = [];
    snapshot.forEach((childSnapshot) => {
      battles.push({
        id: childSnapshot.key,
        ...childSnapshot.val()
      });
    });
    callback(battles);
  });
}

// Export functions
window.firebaseDB = {
  db,
  generateBattleId,
  createBattleInFirebase,
  updateBattleInFirebase,
  listenToBattle,
  joinBattle,
  removeBattle,
  getActiveBattles
};

console.log('✅ Firebase initialized');
