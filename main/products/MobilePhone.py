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
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PhoneCharacteristic.price.value))
        max_price = phone_list[len(phone_list) - 1].get_characteristic_value(PhoneCharacteristic.price.value)
        min_price = phone_list[0].get_characteristic_value(PhoneCharacteristic.price.value)
        return min_price, max_price

    @staticmethod
    def min_max_diagonal(phone_list):
        phone_list.sort(key=lambda phone: phone.get_characteristic_value(PhoneCharacteristic.diagonal.value))
        max_diagonal = phone_list[len(phone_list) - 1].get_characteristic_value(PhoneCharacteristic.diagonal.value)
        min_diagonal = phone_list[0].get_characteristic_value(PhoneCharacteristic.diagonal.value)
        return min_diagonal, max_diagonal

    @staticmethod
    def is_equals(phone1, phone2):
        print("\n\n" + PhoneCharacteristic.ram.value + "\n\n")
        if (phone1.get_characteristic_value(PhoneCharacteristic.ram.value) == phone2.get_characteristic_value(PhoneCharacteristic.ram.value)
            and phone1.get_characteristic_value(PhoneCharacteristic.os.value) == phone2.get_characteristic_value(PhoneCharacteristic.os.value)
            and phone1.get_characteristic_value(PhoneCharacteristic.diagonal.value) == phone2.get_characteristic_value(PhoneCharacteristic.diagonal.value)
            and phone1.get_characteristic_value(PhoneCharacteristic.screen_resolution.value) == phone2.get_characteristic_value(PhoneCharacteristic.screen_resolution.value)):
            return True
        else: return False

