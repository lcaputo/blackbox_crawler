import os, time, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests, logging, threading

_URL = 'http://192.168.0.250/'
#downloadFolder = r''+os.getcwd()+'\Downloads\\'

logging.basicConfig( level=logging.DEBUG, format="%(threadName)s|%(message)s" )


class Page():

    def conn(municipio, accion=''):
        chromeDriver = ChromeDriverManager().install()
        # CONFIG WEBDRIVER OPTIONS
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-referrers")
        options.add_argument("--disable-popup-blocking")
        # OCULTAR NAVEGADOR
        options.add_argument("--headless")
        prefs = {
            #"download.default_directory": downloadFolder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "profile.default_content_settings" : 2,
            "profile.default_content_settings.popups": 0,
            "profile.default_content_settings.notifications": 1,
            #"profile.managed_default_content_settings.images": 2,
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

        driver = webdriver.Chrome(executable_path=chromeDriver, chrome_options=options)
        driver.implicitly_wait(10)
        driver.get(_URL+municipio)
        Page.login(driver)
        #driver.delete_all_cookies()
        #cookie = {'name': 'ASP.NET_SessionId', 'value': Page.login(municipio)}
        #driver.add_cookie(cookie)
        return driver


    def login(driver):
        #payload = {'vUSERNICK': 'ADMINCS3', 'vUSERPASS': '18968934!', 'vVGFCOD': '2020', 'GXState': '{"_EventName":"EENTER.","_EventGridId":"","_EventRowId":"","vSWITTITULO1":"","vSWITTITULO2":"","GXFIELDHANDLER1_Control":"vUSERPASS","SCAMESSAGE1_Messagetype":"dialog","GXFIELDHANDLER1_Keycode":"","GX_FocusControl":"vSWITTITULO1","GX_AJAX_KEY":"2095BCCA5EEC7630D4A79BE44EE42942","AJAX_SECURITY_TOKEN":"B8284BEA03BEC307EE7F21FFD4A1CB55AB4790D15DE3CB0237EB74FE92236ADC","GX_CMP_OBJS":{},"sCallerURL":"'+_URL+municipio+'/bienvenido.aspx","GX_RES_PROVIDER":"GXResourceProvider.aspx","GX_THEME":"TemaAzul","_MODE":"","Mode":"","IsModified":"1","SCAMESSAGE1_Width":"312","SCAMESSAGE1_Height":"62","SCAMESSAGE1_Animationtype":"show","SCAMESSAGE1_Visible":1,"GXBALLOON1_Width":"100","GXBALLOON1_Height":"100","GXBALLOON1_Maxwidth":400,"GXBALLOON1_Delay":0,"GXBALLOON1_Position":"right","GXBALLOON1_Offset":2,"GXBALLOON1_Keepalive":0,"GXBALLOON1_Timetolive":2000,"GXBALLOON1_Visible":1,"WIJMODATEPICKER1_Width":"100","WIJMODATEPICKER1_Height":"100","WIJMODATEPICKER1_Culture":"es-MX","WIJMODATEPICKER1_Visible":1,"CS3NOMOUSEUP1_Width":"100","CS3NOMOUSEUP1_Height":"100","CS3NOMOUSEUP1_Visible":1,"GXPLACEHOLDER1_Width":"100","GXPLACEHOLDER1_Height":"100","GXPLACEHOLDER1_Visible":1,"GXCS3BUGSFIXER1_Width":"40","GXCS3BUGSFIXER1_Height":"40","GXCS3BUGSFIXER1_Visible":1,"GXFIELDHANDLER1_Value":"","GXFIELDHANDLER1_Clicktype":"","GXFIELDHANDLER1_Visible":1}'}
        #headers = {'content-type': 'application/x-www-form-urlencoded'}
        #response = requests.post(_URL+municipio+'/loginswimun.aspx', data=json.dumps(payload))
        #cookie = response.cookies['ASP.NET_SessionId']
        #logging.info(cookie)
        #return cookie
        usr = driver.find_element_by_id('vUSERNICK')
        usr.clear()
        usr.send_keys('ADMINCS3')
        psw = driver.find_element_by_id('vUSERPASS')
        psw.clear()
        psw.send_keys('18968934!')
        psw.send_keys(u'\ue007')


    def clearSession(driver):
        driver.delete_cookie('ASP.NET_SessionId')


    def reload(driver):
        Page.clearSession()
        driver.refresh()
        Page.login()


    def quit(driver):
        driver.quit()




class AtencionAlCliente():

    def fillRefCatastral(driver, municipio, codRefCatastral):
        time.sleep(2)
        refCatastral = driver.find_element_by_id('vWRGCDOCID_MPAGE')
        refCatastral.clear()
        refCatastral.send_keys(codRefCatastral)
        refCatastral.send_keys(Keys.ENTER)

    def reciboDePago(municipio, codRefCatastral):

        driver: webdriver = Page.conn(municipio)
        driver.get(_URL+municipio+'/atn_prd_estadocuenta.aspx')

        AtencionAlCliente.fillRefCatastral(driver, municipio, codRefCatastral)

        btnRecibo = driver.find_element_by_id('BTNRECIBOF_MPAGE')
        btnRecibo.click()

        time.sleep(1)

        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        btnGenerar = driver.find_element_by_name('BUTTON1')
        btnGenerar.click()

        time.sleep(2)
        first_window = driver.window_handles[0]
        popup_window = driver.window_handles[1]
        driver.switch_to.window(popup_window)
        driver.close()
        driver.switch_to.window(first_window)

        #driver.get(_URL)




if __name__ == '__main__':
    """ WEBDRIVER CONNECTION """
    #driver.implicitly_wait(10)
