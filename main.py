# Importing libraries
import pygame, sys, random

# Importing modules from packet

from code_files.interface import Interface
from code_files.button import Button
from code_files.coin import Coin
from code_files.config import *

# Setting up display
pygame.init() # Initializing pygame
WIN = pygame.display.set_mode(STARTINGWINSIZE, pygame.RESIZABLE) # Creating window
pygame.display.set_caption(TITLE) # Setting title for window

# Main round class
class Round:
    global __clock
    __clock = pygame.time.Clock()

    def __init__(self, current_round_id=1):
        self.current_round_id = current_round_id # Defining Round setting
        
        # Define attributes, depends on round id
        match self.current_round_id:
            case 1:
                self.CURRENT_QUESTIONS_LIST = QUESTIONS_FOR_ROUND1
                self.CURRENT_AMMOUNT_OF_BTNS = AMMOUNT_OF_BUTTONS_FR1
            case 2: 
                self.CURRENT_QUESTIONS_LIST = QUESTIONS_FOR_ROUND2
                self.CURRENT_AMMOUNT_OF_BTNS = AMMOUNT_OF_BUTTONS_FR2
            case 3:
                self.CURRENT_QUESTIONS_LIST = QUESTIONS_FOR_ROUND3
                self.CURRENT_AMMOUNT_OF_BTNS = AMMOUNT_OF_BUTTONS_FR3
        
        # Create an interface 
        self.interface = Interface(WIN = WIN, round_id = current_round_id)

        self.defineObjects()

        self.gameIteration()

        self.gameLoop()

    def gameIteration(self):
        pass

    def gameLoop(self):
        while True:
            # Setting fps
            __clock.tick(MAXFPS)
            
            # Update
            self.current_win_size = pygame.display.get_window_size()
            self.current_win_x, self.current_win_y = self.current_win_size

            # Adaptive
            self.x_offset = 0
            if self.current_win_size >= STARTINGWINSIZE:
                self.x_offset = (self.current_win_x - 1000) / 2
            else:
                self.x_offset = 0

            self.button_group.update(self.x_offset)

            self.interface.update(win_size=self.current_win_size, x_offset = self.x_offset)
            self.button_group.draw(WIN)

            # Event loop
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update display
            pygame.display.flip()

    def defineObjects(self):
        # Algorith for defining possible button ids
        self.availiable_button_ids = []
        for i in range(0, self.CURRENT_AMMOUNT_OF_BTNS):
            self.availiable_button_ids.append(i)

        random.shuffle(self.availiable_button_ids)
        
        # Algorith for creating objects for buttons
        self.button_group = pygame.sprite.Group()
        self.button_objects = {}
        for i in range(0, self.CURRENT_AMMOUNT_OF_BTNS):
            self.button_objects[f"button{i}"] = Button(ans_id = self.availiable_button_ids[0], ammount_of_btns = self.CURRENT_AMMOUNT_OF_BTNS, _id = i)
            self.button_group.add(self.button_objects[f"button{i}"])
            self.availiable_button_ids.pop(0)
        print(self.button_group)
        
        # Algorith for creating objects for coins
        self.coin_objects = {  
    
            
        }
        for i in range(0, AMMOUNT_OF_COINS):
            self.coin_objects[f"coin{i}"] = Coin(coin_id = i)
    
    def loseEvent(self):
        pass

    def winEvent(self):
        pass

if __name__ == "__main__":
    round1 = Round()