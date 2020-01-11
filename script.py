import time, threading, logging, requests, json
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
import os, time, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from threading import Thread
import multiprocessing, concurrent
import io
import requests
import PyPDF2
from tika import parser

_URL = 'http://192.168.0.250/clemencia/loginswimun.aspx'

logging.basicConfig( level=logging.DEBUG, format="%(threadName)s|%(message)s" )
#(
#    level=logging.DEBUG,
#    format="""
#    %(message)s
#    -----------------------------------
#    %(asctime)s | %(filename)s #%(lineno)s | %(funcName)s
#    %(threadName)s | %(processName)s | %(levelname)s
#    -----------------------------------
#    """,
#    datefmt='%H:%M:%S',
#    #filename='messages.txt'
#)

"""def mensajes():
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical')



def count(contador):
    while contador < 5:
        time.sleep(1)
        contador += 1
        logging.info(f'{contador} secs')

def count2(contador):
    while contador < 80:
        time.sleep(1)
        contador += 10
        logging.info(f'#{contador}')

if __name__ == '__main__':
    contador = 0
    contador2 = 0
    thread = threading.Thread(target=count, args=[contador])
    thread.start()
    thread2 = threading.Thread(target=count2, args=[contador2])
    thread2.start()"""


"""if __name__ == '__main__':
    contador = 0
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit(count, contador)
    headers = {'content-type': 'application/json'}
    payload = {'vUSERNICK': 'ADMINCS3', 'vUSERPASS': '18968934!', 'vVGFCOD': '2020', 'GXState': '{"_EventName":"EENTER.","_EventGridId":"","_EventRowId":"","vSWITTITULO1":"","vSWITTITULO2":"","GXFIELDHANDLER1_Control":"vUSERPASS","SCAMESSAGE1_Messagetype":"dialog","GXFIELDHANDLER1_Keycode":"","GX_FocusControl":"vSWITTITULO1","GX_AJAX_KEY":"2095BCCA5EEC7630D4A79BE44EE42942","AJAX_SECURITY_TOKEN":"B8284BEA03BEC307EE7F21FFD4A1CB55AB4790D15DE3CB0237EB74FE92236ADC","GX_CMP_OBJS":{},"sCallerURL":"http://192.168.0.250/clemencia/bienvenido.aspx","GX_RES_PROVIDER":"GXResourceProvider.aspx","GX_THEME":"TemaAzul","_MODE":"","Mode":"","IsModified":"1","SCAMESSAGE1_Width":"312","SCAMESSAGE1_Height":"62","SCAMESSAGE1_Animationtype":"show","SCAMESSAGE1_Visible":1,"GXBALLOON1_Width":"100","GXBALLOON1_Height":"100","GXBALLOON1_Maxwidth":400,"GXBALLOON1_Delay":0,"GXBALLOON1_Position":"right","GXBALLOON1_Offset":2,"GXBALLOON1_Keepalive":0,"GXBALLOON1_Timetolive":2000,"GXBALLOON1_Visible":1,"WIJMODATEPICKER1_Width":"100","WIJMODATEPICKER1_Height":"100","WIJMODATEPICKER1_Culture":"es-MX","WIJMODATEPICKER1_Visible":1,"CS3NOMOUSEUP1_Width":"100","CS3NOMOUSEUP1_Height":"100","CS3NOMOUSEUP1_Visible":1,"GXPLACEHOLDER1_Width":"100","GXPLACEHOLDER1_Height":"100","GXPLACEHOLDER1_Visible":1,"GXCS3BUGSFIXER1_Width":"40","GXCS3BUGSFIXER1_Height":"40","GXCS3BUGSFIXER1_Visible":1,"GXFIELDHANDLER1_Value":"","GXFIELDHANDLER1_Clicktype":"","GXFIELDHANDLER1_Visible":1}'}
    r = requests.post(_URL, data=json.dumps(payload), headers=headers)
    logging.info(r.cookies['ASP.NET_SessionId'])

threads = []

for _ in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()"""






# def get_driver():
#   driver = getattr(threadLocal, 'driver', None)
#   if driver is None:
#     chromeDriver = ChromeDriverManager().install()
#     chromeOptions = webdriver.ChromeOptions()
#     #chromeOptions.add_argument("--headless")
#     driver = webdriver.Chrome(executable_path=chromeDriver, chrome_options=chromeOptions)
#     setattr(threadLocal, 'driver', driver)
#   return driver

drivers = []

def driver():
    #driver: webdriver = get_driver()
    driver.get(_URL)

    #executor = ThreadPool(max_workers=3)

    #if(driver.toString().contains("null")):

    chromeDriver = ChromeDriverManager().install()
    # CONFIG WEBDRIVER OPTIONS
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-referrers")
    options.add_argument("--disable-popup-blocking")
    # OCULTAR NAVEGADOR
    # options.add_argument("--headless")
    prefs = {
        # "download.default_directory": downloadFolder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "profile.default_content_settings": 2,
        "profile.default_content_settings.popups": 0,
        "profile.default_content_settings.notifications": 1,
        # "profile.managed_default_content_settings.images": 2,
        "profile.browser.cache.disk.enable": False,
        "profile.browser.cache.memory.enable": False,
        "browser.cache.offline.enable": False,
        "network.http.use-cache": False,
        "profile.default_content_setting_values.plugins": 1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
        "PluginsAllowedForUrls": _URL,
        "profile.default_content_settings.popups": 0
    }
    options.add_experimental_option('prefs', prefs)

def conn():
    driver = webdriver.Chrome(executable_path=chromeDriver, chrome_options=options)
    driver.implicitly_wait(10)
    # driver.maximize_window()
    # driver.get(_URL)
    # Page.login(driver)
    # driver.delete_all_cookies()
    # cookie = {'name': 'ASP.NET_SessionId', 'value': Page.login(municipio)}
    # driver.add_cookie(cookie)
    drivers.append( {'driver': driver, 'status': 'open'} )
    return driver


def sumar(a,b):
    logging.info(a+b)

threads = []
# if __name__ == '__main__':
#     for _ in range(1):
#         conn()
#     for i in range(len(drivers)):
#         logging.info(drivers[i]['driver'])
#         drivers[i]['driver'].get('http://www.google.com')
    # for _ in range(3):
    #     thread = Thread(target=conn())
    #     threads.append(thread)
    #     thread.start()
    #
    # for thread in threads:
    #     thread.join()
    #
    # for i in range(0,len(drivers)):
    #     driver: webdriver = threads[i].driver
    #     driver.get('http://www.google.com')


    #sdriver.get('http://www.google.com')
"""    thread = Thread(target=driver())
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()
    current_process = multiprocessing.current_process() """
    #    thread.get().get(_URL)
    #with ThreadPool() as executor:
    #    result = executor.apply_async(get_driver())
    #    result.get().driver.get(_URL)

if __name__ == '__main__':
    url = 'http://192.168.0.250/clemencia/arptrecofpag_850_1100.aspx?2020,C,3,170,1,2,1'

    r = requests.get(url)
    f = io.BytesIO(r.content)

    raw = parser.from_file(f)
    print(raw['content'])