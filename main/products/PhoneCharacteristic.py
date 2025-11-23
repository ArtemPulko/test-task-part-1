import enum

class PhoneCharacteristic(enum.Enum):
    """Перечисление с названием характеристик телефона"""
    price = "Цена"
    diagonal = "Размер экрана"
    screen_resolution = "Разрешение экрана"
    ram = "Объем оперативной памяти"
    os = "Операционная система"