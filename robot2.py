import random


class robot:
    name = "machine2"
    game = ["cara","creu"]

    def playing(self):
        choice = random.choice(self.game)
        return choice
