import requests
import time
import random
import math
from bs4 import BeautifulSoup



#Получение ответа от сервера
def get_response(ceil_rnd):
    resp_get = requests.get ("http://google.com")
    #print(head)                                #Логирование ответов от сервера. Для отладки
    #write_txt(str(resp_get), str(head))        #Логирование ответов от сервера. Для отладки
    time.sleep(ceil_rnd)
    return resp_get.headers


#Запись ответа от сервера в файл
#Логирование ответов от сервера. Для отладки
#def write_txt(resp_get,head):
    #with open('headers.txt', 'a') as h:
       # h.write (resp_get + head + '\n')  
       # h.close () 



# Генерация случайных промежутков проверки доступности интернета
def random_timer():
    for i in range(10):
        rnd = random.uniform(1.0, 5.0)
        M_Exp =  math.exp(0.9)
        _rnd = rnd * M_Exp
        return math.ceil(_rnd) # Возврат как результат функции

def sendPost():
    url = 'https://startwifi.beeline.ru/status'
    response = requests.post(url, 'lang=ru&screen=normal&url=&mode=partner')
    print(str(response)+' post')
    print(response.headers)


# Проверка на наличие в залоговке поля 'Connection': 'close'
def check_response(check_head):

    obj = eval(check_head)
    

    try:
        print(obj['Connection'])    
        sendPost()
    except:
        print ('except')    


 

if __name__ == "__main__":

    while True:
        ceil_rnd = random_timer() # Присваивание значение функции переменной
        check_head = str (get_response(ceil_rnd))
        check_response(check_head)
        
   
