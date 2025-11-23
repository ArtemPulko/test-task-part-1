from main.products.PhoneCharacteristic import PhoneCharacteristic as PC
from decimal import Decimal

class MobilePhone:
    def __init__(self):
        self.characteristics = {}

    def add_characteristic(self, name: str, value):
        """
        Метод для добавления характеристики для телефона.
        :param name: Название характеристики.
        :param value: Значение характеристики.
        """
        self.characteristics[name] = value

    def get_characteristic_value(self, characteristic: str):
        """
        Метод возвращает значение характеристики телефона.
        :param characteristic: Название характеристики.
        :return: Значение характеристики.
        """
        return self.characteristics[characteristic]

    @staticmethod
    def min_max_price(phone_list: list['MobilePhone']) -> tuple[Decimal, Decimal]:
        """
        Статический метод для создания картежа с минимальной и максимальной ценой телефонов
        :param phone_list: Список телефонов.
        :return: Картеж из минимальной и максимальной цены.
        """
        # Сортировка цен по возрастанию
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PC.price.value))
        # Формирование картежа с минимальной и максимальной ценой
        max_price = phone_list[len(phone_list) - 1].get_characteristic_value(PC.price.value)
        min_price = phone_list[0].get_characteristic_value(PC.price.value)
        return min_price, max_price

    @staticmethod
    def min_max_diagonal(phone_list: list['MobilePhone']) -> tuple[Decimal, Decimal]:
        """
        Статический метод для создания картежа с минимальной и максимальной диагональю экрана.
        :param phone_list: Список телефонов.
        :return: Картеж из минимальной и максимальной диагонали экрана.
        """
        # Сортировка размеров экрана по возрастанию
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PC.diagonal.value))
        # Формирование картежа с минимальным и максимальным размером экрана
        max_diagonal = phone_list[len(phone_list) - 1].get_characteristic_value(PC.diagonal.value)
        min_diagonal = phone_list[0].get_characteristic_value(PC.diagonal.value)
        return min_diagonal, max_diagonal

    @staticmethod
    def is_equals(phone1: 'MobilePhone', phone2: 'MobilePhone') -> bool:
        """
        Статический метод для сравнивания двух телефонов.
        :param phone1: Первый телефон.
        :param phone2: Второй телефон.
        :return: True если параметры телефонов равны, иначе False
        """
        if (phone1.get_characteristic_value(PC.ram.value) == phone2.get_characteristic_value(PC.ram.value)
            and phone1.get_characteristic_value(PC.os.value) == phone2.get_characteristic_value(PC.os.value)
            and phone1.get_characteristic_value(PC.diagonal.value) == phone2.get_characteristic_value(PC.diagonal.value)
            and phone1.get_characteristic_value(PC.screen_resolution.value) == phone2.get_characteristic_value(PC.screen_resolution.value)):
            return True
        else: return False

