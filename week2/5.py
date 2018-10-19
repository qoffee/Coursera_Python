"""Чтобы передавать данные между функциями, модулями или разными системами используются форматы данных. 
Одним из самых популярных форматов является JSON. Напишите декоратор to_json, который можно применить к различным функциям, 
чтобы преобразовывать их возвращаемое значение в JSON-формат. 
Не забудьте про сохранение корректного имени декорируемой функции.
@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data()  # вернёт '{"data": 42}'
"""
import json

def to_json(func):
    def inner(*args, **kwargs):
        temp = func(*args, **kwargs)
        print(f"temp = {temp}")
        j = json.dumps(temp)
        print(f"type of j = {type(j)}")
        return j
    return inner

@to_json
def test(n):
    #l = [0, 1]
    #for i in range(n-1):
    #    l.append(l[i] + l[i+1])
    #return l[n-1]
    return "asfasfasfassf"

print(test(4))
print(type(test(4)))

@to_json
def test2(n):
    return {'data': 42}

print(test2(4))

