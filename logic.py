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

        logic = {
            0 : "programming",  # 1 разряд - 10^5
            1 : 'marketing',    # 2 разряд - 10^4
            2 : 'analytics',    # 3 разряд - 10^3
            3 : 'management',   # 4 разряд - 10^2
            4 : 'design'        # 5 разряд - 10^1
        }
        redirects = {
            0 : "https://ai.geekbrains.ru/programming?from_test_with_love",  # 1 разряд - 10^5
            1 : 'https://ai.geekbrains.ru/marketing?from_test_with_love',    # 2 разряд - 10^4
            2 : 'https://ai.geekbrains.ru/analytics?from_test_with_love',    # 3 разряд - 10^3
            3 : 'https://ai.geekbrains.ru/management?from_test_with_love',   # 4 разряд - 10^2
            4 : 'https://ai.geekbrains.ru/design?from_test_with_love'        # 5 разряд - 10^1
        }
        print(redirects[max_result])
        return(redirects[max_result])
    else:
        return ('https://geekbrains.ru')




