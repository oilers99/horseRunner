import pygame
import visual_settings
import os
pygame.init()

class StartWindows:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.set_up_canvas()
        self.prompt = Prompt(visual_settings.INPUT_FIELD_COLOR,
                             (20, 70, 315, 25),
                             (350 // 2),
                             ((70 * 0.7) + 70 // 2),
                             visual_settings.START_TEXT_COLOR)
        self.text_1 = Text(self.font, text=visual_settings.TEXT_NUM_PLAYERS,
                           color_text=visual_settings.START_TEXT_COLOR,
                           pos_x= 20, pos_y= 30,
                           screen=self.screen)
        self.launch()


    def set_up_canvas(self):
        self.screen = pygame.display.set_mode(visual_settings.SIZE_START_WINDOWS)
        pygame.display.set_caption(visual_settings.NAME_START_WINDOWS)
        self.font = visual_settings.FONT_START_WINDOWS
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def launch(self):
        while self.running:
            self.game_event()
            self.clock.tick(visual_settings.FPS_VAR)
            self.draw()

    def game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.kay_press(event.key)

    def kay_press(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        if 50 <= key <= 56:
            self.prompt.value = str(key - 48)
            print(self.prompt.value)

    def draw(self):
        self.bg_color()
        self.prompt.input(self.screen, self.font)
        self.text_1.draw_text()
        pygame.display.flip()

    def bg_color(self):
        self.screen.fill(visual_settings.START_BG_COLOR)


class Prompt:
    """
    поле ввода текста
    """

    def __init__(self, input_field_color, rect, centre_x, centre_y, text_color):
        """
        @param input_field_color: цвет поля ввода. кортеж РГБ
        @param rect: размер поля ввода кортеж (х, у, длинна, ширина)
        @param centre_x: центровка вывода текста по Х число или формула
        @param centre_y: центровка вывода текста  по У число или формула
        @param text_color: цвет текста вывода. кортеж РГБ
        """
        # вывод текста
        self.value = ""

        self.input_field_color = input_field_color
        self.rect = rect
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.text_color = text_color

    def input(self, screen, font):
        """
        @param screen: in draw self.screen поле где рисовать
        @param font: in draw self.font шрифт окна
        """
        pygame.draw.rect(screen, self.input_field_color, self.rect)
        text_input = font.render(self.value, True, self.text_color)
        text_input_rect = text_input.get_rect()
        text_input_rect.centerx = self.centre_x
        text_input_rect.centery = self.centre_y
        screen.blit(text_input, text_input_rect)


class Text:
    """
    отрисовка текста на окне
    """
    def __init__(self, font, text, color_text, pos_x, pos_y, screen):
        """
        @param font: шрифт
        @param text: текст
        @param color_text: цвет текста
        @param pos_x: позиция Х
        @param pos_y: позиция У
        @param screen: окно на котором рисовать
        """
        self.font = font
        self.text = text
        self.color_text = color_text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.screen = screen

    def draw_text(self):
        text = self.font.render(self.text, True, self.color_text)
        text_rect = text.get_rect()
        text_rect.x = self.pos_x
        text_rect.y = self.pos_y
        self.screen.blit(text, text_rect)


start_windows = StartWindows()

