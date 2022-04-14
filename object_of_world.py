from object import Object

class ObjectOfWorld(Object):

    def __init__(self, x, y, position_x, position_y):
        assert position_x > 0 and position_y > 0, "Position of the object must be greater than 0"
        super().__init__(x, y)
        self.dimension_x = x
        self.dimension_y = y
        self.position_x = position_x 
        self.position_y = position_y 