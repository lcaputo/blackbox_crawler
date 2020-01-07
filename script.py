import time, threading, logging

logging.basicConfig(
    level=logging.DEBUG, #10
    format='%(filename)s - %(asctime)s'
    datefmt='%H:%M:%S'
)

def mensajes():
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical')

def worker():
    print('inicio')
    time.sleep(1)
    print('fin')

def worker2():
    print('inicio2')
    time.sleep(1)
    print('fin2')

def worker3():
    print('inicio3')
    time.sleep(1)
    print('fin3')

thread_a = threading.Thread(target=worker)
thread_b = threading.Thread(target=worker2)
thread_c = threading.Thread(target=worker3)

thread_a.start()
thread_b.start()
thread_c.start()


if __name__ == '__main__':
    mensajes()

"""threads = []

for _ in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()"""