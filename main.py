from enum import Enum
import re


# Helper functions
def check_coord(i):
    if i < 0 or i > 4:
        return False
    else:
        return True


def check_dir(i):
    if i < 1 or i > 4:
        return False
    else:
        return True


class Direction(Enum):
    INIT = 0
    NORTH = 1
    SOUTH = 3
    EAST = 4
    WEST = 2


class Instructions(Enum):
    PLACE = 0
    MOVE = 1
    REPORT = 2
    LEFT = 3
    RIGHT = 4


class InputParser:
    def __init__(self):
        self.instructions

    def parse_input_file(self, file):
        file = open(file, 'r')
        lines = file.readlines()
        for line in lines:
            parts = re.split(r" |,", line)

            for part in parts:
                if "PLACE" in part:
                    self.instructions.append([int(Instructions.PLACE), int(parts[1]), int(parts[2]), Direction(int(parts[3]))])
                elif "MOVE" in part:
                    self.instructions.append(int(Instructions.MOVE))
                elif "LEFT" in part:
                    self.instructions.append(int(Instructions.LEFT))
                elif "RIGHT" in part:
                    self.instructions.append(int(Instructions.RIGHT))
                elif "REPORT" in part:
                    self.instructions.append(int(Instructions.REPORT))



class PythonRobot:

    def __init__(self):
        self.world_location = [-1, -1]
        self.dir = Direction
        self.dir = Direction.INIT
        self.placed = False

    def report(self):

        string = ""

        if not self.placed:
            string = "Not yet placed!"
        else:
            string += "[" + str(self.world_location[0]) + "," + str(self.world_location[1]) + "], "

            if Direction(self.dir) == Direction.SOUTH:
                string += "SOUTH"
            elif Direction(self.dir) == Direction.EAST:
                string += "EAST"
            elif Direction(self.dir) == Direction.WEST:
                string += "WEST"
            elif Direction(self.dir) == Direction.NORTH:
                string += "NORTH"

        print(string)

    def place(self, x, y, f):
        if not check_coord(x) & check_coord(y) & check_dir(f):
            print("Invalid coords")
        else:
            self.world_location[0] = x
            self.world_location[1] = y
            self.dir = f
            self.placed = True

    def rotate_left(self):
        if not self.placed:
            return
        elif self.dir == 1:
            self.dir = 4
        else:
            self.dir -= 1

    def rotate_right(self):
        if not self.placed:
            return
        else:
            self.dir += 1
            if self.dir > 4:
                self.dir = 1

    def move(self):
        if not self.placed:
            return
        elif self.dir is Direction.NORTH & check_coord(self.world_location[0]):
            self.world_location += 1
        elif self.dir is Direction.SOUTH & check_coord(self.world_location[0]):
            self.world_location -= 1
        elif self.dir is Direction.WEST & check_coord(self.world_location[1]):
            self.world_location += 1
        elif self.dir is Direction.EAST & check_coord(self.world_location[1]):
            self.world_location -= 1


def main():
    """ Main program """
    # Code goes over here.

    robot = PythonRobot()
    robot.report()

    robot.rotate_right()
    robot.place(1, 1, 1)
    robot.report()
    robot.rotate_right()
    robot.report()
    robot.rotate_right()
    robot.report()
    robot.rotate_right()
    robot.report()
    robot.rotate_right()
    robot.report()
    robot.rotate_right()

    i = InputParser()
    i.parse_input_file("InstructionSetOne.txt")

    return 0


if __name__ == "__main__":
    main()
