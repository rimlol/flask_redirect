import time
from urllib.parse import urlparse

from urllib import request

import random


attempts = 100

pause = 0.01
test_data =  [
    '?result=00000010',
    '?result=09010000',
    '?result=03030301',
    '?result=05000500',
    '?result=06040000' ,
    '?result=04040200',
    '?result=06030001'
]
result_data = [
    'https://ai.geekbrains.ru/marketing?from_test_with_loveprog=00&manage=00&diz=00&mark=10',
    'https://ai.geekbrains.ru/programming?prog=09&manage=01&diz=00&mark=00',
    'https://ai.geekbrains.ru/programming?prog=03&manage=03&diz=03&mark=01',
    'https://ai.geekbrains.ru/programming?prog_diz?prog=05&manage=00&diz=05&mark=00',
    'https://ai.geekbrains.ru/programming?prog_manage?prog=06&manage=04&diz=00&mark=00',
    'https://ai.geekbrains.ru/programming?prog_manage?prog=04&manage=04&diz=02&mark=00',
    'https://ai.geekbrains.ru/programming?prog=06&manage=03&diz=00&mark=01'


]
# a = 'https://dry-sea-25112.herokuapp.com/ann_o/' + str(test_data[6])
# print (a)


for i in range(attempts):
    rand = random.randint(0,6)
    url = 'https://dry-sea-25112.herokuapp.com/ann_o/' + str(test_data[rand])
    url = str(url)
    a = request.urlopen(url)
    b = a.geturl()
    if b == result_data[rand]:
        print ('ok')
    else: 
        print ('fail')

    time.sleep(pause)
