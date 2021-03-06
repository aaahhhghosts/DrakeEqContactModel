import pygame, math
from constants import green

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = green
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)



class Slider():
    def __init__(self, name, val, maxi, mini, pos):
        pygame.init()
        font = pygame.font.SysFont("Consolas", 12)
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos, self.ypos = pos
        self.surf = pygame.surface.Surface((100, 60))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 17))



        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, GREY, [0, 0, 100, 60], 3)
        pygame.draw.rect(self.surf, GREEN, [10, 10, 80, 13], 0)
        pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes


        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, GREEN, (10, 10), 4, 0)

    def draw(self, screen, cur_val):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        font = pygame.font.SysFont("Consolas", 12)
        self.txt_val_surf = font.render(str('{0:.4g}'.format(cur_val)), 1, BLACK)
        self.txt_val_rect = self.txt_val_surf.get_rect(center=(50, 47))
        surf.blit(self.txt_val_surf, self.txt_val_rect)

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

        # screen
        screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi


def build_sliders(init_drake_vals, width, height):

    slides = []
    num_sliders = 7
    slider_labels = ["R*", "fp", "ne", "fl", "fi", "fc", "L"]
    slider_max_vals = [5000, 1, 5, 1, 1, 1, 100]

    for i in range(num_sliders):
        slide_pos = width - 150, height - 450 - 75*i
        s = Slider(slider_labels[i], init_drake_vals[i], slider_max_vals[i], 0.01, slide_pos)
        slides.append(s)

    return slides
