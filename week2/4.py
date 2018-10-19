"""На этой неделе мы с вами реализуем собственный key-value storage. 
Вашей задачей будет написать скрипт, который принимает в качестве аргументов 
ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).
Запись значения по ключу
> storage.py --key key_name --val value
Получение значения по ключу
> storage.py --key key_name
Ответом в данном случае будет вывод с помощью print соответствующего значения
> value
или
> value_1, value_2
если значений по этому ключу было записано несколько. 
Метрики сохраняйте в порядке их добавления. 
Обратите внимание на пробел после запятой.
Если значений по ключу не было найдено, выводите пустую строку или None.
Для работы с аргументами командной строки используйте модуль argparse. 
Вашей задачей будет считать аргументы, переданные вашей программе, 
и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, 
если был передан только ключ. 
Хранить данные вы можете в формате JSON с помощью стандартного модуля json. 
Проверьте добавление нескольких ключей и разных значений.

Файл следует создавать с помощью модуля tempfile.

import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'w') as f:
  ...
"""

import os
import tempfile
import argparse
import json
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--val', help='this arg for val')
parser.add_argument('-k', '--key', help='this arg for key', required=True)
with open(storage_path, 'w') as f:
    argsDict = vars(parser.parse_args())
    print(argsDict)
    if argsDict['key']:
        if argsDict['val']:
            print('writing value')
            f.write(json.dumps({argsDict['key']: argsDict['val']}))
        else:
            with open(storage_path, 'r') as r:
                jsonLines = r.readlines()
                print(jsonLines)
                lines = json.loads(jsonLines)
                print(lines[argsDict['val']])
                if lines[argsDict['val']]:
                    print(lines[argsDict['val']])
                else:
                    print('VALUE DOESN\'T EXIST!!!')
    else:
        print('no valid input')

    #print(f.readlines())



