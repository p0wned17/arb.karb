import undetected_chromedriver.v2 as uc
import time
from fake_useragent import UserAgent
import requests
ua = UserAgent()
session = requests.Session()
# proxy_options = {
#     "proxy": {
#         "https": f"http://kbKX7z:XgHM45@138.128.91.65:8000"
#     }
# }
# driver = uc.Chrome(executable_path=r'C:\Games\chromedriver.exe', use_subprocess=True)
# with driver:
#     driver.get('https://kad.arbitr.ru/Card/efaa8b67-873c-4d87-b6c7-7ac046bfe30d')
# time.sleep(10)
# cooks = driver.get_cookies()
# for cookie in cooks:
#     session.cookies.set(cookie['name'], cookie['value'])
# driver.close()
# driver.quit()
data = {
        'RecaptchaToken': 'undefined',
    }
cookies = {
    'notShowTooltip': 'yes',
    '__ddg1_': '8Fbu5Yuq3ufPes4SfNvp',
    'CUID': '893ad8ce-f21d-4701-b185-2def7dc8324a:NIKMOxQtGvWBrlOpbwQKkw==',
    '__ddgid_': 'WMHxjW8DYsxPHYf1',
    '__ddgmark_': 'x9N49h3Cm77idB61',
    '__ddg5_': 'NDlxXj1tPo9XCdLz',
    'ASP.NET_SessionId': 'boere0se4xjh2u00mtkmgmgn',
    'pr_fp': '049b8694888c6464fad6fefdc86a40ab6e8260df3ee7345af505ab2f799caad8',
    '__ddg2_': 'U62c46jJzAqB58Xr',
    'rcid': 'aabd971d-4d16-483f-8f79-e94b4bd209fc',
    'Notification_All': '935883f98a834dcc92e951cd3916f45b_1659966300000_shown',
    '_ga': 'GA1.2.990540912.1657744267',
    '_gid': 'GA1.2.382787254.1657744267',
    'tmr_lvid': '35ccbf60cd814ca42be80668be0d2e49',
    'tmr_lvidTS': '1657744267319',
    '_ym_uid': '16577442671001805050',
    '_ym_d': '1657744267',
    '_ym_isad': '1',
    'KadLVCards': '%d0%9076-23426%2f2022',
    'tmr_detect': '1%7C1657744616769',
    'wasm': 'd24589feacaa819858fbdf43519485a6',
    'tmr_reqNum': '353',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': ua.random,  # Заголовок браузера
    # Типы контента, которые клиент может получить
    'Accept-Language': 'en-US,en;q=0.5',  # Браузер приемлемых языков
    'Connection': 'keep-alive',  # Указывает, требуется ли постоянное соединение
}
params = {
        'id': '15cc182b-0c0a-4b7e-9ba4-3a16366080a3',
        'caseId': "7f78d02e-0d8a-4a6e-a60f-82535b810ead",
        'withProtocols': 'true',
        'perPage': '30',
        'page': '1',
    }
session.cookies.clear()
response = requests.post('https://kad.arbitr.ru/Kad/InstanceDocumentsPage', params=params, headers=headers, timeout=20)
print(response.text)
session.cookies.clear()