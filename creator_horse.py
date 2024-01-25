import settings


class Creator:
    """
    Передача параметров в Horse
    """
    def __init__(self):
        self.name_horse = settings.name_horse()
        self.power = settings.power_horse()
        self.speed = settings.max_speed_horse()

    def name_creator(self, number_of_horses):
        self.list_name_horse = []
        for i in range(number_of_horses):
            self.list_name_horse.append(settings.name_horse())
        print(self.list_name_horse)
