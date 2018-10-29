"""
Тип (car_type)	Марка (brand)	Кол-во пассажирских мест (passenger_seats_count)	Фото (photo_file_name)	Кузов ДxШxВ, м (body_whl)	Грузоподъемность, Тонн (carrying)	Дополнительно (extra)
car	Nissan xTtrail	4	f1.jpeg		2.5	
truck	Man		f2.jpeg	8x3x2.5	20	
car	Mazda 6	4	f3.jpeg		2.5	
spec_machine	Hitachi		f4.jpeg	

Вам необходимо создать свою иерархию классов для данных, которые описаны в таблице.
BaseCar
Car(BaseCar)
Truck(BaseCar)
SpecMachine(BaseCar)

У любого объекта есть обязательный атрибут car_type. 
Он означает тип объекта и может принимать одно из значений: car, truck, spec_machine.
Также у любого объекта из иерархии есть фото в виде имени файла — обязательный атрибут photo_file_name.
В базовом классе нужно реализовать метод get_photo_file_ext для получения расширения файла (“.png”, “.jpeg” и т.д.) с фото. 
Расширение файла можно получить при помощи os.path.splitext.
Для грузового автомобиля необходимо разделить характеристики кузова на отдельные составляющие body_length, body_width, body_height. 
Разделитель — латинская буква x. Характеристики кузова могут быть заданы в виде пустой строки, в таком случае все составляющие равны 0. 
Обратите внимание на то, что характеристики кузова должны быть вещественными числами.

Также для класса грузового автомобиля необходимо реализовать метод get_body_volume, возвращающий объем кузова в метрах кубических.
Все обязательные атрибуты для объектов Car, Truck и SpecMachine перечислены в таблице ниже, где 1 - означает, что атрибут обязателен для объекта, 0 - атрибут должен отсутствовать.
	Car	Truck	SpecMachine
car_type	1	1	1
photo_file_name	1	1	1
brand	1	1	1
carrying	1	1	1
passenger_seats_count	1	0	0
body_width	0	1	0
body_height	0	1	0
body_length	0	1	0
extra	0	0	1

"""

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []
    return car_list
