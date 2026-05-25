import requests
import random
import string
import time
import sys
import threading
from cfonts import render
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

RED = "\033[1m\033[31m"
GREEN = "\033[1m\033[32m"
YELLOW = "\033[1m\033[33m"
BLUE = "\033[1m\033[34m"
CYAN = "\033[1m\033[36m"
MAGENTA = "\033[1m\033[35m"
WHITE = "\033[1m\033[37m"
ORANGE = "\033[1m\033[38;5;208m"
RESET = "\033[0m"

AthexPy = render('AX X', colors=['white', 'red'], align='center')
AthexPy2 = render('SVRCORN', colors=['white', 'red'], align='center')

print("—" * 60)
print(AthexPy)
print(AthexPy2)
print("—" * 60)
print(f"\033[91m   ✦ 𝐓ᴏᴏʟ 𝐁ʏ ➜ @athexogu | @c0dewithamn ✦  {RESET}")
print("—" * 60)

class athex:
    def __init__(self):
        self.token = input(f"\033[96m  • 𝐓ᴏᴋᴇɴ  ➜  \033[1m\033[32m")
        self.id = input(f"\033[96m  • 𝐈𝐃  ➜  \033[1m\033[32m") 

        self.domains = ['@hi2.in', '@telegmail.com']
        self.hits = 0  
        self.bad_insta = 0  
        self.bad_email = 0  
        self.capsolve = 0  

        self.lock = threading.Lock()
        self.running = True
        
        # FIX: Create session here
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def update_stats(self):
        with self.lock:
            status = f"  \033[92mHits\033[0m: {self.hits} // \033[91mBad İnsta\033[0m: {self.bad_insta} // \033[95mBad hi2in\033[0m: {self.bad_email} \r "
            sys.stdout.write(status)
            sys.stdout.flush()

    def send_telegram(self, message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            'chat_id': self.id,
            'text': message,
            'parse_mode': 'HTML'
        }
        try:
            self.session.post(url, data=payload, timeout=10)
        except:
            pass

    def solve_recaptcha(self):
        try:
            anchor_url = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct&co=aHR0cHM6Ly9oaTIuaW46NDQz&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=invisible"
            params = anchor_url.split('?')[1]
            r = self.session.get(f'https://www.google.com/recaptcha/enterprise/anchor?{params}', timeout=67)
            token = r.text.split('recaptcha-token" value="')[1].split('"')[0]

            payload = {
                'v': params.split('v=')[1].split('&')[0],
                'reason': 'q',
                'c': token,
                'k': "6LfEUPkgAAAAAKTgbMoewQkWBEQhO2VPL4QviKct",
                'co': "aHR0cHM6Ly9oaTIuaW46NDQz",
                'hl': 'en',
                'size': 'invisible'
            }

            headers = {
                "User-Agent": "Mozilla/5.0",
                "Referer": f"https://www.google.com/recaptcha/enterprise/anchor?{params}",
                "Content-Type": "application/x-www-form-urlencoded"
            }

            resp = self.session.post('https://www.google.com/recaptcha/enterprise/reload', data=payload, headers=headers, timeout=67)
            captcha_token = resp.text.split('resp","')[1].split('"')[0]

            with self.lock:
                self.capsolve += 1
            return captcha_token
        except Exception as e:
            return None

    def check_instagram_email(self, email):
        try:
            url = "https://i.instagram.com/api/v1/users/check_email/"

            with httpx.Client(http2=True, timeout=30) as client:
                response = client.post(
                    url, 
                    data=f"email={email}",
                    headers={
                        'User-Agent': "Instagram 166.0.0.30.120 Android (30/11; 1440dpi; 2560x1440; samsung; SM-G973F; x86_64; tablet; en_US; kirin)",
                        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
                    }
                )

            result = response.json()

            if result.get("available") == False or result.get("taken") == True:
                return True
            else:
                return False

        except Exception as e:
            return False

    def check_email_availability(self, username, domain):
        if "@" in username:
            username = username.split("@")[0]

        solve = self.solve_recaptcha()
        if not solve:
            return False

        data = {
            'domain': domain,
            'prefix': username,
            'recaptcha': solve,
        }

        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Content-Type': "application/x-www-form-urlencoded",
            'authorization': "Basic bnVsbA==",
        }

        try:
            response = self.session.post("https://hi2.in/api/custom", data=data, headers=headers, timeout=30)
            if 'address already taken' in response.text:
                return False
            else:
                return True
        except:
            return False

    def worker(self):
        while self.running:
            abc = 'qwertyuioplkjhgfdsazxcvbnm'
            name = ''.join(random.choice(abc) for _ in range(random.randrange(6, 7)))

            for domain in self.domains:
                email_available = self.check_email_availability(name, domain)

                if email_available:
                    email_full = name + domain
                    insta_available = self.check_instagram_email(email_full)

                    if insta_available:
                        with self.lock:
                            self.hits += 1
                            with open('athexighits.txt', 'a') as f:
                                f.write(email_full + '\n')
                            self.send_telegram(f"""
╔══════════════════════╗
      ✦  AX  x  SVRCORN  ✦
╠══════════════════════╣
• Hits: {self.hits}
• Email: {email_full}
╚══════════════════════╝
TOOL BY -  @oguport | @c0dewithamn
""")
                    else:
                        with self.lock:
                            self.bad_insta += 1
                else:
                    with self.lock:
                        self.bad_email += 1

                self.update_stats()
                time.sleep(random.uniform(0.3, 0.7))

            time.sleep(random.uniform(0.2, 0.5))

    def start(self):
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.worker) for _ in range(10)]
            try:
                for future in as_completed(futures):
                    future.result()
            except KeyboardInterrupt:
                self.running = False
                for future in futures:
                    future.cancel()

if __name__ == "__main__":
    checker = athex()
    checker.start()