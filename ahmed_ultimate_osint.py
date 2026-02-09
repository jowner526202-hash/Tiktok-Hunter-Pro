import requests
import re
import os
import json
from datetime import datetime

def banner():
    os.system('clear')
    print(f"""
    \033[1;31m
     █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ 
    ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗
    ███████║███████║██╔████╔██║█████╗  ██║  ██║
    ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║
    ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝
    \033[1;33m [!] TITAN EDITION v4.0 | Developed by: AHMED \033[0m
    """)

def get_data(username):
    username = username.replace('@', '').lower()
    url = f"https://www.tiktok.com/@{username}"
    
    # قائمة رؤوس متغيرة لتجنب كشف البوت
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }

    print(f"[*] Ahmed's Engine is Deep Scanning: @{username}...")
    
    try:
        session = requests.Session()
        res = session.get(url, headers=headers, timeout=15)
        
        if res.status_code == 200:
            html = res.text
            
            # 1. جلب الـ ID بذكاء (أنماط متعددة)
            uid = "Not Found"
            id_patterns = [r'\"userId\":\"(\d+)\"', r'\"id\":\"(\d+)\"', r'authorId\":\"(\d+)\"']
            for pattern in id_patterns:
                match = re.search(pattern, html)
                if match:
                    uid = match.group(1)
                    break
            
            # 2. تاريخ الإنشاء (تحسين الحساب)
            c_date = "N/A"
            if uid != "Not Found":
                try:
                    ts = int(bin(int(uid))[2:33], 2)
                    c_date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                except: pass

            # 3. المنطقة (Region)
            reg = re.search(r'\"region\":\"([A-Z]{2})\"', html)
            region = reg.group(1) if reg else "N/A"

            # 4. السيرة الذاتية (Bio) - ميزة جديدة
            bio_match = re.search(r'\"signature\":\"(.*?)\"', html)
            bio = bio_match.group(1).encode().decode('unicode-escape') if bio_match else "No Bio"

            # 5. صيد الإيميلات (تحسين الفلترة)
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))

            # --- عرض النتائج الاحترافية ---
            print(f"\n\033[1;32m[✔] Deep Scan Results:\033[0m")
            print(f"─" * 45)
            print(f"\033[1;37m👤 User:       \033[1;34m@{username}\033[0m")
            print(f"\033[1;37m🆔 ID:         \033[1;36m{uid}\033[0m")
            print(f"\033[1;37m📅 Created:    \033[1;36m{c_date}\033[0m")
            print(f"\033[1;37m🌍 Region:     \033[1;31m{region}\033[0m")
            print(f"\033[1;37m📝 Bio:        \033[1;32m{bio}\033[0m")
            print(f"\033[1;37m📧 Emails:     \033[1;33m{', '.join(emails) if emails else 'Private'}\033[0m")
            print(f"─" * 45)
            
        else:
            print(f"\033[1;31m[-] TikTok blocked the request (Status: {res.status_code})\033[0m")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    banner()
    get_data(input("Enter Target Username: "))
    
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
