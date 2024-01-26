import pygame
import creator_horse
import visual_settings
import os
import random
pygame.init()


class StartWindows:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.set_up_canvas()
        self.prompt = Prompt(visual_settings.SW_INPUT_FIELD_COLOR,
                             (20, 70, 315, 25),
                             (350 // 2),
                             ((70 * 0.7) + 70 // 2),
                             visual_settings.SW_START_TEXT_COLOR)
        self.text_1 = Text(self.font, text=visual_settings.SW_TEXT_NUM_PLAYERS,
                           color_text=visual_settings.SW_START_TEXT_COLOR,
                           pos_x=20, pos_y=30,
                           screen=self.screen)
        self.button_ok = Button(rect=(150, 120, 50, 25), pos_x=175, pos_y=132,
                                inactive_color=visual_settings.SW_BUTTON_INACTIVE_COLOR,
                                active_color=visual_settings.SW_BUTTON_ACTIVE_COLOR,
                                massage="OK",
                                massage_color=visual_settings.SW_BUTTON_TEXT_COLOR)
        self.horse_creator = creator_horse.Creator()
        self.launch()

    def set_up_canvas(self):
        self.screen = pygame.display.set_mode(visual_settings.SW_SIZE_START_WINDOWS)
        pygame.display.set_caption(visual_settings.SW_NAME_START_WINDOWS)
        self.font = visual_settings.SW_FONT_START_WINDOWS
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_icon(visual_settings.MAIN_ICON_WINDOWS)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.kay_press(event.button)

    def kay_press(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        if 50 <= key <= 56:
            self.prompt.value = str(key - 48)
            print(self.prompt.value)
        if len(self.prompt.value) == 1:
            if self.button_ok.active_button == True:
                if key == 1:
                    self.running = False
                    MainWindows(int(self.prompt.value))
        if len(self.prompt.value) == 1:
            if key == pygame.K_RETURN:
                self.running = False
                MainWindows(int(self.prompt.value))
        if len(self.prompt.value) == 1:
            if key == pygame.K_BACKSPACE:
                self.prompt.value = self.prompt.value[:-1]

    def draw(self):
        self.bg_color()
        self.prompt.input(self.screen, self.font)
        self.text_1.draw_text()
        self.button_ok.draw(self.screen, self.font)
        pygame.display.flip()

    def bg_color(self):
        self.screen.fill(visual_settings.SW_START_BG_COLOR)


class MainWindows:
    def __init__(self, number_of_players):
        self.start_press = False
        self.horse_creator = creator_horse.Creator()
        self.button_start = Button(rect=(740, 950 , 120, 50), pos_x=800, pos_y=975,
                                   inactive_color=visual_settings.MAIN_BUTTON_INACTIVE_COLOR,
                                   active_color=visual_settings.MAIN_BUTTON_ACTIVE_COLOR, massage="START",
                                   massage_color=visual_settings.MAIN_BUTTON_TEXT_COLOR)

        self.number_of_players = number_of_players
        self.horse_creator.name_creator(self.number_of_players)
        self.running = True
        self.clock = pygame.time.Clock()
        self.set_up_canvas()
        self.poss_x = 110
        self.poss_x_1 = 110
        self.poss_x_2 = 110
        self.poss_x_3 = 110
        self.poss_x_4 = 110
        self.poss_x_5 = 110
        self.poss_x_6 = 110
        self.poss_x_7 = 110
        self.poss_x_8 = 110

        self.launch()

    def set_up_canvas(self):
        self.screen = pygame.display.set_mode(visual_settings.MAIN_SIZE_WINDOWS)
        pygame.display.set_caption(visual_settings.MAIN_NAME_WINDOWS)
        self.font = visual_settings.MAIN_FONT
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.kay_press(event.button)

    def kay_press(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        if key == pygame.K_RETURN:
            self.start_press = True
        if key == 1:
            self.start_press = True

    def draw(self):
        self.draw_bg_imege()
        self.draw_title()
        self.draw_roads()
        self.draw_lines_start_finish()
        self.draw_name_horses()
        self.button_start.draw(self.screen, self.font)
        self.draw_horses()
        pygame.display.flip()

    def draw_bg_imege(self):
        self.screen.blit(visual_settings.MAIN_BG, (0, 0))

    def draw_title(self):
        self.screen.blit(visual_settings.MAIN_TITLE, (0,0))

    def draw_roads(self):
        poss_y = 290
        for i in range(int(self.number_of_players)):
            self.screen.blit(visual_settings.MAIN_ROAD, (100, poss_y))
            poss_y += 80

    def draw_lines_start_finish(self):
        poss_y = 290
        for i in range(int(self.number_of_players)):
            self.screen.blit(visual_settings.MAIN_START_LINE, (195, poss_y))
            self.screen.blit(visual_settings.MAIN_FINISH_LINE, (1435, poss_y))
            poss_y += 80

    def draw_name_horses(self):
        poss_y = 310
        for text in self.horse_creator.list_name_horse:
            self.name_horse_text = Text(font=self.font, text=text,
                                        color_text=visual_settings.MAIN_NAME_TEXT_COLOR,
                                        pos_x=250, pos_y=poss_y, screen=self.screen)
            self.name_horse_text.draw_text()
            poss_y += 80

    def draw_horses(self):
        """
        долбаный хард

        """
        vin_line = 1350
        start_random = 0
        stop_random = 3
        self.poss_y = 290

        if int(self.number_of_players) == 2:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y ))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 3:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 4:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_4, self.poss_y + 240))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                self.poss_x_4 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3, self.poss_x_4)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 5:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_4, self.poss_y + 240))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_5, self.poss_y + 320))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                self.poss_x_4 += random.randint(start_random, stop_random)
                self.poss_x_5 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3, self.poss_x_4, self.poss_x_5)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 6:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_4, self.poss_y + 240))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_5, self.poss_y + 320))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_6, self.poss_y + 400))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                self.poss_x_4 += random.randint(start_random, stop_random)
                self.poss_x_5 += random.randint(start_random, stop_random)
                self.poss_x_6 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3, self.poss_x_4, self.poss_x_5,
                                self.poss_x_6)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 7:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_4, self.poss_y + 240))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_5, self.poss_y + 320))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_6, self.poss_y + 400))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_7, self.poss_y + 480))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                self.poss_x_4 += random.randint(start_random, stop_random)
                self.poss_x_5 += random.randint(start_random, stop_random)
                self.poss_x_6 += random.randint(start_random, stop_random)
                self.poss_x_7 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3, self.poss_x_4, self.poss_x_5,
                                self.poss_x_6, self.poss_x_7)
                if super_pos >= vin_line:
                    self.start_press = False

        elif int(self.number_of_players) == 8:
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_1, self.poss_y))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_2, self.poss_y + 80))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_3, self.poss_y + 160))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_4, self.poss_y + 240))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_5, self.poss_y + 320))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_6, self.poss_y + 400))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_7, self.poss_y + 480))
            self.screen.blit(visual_settings.MAIN_TRACTOR, (self.poss_x_8, self.poss_y + 560))
            if self.start_press == True:
                self.poss_x_1 += random.randint(start_random, stop_random)
                self.poss_x_2 += random.randint(start_random, stop_random)
                self.poss_x_3 += random.randint(start_random, stop_random)
                self.poss_x_4 += random.randint(start_random, stop_random)
                self.poss_x_5 += random.randint(start_random, stop_random)
                self.poss_x_6 += random.randint(start_random, stop_random)
                self.poss_x_7 += random.randint(start_random, stop_random)
                self.poss_x_8 += random.randint(start_random, stop_random)
                super_pos = max(self.poss_x_1, self.poss_x_2, self.poss_x_3, self.poss_x_4, self.poss_x_5,
                                self.poss_x_6, self.poss_x_7, self.poss_x_8)
                if super_pos >= vin_line:
                    self.start_press = False


