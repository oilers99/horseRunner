import settings

class Horse:
    """
    Атрибуты лошадей
    """
    def __init__(self, name_horse, power, speed):
        """
        :param name_horse: str
        :param power: int
        :param speed: int
        """
        self.name_horse = name_horse
        self.power = power
        self.speed = speed

class Creator(Horse):
    """
    Передача параметров в Horse
    """
    def __init__(self):
        self.name_horse = settings.name_horse()
        self.power = settings.power_horse()
        self.speed = settings.max_speed_horse()


def creator():
    """
    Создан необходимого кол-во экземпляров Horse
    """
    horses = {}
    for i in range(1, 3):
        h = Creator()
        # Решение без класса Creator
        # h = Horse(name_horse=settings.name_horse(), power=settings.power_horse(), speed=settings.max_speed_horse())
        horses[i] = h.name_horse, h.power, h.speed
    print(horses)


