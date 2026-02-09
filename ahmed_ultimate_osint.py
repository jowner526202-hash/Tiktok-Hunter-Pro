import requests
import re
import os
import json
import urllib.request
from datetime import datetime

# --- واجهة المطور أحمد ---
def banner():
    os.system('clear')
    print(f"""
    \033[1;36m
     █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ 
    ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗
    ███████║███████║██╔████╔██║█████╗  ██║  ██║
    ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║
    ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝ 
    \033[1;32m
    [+] Developer: AHMED (Ultimate OSINT Tool)
    [+] Features: Emails, HD Avatar, Creation Date, Region
    [+] Socials: Auto-Detection Enabled
    \033[0m
    """)

def get_creation_date(uid):
    try:
        binary = bin(int(uid))
        timestamp = int(binary[2:33], 2)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    except:
        return "Unknown"

def ahmed_ultimate_scan(username):
    username = username.replace('@', '').lower()
    url = f"https://www.tiktok.com/@{username}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    print(f"\033[1;33m[*] Ahmed's Engine is Scanning: @{username}...\033[0m")
    
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            html = res.text
            
            # 1. استخراج الـ User ID
            uid_match = re.search(r'\"userId\":\"(\d+)\"', html)
            uid = uid_match.group(1) if uid_match else "N/A"
            
            # 2. استخراج الدولة/المنطقة
            region_match = re.search(r'\"region\":\"([A-Z]{2})\"', html)
            region = region_match.group(1) if region_match else "N/A"
            
            # 3. تاريخ الإنشاء
            c_date = get_creation_date(uid) if uid != "N/A" else "N/A"
            
            # 4. صيد الإيميلات
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))
            
            # 5. نوع الحساب
            verified = "verified\":true" in html
            acc_type = "Verified Official" if verified else "Standard Account"
            
            # 6. الروابط الاجتماعية
            socials = []
            for p in ['instagram', 'facebook', 'twitter', 'youtube']:
                if p in html.lower(): socials.append(p.capitalize())

            # 7. تحميل الصورة الشخصية HD
            avatar_match = re.search(r'\"avatarLarger\":\"(https://.*?)\"', html)
            if avatar_match:
                img_url = avatar_match.group(1).replace('\\u002F', '/')
                urllib.request.urlretrieve(img_url, f"{username}_avatar.jpg")
                img_status = f"Downloaded ({username}_avatar.jpg)"
            else:
                img_status = "Not Found"

            # --- عرض النتائج النهائية ---
            print(f"\n\033[1;32m[✔] Scan Finished Successfully!\033[0m")
            print(f"\033[1;37m" + "─"*45 + "\033[0m")
            print(f"\033[1;32m👤 User:\033[0m {username} | \033[1;32mType:\033[0m {acc_type}")
            print(f"\033[1;32m🆔 ID:\033[0m   {uid} | \033[1;32mRegion:\033[0m {region}")
            print(f"\033[1;32m📅 Date:\033[0m {c_date} | \033[1;32mAvatar:\033[0m {img_status}")
            print(f"\033[1;32m📧 Mail:\033[0m {', '.join(emails) if emails else 'No Public Emails'}")
            print(f"\033[1;32m🔗 Socials:\033[0m {', '.join(socials) if socials else 'None'}")
            print(f"\033[1;37m" + "─"*45 + "\033[0m")

            # حفظ التقرير
            report = {
                "dev": "AHMED",
                "target": username,
                "user_id": uid,
                "region": region,
                "created": c_date,
                "emails": emails,
                "verified": verified
            }
            with open(f"{username}_report.json", "w") as f:
                json.dump(report, f, indent=4)
            print(f"\033[1;34m[!] JSON Report Saved.\033[0m\n")

        else:
            print("\033[1;31m[-] Error: Profile not found or IP Blocked.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[-] System Error: {e}\033[0m")

if __name__ == "__main__":
    banner()
    target_user = input("\033[1;37m[?] Enter Target Username: \033[0m")
    ahmed_ultimate_scan(target_user)
