from object import Object
from robot import Robot
from object_of_world import ObjectOfWorld

class World(Object):

    def __init__(self, x, y, x_robot, y_robot
                 , position_robot_x, position_robot_y
                 , x_object, y_object, position_object_x, position_object_y):
        assert x_robot < x and y_robot < y, "Robot must be smaller than the world"
        assert x_object < x and y_object < y, "Object must be smaller than the world"
        assert position_robot_x < x and position_robot_y < y, "Robot position must be smaller than the world"
        assert position_object_x < x and position_object_y < y, "Object position must be smaller than the world"

        super().__init__(x, y)
        self.robot = Robot(x_robot, y_robot, position_robot_x, position_robot_y, self)
        self.object = ObjectOfWorld(x_object, y_object, position_object_x, position_object_y)
        
