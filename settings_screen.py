import pygame
from settings import *
from text import Text
from button import Button


class SettingsScreen:
    def __init__(self,create_title):
        # general setup
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT,OW_FONT_SIZE)
        self.create_title = create_title

        # text and buttons setup
        self.music_text = Text('Music',(WIDTH/2-300,HEIGHT/2-200))
        self.volume_text = Text('Volume',(WIDTH/2-300,HEIGHT/2-150))
        self.controls_text = Text('Controls',(WIDTH/2-300,HEIGHT/2-100))
        self.create_controls()
        self.back_button = Button('BACK',(10,5),self.create_title)

    def create_controls(self):
        # controls text setup
        self.keys = []
        self.actions = []
        for i in range(len(CONTROLS)):
            key = CONTROLS[i][0]
            act = CONTROLS[i][1]
            self.keys.append(Button(key,(WIDTH/2-100,HEIGHT/2-100+(i*50)),self.blank))
            self.actions.append(Text(act,(WIDTH/2+150,HEIGHT/2-100+(i*50))))

    def blank(self):
        # button function placeholder
        pass

    def run(self):
        # update and draw the settings screen
        self.music_text.display()
        self.volume_text.display()
        self.controls_text.display()
        for key in self.keys:
            key.display()
        for act in self.actions:
            act.display()
        self.back_button.display()