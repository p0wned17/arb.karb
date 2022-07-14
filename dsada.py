# -*- coding: utf-8 -*-
from os import stat
from selenium import webdriver
import time
import requests
from fake_useragent import UserAgent
import pandas as pd
from bs4 import BeautifulSoup as bs4
import re
from lxml import etree
import undetected_chromedriver.v2 as uc
import random

ua = UserAgent()
session = requests.Session()

def data_to_excel(fio, adress, case_instance_number, date, statuses):
    df = pd.DataFrame({'ФИО ответчик': fio,
                    'Адрес (контакты должника)': adress,
                    'Номер дела (должника)':case_instance_number, 
                    'Арбитражный суд':'АС Челябинской области',
                    'Дата начала дела':date,
                    'Статусы дела':statuses})

    df.to_excel('./парсинг.xlsx', index=False)
    print("Сохранил в Excel")


def get_cookies():
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



def get_id(url):
    cookie = {
    'notShowTooltip': 'yes',
    '__ddg1_': '8Fbu5Yuq3ufPes4SfNvp',
    'CUID': '893ad8ce-f21d-4701-b185-2def7dc8324a:NIKMOxQtGvWBrlOpbwQKkw==',
    '__ddgid_': 'WMHxjW8DYsxPHYf1',
    '__ddgmark_': 'x9N49h3Cm77idB61',
    '__ddg2_': 'U62c46jJzAqB58Xr',
    'Notification_All': '935883f98a834dcc92e951cd3916f45b_1659966300000_shown',
    '_ga': 'GA1.2.990540912.1657744267',
    '_gid': 'GA1.2.382787254.1657744267',
    'tmr_lvid': '35ccbf60cd814ca42be80668be0d2e49',
    'tmr_lvidTS': '1657744267319',
    '_ym_d': '1657744267',
    '_ym_uid': '16577442671001805050',
    '_ym_isad': '1',
    'KadLVCards': '%d0%9076-23426%2f2022',
    'ASP.NET_SessionId': 'gourcoxnhrp5i0upmrtdbss5',
    'pr_fp': '049b8694888c6464fad6fefdc86a40ab6e8260df3ee7345af505ab2f799caad8',
    'wasm': '3f03d4ef31fd9e6c0ebee51a3c07f564',
    'rcid': '09965b4e-536b-49d1-937c-5a5b1cc402a8',
    'tmr_detect': '1%7C1657776911090',
    'tmr_reqNum': '373',
}
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
    data = {
        'RecaptchaToken': 'undefined',
    }
    response = session.post(url,cookies=cookie, headers=headers, data=data)
    html_bytes = response.text  
    soup = bs4(html_bytes, 'lxml')
    token = soup.find('input', {'class':'js-instanceId'})['value']
    case_instance_number = soup.find('div', class_ = 'r-col').find('strong').get_text()
    changed_url = re.findall("\S+\/(\S+)", url)[0]
    fio = etree.HTML(str(soup))
    try:
        fio = fio.xpath('//*[@id="gr_case_partps"]/table/tbody/tr/td[2]/div/ul/li/span/a/text()')[0].strip()
        if fio == ' ':
            fio = ' '
    except IndexError:
        fio = ' '
    return token, changed_url, fio, case_instance_number

