from django import template
#from censor_list import censor_list

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='multiply')  # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg  # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

@register.filter(name='censor')
def censor(value):
    value1 = (str(value)).split()
    censor_list = ['дебил',
                   'дурак',
                   'придурок',
                   'Алма-Аты', # для теста
                   'связи' # для теста
                   ]
#    censor_list = []
#    with open('news/censor_list.txt') as f:
 #       censor_list = f.read().splitlines()

    for i, word in enumerate(censor_list):
        for j, word1 in enumerate(value1):
            if word1 == word:
                value1[j] = "*****"

 #   for i in censor_list:
 #       for j in value1:
  #          if j == i:
  #              value1.remove(i)
                # value1.replace(i, '***')
    value = ' '.join(value1)
    return str(value)


 #   for i in censor_list:
   #     if a == censor_list and a == b:
   #         b = '*****'
    #        return b
  #      else:
   #         return f'Нелья писать следующие слова:{censor_list}'