import settings


class Horse(object):
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


class HorseCreator(Horse):
    """
    создает экземпляры лошади
    """
    def horse_creator(*args):
        new_horse = [settings.NAMEHORSE, settings.POWERHORSE, settings.SPEEDHORSE]


def main():
    HorseCreator.horse_creator()


if __name__ == "__main__":
    main()