def get_information(token, url, fio, case_instance_number):
    cookie = {
    'notShowTooltip': 'yes',
    '__ddg1_': '8Fbu5Yuq3ufPes4SfNvp',
    'CUID': '893ad8ce-f21d-4701-b185-2def7dc8324a:NIKMOxQtGvWBrlOpbwQKkw==',
    '__ddgid_': 'WMHxjW8DYsxPHYf1',
    '__ddgmark_': 'x9N49h3Cm77idB61',
    '__ddg2_': 'U62c46jJzAqB58Xr',
    'Notification_All': '935883f98a834dcc92e951cd3916f45b_1659966300000_shown',
    '_ga': 'GA1.2.990540912.1657744267',
    '_gid': 'GA1.2.382787254.1657744267',
    'tmr_lvid': '35ccbf60cd814ca42be80668be0d2e49',
    'tmr_lvidTS': '1657744267319',
    '_ym_d': '1657744267',
    '_ym_uid': '16577442671001805050',
    '_ym_isad': '1',
    'KadLVCards': '%d0%9076-23426%2f2022',
    'ASP.NET_SessionId': 'gourcoxnhrp5i0upmrtdbss5',
    'pr_fp': '049b8694888c6464fad6fefdc86a40ab6e8260df3ee7345af505ab2f799caad8',
    'wasm': '3f03d4ef31fd9e6c0ebee51a3c07f564',
    'rcid': '09965b4e-536b-49d1-937c-5a5b1cc402a8',
    'tmr_detect': '1%7C1657776911090',
    'tmr_reqNum': '373',
}
    params = {
        'id': f'{token}',
        'caseId': f"{url}",
        'withProtocols': 'true',
        'perPage': '30',
        'page': '1',
    }

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

    response = session.get('https://kad.arbitr.ru/Kad/InstanceDocumentsPage', cookies=cookie, params=params, headers=headers)
    print(response.text)
    data = response.json()
    date = data["Result"]["Items"][0]['DisplayDate']
    statuses = []
    fio_massiv = []
    adress_massiv = []
    for item in data["Result"]["Items"]:
        try:
            status = item['ContentTypes'][0]
            statuses.append(status)
        except:
            pass
        for adr in item['Declarers']:
            org = adr["Organization"]
            adress = adr["Address"]
            if org == fio:
                fio_massiv.append(org)
                adress_massiv.append(adress)

    return fio, adress_massiv, case_instance_number, date, statuses


