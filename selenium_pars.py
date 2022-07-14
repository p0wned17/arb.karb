# -*- coding: utf-8 -*-
from nturl2path import url2pathname
from os import stat
from seleniumwire import webdriver
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
    options.add_argument("--start-maximized")
    options_seleniumWire = {
    'proxy': {
        'https': f'https://sxlJnnlVou:UlSch0Kc4E@51.15.15.230:',
    }
}
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
    print(url)
    proxy = 'http://sxlJnnlVou:UlSch0Kc4E@51.15.15.230:9035'
    response = session.post(url, headers=headers, data=data, timeout=20)
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
    params = {
        'id': f'{token}',
        'caseId': f"{url}",
        'withProtocols': 'true',
        'perPage': '30',
        'page': '1',
    }
    headers = {
    'authority': 'kad.arbitr.ru',
    'accept': 'application/json, text/javascript, */*',
    'accept-language': 'ru,en;q=0.9',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__ddg1_=8Fbu5Yuq3ufPes4SfNvp; CUID=893ad8ce-f21d-4701-b185-2def7dc8324a:NIKMOxQtGvWBrlOpbwQKkw==; __ddgid_=WMHxjW8DYsxPHYf1; __ddgmark_=x9N49h3Cm77idB61; __ddg2_=U62c46jJzAqB58Xr; Notification_All=935883f98a834dcc92e951cd3916f45b_1659966300000_shown; _ga=GA1.2.990540912.1657744267; _gid=GA1.2.382787254.1657744267; tmr_lvid=35ccbf60cd814ca42be80668be0d2e49; tmr_lvidTS=1657744267319; _ym_d=1657744267; _ym_uid=16577442671001805050; _ym_isad=1; ASP.NET_SessionId=gourcoxnhrp5i0upmrtdbss5; pr_fp=049b8694888c6464fad6fefdc86a40ab6e8260df3ee7345af505ab2f799caad8; KadLVCards=%d0%9076-9400%2f2022~%d0%9076-23426%2f2022; rcid=d2f329c9-9614-4763-a850-0664f1b1e70a; tmr_detect=1%7C1657777376675; tmr_reqNum=381; wasm=01addbe0268b10747c07e3121fae6f5d',
    'referer': 'https://kad.arbitr.ru/Card/7f78d02e-0d8a-4a6e-a60f-82535b810ead',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
    proxy = 'http://sxlJnnlVou:UlSch0Kc4E@51.15.15.230:9035'
    response = session.post('https://kad.arbitr.ru/Kad/InstanceDocumentsPage', params=params, headers=headers)
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
    data = ["https://kad.arbitr.ru/Card/2ee0cd2f-1292-4ccd-86e9-aa0cad74c621", "https://kad.arbitr.ru/Card/db8c719a-b981-4b80-937c-9820e65f98eb", "https://kad.arbitr.ru/Card/93c99ca0-8f93-4bed-ad22-77ec679d5cd5", "https://kad.arbitr.ru/Card/4b87eb09-60c5-42b6-aaa4-c69fa503de57", "https://kad.arbitr.ru/Card/8158a334-9d21-4f05-8661-d36e3bbcfd37", "https://kad.arbitr.ru/Card/92f4eb80-3160-4f6c-adc1-2be3c1c84252", "https://kad.arbitr.ru/Card/91c07541-19ee-485b-bbfd-23e8f081295f", "https://kad.arbitr.ru/Card/b15637ea-00a8-4c6e-825a-689546516ca8", "https://kad.arbitr.ru/Card/888d0f71-2af2-45ff-87fa-272a81198c07", "https://kad.arbitr.ru/Card/01daf779-a84c-427a-b8e8-acf90d556d9d", "https://kad.arbitr.ru/Card/ada7b56c-1419-431d-a816-1cd13111d819", "https://kad.arbitr.ru/Card/033ced61-696b-42f4-a26c-f1d6fefadbe4", "https://kad.arbitr.ru/Card/506e12b4-ef4d-4170-95a5-2e2f16b27f5b", "https://kad.arbitr.ru/Card/f35b8806-3ca0-49cc-89fc-ddad668cd9a0", "https://kad.arbitr.ru/Card/6b384fac-3d94-4548-9e30-ac61dee263d1", "https://kad.arbitr.ru/Card/a5f6941f-0eb7-4356-a4d4-67f94abea809", "https://kad.arbitr.ru/Card/3995a00f-2397-4705-8229-b2cfbf486adf", "https://kad.arbitr.ru/Card/f9108278-bc27-4b30-b0ae-8ad41eed0241", "https://kad.arbitr.ru/Card/fef43af8-49ac-4072-8c3b-c4adec2d2743", "https://kad.arbitr.ru/Card/8b8d47eb-aeb4-4f4d-b276-605eb2975320", "https://kad.arbitr.ru/Card/27dd4243-6271-45e2-9321-345092bc98bc", "https://kad.arbitr.ru/Card/6d864ad8-474e-4a16-800e-93c691f25ff0", "https://kad.arbitr.ru/Card/bf899221-7e6c-48a5-9c07-67d43223619a", "https://kad.arbitr.ru/Card/03cce985-c6e2-4840-a465-c71cd7fc3269", "https://kad.arbitr.ru/Card/925de67c-4c03-420f-b6bd-fa91474dcd7f", "https://kad.arbitr.ru/Card/e7a004a4-e6fc-42e5-aa2d-b09ec6a41c40", "https://kad.arbitr.ru/Card/75b52450-c31b-4214-80c6-a3cb01787f88", "https://kad.arbitr.ru/Card/ee4f68f9-a14a-4949-8bfe-ff0367063ab3", "https://kad.arbitr.ru/Card/528a65f8-2dcb-4b9e-a253-2344edfde79f", "https://kad.arbitr.ru/Card/55f3ec10-13a5-4b8d-bc11-ef114d9a5fc1", "https://kad.arbitr.ru/Card/11ec90c4-7a6b-4ba1-b446-7791020a0adf", "https://kad.arbitr.ru/Card/fe760624-2c45-49c4-9c75-556c65949afd", "https://kad.arbitr.ru/Card/a4b900ae-a3fa-4c91-b36e-6a52fd2e1e5b", "https://kad.arbitr.ru/Card/7694da3e-b207-4f74-94fd-f890632bf59c", "https://kad.arbitr.ru/Card/7a808c82-d827-436f-9397-28297a0fb2d3", "https://kad.arbitr.ru/Card/bc8425ad-35a1-4c8a-91d2-2bed33eb55aa", "https://kad.arbitr.ru/Card/93dd7b48-c0b8-41e5-9468-36eb4b1d80f1", "https://kad.arbitr.ru/Card/4d7312b3-c33b-488e-bf13-95e82845e41b", "https://kad.arbitr.ru/Card/a9c5081b-8fda-4624-9063-80cf3106db7f", "https://kad.arbitr.ru/Card/caf68398-505d-4b18-a1dd-cbc51c9ab0f1", "https://kad.arbitr.ru/Card/6a06a246-4cff-4795-a7b1-c3832090954e", "https://kad.arbitr.ru/Card/c34b13ed-1e2e-4c4b-b6b4-eb821d47f862", "https://kad.arbitr.ru/Card/6bc422be-def9-4d6c-ab0c-24b9cfaeed06", "https://kad.arbitr.ru/Card/ce50d3ce-281b-4e59-a202-811037443916", "https://kad.arbitr.ru/Card/972fc4b6-70b4-4c78-98eb-1a4ffb5b925e", "https://kad.arbitr.ru/Card/f4ad7b27-8636-4fae-87d4-bb2fcb7f606f", "https://kad.arbitr.ru/Card/620daa3e-10d0-4b63-8076-7c99e5d836c1", "https://kad.arbitr.ru/Card/d06fb41f-0f8a-4d8f-b2c5-fdf261395e59", "https://kad.arbitr.ru/Card/f98dd975-5bdd-468e-8726-81d3e796d10c", "https://kad.arbitr.ru/Card/18c82790-b098-4e18-aa74-8b3ef1d5178b", "https://kad.arbitr.ru/Card/af332de6-2891-478f-92ca-9d1683ea18f6", "https://kad.arbitr.ru/Card/afeda939-2fec-49a3-ab84-8cf41956c1c6", "https://kad.arbitr.ru/Card/a94d55aa-71a3-4cf4-8ccd-9983478ef1ad", "https://kad.arbitr.ru/Card/9c35ed48-ea4c-4be7-9922-0a851af1cd68", "https://kad.arbitr.ru/Card/d8090660-3390-48fa-852e-028c124d24ce", "https://kad.arbitr.ru/Card/3eed94a0-4f3f-4f8d-9cef-1f4159ee5a01", "https://kad.arbitr.ru/Card/69e66fd6-e2e1-4f74-9225-971e1683b474", "https://kad.arbitr.ru/Card/b5e39074-ca9c-4598-9014-9f6b243d70dd", "https://kad.arbitr.ru/Card/807340e7-2629-429a-b1ca-725a326e9508", "https://kad.arbitr.ru/Card/606bc151-5c5f-400a-8570-0895b7996c3f", "https://kad.arbitr.ru/Card/7a7541b3-4d62-421b-95c4-752963482ae5", "https://kad.arbitr.ru/Card/934db546-03f3-4660-9854-b8f6d7561029", "https://kad.arbitr.ru/Card/8199f938-3d51-4e48-8159-3d638bc0682b", "https://kad.arbitr.ru/Card/a2bc44be-efa7-4d4e-8ebc-33d4d29ff14c", "https://kad.arbitr.ru/Card/1aadd6f6-6d94-4e5e-ab5a-aebf0557c74e", "https://kad.arbitr.ru/Card/5e2f5a2a-cac1-4170-b4b9-69d8ba3ecb46", "https://kad.arbitr.ru/Card/739b7f3f-1fe1-4faf-a1c5-aa6cf572896b", "https://kad.arbitr.ru/Card/47e0d5cc-9361-417a-946b-a0ab6f088f23", "https://kad.arbitr.ru/Card/b6e0f9d8-f18d-4b80-95f7-2cdea1b58ed0", "https://kad.arbitr.ru/Card/9bfeadaf-2181-4b92-a359-9d2a62608f8f", "https://kad.arbitr.ru/Card/8e2b1dae-e09e-4433-bf10-3226fc3be781", "https://kad.arbitr.ru/Card/90aa1d0c-87f3-41c8-9e50-391f9c292a40", "https://kad.arbitr.ru/Card/3020205b-b7c4-4b87-a5aa-e8b537f78ec4", "https://kad.arbitr.ru/Card/1b4ba069-b49b-4f6a-be6d-893988a3f490", "https://kad.arbitr.ru/Card/ca05d0ba-221c-436e-b9e4-fa6adb9e3f0a", "https://kad.arbitr.ru/Card/add4fc94-71ca-44a2-a4fa-22c3dc9252d4", "https://kad.arbitr.ru/Card/8d1299f4-9c08-4c4b-bcc2-bec396e53e1d", "https://kad.arbitr.ru/Card/eae57711-1426-4b21-88fd-88c2cb56eef6", "https://kad.arbitr.ru/Card/6b2e041e-8721-4db8-bdd6-c2256e8a735c", "https://kad.arbitr.ru/Card/e73c95c8-3c61-4969-a3fd-90e18f06a0b5", "https://kad.arbitr.ru/Card/685f7085-d222-4ec8-ba93-4cfc07d57140", "https://kad.arbitr.ru/Card/8b276c66-caea-4770-810d-6daa554808db", "https://kad.arbitr.ru/Card/b529c23c-e3bc-4728-9ca5-9926b3883a08", "https://kad.arbitr.ru/Card/85adf471-9178-4850-af1f-f40dd3bf1471", "https://kad.arbitr.ru/Card/20c091d2-217b-4e7c-b868-80b6dd8b6f6e", "https://kad.arbitr.ru/Card/a1abdb57-ec93-4c3b-a1c7-a9b87bcda392", "https://kad.arbitr.ru/Card/14d43c6b-6779-4eb0-bd5a-a0b6e36ba511", "https://kad.arbitr.ru/Card/9f3fc6e9-1260-433d-bdc3-cad4e4ce19bd", "https://kad.arbitr.ru/Card/abb4ae8e-bc8f-4f7d-b6bc-c701bd5c0bb5", "https://kad.arbitr.ru/Card/9d08ba4e-adeb-4245-84a1-c1d45c8d2afd", "https://kad.arbitr.ru/Card/9053d280-152b-4e8d-a9dc-4788487c2953", "https://kad.arbitr.ru/Card/e0e7d1fa-1de8-4861-aebd-a6242c4ecb74", "https://kad.arbitr.ru/Card/ffc611b8-e984-40ac-a8b0-0665f31495f0", "https://kad.arbitr.ru/Card/712820dd-8401-471b-9fd4-d8dfc97cf80f", "https://kad.arbitr.ru/Card/99cbef6f-3e34-40ac-b996-90d6d095f827", "https://kad.arbitr.ru/Card/fb112644-eef8-4199-8e2a-249ab956e8b2", "https://kad.arbitr.ru/Card/e451ba76-3af9-4fd7-b025-302f102afcfa", "https://kad.arbitr.ru/Card/f36faad1-e9e6-4625-bef3-f53c61766539", "https://kad.arbitr.ru/Card/ac089fd7-e474-4a73-8074-76f6cf5c333a", "https://kad.arbitr.ru/Card/c12f27fc-f51e-4434-8da0-4787bbde9e06", "https://kad.arbitr.ru/Card/fc312f14-63a2-4990-8280-344b23622c59", "https://kad.arbitr.ru/Card/10fd1a31-b137-4033-b252-c837b30421be", "https://kad.arbitr.ru/Card/fac0645d-1edd-4642-8599-ea615db37e0f", "https://kad.arbitr.ru/Card/311ff53f-d892-4335-87cc-94491670d4dd", "https://kad.arbitr.ru/Card/9dc227fc-dc67-46bd-96da-09488acb1092", "https://kad.arbitr.ru/Card/5040d1e0-35c0-43dc-8b5d-d176320348ef", "https://kad.arbitr.ru/Card/7f22fcb7-868f-4efc-a126-6ee92f42d5c6", "https://kad.arbitr.ru/Card/5f4248cb-c702-4a20-9fae-fa4847e397bf", "https://kad.arbitr.ru/Card/88d44bfe-afdf-4c85-8eb7-574b0fd6d9f5", "https://kad.arbitr.ru/Card/042627c4-9d15-4009-828f-f4795fbcc7cf", "https://kad.arbitr.ru/Card/4be933f0-0c01-4cf5-a529-adb37aecb187", "https://kad.arbitr.ru/Card/ae681df6-bbf9-4643-b924-a0498080d0fd", "https://kad.arbitr.ru/Card/fefe77e2-5570-4867-a3aa-85c3748656bf", "https://kad.arbitr.ru/Card/33d4afdc-48b3-4573-9db4-0b9e076a8651", "https://kad.arbitr.ru/Card/57c2c594-fc67-46c1-a5ff-b9681bed809a", "https://kad.arbitr.ru/Card/0468890f-e117-41dd-a04c-5db4a71aa141", "https://kad.arbitr.ru/Card/f64e69e4-2d89-48a3-b9d8-5f4a5f9b3524", "https://kad.arbitr.ru/Card/a0d9189a-2671-4a51-ab79-57fc7bee2e78", "https://kad.arbitr.ru/Card/29e19391-8d5b-4276-afb2-1ecb9283c048", "https://kad.arbitr.ru/Card/42352b7c-e35e-4ab3-9337-26c47c9e0f46"]




    fio_massiv = []
    adress_massiv = []
    case_instance_number_massiv = [] 
    date_massiv = []
    statuses_massiv = []
    schetchik = 0
    get_cookies()
    for item in data:
        schetchik += 1 
        print(schetchik)
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
