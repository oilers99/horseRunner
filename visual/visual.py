import pygame
import visual_settings


class Game:
    """
    основное окно игры
    """
    def __init__(self):
        pygame.init()
        self.set_up_canvas()
        self.running = True
        self.start_new_game()
        self.clock = pygame.time.Clock()

    def set_up_canvas(self):
        """
        settings windows
        """
        """create wind and param: SCALED"""
        self.screen = pygame.display.set_mode(visual_settings.SIZE_MAIN_WINDOWS)
        """name wind"""
        pygame.display.set_caption(visual_settings.NAME_WINDOWS)
        """icon wind"""
        # pygame.display.set_icon(visual_settings.ICON_WINDOWS) # вставить икону в переменную
        """Font"""
        self.font = visual_settings.FONT

    def start_new_game(self):
        """
        Пока что только перевенная для последующего вывода победителя
        """
        self.winner = []

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

    def __del__(self):
        """
        pygame close
        """
        pygame.quit()


class StartWindows:
    """
    Стартовое окно
    после ввода количества играков передает в Game
    и закрывается
    """
    def __init__(self):
        pygame.init()
        self.set_up_start_canvas()
        self.clock = pygame.time.Clock()
        self.running = True

    def set_up_start_canvas(self):
        """
        Параметры стартового окна
        """
        """create start wind"""
        self.screen = pygame.display.set_mode(visual_settings.SIZE_START_WINDOWS)
        """name start wind"""
        pygame.display.set_caption(visual_settings.NAME_START_WINDOWS)
        """icon start wind"""
        # pygame.display.set_icon(visual_settings.ICON_START_WINDOWS) # вставить икону в переменную
        """Font start wind"""
        self.font = visual_settings.FONT_START_WINDOWS

    def launch_start_windows(self):
        """
        цикл обновления
        """
        while self.running:
            self.game_events_start_windows()
            self.clock.tick(visual_settings.FPS_VAR)

    def game_events_start_windows(self):
        """
        отслеживание нажатия клавиш
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.handle_kay_press_for_start_windows(event.key)

    def handle_kay_press_for_start_windows(self, key):
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
            """запуск основного окна, закрытие стартового окна"""
            game = Game()
            game.launch()
            self.running = False


start_windows = StartWindows()
start_windows.launch_start_windows()