if __name__ == '__main__':
    data = ["https://kad.arbitr.ru/Card/7f78d02e-0d8a-4a6e-a60f-82535b810ead", "https://kad.arbitr.ru/Card/02e74c09-932e-4cf7-994a-6128df7cc3d5", "https://kad.arbitr.ru/Card/64d084ee-05c5-432b-a6bc-87f5696456e9", "https://kad.arbitr.ru/Card/147fb907-4540-4b22-8aff-66ab952e8a2e", "https://kad.arbitr.ru/Card/2c463175-f7b7-4776-acb4-ec2e5f21f38a", "https://kad.arbitr.ru/Card/ef7e4013-dcfe-4f5a-97e9-7c3ef685a681", "https://kad.arbitr.ru/Card/07404b2e-46d3-4bf8-8453-f4d8cff13884", "https://kad.arbitr.ru/Card/241f5887-3628-4ea8-bb33-082c1589d50d", "https://kad.arbitr.ru/Card/039f1e67-11de-4a47-a8fc-f0446f4cae18", "https://kad.arbitr.ru/Card/fd157872-19af-402d-92db-4e48614acbd8", "https://kad.arbitr.ru/Card/2e130dfd-2ea4-433d-9553-4fe15f6caf56", "https://kad.arbitr.ru/Card/20c677a4-5fe6-4a5c-bdba-85fe3896ab38", "https://kad.arbitr.ru/Card/f747e0c4-16ef-49bb-bf0f-70d3db08b97f", "https://kad.arbitr.ru/Card/ac9ad50e-c079-4553-9dbd-f9fbc75b65d4", "https://kad.arbitr.ru/Card/820664dd-933b-4120-9350-fef0c2392a0f", "https://kad.arbitr.ru/Card/597fc894-4c82-4c54-b5fe-0a4475e24910", "https://kad.arbitr.ru/Card/ebf106e4-da69-4746-9984-48b53c7e5e69", "https://kad.arbitr.ru/Card/f650a2a3-2b0a-413e-9017-a75c4c8d6983", "https://kad.arbitr.ru/Card/b3b526e3-d23a-427f-9ecf-cf54988e25bf", "https://kad.arbitr.ru/Card/9d6c66c0-046f-4a0d-9a8b-d782e91d4035", "https://kad.arbitr.ru/Card/e0e586d5-188e-47dc-97e7-3612b2f7d40c", "https://kad.arbitr.ru/Card/34d87dc3-93eb-4135-975e-1a2bb72cc27c", "https://kad.arbitr.ru/Card/d48f6480-b703-4131-a2f0-4655313e52d0", "https://kad.arbitr.ru/Card/a8d3fa0f-e650-4bf9-81f6-e87ae56b3b41", "https://kad.arbitr.ru/Card/ec209394-db8c-44f3-a4dd-defed68fbeff", "https://kad.arbitr.ru/Card/307feca2-9666-4a8a-8dbe-ebbd6dcd36c6", "https://kad.arbitr.ru/Card/2159ce0c-b704-4b6f-9845-15cf216c94ba", "https://kad.arbitr.ru/Card/8aa3314b-2eaa-4258-9cb3-6b9ef59e09aa", "https://kad.arbitr.ru/Card/d4c10d99-77a7-4db8-9c46-193a50edb48c", "https://kad.arbitr.ru/Card/9e2bde0b-8ab2-4a97-afb0-d5e9bf0381f2", "https://kad.arbitr.ru/Card/b7a2b1d9-ba43-4c87-bb75-49f585da1151", "https://kad.arbitr.ru/Card/f6f8b158-839f-4532-a9bd-a458032043a2", "https://kad.arbitr.ru/Card/95cc0113-4f36-44b6-a2c2-483dc4ec25cd", "https://kad.arbitr.ru/Card/5c4959ee-a48d-4a3c-a9b1-edc3017f0d9e", "https://kad.arbitr.ru/Card/32ea111a-55be-45c8-9183-4f0df31d40c1", "https://kad.arbitr.ru/Card/cc290e98-0864-455e-9a95-ccc98727a061", "https://kad.arbitr.ru/Card/6a70445e-ff25-46da-9860-0a8d6cd04597", "https://kad.arbitr.ru/Card/f6b0bdf8-ad2b-4e0d-880d-1ed3163ab277", "https://kad.arbitr.ru/Card/fe6b9e1f-9c72-4bc1-b707-3a03a39f5a3a", "https://kad.arbitr.ru/Card/68ac8b52-4504-477c-ae93-25770fb10baa", "https://kad.arbitr.ru/Card/2a4dc4b0-4309-4718-8018-2106ad93393c", "https://kad.arbitr.ru/Card/6839ef76-3fa6-46b7-a893-4100c816cd7d", "https://kad.arbitr.ru/Card/aded2ee2-8218-4fce-95d4-2c36f65f2a95", "https://kad.arbitr.ru/Card/0bd31e11-c76a-468a-8545-51bfebc53863", "https://kad.arbitr.ru/Card/3d259c65-edc2-4ae5-a46c-ae17b0cdf19b", "https://kad.arbitr.ru/Card/e8cfb6ba-e715-4b80-b055-3151af964934", "https://kad.arbitr.ru/Card/a4e426b5-b01d-4537-9afd-51dfa50c2e58", "https://kad.arbitr.ru/Card/6ef71118-b696-42d9-83d6-06a28376acbf", "https://kad.arbitr.ru/Card/0eb0e9c4-8a70-4cfd-99ec-2336ca23cf0f", "https://kad.arbitr.ru/Card/b32fb7f1-d285-4b74-a50d-028335f8c98c", "https://kad.arbitr.ru/Card/e31a3c39-8d7e-46e3-a08e-a49dfe48c199", "https://kad.arbitr.ru/Card/84ef2927-d125-4052-ab3e-ab4c2a35dd59", "https://kad.arbitr.ru/Card/e7d2c169-89f8-4946-a886-7f3b5760b7b7", "https://kad.arbitr.ru/Card/f63d43df-7f10-4ca9-bd8b-a36c79776a28", "https://kad.arbitr.ru/Card/622820df-4f24-4fdd-8fba-978d76b9d94f", "https://kad.arbitr.ru/Card/aad8e0e7-83cd-4255-b8a1-b3f983010119", "https://kad.arbitr.ru/Card/f083c3e0-61cb-4549-8e11-77aa13f2647d", "https://kad.arbitr.ru/Card/65482a59-62de-4ab4-b15b-38c82173ee8d", "https://kad.arbitr.ru/Card/965e00ab-3ce1-4f8d-842b-aaf40a55d47a", "https://kad.arbitr.ru/Card/9b193ee7-43e9-4069-8f34-ee9ee6340a41", "https://kad.arbitr.ru/Card/72603b34-8bfd-44b7-bd87-a4b985226d79", "https://kad.arbitr.ru/Card/28711522-82c8-4013-89d3-01b767f986ba", "https://kad.arbitr.ru/Card/c4b121d6-c119-4f19-bc86-acc80f9f8e65", "https://kad.arbitr.ru/Card/26036007-6f1c-4733-830d-3489e3adad4a", "https://kad.arbitr.ru/Card/a4f11cf3-7623-4137-892b-01b824319ed2", "https://kad.arbitr.ru/Card/e3c57e9c-7607-4ceb-8c4a-3dbc9e3a970b", "https://kad.arbitr.ru/Card/266bfb96-53a8-4fed-8e00-9b13c6546ad5", "https://kad.arbitr.ru/Card/936db133-d184-4402-8dd5-447b35c88095", "https://kad.arbitr.ru/Card/b7c9217c-7256-4491-80a5-3a7c625e210e", "https://kad.arbitr.ru/Card/5c23356e-b197-4edf-aad7-60201d5c7763", "https://kad.arbitr.ru/Card/374c947a-b384-40a1-b4f8-2e68b9d0ffe3", "https://kad.arbitr.ru/Card/e0f74637-ceeb-4fb9-b36d-be48e5967104", "https://kad.arbitr.ru/Card/8d2bfc19-0991-4721-adb6-30cf8084aa6d", "https://kad.arbitr.ru/Card/8794529d-c7fb-4a21-afe1-e0c118d02823", "https://kad.arbitr.ru/Card/0db8b6d5-0625-406a-932d-2fcdf7c0b517", "https://kad.arbitr.ru/Card/7be74fa1-921c-4c50-a40a-80808988a4e8", "https://kad.arbitr.ru/Card/eed4c367-1ae8-4b91-b9da-27b3d25d1089", "https://kad.arbitr.ru/Card/12c8dde6-769a-404d-b355-4c33d2af688b", "https://kad.arbitr.ru/Card/1411df77-61eb-434a-a675-e28f3ab1e940", "https://kad.arbitr.ru/Card/2508a42c-54e3-45da-9c7f-637fc1af37f4", "https://kad.arbitr.ru/Card/4d3f0845-f2aa-44f7-b354-681b6ee1336a", "https://kad.arbitr.ru/Card/9693981c-1111-4272-97e0-6200ff6afd0b", "https://kad.arbitr.ru/Card/fa17dbf3-c16d-4b78-85a3-f2034df827ba", "https://kad.arbitr.ru/Card/ce14fdcd-71f8-4d00-8791-980f8e632d70", "https://kad.arbitr.ru/Card/598d68b2-5f49-43c1-8cef-7510ca929bfa", "https://kad.arbitr.ru/Card/06d99979-5d1a-4f96-bf23-b45547aa1777", "https://kad.arbitr.ru/Card/88c8f418-986c-4237-8983-9bb4a72d33a6", "https://kad.arbitr.ru/Card/69c1816a-b822-4d23-b538-b6d09c468df4", "https://kad.arbitr.ru/Card/ea2050e7-76ea-44d4-a42c-c93c2a818e9c", "https://kad.arbitr.ru/Card/23d17b3a-f3b8-4996-a7c9-ae18a3dafc93", "https://kad.arbitr.ru/Card/5a0f9fb1-d87f-452d-865a-8fe408c782bf", "https://kad.arbitr.ru/Card/90bc82fe-cfa9-4396-af5a-e3813133c3e4", "https://kad.arbitr.ru/Card/d2d322bf-1677-4faa-bf65-d1250bcdde72", "https://kad.arbitr.ru/Card/7d729c9b-0816-4a73-8949-e0aadfcb8a01", "https://kad.arbitr.ru/Card/a0086acc-5082-4d3f-af06-b263cbd3c665", "https://kad.arbitr.ru/Card/1916beac-b39c-4b01-8b81-3298452fd613", "https://kad.arbitr.ru/Card/78723b9a-d2c9-4a5d-94b7-68a625c781be", "https://kad.arbitr.ru/Card/74dc53bb-6d8a-4aa5-a78a-5c04a3b9e803", "https://kad.arbitr.ru/Card/5f4d8954-660c-437f-b679-0ebcbdb555d0"]
    fio_massiv = []
    adress_massiv = []
    case_instance_number_massiv = [] 
    date_massiv = []
    statuses_massiv = []
    schetchik = 0
    get_cookies()
    for item in data:
        schetchik += 1 
        print(item)
        token, changed_url, fio, case_instance_number = get_id(item)
        fio, adress, case_instance_number, date, statuses = get_information(token, changed_url, fio, case_instance_number)
        if bool(adress) is False:
            adress = ' '
        else:
            adress = adress[0]
        fio_massiv.append(fio)
        adress_massiv.append(adress)
        case_instance_number_massiv.append(case_instance_number)
        date_massiv.append(date)
        statuses_massiv.append(statuses)
    data_to_excel(fio_massiv, adress_massiv, case_instance_number_massiv, date_massiv, statuses_massiv)
