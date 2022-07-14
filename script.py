import requests
import time
from seleniumwire import webdriver
import os
from fake_useragent import UserAgent
headers = {
    'authority': 'kad.arbitr.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'notShowTooltip=yes; __ddg1_=1SePSG189ln42ZQnS84b; CUID=e3c1146e-05d3-4250-b31c-2129ee36defa:FJt1vnOSIf5lmePhOHPMQQ==; _ga=GA1.2.950544848.1655812397; _ym_d=1655812397; _ym_uid=1655812397485536061; tmr_lvid=ecfa4852c231b85cc7b696ad863229f9; tmr_lvidTS=1655812397447; __ddgid_=8Jl1DGS4WhPxVq7n; __ddg2_=ckZz5z7MEPL8LBGc; ASP.NET_SessionId=0bhnubkmmh4mfsm4s5mcq51d; _gid=GA1.2.1018585093.1657547161; Notification_All=935883f98a834dcc92e951cd3916f45b_1659966300000_shown; pr_fp=1ddd817c2811120a6a255890dd91934b67a744c375c0d7bfb022863cbca1326d; _ym_isad=1; KadLVCards=%d0%9076-322%2f2022~%d0%9076-316%2f2022~%d0%9076-318%2f2022~%d0%9076-2542%2f2022~%d0%9076-2539%2f2022; wasm=ed782b1b863e7101fd813801a9cbf0d4; rcid=68fe3224-84ea-4ef3-86ac-fc92e44e1cfe; tmr_detect=1%7C1657706185379; _gat=1; _gat_FrontEndTracker=1; _dc_gtm_UA-157906562-1=1; tmr_reqNum=275',
    'origin': 'https://kad.arbitr.ru',
    'referer': 'https://kad.arbitr.ru/Card/17345995-a2a3-422b-9cf2-a38ba4112b73',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36',
}

session = requests.Session()
ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"user-agent={ua.random}")
driver = webdriver.Chrome(
    executable_path="C:\Games\chromedriver.exe", options=options
)
driver.get("https://kad.arbitr.ru/Card/6c297508-0d77-458e-9b33-c4de0d9d75e8")

time.sleep(5)

driver.refresh()

time.sleep(10)

data = {
        'RecaptchaToken': 'undefined',
    }

cooks = driver.get_cookies()
for cookie in cooks:
    session.cookies.set(cookie['name'], cookie['value'])
driver.close()
driver.quit()

response = session.post("https://kad.arbitr.ru/Card/17345995-a2a3-422b-9cf2-a38ba4112b73", headers=headers, data=data)

print(response.text)