from urllib.parse import urlparse
import re
def parse_and_redirect(urla):
    

    url = urlparse(urla)

    # Проверяем строку на наличие  нужной нам метки  result= и если все ок то выбираем куда редиректить
    # если все не ок то редиректим на главную
    if re.search( 'result=',(url.query)) != None:
        result_all = url.query.split('=')
        result_num = str(result_all[1])

        max_result = result_num.index(max(result_num))

        redirects = {
            0 : "https://ai.geekbrains.ru/programming?from_test_with_love",  # 1 разряд - 10^4
            1 : 'https://ai.geekbrains.ru/management?from_test_with_love',   # 3 разряд - 10^2
            2 : 'https://ai.geekbrains.ru/design?from_test_with_love',       # 4 разряд - 10^1

            3 : 'https://ai.geekbrains.ru/marketing?from_test_with_love'     # 2 разряд - 10^3
            # 2 : 'https://ai.geekbrains.ru/analytics?from_test_with_love',  # 3 разряд - 10^3
        }
        print(redirects[max_result])
        return(redirects[max_result])
    else:
        return ('https://geekbrains.ru')




def geekschool_parse_and_redirect(urla):
    # Проверяем строку на наличие  нужной нам метки  product_id= и если все ок то выбираем куда редиректить
    # если все не ок то редиректим на главную
    url = urlparse(urla)

    if re.search( 'product_id=',(url.query)) != None:
        result_all = url.query.split('=')
        result_num = (result_all[1])
        redirects = {
            '0': 'https://geekbrains.ru',
            '4' : 'https://geek-school.geekbrains.ru/python/?utm_source=cm_career&utm_medium=python&utm_campaign=geekschool_test',
            '8' : 'https://geek-school.geekbrains.ru/gamedev/?utm_source=cm_career&utm_medium=gamedev&utm_campaign=geekschool_test',
            '5' : 'https://geek-school.geekbrains.ru/web/?utm_source=cm_career&utm_medium=web&utm_campaign=geekschool_test',
            '10' : 'https://geek-school.geekbrains.ru/java/?utm_source=cm_career&utm_medium=java&utm_campaign=geekschool_test',
            '11' : 'https://geek-school.geekbrains.ru/pygame/?utm_source=cm_career&utm_medium=pygame&utm_campaign=geekschool_test',
            '1' : 'https://geek-school.geekbrains.ru/security/?utm_source=cm_career&utm_medium=security&utm_campaign=geekschool_test',
            '12' : 'https://geek-school.geekbrains.ru/scratch/?utm_source=cm_career&utm_medium=scratch&utm_campaign=geekschool_test',
            '7' : 'https://geek-school.geekbrains.ru/minecraft/?utm_source=cm_career&utm_medium=minecraft&utm_campaign=geekschool_test',
            '2' : 'https://geek-school.geekbrains.ru/arduino/?utm_source=cm_career&utm_medium=arduino&utm_campaign=geekschool_test',
            '3' : 'https://geek-school.geekbrains.ru/blogging/?utm_source=cm_career&utm_medium=blogging&utm_campaign=geekschool_test',
            '6' : 'https://geek-school.geekbrains.ru/webdesign/?utm_source=cm_career&utm_medium=webdesign&utm_campaign=geekschool_test',
            '100' : 'https://geek-school.geekbrains.ru/creativity/?utm_source=cm_career&utm_medium=creativity&utm_campaign=geekschool_test',
            '13' : 'https://geek-school.geekbrains.ru/aibasic/?utm_source=cm_career&utm_medium=aibasic&utm_campaign=geekschool_test',
            '200' : 'https://geek-school.geekbrains.ru/literacy/?utm_source=cm_career&utm_medium=literacy&utm_campaign=geekschool_test',
            '9' : 'https://geek-school.geekbrains.ru/swift/?utm_source=cm_career&utm_medium=swift&utm_campaign=geekschool_test',
        }

        try:
            
            print(redirects[result_num])
            return(redirects[result_num])
        except KeyError:
            print('https://geekbrains.ru')

            return ('https://geekbrains.ru/?utm_source=cm_career&utm_medium=test&utm_campaign=geekschool_test')
    else:
        return ('https://geekbrains.ru/?utm_source=cm_career&utm_medium=test&utm_campaign=geekschool_test')


