class FileReader():
    """ 
    Первое задание у нас для разогрева. 
    Ваша задача написать Python-модуль solution.py, 
    внутри которого определен класс FileReader.
    Инициализатор этого класса принимает аргумент - путь до файла на диске.
    У класса должен быть метод read, 
    возвращающий содержимое файла в виде строки.
    Еще один момент - внутри метода read вы должны 
    обрабатывать исключение IOError,
    возникающее, когда файла, с которым был инициализирован класс, 
    на самом деле нет на жестком диске. 
    В случае возникновения такой ошибки метод read должен 
    возвращать пустую строку 
    """
    def __init__(self, path):
        self.path = path
    
    def read(self):
        try:
            f = open(self.path, 'r')
            lines = f.read()
            f.close()
            return lines
        except IOError:
            return "empty string"

reader = FileReader("example.txt")
print(reader.read())

