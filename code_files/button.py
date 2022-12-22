import pygame, math


class Button(pygame.sprite.Sprite):
    def __init__(self, ans_id, ammount_of_btns, _id):
        super().__init__()
        print(f"Initializing button {_id}")

        self.ans_id = ans_id # id of an answer
        self.id = _id        # id of a button
        self.ammount_of_btns = ammount_of_btns  # defining argument as a variable
        self.y_pos = 100     # y position of a button 
        
        self.cords, self.size = self.defCords(self.id, self.ammount_of_btns) # Defining cords for the button
        print(self.id)

        # Define sprite attributes
        self.image = pygame.image.load("Resources/Backgrounds/blank_png_file.png")
        self.image = pygame.transform.scale(self.image, (self.size))
        self.rect = self.image.get_rect(topleft = self.cords)

    @staticmethod
    def defCords(_id, ammount_of_buttons):
        
        @staticmethod
        def defSize(ammount_of_buttons):
            # Defining size of a button
            if ammount_of_buttons <= 12:
                size = 225
                ammount_of_buttons_in_one_row = 4
                four_in_one_row = 0
            elif ammount_of_buttons > 12:
                size = 176
                ammount_of_buttons_in_one_row = 5
                four_in_one_row = 1

            return size, four_in_one_row, ammount_of_buttons_in_one_row
        
        @staticmethod
        def defRows(spare_buttons, ammount_of_buttons, ammount_of_buttons_in_one_row, four_in_one_row):

            def defTopBottomRows(spare_buttons, four_in_one_row):
                match four_in_one_row:
                    case 0:
                        top_row = 0
                        bottom_row = 0
                        match spare_buttons:
                            case 1:
                                top_row = 3
                                bottom_row = 2
                            case 2:
                                top_row = 4
                                bottom_row = 2
                            case 3:
                                top_row = 4
                                bottom_row = 3
                    case 1:
                        top_row = 5
                        bottom_row = 0
                        match spare_buttons:
                            case 1:
                                top_row = 4
                                bottom_row = 2
                            case 2:
                                bottom_row = 2
                            case 3:
                                bottom_row = 3
                            case 4:
                                bottom_row = 4

                rows_sum = top_row + bottom_row
                return top_row, bottom_row, rows_sum

            def defMidRows(ammount_of_buttons, rows_sum):
                mid_row = ammount_of_buttons - rows_sum
                return mid_row
            
            def findIds(top_row_buttons, bottom_row_buttons, mid_row_buttons):
                top_row_ids = []
                mid_row_ids = []
                bottom_row_ids = []
            
                iterations = 0
                for i in range(top_row_buttons):
                    top_row_ids.append(iterations)
                    iterations += 1
                for i in range(mid_row_buttons):
                    mid_row_ids.append(iterations)
                    iterations += 1
                for i in range(bottom_row_buttons):
                    bottom_row_ids.append(iterations)
                    iterations += 1
                
                return top_row_ids, mid_row_ids, bottom_row_ids

            top_row_buttons, bottom_row_buttons, sum_top_bottom = defTopBottomRows(spare_buttons, four_in_one_row)
            mid_row_buttons = defMidRows(ammount_of_buttons, sum_top_bottom)
            top_row_ids, mid_row_ids, bottom_row_ids = findIds(top_row_buttons, bottom_row_buttons, mid_row_buttons)

            return top_row_ids, mid_row_ids, bottom_row_ids
        
        @staticmethod
        def defCords(size, _id, ammount_of_buttons_in_one_row, top_row_ids, mid_row_ids, bottom_row_ids, ammount_of_buttons):
            ammount_of_mid_rows = len(mid_row_ids) // ammount_of_buttons_in_one_row
            print(ammount_of_mid_rows)
            cords_list = []
            for button_id in top_row_ids:
                if button_id == _id:                        
                    x = (((size + 20) * _id - ammount_of_buttons_in_one_row) + 20)
                    y =  220

            for button_id in mid_row_ids:
                if button_id == _id:                        
                    x = (((size + 20) * _id - ammount_of_buttons_in_one_row) + 20) - 980
                    y =  440
            
            for button_id in bottom_row_ids:
                if button_id == _id:       
                    if len(bottom_row_ids) < ammount_of_buttons_in_one_row:
                        x_offset = 0
                        x_offset2 = (len(bottom_row_ids) * (size + 20)) / 2
                        x_offset = 500-x_offset2
                        print(f"x" +  str(x_offset2))
                        x = x_offset + (((size + 20) * _id - ammount_of_buttons_in_one_row) + 20) - (980 * 2)
                        y =  680 
                    else:
                        x = (((size + 20) * _id - ammount_of_buttons_in_one_row) + 20) - (980 * 2)
                        y =  680
                    cords_list.append(x)
            



            cords = (x, y)
            return cords

        size, four_in_one_row, ammount_of_buttons_in_one_row = defSize(ammount_of_buttons)

        spare_buttons = ammount_of_buttons % ammount_of_buttons_in_one_row
        
        top_row_ids, mid_row_ids, bottom_row_ids = defRows(spare_buttons, ammount_of_buttons, ammount_of_buttons_in_one_row, four_in_one_row)

        print(top_row_ids, mid_row_ids, bottom_row_ids)
        cords = defCords(size, _id, ammount_of_buttons_in_one_row, top_row_ids, mid_row_ids, bottom_row_ids, ammount_of_buttons)
    
        return cords, (size, size)

    def eventClick(self):
        pass

    def update(self, x_offset):
        self.x, self.y = self.cords
        self.rect = self.image.get_rect(topleft = (self.x + x_offset, self.y) )

