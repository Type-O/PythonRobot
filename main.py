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


def parse_direction(dir):
    if "NORTH" in dir:
        return Direction.NORTH
    elif "SOUTH" in dir:
        return Direction.SOUTH
    elif "EAST" in dir:
        return Direction.EAST
    elif "WEST" in Direction.WEST:
        return Direction.WEST


class InputParser:
    def __init__(self):
        self.instructions = []

    def parse_input_file(self, file):
        file = open(file, 'r')
        lines = file.readlines()
        for line in lines:
            parts = re.split(r" |,", line)

            for part in parts:
                if "PLACE" in part:
                    obj = [Instructions.PLACE, int(parts[1]), int(parts[2]), parse_direction(parts[3])]
                    self.instructions.append(obj)
                elif "MOVE" in part:
                    self.instructions.append(Instructions.MOVE)
                elif "LEFT" in part:
                    self.instructions.append(Instructions.LEFT)
                elif "RIGHT" in part:
                    self.instructions.append(Instructions.RIGHT)
                elif "REPORT" in part:
                    self.instructions.append(Instructions.REPORT)



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

    def run_instructions(self, instruction_set):
        if not self.placed and bool(instruction_set[0][0] is not Instructions.PLACE):
            return
        else:
            for instruction in instruction_set:
                print("Hello")



def main():
    """ Main program """
    # Code goes over here.

    robot = PythonRobot()
    i = InputParser()
    i.parse_input_file("InstructionSetOne.txt")

    robot.run_instructions(i.instructions)

    return 0


if __name__ == "__main__":
    main()