class NewGame:
    pass

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


class Button:
    def __init__(self, rect, pos_x, pos_y, inactive_color, active_color, massage,
                 massage_color):
        """
        @param rect: размер поля ввода кортеж (х, у, длинна, ширина)
        @param pos_x: поза по Х
        @param pos_y: поза по У
        @param inactive_color: неактивный цвет (РГБ)
        @param active_color: цвет при наведение (РГБ)
        @param massage: текст кнопки
        @param massage_color: цвет ткста (РГБ)
        """
        self.rect = rect
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.massage = massage
        self.massage_color = massage_color
        self.tmp_color = self.inactive_color
        self.active_button = False

    def draw(self, screen, font):
        """
        @param screen: где рисовать self.screen
        @param font: параметрт шрифта self.font
        """
        pygame.draw.rect(screen, self.tmp_color, self.rect)
        text_input = font.render(self.massage, True, self.massage_color)
        text_input_rect = text_input.get_rect()
        text_input_rect.centerx = self.pos_x
        text_input_rect.centery = self.pos_y
        screen.blit(text_input, text_input_rect)
        pos_mouse = pygame.mouse.get_pos()
        if self.rect[0] < pos_mouse[0] < self.rect[0] + self.rect[2]:
            if self.rect[1] < pos_mouse[1] < self.rect[1] + self.rect[3]:
                self.tmp_color = self.active_color
                self.active_button = True
            else:
                self.tmp_color = self.inactive_color
        else:
            self.tmp_color = self.inactive_color


StartWindows()
