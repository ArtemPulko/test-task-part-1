from main.products.PhoneCharacteristic import PhoneCharacteristic


class MobilePhone:

    def __init__(self):
        self.characteristics = {}
    def add_characteristic(self, name, value):
        self.characteristics[name] = value

    def get_characteristic_value(self, characteristic):
        return self.characteristics[characteristic]

    @staticmethod
    def min_max_price(phone_list):
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PhoneCharacteristic.price))
        min_price = phone_list[0].get_characteristic_value(PhoneCharacteristic.price)
        max_price = phone_list[len(phone_list) - 1].get_characteristic_value(PhoneCharacteristic.price)
        return min_price, max_price

    @staticmethod
    def min_max_diagonal(phone_list):
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PhoneCharacteristic.diagonal))
        min_diagonal = phone_list[0].get_characteristic_value(PhoneCharacteristic.diagonal)
        max_diagonal = phone_list[len(phone_list) - 1].get_characteristic_value(PhoneCharacteristic.diagonal)
        return min_diagonal, max_diagonal