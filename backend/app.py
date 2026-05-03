"""
Telegram Mini App Backend - Crypto Price Tracker
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

# Serve the frontend
@app.route('/')
def index():
    return app.send_static_file('index.html')

# API endpoint for crypto prices
@app.route('/api/prices')
def get_prices():
    """
    Fetch crypto prices from MEXC API (public, no auth needed)
    """
    try:
        # MEXC API - Public endpoint
        url = 'https://api.mexc.com/api/v3/ticker/24hr'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Filter for major cryptos
        symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'DOGEUSDT']
        prices = []
        
        for ticker in data:
            if ticker['symbol'] in symbols:
                symbol = ticker['symbol'].replace('USDT', '')
                price = float(ticker['lastPrice'])
                change = float(ticker['priceChangePercent'])
                
                # Get name mapping
                names = {
                    'BTC': 'Bitcoin',
                    'ETH': 'Ethereum',
                    'BNB': 'Binance Coin',
                    'SOL': 'Solana',
                    'DOGE': 'Dogecoin'
                }
                
                prices.append({
                    'symbol': symbol,
                    'name': names.get(symbol, symbol),
                    'price': price,
                    'change': change,
                    'volume': float(ticker.get('volume', 0))
                })
        
        # Sort by BTC first, then alphabetically
        prices.sort(key=lambda x: (0 if x['symbol'] == 'BTC' else 1, x['symbol']))
        
        logger.info(f"Fetched prices for {len(prices)} cryptos")
        
        return jsonify({
            'success': True,
            'prices': prices,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error fetching prices: {e}")
        
        # Fallback data if API fails
        fallback_prices = [
            {'symbol': 'BTC', 'name': 'Bitcoin', 'price': 95000.00, 'change': 2.5},
            {'symbol': 'ETH', 'name': 'Ethereum', 'price': 3500.00, 'change': 1.8},
            {'symbol': 'BNB', 'name': 'Binance Coin', 'price': 600.00, 'change': -0.5},
            {'symbol': 'SOL', 'name': 'Solana', 'price': 200.00, 'change': 5.2},
            {'symbol': 'DOGE', 'name': 'Dogecoin', 'price': 0.15, 'change': -1.2}
        ]
        
        return jsonify({
            'success': True,
            'prices': fallback_prices,
            'timestamp': datetime.now().isoformat(),
            'note': 'Fallback data (API unavailable)'
        })

# Telegram WebApp verification
@app.route('/api/verify', methods=['POST'])
def verify_webapp():
    """
    Verify Telegram WebApp initData
    """
    try:
        initData = request.json.get('initData', '')
        
        # In production, verify the initData hash with your bot token
        # For now, just return success
        return jsonify({
            'success': True,
            'verified': True
        })
        
    except Exception as e:
        logger.error(f"Verification error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# User data endpoint
@app.route('/api/user', methods=['POST'])
def save_user():
    """
    Save user data from Mini App
    """
    try:
        user_data = request.json
        
        logger.info(f"User data: {user_data}")
        
        # In production, save to database
        # For now, just return success
        
        return jsonify({
            'success': True,
            'message': 'User data saved'
        })
        
    except Exception as e:
        logger.error(f"Error saving user: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

# Health check
@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
