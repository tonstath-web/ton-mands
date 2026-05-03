#!/usr/bin/env python3
"""
Deploy TON MANDS Mini App to Cloudflare Pages
Usage: python deploy_cloudflare.py
"""

import os
import subprocess
import requests
import json
from pathlib import Path

# Config
CLOUDFLARE_API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN', '')
CLOUDFLARE_ACCOUNT_ID = os.getenv('CLOUDFLARE_ACCOUNT_ID', '')
PROJECT_NAME = 'ton-mands'

def zip_public_folder():
    """Zip the public folder for upload"""
    print("📦 Zipping public folder...")
    
    # Create zip file
    import shutil
    public_dir = Path('public')
    zip_path = Path('public_deploy')
    
    shutil.make_archive(str(zip_path), 'zip', public_dir)
    
    print(f"✅ Zipped to {zip_path}.zip")
    return f"{zip_path}.zip"

def deploy_to_cloudflare(zip_file):
    """Deploy to Cloudflare Pages via API"""
    
    if not CLOUDFLARE_API_TOKEN:
        print("❌ CLOUDFLARE_API_TOKEN not set!")
        print("\n📝 Setup instructions:")
        print("1. Go to: https://dash.cloudflare.com/profile/api-tokens")
        print("2. Create token with 'Cloudflare Pages: Edit' permission")
        print("3. Set env var: export CLOUDFLARE_API_TOKEN='your_token'")
        return None
    
    if not CLOUDFLARE_ACCOUNT_ID:
        print("❌ CLOUDFLARE_ACCOUNT_ID not set!")
        print("\n📝 Find your Account ID:")
        print("1. Go to: https://dash.cloudflare.com")
        print("2. Copy Account ID from right sidebar")
        print("3. Set env var: export CLOUDFLARE_ACCOUNT_ID='your_id'")
        return None
    
    print("🚀 Deploying to Cloudflare Pages...")
    
    # Cloudflare Pages API endpoint
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/pages/projects/{PROJECT_NAME}/deployments"
    
    headers = {
        'Authorization': f'Bearer {CLOUDFLARE_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    
    try:
        # Read zip file
        with open(zip_file, 'rb') as f:
            files = {'file': f}
            
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('success'):
                deployment_url = result['result']['url']
                print(f"\n✅ Deployment successful!")
                print(f"🌐 Mini App URL: https://{deployment_url}")
                return deployment_url
            else:
                print(f"❌ Deployment failed: {result}")
                return None
                
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Alternative: Deploy manually via Cloudflare Dashboard")
        print("   1. Go to: https://pages.cloudflare.com")
        print("   2. Create project → Direct Upload")
        print("   3. Upload public folder")
        return None

def update_bot_env(cloudflare_url):
    """Update .env with Cloudflare URL"""
    
    if not cloudflare_url:
        return
    
    env_file = Path('.env')
    if env_file.exists():
        # Read current .env
        with open(env_file, 'r') as f:
            content = f.read()
        
        # Update MINI_APP_URL
        content = content.replace(
            'MINI_APP_URL=https://ton-mands.vercel.app',
            f'MINI_APP_URL=https://{cloudflare_url}'
        )
        
        # Write back
        with open(env_file, 'w') as f:
            f.write(content)
        
        print(f"\n✅ Updated .env with new URL")
        print(f"   MINI_APP_URL=https://{cloudflare_url}")

def main():
    """Main deployment function"""
    
    print("☁️  TON MANDS - Cloudflare Pages Deployment")
    print("=" * 50)
    
    # Check if public folder exists
    if not Path('public').exists():
        print("❌ public folder not found!")
        return
    
    # Zip public folder
    zip_file = zip_public_folder()
    
    # Deploy to Cloudflare
    cloudflare_url = deploy_to_cloudflare(zip_file)
    
    # Update .env
    update_bot_env(cloudflare_url)
    
    # Cleanup
    if Path(zip_file).exists():
        os.remove(zip_file)
        print(f"\n🧹 Cleaned up {zip_file}")
    
    print("\n" + "=" * 50)
    if cloudflare_url:
        print("🎉 Deployment complete!")
        print(f"\n📱 Next steps:")
        print(f"   1. Open @BotFather")
        print(f"   2. /newapp → Select @tonsaikhbot")
        print(f"   3. URL: https://{cloudflare_url}")
        print(f"   4. Test Mini App!")
    else:
        print("⚠️  Manual deployment required")
        print("\n📝 Deploy manually:")
        print("   1. Go to: https://pages.cloudflare.com")
        print("   2. Create project → Direct Upload")
        print("   3. Upload 'public' folder")
        print("   4. Get URL and update .env")

if __name__ == '__main__':
    main()
