class Object:

    def __init__(self, x, y):
        assert x > 0 and y > 0, "Dimension of the object must be greater than 0"
        self.dimension_x = x
        self.dimension_y = y

    