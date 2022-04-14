from object_of_world import ObjectOfWorld


class Robot(ObjectOfWorld):

    def __init__(self, x, y, position_x, position_y ):
        super().__init__(x, y, position_x, position_y)
        self.velocity = 3
        self.path = []
        
    def move_up(self):
        self.path.append([[self.position_x, self.position_y], 
                            [self.position_x, self.position_y - self.velocity]])
        self.position_y -= self.velocity

    def move_down(self):
        self.path.append([[self.position_x, self.position_y],
                            [self.position_x, self.position_y + self.velocity]])
        self.position_y += self.velocity

    def move_left(self):
        self.path.append([[self.position_x, self.position_y],
                            [self.position_x, self.position_y - self.velocity]])
        self.position_x -= self.velocity

    def move_right(self):
        self.path.append([[self.position_x, self.position_y],
                            [self.position_x, self.position_y + self.velocity]])
        self.position_x += self.velocity

    
    