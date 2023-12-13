import pygame
import visual_settings


class Game:
    """

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
        self.screen = pygame.display.set_mode(visual_settings.SIZE_WINDOWS, pygame.SCALED)
        """name wind"""
        pygame.display.set_caption(visual_settings.NAME_WINDOWS)
        """icon wind"""
        # pygame.display.set_icon(visual_settings.ICON_WINDOWS) # вставить икону в переменную

    def start_new_game(self):
        """

        """
        self.winner = []

    def launch(self):
        """

        """
        while self.running:
            self.game_events()
            self.clock.tick(visual_settings.FPS_VAR)

    def game_events(self):
        """

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

        elif 49 <= key <= 57:
            pass

        elif key == pygame.K_RETURN:
            pass


    def __del__(self):
        """
        pygame close
        """
        pygame.quit()


gam = Game()
gam.launch()


