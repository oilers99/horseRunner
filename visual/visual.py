import pygame
pygame.init()

import visual_settings


screen = pygame.display.set_mode(visual_settings.size_windows)
pygame.display.set_caption(visual_settings.name_windows)
# pygame.display.set_icon(visual_settings.icon_windows)  # Всатвить икону

test_text = visual_settings.font.render("Test_text", 0, (255, 0, 0), (0, 55, 55))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(test_text, (10, 10))
    pygame.display.update()
