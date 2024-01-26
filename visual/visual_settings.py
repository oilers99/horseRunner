import pygame
pygame.init()

"""
Параметры главного окна class Game
"""
"""Размер главного окна"""
size_main_x, size_main_y = 1600, 1050
MAIN_SIZE_WINDOWS = (size_main_x, size_main_y)
"""Заголовок окна"""
MAIN_NAME_WINDOWS = "_HorseRacer_"
"""Икона окна"""
MAIN_ICON_WINDOWS = None
"""Шрифт и размер для теста"""
MAIN_FONT = pygame.font.SysFont('arial', 32)
"""Картинка and подложки"""
MAIN_BG = pygame.image.load("media//bg_1.png")
MAIN_ROAD = pygame.image.load("media//road_2.png")
MAIN_TRACTOR = pygame.image.load("media//tractor.png")

"""цвет кнопка"""
MAIN_BUTTON_INACTIVE_COLOR = (150, 150, 150)
MAIN_BUTTON_ACTIVE_COLOR = (200, 200, 200)
MAIN_BUTTON_TEXT_COLOR = (0, 0, 0)
"""Цвет текста имен"""
MAIN_NAME_TEXT_COLOR = (100, 255, 255)


"""
Параметры стартового окна class StartWindows
"""
"""Размер стартового окна"""
size_start_x, size_start_y = 350, 200
SW_SIZE_START_WINDOWS = (size_start_x, size_start_y)
"""Заголовок окна"""
SW_NAME_START_WINDOWS = "_HorseRacer_"
"""Икона окна"""
SW_ICON_START_WINDOWS = None
"""Шрифт и размер для теста"""
SW_FONT_START_WINDOWS = pygame.font.SysFont('arial', 20)
"""Текст запроса количества играков"""
SW_TEXT_NUM_PLAYERS = "Введите количество играков (2-8)"
"""цвет стартового окна"""
SW_START_BG_COLOR = (240, 240, 240)
SW_START_TEXT_COLOR = (0, 0, 0)
SW_INPUT_FIELD_COLOR = (255, 255, 255)
SW_BUTTON_INACTIVE_COLOR = (150, 150, 150)
SW_BUTTON_ACTIVE_COLOR = (200, 200, 200)
SW_BUTTON_TEXT_COLOR = (0, 0, 0)


"""
Обшие значения
"""
"""FPS var"""
FPS_VAR = 30