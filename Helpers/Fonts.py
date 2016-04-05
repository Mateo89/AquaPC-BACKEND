__author__ = 'mateo'

import pygame

class Fonts:

    font_10 = None
    font_20 = None
    font_30 = None
    font_40 = None
    font_50 = None
    font_60 = None
    font_100 = None

    @staticmethod
    def initFonts():
        Fonts.font_10 = pygame.font.Font(None, 10)
        Fonts.font_20 = pygame.font.Font(None, 20)
        Fonts.font_30 = pygame.font.Font(None, 30)
        Fonts.font_40 = pygame.font.Font(None, 40)
        Fonts.font_50 = pygame.font.Font(None, 50)
        Fonts.font_60 = pygame.font.Font(None, 60)
        Fonts.font_100 = pygame.font.Font(None, 80)
