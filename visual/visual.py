import pygame
import visual_settings
import os


class SetUpCanvas:
    """
    Настройки отображения окна
    screen: размер
    name: имя окна
    font: шрифт и размер
    os: выравнивание по центру
    """
    def __init__(self):
        self.screen = None
        self.name = None
        self.font = None

    def set_up_canvas(self, screen, name, font):
        self.screen = pygame.display.set_mode(screen)
        pygame.display.set_caption(name)
        self.font = font
        os.environ['SDL_VIDEO_CENTERED'] = '1'


class Launch:
    """
    обработка циклов и отслеж нажатий кнопок
    """
    def __init__(self):
        self.clock = None
        self.running = None

    def launch(self):
        """
        цикл обновления
        """
        while self.running:
            self.game_events()
            self.clock.tick(visual_settings.FPS_VAR)

    def game_events(self):
        """
        отслеживание нажатия клавиш
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.handle_kay_press(event.key)
                
    def handle_kay_press(self, key):
        """
        обработка нажатия клавиш
        """
        if key == pygame.K_ESCAPE:
            self.running = False

        elif key == pygame.K_BACKSPACE:
            pass

        elif 49 <= key <= 57:
            pass

        elif key == pygame.K_RETURN:
            pass


class Button:
    def __init__(self, x, y, width, height, button_text=None, on_click_function=None, one_press=False):
        pygame.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_text = button_text
        self.on_click_Function = on_click_function
        self.one_press = one_press
        self.already_pressed = False

        self.fill_colors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

    def render(self):
        pass


class Game(SetUpCanvas, Launch):
    """
    основное окно игры
    """
    def __init__(self):
        super().__init__()
        pygame.init()
        self.set_up_canvas(visual_settings.SIZE_MAIN_WINDOWS, visual_settings.NAME_MAIN_WINDOWS,
                           visual_settings.MAIN_FONT)
        self.running = True
        self.start_new_game()
        self.clock = pygame.time.Clock()

    def start_new_game(self):
        """
        Пока что только перевенная для последующего вывода победителя
        """
        self.winner = []

    def __del__(self):
        """
        pygame close
        """
        pygame.quit()


class StartWindows(SetUpCanvas, Launch):
    """
    Стартовое окно
    после ввода количества играков передает в Game
    и закрывается
    """
    def __init__(self):
        super().__init__()
        pygame.init()
        self.set_up_canvas(visual_settings.SIZE_START_WINDOWS, visual_settings.NAME_START_WINDOWS,
                           visual_settings.FONT_START_WINDOWS)
        self.clock = pygame.time.Clock()
        self.running = True
        self.draw()

    def launcher(self):
        """запуск"""
        self.launch()

    def handle_kay_press(self, key):
        """
        переопределение функции
        запуск основного окна
        """
        if key == pygame.K_RETURN:
            """запуск основного окна, закрытие стартового окна"""
            class_game_start = Game()
            class_game_start.launch()
            self.running = False

    def draw(self):
        self.screen.fill(visual_settings.START_BG_COLOR)
        self.prompt()
        self.button_ok()
        pygame.display.flip()

    def prompt(self):
        """
        поле ввода количество играков
        """
        num_players = self.font.render(visual_settings.TEXT_NUM_PLAYERS, True, visual_settings.START_TEXT_COLOR)
        text_rect = num_players.get_rect()
        text_rect.x, text_rect.y = 20, 30
        self.screen.blit(num_players, text_rect)

    def button_ok(self):
        """
        кнопка передает количество играков в логику и отрисовку
        """
        pass


starting_start_windows = StartWindows()
starting_start_windows.launcher()
