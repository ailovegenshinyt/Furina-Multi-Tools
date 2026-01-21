import os
import requests
import subprocess
import ctypes
from pathlib import Path

# --- ตั้งค่าเริ่มต้น ---
REPO_URL = "https://raw.githubusercontent.com/ailovegenshinyt/Furina-Multi-Tools/main"
INSTALL_DIR = Path.home() / "Furina-MT"
FILES_TO_DOWNLOAD = ["furina_tool.py", "furina_tool.bat", "requirements.txt", "commandscode.txt", "version.txt"]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_file(filename):
    url = f"{REPO_URL}/{filename}"
    print(f"📥 Downloading {filename}...")
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(INSTALL_DIR / filename, 'wb') as f:
            f.write(r.content)
        return True
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
        return False

def setup():
    print("============================================")
    print("      ✨ FURINA'S MULTI-TOOL INSTALLER ✨      ")
    print("============================================\n")

    # 1. สร้างโฟลเดอร์
    if not INSTALL_DIR.exists():
        INSTALL_DIR.mkdir(parents=True)
        print(f"📁 Created folder: {INSTALL_DIR}")

    # 2. ดาวน์โหลดไฟล์
    for file in FILES_TO_DOWNLOAD:
        download_file(file)

    # 3. สร้าง Shortcut (เฉพาะ Windows)
    if os.name == 'nt':
        print("🔗 Creating Desktop Shortcut...")
        desktop = Path.home() / "Desktop"
        shortcut_path = desktop / "Furina Multi-Tool.bat"
        # สร้างไฟล์ .bat เล็กๆ ไว้ที่หน้าจอเพื่อกดเปิดตัว .py ได้ง่ายๆ
        with open(shortcut_path, "w") as f:
            f.write(f"@echo off\npython \"{INSTALL_DIR / 'furina_tool.py'}\"\npause")

    print("\n✅ การติดตั้งเสร็จสมบูรณ์แล้วค่ะพี่! 🎉")
    print(f"🎭 พี่สามารถเริ่มการแสดงได้จากไอคอนบน Desktop นะคะ")

if __name__ ==

