
from urllib.parse import urlparse
import re

def find_spec(urla):
    
    url = urlparse(urla)

    # Проверяем строку на наличие  нужной нам метки  result= и если все ок то выбираем куда редиректить
    # если все не ок то редиректим на главную
    if re.search( 'result=',(url.query)) != None:
        result_all = url.query.split('=')
        result_num = str(result_all[1])
        data = result_num
        n =2
        splited = [data[i:i+n] for i in range(0, len(data), n)]
        print (splited)

        result_dict = [
            'prog',
            'manage',
            'diz',
            'mark'
        ]

    # прописываем редирект


        redirects_1_lead ={
            'prog' : 'https://ai.geekbrains.ru/programming?',
            'manage' : 'https://ai.geekbrains.ru/management?',
            'diz' : 'https://ai.geekbrains.ru/design?from_test_with_love',
            'mark' : 'https://ai.geekbrains.ru/marketing?from_test_with_love'
        }

        redirects_2_leads = {

            'prog_diz': 'https://ai.geekbrains.ru/programming?prog_diz?',
            'prog_manage':'https://ai.geekbrains.ru/programming?prog_manage?',
            'prog_mark': 'https://ai.geekbrains.ru/programming?prog_mark?',
            'manage_diz': 'https://ai.geekbrains.ru/programming?manage_diz?',
            'manage_mark': 'https://ai.geekbrains.ru/programming?manage_mark?',
            'diz_mark': 'https://ai.geekbrains.ru/programming?diz_mark?'
        }

        redirects_3_leads = "https://ai.geekbrains.ru/programming?special?"




    # создаем параметры для ссылки
        result_params = ''

        for i in range(len (splited)):
            result_params = result_params + result_dict[i] + '='+ splited[i] + '&'
        result_params = result_params[:-1]
        print('params',result_params)


    # прописываем случай 3-3-3

        if splited.count(max(splited)) > 2:
            total_result = redirects_3_leads
            print(total_result + result_params)
            return(total_result +result_params)

    # прописываем другие сценарии
        else:
            total_result = []
            total_result_count = []
            string = ''
            max_splited_index = splited.index(max(splited))

            counter =0
            for elem in splited:
                if abs(int(elem) - int(splited[max_splited_index])) < 3 and int(elem) >= 4:
                    total_result.append(result_dict[counter])
                    total_result_count.append(elem)
                counter += 1
            
            for iter in range(len(total_result)):
                if iter != len(total_result):
                    string = string  + total_result[iter] + '='  + total_result_count[iter] + '&'
                else:
                    string = string  + total_result[iter] + '='  + total_result_count[iter]


            print(total_result)

    # прописываем логику генерации ссылок редиректа

            if len(total_result) == 1:
                print (redirects_1_lead[total_result[0]]+ result_params)
                return  (redirects_1_lead[total_result[0]] + result_params)
            elif len(total_result) == 2:

                print (redirects_2_leads[total_result[0]+'_' +total_result[1]] + result_params)
                return  (redirects_2_leads[total_result[0]+'_' +total_result[1]] +result_params)


            print ('index',string)
            print ( string[:-1])
            #  поправить адресные строки вывода ниже
            return (string[:-1])


    else:
        return ('https://geekbrains.ru')
    """
    Логика

    00 00 00 00

    00          - прог
    00       - менеджмент
         00    - дизайн
            00 - маркетинг

        '00000010', -  маркетинг
        '09010000', -  прог
        '03030301', -  всё
        '05000500', -  прог+диз
        '05040001', -  прог+менеджемнт
        '04040200', -  прог+менедж
        '04040101', -  прог+ менедж
    """




test_data =  [
    'https://ai.geekbrains.ru/?result=00000010',
    'https://ai.geekbrains.ru/?result=09010000',
    'https://ai.geekbrains.ru/?result=03030301',
    'https://ai.geekbrains.ru/?result=05000500',
    'https://ai.geekbrains.ru/?result=06040000' ,
    'https://ai.geekbrains.ru/?result=04040200',
    'https://ai.geekbrains.ru/?result=06030001'
]

def test():
    i = 0
    for elem in test_data:
        i += 1
        print('test No', i )
        find_spec(elem)

test()

