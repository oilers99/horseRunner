import pygame
pygame.init()

"""
Параметры главного окна class Game
"""
"""Размер главного окна"""
size_main_x, size_main_y = 1600, 800
SIZE_MAIN_WINDOWS = (size_main_x, size_main_y)
"""Заголовок окна"""
NAME_MAIN_WINDOWS = "_HorseRacer_"
"""Икона окна"""
ICON_WINDOWS = None
"""Шрифт и размер для теста"""
MAIN_FONT = pygame.font.SysFont('arial', 32)


"""
Параметры стартового окна class StartWindows
"""
"""Размер стартового окна"""
size_start_x, size_start_y = 350, 200
SIZE_START_WINDOWS = (size_start_x, size_start_y)
"""Заголовок окна"""
NAME_START_WINDOWS = "_HorseRacer_"
"""Икона окна"""
ICON_START_WINDOWS = None
"""Шрифт и размер для теста"""
FONT_START_WINDOWS = pygame.font.SysFont('arial', 20)
"""Текст запроса количества играков"""
TEXT_NUM_PLAYERS = "Введите количество играков (2-8)"
"""цвет стартового БГ"""
START_BG_COLOR = (255, 255, 255)
START_TEXT_COLOR = (0, 0, 0)


"""
Обшие значения
"""
"""FPS var"""
FPS_VAR = 30