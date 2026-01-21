import os
import subprocess
import requests

# ข้อมูลเบื้องต้น
VERSION = "1.0"
REPO_URL = "https://raw.githubusercontent.com/ailovegenshinyt/Furina-Multi-Tools/main"

def check_requirements():
    print("🔍 Checking stage equipment...")
    try:
        r = requests.get(f"{REPO_URL}/requirements.txt")
        items = r.text.splitlines()
        for item in items:
            # ตรวจสอบเบื้องต้น (เช่น yt-dlp)
            print(f"✅ Requirement '{item}' should be installed via pip/system.")
    except:
        print("❌ Could not check requirements online.")

def run_performance():
    print(f"\n============================================")
    print(f"      ✨ FURINA'S PYTHON THEATER v{VERSION} ✨")
    print(f"============================================\n")
    
    try:
        r = requests.get(f"{REPO_URL}/commandscode.txt")
        commands = {}
        lines = r.text.splitlines()
        
        for i, line in enumerate(lines, 1):
            if "=" in line:
                name, cmd = line.split("=", 1)
                commands[str(i)] = (name.strip(), cmd.strip())
                print(f"  [{i}] {name.strip()}")
        
        print("  [E] Exit Stage Left 🚪")
        choice = input("\nWhich act, brother?: ")
        
        if choice.lower() == 'e':
            return

        if choice in commands:
            name, cmd_base = commands[choice]
            target = input(f"🎭 Activating {name}\nEnter URL/Input: ")
            
            # รันคำสั่ง (ใช้ shell=True สำหรับความง่าย)
            full_cmd = f"{cmd_base} {target}"
            print(f"🎬 Starting: {full_cmd}")
            os.system(full_cmd)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    check_requirements()
    while True:
        run_performance()
        if input("\nContinue? (y/n): ").lower() != 'y':
            break
          
