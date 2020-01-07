import os, time
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


_URL = 'http://192.168.0.250/'
#downloadFolder = r''+os.getcwd()+'\Downloads\\'

class Page():

    def conn():

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
        #driver.get(_URL)
        time.sleep(1)
        return driver


    def login():
        time.sleep(4)
        usr = driver.find_element_by_id('vUSERNICK')
        usr.clear()
        usr.send_keys('ADMINCS3')
        psw = driver.find_element_by_id('vUSERPASS')
        psw.clear()
        psw.send_keys('18968934!')
        psw.send_keys(u'\ue007')


    def clearSession():
        driver.delete_cookie('ASP.NET_SessionId')


    def reload():
        Page.clearSession()
        driver.refresh()
        Page.login()


    def quit():
        driver.quit()



""" WEBDRIVER CONNECTION """
driver: webdriver = Page.conn()
driver.implicitly_wait(10)


class Actions():

    def goToNovedades():
        driver.get(_URL+'VerNovedadesGrales.aspx')


    def goToLiquidacionImpuestoPredial():
        driver.get(_URL+'FormAsistenteIgac.aspx')


    def goToAtencionAlCliente():
        driver.get(_URL+'atn_prd_estadocuenta.aspx')


class Novedad():

    def seleccionar(resolucion, tipo_novedad):

        driver.find_element_by_id('IMGINS').click()

        formulario = driver.find_element_by_xpath("//table[@id='TABLE1']")

        print(formulario)

        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_id("vVRNIRES")

        input_resolucion = driver.find_element_by_id("vVRNIRES")
        input_resolucion.send_keys(resolucion)

        input_tipo_novedad = driver.find_element_by_id("vVRNITIP")

        input_tipo_novedad.send_keys(tipo_novedad)

        submit = driver.find_element_by_xpath("//input[@name='BUTTON1']").click()


class EstadoCuenta():

    def seleccionar(resolucion, tipo_novedad):

        driver.find_element_by_id('IMGINS').click()

        formulario = driver.find_element_by_xpath("//table[@id='TABLE1']")

        print(formulario)

        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_id("vVRNIRES")

        input_resolucion = driver.find_element_by_id("vVRNIRES")
        input_resolucion.send_keys(resolucion)

        input_tipo_novedad = driver.find_element_by_id("vVRNITIP")

        input_tipo_novedad.send_keys(tipo_novedad)

        submit = driver.find_element_by_xpath("//input[@name='BUTTON1']").click()


class AtencionAlCliente():

    def fillRefCatastral(codRefCatastral):
        refCatastral = driver.find_element_by_id('vWRGCDOCID_MPAGE')
        refCatastral.clear()
        refCatastral.send_keys(codRefCatastral)
        refCatastral.send_keys(Keys.ENTER)

    def reciboDePago(codRefCatastral,):
        AtencionAlCliente.fillRefCatastral(codRefCatastral)

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


    def registrarPago(codRefCatastral, codRecibo, codCtaRecaudadora):
        AtencionAlCliente.fillRefCatastral(codRefCatastral)

        btn = driver.find_element_by_id('BTNPAG_MPAGE')
        btn.click()

        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(1)
        tabla = driver.find_element_by_id('Grid1ContainerTbl')
        rows = tabla.find_elements_by_tag_name("tr")
        for i in range(1,len(rows)):
            print(rows[i].text.split(' ')[2].split('\n')[1])
            if int(codRecibo) == int(rows[i].text.split(' ')[2].split('\n')[1]) :
                checkBoxID = 'IMAGECHK_'+'{:04d}'.format(i)
                driver.find_element_by_id(checkBoxID).click()
                break
        # SELECT CUENTA RECAUDADORA
        selectCtaRecaudadora = driver.find_element_by_id("vCTACOD")
        numCtas = selectCtaRecaudadora.find_elements_by_tag_name('option')
        for cta in numCtas:
            if codCtaRecaudadora == cta.get_attribute("value") :
                cta.click()
                break
        # APLCIAR
        driver.find_element_by_xpath("//table[@id='TABLE6']//input[@value='APLICAR']").click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(2)
        first_window = driver.window_handles[0]
        popup_window = driver.window_handles[1]
        driver.switch_to.window(popup_window)
        driver.close()
        driver.switch_to.window(first_window)

        #driver.get(_URL)



    def pazYSalvo(codRefCatastral):
        AtencionAlCliente.fillRefCatastral(codRefCatastral)
        btn = driver.find_element_by_id('BTNPYZ_MPAGE')
        btn.click()
        time.sleep(1)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(1)
        driver.find_element_by_xpath("//table[@id='TABBUT']//input[@value='Emitir Paz y Salvo']").click()
        time.sleep(2)
        first_window = driver.window_handles[0]
        popup_window = driver.window_handles[1]
        driver.switch_to.window(popup_window)
        driver.close()
        driver.switch_to.window(first_window)
        #driver.get(_URL)



""" class Liquidación:

    class ImpuestoPredial():

        def montarCinta():
 """

