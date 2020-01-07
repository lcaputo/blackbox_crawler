import time, threading, logging, requests, json
from concurrent.futures import ThreadPoolExecutor

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

def mensajes():
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

"""if __name__ == '__main__':
    contador = 0
    contador2 = 0
    thread = threading.Thread(target=count, args=[contador])
    thread.start()
    thread2 = threading.Thread(target=count2, args=[contador2])
    thread2.start()"""

if __name__ == '__main__':
    contador = 0
    executor = ThreadPoolExecutor(max_workers=3)
    executor.submit(count, contador)
    headers = {'content-type': 'application/json'}
    payload = {'vUSERNICK': 'ADMINCS3', 'vUSERPASS': '18968934!', 'vVGFCOD': '2020', 'GXState': '{"_EventName":"EENTER.","_EventGridId":"","_EventRowId":"","vSWITTITULO1":"","vSWITTITULO2":"","GXFIELDHANDLER1_Control":"vUSERPASS","SCAMESSAGE1_Messagetype":"dialog","GXFIELDHANDLER1_Keycode":"","GX_FocusControl":"vSWITTITULO1","GX_AJAX_KEY":"2095BCCA5EEC7630D4A79BE44EE42942","AJAX_SECURITY_TOKEN":"B8284BEA03BEC307EE7F21FFD4A1CB55AB4790D15DE3CB0237EB74FE92236ADC","GX_CMP_OBJS":{},"sCallerURL":"http://192.168.0.250/clemencia/bienvenido.aspx","GX_RES_PROVIDER":"GXResourceProvider.aspx","GX_THEME":"TemaAzul","_MODE":"","Mode":"","IsModified":"1","SCAMESSAGE1_Width":"312","SCAMESSAGE1_Height":"62","SCAMESSAGE1_Animationtype":"show","SCAMESSAGE1_Visible":1,"GXBALLOON1_Width":"100","GXBALLOON1_Height":"100","GXBALLOON1_Maxwidth":400,"GXBALLOON1_Delay":0,"GXBALLOON1_Position":"right","GXBALLOON1_Offset":2,"GXBALLOON1_Keepalive":0,"GXBALLOON1_Timetolive":2000,"GXBALLOON1_Visible":1,"WIJMODATEPICKER1_Width":"100","WIJMODATEPICKER1_Height":"100","WIJMODATEPICKER1_Culture":"es-MX","WIJMODATEPICKER1_Visible":1,"CS3NOMOUSEUP1_Width":"100","CS3NOMOUSEUP1_Height":"100","CS3NOMOUSEUP1_Visible":1,"GXPLACEHOLDER1_Width":"100","GXPLACEHOLDER1_Height":"100","GXPLACEHOLDER1_Visible":1,"GXCS3BUGSFIXER1_Width":"40","GXCS3BUGSFIXER1_Height":"40","GXCS3BUGSFIXER1_Visible":1,"GXFIELDHANDLER1_Value":"","GXFIELDHANDLER1_Clicktype":"","GXFIELDHANDLER1_Visible":1}'}
    r = requests.post(_URL, data=json.dumps(payload), headers=headers)
    logging.info(r.cookies['ASP.NET_SessionId'])


"""threads = []

for _ in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()"""