import pygame
from settings import *
from text import Text


class TextBox:
    def __init__(self,pos):
        # general setup
        self.screen = pygame.display.get_surface()
        self.screen_colour = 'white'

        # text box setup
        self.text = ''
        self.pos = pos
        self.active = False

        # line flash
        self.flash = True
        self.flash_cooldown = 750
        self.flash_time = None

        # overlay rect -> allow you hide to textbox
        self.alpha = 255

    def draw_line(self):
        # draw flashing current character indicator
        current_time = pygame.time.get_ticks()

        # alternate between showing and not showing the line
        if current_time - self.flash_time >= self.flash_cooldown:
            self.flash = not self.flash
            self.flash_time = pygame.time.get_ticks()

        if self.flash:
            size = self.input_text.get_size()
            self.line = pygame.Rect((self.pos[0]+size[0]+5,self.pos[1]+2),(2,30))
            pygame.draw.rect(self.screen,COLOUR_4,self.line)

    def draw_text_box(self):
        # draw text box outline
        # change colour if the box has been selected
        if self.active:
            colour = COLOUR_4
            self.draw_line()
        else:
            colour = COLOUR_2

        self.rect = pygame.Rect(self.pos,(300,35))
        pygame.draw.rect(self.screen,colour,self.rect,1)

    def draw_text(self):
        # draw input text
        self.input_text = Text(self.text,(self.pos[0]+5,self.pos[1]-3))
        self.input_text.display()

    def check_hover(self):
        # change cursor to 'IBEAM' if the cursor is hovering over the text box
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

    def update(self,event_list):
        # update text box when key pressed
        for event in event_list:
            # cehck if the text box has been clicked on
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
                if self.active:
                    self.flash = True
                    self.flash_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN and self.active:
                # check return key
                if event.key == pygame.K_RETURN:
                    self.active = False
                else:
                    self.flash = True
                    self.flash_time = pygame.time.get_ticks()
                    # check backspace key
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    # append the letter pressed
                    else:
                        self.flash = True
                        self.flash_time = pygame.time.get_ticks()
                        if len(self.text) < 11: # 11 characters limit
                            self.text += event.unicode

    def get_text(self):
        return self.text

    def draw_overlay_rect(self):
        # draw overlay rectangle
        rect = pygame.Surface((self.rect.width+1,self.rect.height+1)) # rect has a border of 1 pixel wide
        rect.fill(self.screen_colour)
        rect.set_alpha(255-self.alpha)
        self.screen.blit(rect,(self.pos[0]-0.5,self.pos[1]-0.5))

    def set_alpha(self,alpha):
        # change alpha
        self.alpha = alpha

    def display(self,event_list):
        # update and draw text box
        self.draw_text()
        self.draw_text_box()
        self.draw_overlay_rect()
        self.check_hover()
        self.update(event_list)