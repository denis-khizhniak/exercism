import string
import random


class Robot:
    robotNames = []

    def __init__(self):
        self.name = self.generateRobotName()
        self.robotNames.append(self.name)

    def reset(self):
        self.name = self.generateRobotName()

    def generateRobotName(self):
        name = None
        while name is None or name in self.robotNames:
            name = random.choice(string.ascii_uppercase) \
                + random.choice(string.ascii_uppercase) \
                + str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))

        return name
