
def find_spec(data):
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

        'prog_diz': 'https://ai.geekbrains.ru/prog_diz?',
        'prog_manage':'https://ai.geekbrains.ru/prog_manage?',
        'prog_mark': 'https://ai.geekbrains.ru/prog_mark?',
        'manage_diz': 'https://ai.geekbrains.ru/manage_diz?',
        'manage_mark': 'https://ai.geekbrains.ru/manage_mark?',
        'diz_mark': 'https://ai.geekbrains.ru/diz_mark?'
    }

    redirects_3_leads = "https://special.page/"




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
    '00000010',
    '09010000',
    '03030301',
    '05000500',
    '06040000' ,
    '04040200',
    '06030001'
]

def test():
    i = 0
    for elem in test_data:
        i += 1
        print('test No', i )
        find_spec(elem)

# test()

