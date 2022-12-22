import pygame
from code_files.config import CP_COLOR, FOREGROUND_VISIBILITY, HP_COLOR, TEXTLESSONCOLOR, TEXTROUNDCOLOR

class Interface:
    def __init__(self, WIN, round_id):

            # Define variables
            self.WIN = WIN
            self.round_id = round_id

            # Import font
            self.font = pygame.font.Font('''Resources/Fonts/arial.ttf''', 50)

            # Create a dictionary containing all images
            self.interface = {   
                "foreground" : pygame.image.load("Resources/Backgrounds/foreGround.png").convert_alpha(),
                "background" : pygame.image.load("Resources/Backgrounds/FarmBackground.png").convert_alpha(),
                "left_pb_segment" : pygame.image.load("Resources/Sprites/left_pb_segment.png").convert_alpha(),
                "middle_pb_segment" : pygame.image.load("Resources/Sprites/middle_pb_segment.png").convert_alpha(),
                "right_pb_segment" : pygame.image.load("Resources/Sprites/right_pb_segment.png").convert_alpha(),
                "content_panel" : pygame.image.load("Resources/Backgrounds/blank_png_file.png").convert_alpha(),
                "header_panel" : pygame.image.load("Resources/Backgrounds/blank_png_file.png").convert_alpha()
            }

            # Creating texts
            self.text_lesson = self.font.render("Lesson 1", True, TEXTLESSONCOLOR)
            self.text_round = self.font.render(f"Round {self.round_id}", True, TEXTROUNDCOLOR)

            # Scale Surfaces
            self.interface["middle_pb_segment"] = pygame.transform.scale(self.interface["middle_pb_segment"], (90, 90))
            self.interface["left_pb_segment"] = pygame.transform.scale(self.interface["left_pb_segment"], (90, 90))
            self.interface["right_pb_segment"] = pygame.transform.scale(self.interface["right_pb_segment"], (90, 90))
            self.interface["header_panel"] = pygame.transform.scale(self.interface["header_panel"], (960, 180))

            # Fill surfaces
            self.interface["content_panel"].fill((CP_COLOR))
            self.interface["header_panel"].fill((HP_COLOR))

    def update(self, win_size, x_offset):
        # Update size of surfaces
        self.win_x, self.win_y = win_size
        self.foreground_rect = self.interface["foreground"].get_rect(bottomleft = (0, self.win_y))
        self.interface['foreground'] = pygame.transform.scale(self.interface["foreground"], (self.win_x, 700))
        self.interface["background"] = pygame.transform.scale(self.interface["background"], win_size)
        self.interface["content_panel"] = pygame.transform.scale(self.interface["content_panel"], (1000, self.win_y))
        
            
        # Draw surfaces
        self.WIN.blit(self.interface["background"], (0, 0))
        self.WIN.blit(self.interface["content_panel"], (0 + x_offset, 0))
        if  self.win_x >= 1200 and self.win_y >= 800:
            if FOREGROUND_VISIBILITY == True:
                self.WIN.blit(self.interface["foreground"], self.foreground_rect)
        self.WIN.blit(self.interface["header_panel"], (20 + x_offset, 20))
        self.WIN.blit(self.interface["left_pb_segment"], (50 + x_offset, 90))
        self.WIN.blit(self.interface["right_pb_segment"], (770 + x_offset, 90))
        for i in range (0, 7):
            self.WIN.blit(self.interface["middle_pb_segment"], ((140 + (90 * i)) + x_offset, 90))
        self.WIN.blit(self.text_lesson, (50 + x_offset, 20))
        self.WIN.blit(self.text_round, (250 + x_offset, 20))
        
